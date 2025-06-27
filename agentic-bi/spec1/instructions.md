

Make sure you understand the semantic model folder structure. 
- Its following the Power BI Project (PBIP) file format, documented here: https://learn.microsoft.com/en-us/power-bi/developer/projects/projects-dataset

- The semantic model is represented using TMDL language and all files are located in the definition folder of each semantic model. Learn about TMDL spec here: https://learn.microsoft.com/en-us/analysis-services/tmdl/tmdl-overview?view=sql-analysis-services-2025

This is what I want you to do:

- Add Reseller analysis to semantic model Model01
- Bring tables 'FactResellerSales' and 'DimReseller' as new tables to the semantic model
- Ensure that you use the existing Calendar table, and relate with columns of same type.
- The SQL Server name is 'rrplaygroundsql.database.windows.net' and database 'AdventureWorksDW'
- Schema of the SQL tables is in AzureSQLSchema.csv
- Create base measures for the fact table, but only for aggregatable columns using simple DAX.
- My model calendar table use datetime columns for relationships, if the fact table in source dont have a datetime/date column please create one using PowerQuery language

I want you to follow the following guidelines when creating new semantic model objectS:

- Analize a few tables to understand the existing naming pattern and follow it
- Avoid many-to-many relationships between tables, always prefer many-to-one

