# Assignment Week 7
### Daily ETL Pipeline – Ingesting & Transforming Date-Stamped Files

---

## Problem Statement
Let's suppose you have 3 different types of file 
1. CUST_MSTR_20191112.csv 
2. master_child_export-20191112.csv 
3. H_ECOM_ORDER.csv

All these files will be in the data lake container You have to fetch all three types of files into their respective folders. Note: There could be multiple files on all 3 types for different dates for example CUST_MSTR_20191112.csv and CUST_MSTR_20191113.csv 
1. For the "CUST_MSTR" starting name of the file You have to create an additional column for a date that will fetch the data value from the filename and put it into an additional column Date format: 2019-11-12 and load it into the "CUST_MSTR" table
2. For the "master_child_export" starting name of the file You have to create two additional columns date and date key which will fetch the data from the filename and put it into the additional columns. Date format: 2019-11-12 DateKey format: 20191112 and load it into the "master_child" table
3. for the "H_ECOM_ORDER" type of file you have to load it into the database as it is, and load it into "H_ECOM_Orders" table Note: This process will work on truncate load on a daily basis


---

## Tools & Technologies

- **ETL & Orchestration:** Azure Data Factory (ADF)
- **Storage:** Azure Data Lake Gen2
- **Database:** Azure SQL Database
- **ADF Components:** Pipelines, Mapping Data Flows, Copy Data
- **Automation:** Triggers
- **Monitoring:** Azure Monitor

---

## Implementation Steps
### Step 1: Set Up Tables in Azure SQL Database
First, make sure your destination tables exist. Connect to your Azure SQL DB and run the DDL statements. Adjust the column definitions to match your CSV files.

### Step 2: Set Up Linked Services in ADF
We need two: one for the data lake and one for the SQL database.
In your ADF, go to the Manage tab.
1. Click Linked Services -> New.
2. Create an Azure Data Lake Storage Gen2 Linked Service:
3. Name it `ls_adls_source`
4. Connect it to your ADLS account.
5. Create an Azure SQL Database Linked Service:
6. Name it `ls_azuresql_sink`
7. Connect it to your Azure SQL Database.

### Step 3: Set Up Datasets
We need one source dataset for each file pattern and one sink dataset for each database table.

1. Source Datasets (using wildcards):
    - Go to the Author tab, click Datasets -> New Dataset
    - Dataset for CUST_MSTR:
        - Source: Azure Data Lake Storage Gen2
        - Format: DelimitedText (CSV)
        - Name: `ds_source_cust_mstr`
        - Linked Service: `ls_adls_source`
        - File path: `CUST_MSTR_*.csv`
    - Dataset for master_child_export:
        - Follow the same steps
        - Name: `ds_source_master_child`
        - File path: `master_child_export-*.csv`
    - Dataset for H_ECOM_ORDER:
        - Follow the same steps
        - Name: `ds_source_h_ecom_order`
        - File path: `H_ECOM_ORDER.csv`

2. Sink Datasets (for SQL Tables):
    - Go to Datasets -> New Dataset
    - Dataset for CUST_MSTR table:
        - Source: Azure SQL Database
        - Name: `ds_sink_cust_mstr`
        - Linked Service: `ls_azuresql_sink`
        - Table name: Select dbo.CUST_MSTR from the dropdown

### Step 4: Build Pipelines

1. Go to the Author tab → Pipelines → **New Pipeline**
2. Name: `pl_daily_file_load`
3. Add Data flow activities

#### Configuration Detail 1: CUST_MSTR Flow
1. Activity: `df_process_cust_mstr`  
2. Data Flow Name: `dfl_add_date_cust_mstr`
3. Inside Mapping Data Flow:
    - Source:
        - Name: `sourceCustMstr`
        - Dataset: `ds_source_cust_mstr`
    - Derived Column:
        - Name: `addLoadDate`
        - Column: `LoadDate`
    - Sink:
        - Dataset: `ds_sink_cust_mstr`
        - Table action: `Truncate table`
        - Disable auto mapping and ensure `LoadDate` is mapped.

    ```plaintext
     toDate(concat(substring(item().name, 11, 4), '-', substring(item().name, 15, 2), '-', substring(item().name, 17, 2)), 'yyyy-MM-dd')
     ```

#### Configuration Detail 2: master_child_export Flow

1. Activity: `df_process_master_child`  
2. Data Flow Name: `dfl_add_keys_master_child`
3. Inside Mapping Data Flow:
    - Source:
        - Dataset: `ds_source_master_child`
        - Output: `sourceMasterChild`
    - Derived Columns:
        - Column 1: `date`
        - Column 2: `DateKey`
    - Sink:
        - Dataset: `ds_sink_master_child`
        - Table action: `Truncate table`
        - Ensure all mappings are correct.
    
    ```plaintext
    toDate(concat(substring(item().name, 20, 4), '-', substring(item().name, 24, 2), '-', substring(item().name, 26, 2)), 'yyyy-MM-dd')
    concat(substring(item().name, 20, 4), substring(item().name, 24, 2), substring(item().name, 26, 2))
    ```

#### Configuration Detail 3: H_ECOM_ORDER Flow

1. Activity: `copy_h_ecom_orders`
2. Source: Dataset: `ds_source_h_ecom_order`
3. Sink:
    - Dataset: `ds_sink_h_ecom_orders`
    - Pre-copy script:
        ```sql
        TRUNCATE TABLE dbo.H_ECOM_Orders
        ```
4. Mapping:
    - Click "Import schemas" and validate mappings



### Step 5: Schedule the Pipeline

1. In `pl_daily_file_load` canvas → Add trigger → New/Edit
2. Click + New → Type: **Schedule**
3. Configure to run **Daily** at your preferred time (e.g., 2:00 AM UTC)
4. Activate trigger post-publish

### Final Step: Publish and Monitor

1. Click **Publish all**
2. Manually trigger with **Trigger now**
3. Use **Monitor** tab to view runs and debug issues

---

## Conclusion
This pipeline automates daily data ingestion and transformation for three file types using Azure Data Factory. By extracting metadata from filenames, applying necessary transformations, and using truncate-load logic, it ensures clean, consistent loading into SQL tables. Scheduling and monitoring complete the robust end-to-end ETL process.
