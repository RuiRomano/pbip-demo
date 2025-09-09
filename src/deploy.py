# Install fabric-cicd: https://microsoft.github.io/fabric-cicd/
from azure.identity import InteractiveBrowserCredential, ClientSecretCredential
from fabric_cicd import FabricWorkspace, publish_all_items, change_log_level
import argparse
import os

#change_log_level("DEBUG")

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--spn-auth", default = False)
parser.add_argument("--workspace", default = "PBIP Demo")
parser.add_argument("--environment", default = "DEV")
parser.add_argument("--src", default = ".\\src")

args = parser.parse_args()

spn_auth = args.spn_auth
workspace_name = args.workspace
src_path = args.src
environment = args.environment

# Authentication (SPN or Interactive)

if (not spn_auth):
    credential = InteractiveBrowserCredential() 
else:
    client_id = os.getenv("FABRIC_CLIENT_ID")
    client_secret = os.getenv("FABRIC_CLIENT_SECRET")
    tenant_id = os.getenv("FABRIC_TENANT_ID")

    credential = ClientSecretCredential(client_id=client_id, client_secret=client_secret, tenant_id=tenant_id)

target_workspace = FabricWorkspace(    
    workspace_name = workspace_name,  
    environment = environment,
    repository_directory = src_path,
    item_type_in_scope = ["SemanticModel", "Report"],     
    token_credential = credential,
)

publish_all_items(fabric_workspace_obj = target_workspace)
