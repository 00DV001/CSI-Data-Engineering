# Task 1: Copy Data from Azure SQL to CSV, Parquet, and Avro using Azure Data Factory

## Objective

Extract data from an Azure SQL Database and export it into **three file formats**:
- CSV: Broad compatibility and readability
- Parquet: Efficient storage and analytics
- Avro: Compact binary format with schema evolution support

These formats enable diverse downstream use cases like reporting, analytics, data warehousing, and big data processing.

---

## Prerequisites

Before you begin:
- An **Azure for Students** account
- A **resource group**
- A deployed **Azure SQL Database** with at least one table and data
- An **Azure Blob Storage** account (StorageV2)
- **Azure Data Factory (ADF)** set up

---

## Steps to Complete the Task

### Step 1: Create Linked Services

1. Go to **Azure Data Factory Studio** > Manage > Linked Services
2. Create:
   - **Azure SQL Database** linked service (use SQL authentication or Microsoft Entra ID)
   - **Azure Blob Storage** linked service (use Account Key authentication)
[1.1](/week05/screenshots/img%20task1%20(1).png)
[1.2](/week05/screenshots/img%20task1%20(2).png)
[1.3](/week05/screenshots/img%20task1%20(3).png)
[1.4](/week05/screenshots/img%20task1%20(4).png)
[1.5](/week05/screenshots/img%20task1%20(5).png)
[1.6](/week05/screenshots/img%20task1%20(6).png)
[1.7](/week05/screenshots/img%20task1%20(7).png)
[1.8](/week05/screenshots/img%20task1%20(8).png)
[1.9](/week05/screenshots/img%20task1%20(9).png)
[1.10](/week05/screenshots/img%20task1%20(10).png)
[1.11](/week05/screenshots/img%20task1%20(11).png)
[1.12](/week05/screenshots/img%20task1%20(12).png)
[1.13](/week05/screenshots/img%20task1%20(13).png)
[1.14](/week05/screenshots/img%20task1%20(14).png)
[1.15](/week05/screenshots/img%20task1%20(15).png)
[1.16](/week05/screenshots/img%20task1%20(16).png)
[1.17](/week05/screenshots/img%20task1%20(17).png)
---

### Step 2: Create Source Dataset (SQL Table)

1. Go to **Author > Datasets > + New Dataset**
2. Choose:
   - Data store: **Azure SQL Database**
   - Table: Select your existing table (e.g., `Students`)
3. Name it `SqlInputDataset`

[1.18](/week05/screenshots/img%20task1%20(18).png)
[1.19](/week05/screenshots/img%20task1%20(19).png)
[1.20](/week05/screenshots/img%20task1%20(20).png)
[1.21](/week05/screenshots/img%20task1%20(21).png)
---

### Step 3: Create Sink Datasets

Repeat the following for each format:

#### 🔹 CSV Sink
- Data store: **Azure Blob Storage**
- Format: **DelimitedText**
- Folder: `output/csv/`
- File name: `students.csv`

#### 🔹 Parquet Sink
- Format: **Parquet**
- Folder: `output/parquet/`
- File name: `students.parquet`

#### 🔹 Avro Sink
- Format: **Avro**
- Folder: `output/avro/`
- File name: `students.avro`

Name them: `CsvSinkDataset`, `ParquetSinkDataset`, and `AvroSinkDataset`.

[1.22](/week05/screenshots/img%20task1%20(22).png)

---

### Step 4: Create a Pipeline with 3 Copy Activities

1. Go to **Author > Pipelines > + New pipeline**
2. Add 3 **Copy Data** activities:
   - `CopyToCSV`
   - `CopyToParquet`
   - `CopyToAvro`

For each:
- **Source**: `SqlInputDataset`
- **Sink**: corresponding sink dataset (CSV, Parquet, or Avro)

 Tip: To run them **simultaneously**, don’t connect them with arrows

[1.23](/week05/screenshots/img%20task1%20(23).png)
[1.24](/week05/screenshots/img%20task1%20(24).png)
[1.25](/week05/screenshots/img%20task1%20(25).png)
---

### Step 5: Validate and Publish

1. Click **Validate All**
2. Click **Publish All**

[1.26](/week05/screenshots/img%20task1%20(26).png)
---

### Step 6: Debug or Trigger the Pipeline

- Click **Debug** to test the pipeline
- Click **Add Trigger > Trigger Now** to run it manually

---

## Expected Output

Azure Blob Storage should contain: data file in csv, avro and parquet

[1.27](/week05/screenshots/img%20task1%20(27).png)

---

# Task 2: Automate Data Movement Using Triggers in Azure Data Factory

## Objective

Configure two types of triggers in Azure Data Factory to automate pipeline execution:

1. **Schedule Trigger** – Run the pipeline at regular intervals (e.g., daily at 8 AM)
2. **Event Trigger** – Run the pipeline in real-time when a file is uploaded to Azure Blob Storage

This enables both **batch** and **real-time automation** of your data pipeline with minimal manual intervention.

---

## Prerequisites

- A completed pipeline (e.g., copying SQL data to CSV/Parquet/Avro)
- Linked services already set up for:
  - Azure SQL Database
  - Azure Blob Storage
- At least one table with data in your Azure SQL Database
- Azure Blob Storage container (e.g., `input/`)

---

## Steps to Configure Triggers

---

### PART 1: Add a **Schedule Trigger**

> Run the pipeline automatically at a set time (e.g., daily at 5:00 PM)
[2.1](/week05/screenshots/img%20task2%20(1).png)

### Step 1: Open Your Pipeline

1. In **Author** tab, select your pipeline (e.g., `ExportToAllFormats`)

### Step 2: Add a Trigger

1. Click **Add Trigger > New/Edit**
2. Click **+ New**

### Step 3: Configure Trigger Settings

| Field         | Value                    |
|---------------|--------------------------|
| Name          | `DailyExportTrigger`     |
| Type          | `Schedule`               |
| Start Date    | Today’s date             |
| Time          | 05:00 PM (our time zone) |
| Recurrence    | Every 1 Day              |

Click **Next**, bind our pipeline, and click **OK**

[2.2](/week05/screenshots/img%20task2%20(2).png)
[2.3](/week05/screenshots/img%20task2%20(5).png)
[2.4](/week05/screenshots/img%20task2%20(6).png)

### Step 4: Publish

Click **Publish All**

---

### PART 2: Add an **Event-Based Trigger**

> Trigger the pipeline when a `.csv` file is uploaded to a specific folder in Blob Storage
[2.5](/week05/screenshots/img%20task2%20(7).png)

### Step 1: Go to Manage > Triggers > + New

1. Choose **Event**
2. Select **Storage events**

### Step 2: Configure Trigger Details

| Field                  | Value                         |
|------------------------|-------------------------------|
| Name                   | `FileUploadTrigger`           |
| Storage account        | Select your linked storage    |
| Container              | `input`                       |
| Blob path begins with  | `csv/`                        |
| Blob path ends with    | `.csv`                        |
| Event type             | `Blob Created`                |

[2.6](/week05/screenshots/img%20task2%20(8).png)
[2.7](/week05/screenshots/img%20task2%20(9).png)


### Step 3: Bind Pipeline and Parameters

If your pipeline accepts a parameter `fileName`, map it like this:

```text
fileName = @triggerBody().fileName
```

---
### Step 4: Bind Trigger to Pipeline

1. After defining the trigger, click **Continue**
2. Bind it to the pipeline
3. Map parameters:
```text
fileName = @triggerBody().fileName
```
4. Click **OK** and then **Publish All**

---

## Step 5: Test the Trigger

1. Upload a CSV file to:
```
input/csv/students_live_2025.csv
```
2. Go to **Monitor > Pipeline Runs**
3. Verify the pipeline was triggered and the file was processed

[2.8](/week05/screenshots/img%20task2%20(11).png)
[2.9](/week05/screenshots/img%20task2%20(13).png)
[2.10](/week05/screenshots/img%20task2%20(12).png)
[2.11](/week05/screenshots/img%20task2%20(14).png)
---

# Task 3 - Full Table Replication Using Azure Data Factory

## Objective

**Copy All Tables from One Database to Another**

This pipeline performs a full replication of all user-defined tables and their data from a **source Azure SQL Database** to a **destination Azure SQL Database** using **Azure Data Factory (ADF)**.

This ensures:
- Complete schema and data consistency
- Useful for full backups, environment migrations, or syncing dev/test/prod databases

---

## Tools Used

- Azure Data Factory (ADF)
- Azure SQL Database (Source and Destination)
- Linked Services (LS_SQL_Source and LS_SQL_Destination)
- Lookup, ForEach, and Copy Data Activities
- Parameterized Dummy Datasets

---

## Pipeline Overview

### 1. **Lookup Activity (`getTableList`)**
- Purpose: Retrieve all user-defined table names from the source database
- Query used:
  ```sql
  SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE'
  ```
[3.1](/week05/screenshots/img%20task3%20(8).png)

---

### 2. **ForEach Activity (`loopOverTables`)**
- Iterates over each table name returned by the Lookup
- Dynamically triggers a Copy Data activity for each table
[3.2](/week05/screenshots/img%20task3%20(11).png)
---

### 3. **Copy Data Activity (`copyTableData`)**
- Uses a parameterized dummy source and sink dataset
- Copies all data from each source table to its corresponding destination table
[3.3](/week05/screenshots/img%20task3%20(9).png)
[3.4](/week05/screenshots/img%20task3%20(10).png)
---

## Datasets

### 🔹 `DS_Source_Generic`
- Type: Azure SQL Database
- Table: `dbo.DummyTable` (used only to pass schema validation)
- Parameters:
  - `TableName` (String)
- Optional query override:
  ```sql
  @concat('SELECT * FROM ', item().TABLE_NAME)
  ```
[3.5](/week05/screenshots/img%20task3%20(6).png)
### 🔹 `DS_Destination_Generic`
- Type: Azure SQL Database
- Table: `dbo.DummyTable`
- Parameters:
  - `TableName` (String)
[3.6](/week05/screenshots/img%20task3%20(7).png)
---

## Linked Services

- `LS_SQL_Source`: Linked to source Azure SQL Database
- `LS_SQL_Destination`: Linked to destination Azure SQL Database
[3.7](/week05/screenshots/img%20task3%20(4).png)

---

## Parameter Binding in Copy Activity

### Source Dataset Parameters:
| Name      | Value                |
|-----------|----------------------|
| TableName | `@item().TABLE_NAME` |

### Sink Dataset Parameters:
| Name      | Value                |
|-----------|----------------------|
| TableName | `@item().TABLE_NAME` |

---


## Dummy Table Setup

Create a dummy table in both databases to satisfy schema validation:

```sql
CREATE TABLE DummyTable (
    DummyCol VARCHAR(10)
);
```

This table is never queried during execution due to dynamic SQL override.

---

## Limitations

- Destination tables must exist in advance with the correct schema
- Schema auto-generation is not supported in Azure SQL (only in Synapse DW)
- Dummy tables are used only for validation — not for actual data movement

---

## Final Output

- Dynamically replicates **all user-defined tables and their data** from source to destination
- No hardcoded table names — pipeline adapts to schema changes automatically
[3.8](/week05/screenshots/img%20task3%20(12).png)
[3.9](/week05/screenshots/img%20task3%20(13).png)
[3.10](/week05/screenshots/img%20task3%20(14).png)
---


# Task 4 - Selective Table and Column Copy Using Azure Data Factory

## Objective

**Copy Selective Tables with Selective Columns from One Database to Another**

This pipeline allows selective data migration by choosing specific tables and only specific columns to be copied from the **source Azure SQL Database** to the **destination Azure SQL Database** using **Azure Data Factory (ADF)**.

This approach supports:
- Compliance with data minimization
- Lower data transfer volume
- Business-specific migration needs

---

## Tools Used

- Azure Data Factory (ADF)
- Azure SQL Database (Source and Destination)
- Linked Services
- Lookup, ForEach, and Copy Data Activities
- Parameterized Dummy Datasets
- Control Table for Table + Column Mapping

---

## Control Table Structure

Create a control table in your source DB:

```sql
CREATE TABLE TableColumnMap (
    TableName NVARCHAR(128),
    ColumnList NVARCHAR(MAX)
);

-- Example rows:
INSERT INTO TableColumnMap VALUES 
('Students', 'StudentID, FirstName, Age'),
('Teachers', 'TeacherID, Subject');
```

This drives the entire dynamic copy process.

---

## Pipeline Overview

### 1. **Lookup Activity (`getTableColumnMap`)**
- Reads `TableColumnMap` from the source DB
- Output is a list of table + column combinations:
  ```json
  [
    { "TableName": "Students", "ColumnList": "StudentID, FirstName, Age" },
    { "TableName": "Teachers", "ColumnList": "TeacherID, Subject" }
  ]
  ```
[4.1](/week05/screenshots/img%20task4%20(1).png)
---

### 2. **ForEach Activity (`loopOverTableColumnMap`)**
- Iterates over each row of the control table
- Passes `TableName` and `ColumnList` to the Copy activity
[4.2](/week05/screenshots/img%20task4%20(6).png)

---

### 3. **Copy Data Activity (`copySelectedColumns`)**
- Uses dummy datasets and dynamic SQL to copy **only selected columns**
- Works for each table/column pair
[4.3](/week05/screenshots/img%20task4%20(5).png)
---

## Datasets

### 🔹 `DS_Source_Generic`
- Type: Azure SQL Database
- Table: `dbo.DummyTable`
- Parameters:
  - `TableName` (String)
  - `ColumnList` (String)
- Query:
  ```sql
  SELECT @{dataset().ColumnList} FROM @{dataset().TableName}
  ```

### 🔹 `DS_Destination_Generic`
- Type: Azure SQL Database
- Table: `dbo.DummyTable`
- Parameters:
  - `TableName` (String)

---

## Linked Services

- `LS_SQL_Source`: Source Azure SQL DB
- `LS_SQL_Destination`: Destination Azure SQL DB

[4.4](/week05/screenshots/img%20task4%20(4).png)
[4.5](/week05/screenshots/img%20task4%20(5).png)

---

## Copy Activity Parameter Mapping

| Parameter       | Value                |
|------------------|------------------------|
| TableName        | `@item().TableName`    |
| ColumnList       | `@item().ColumnList`   |

### Source Query Override:
Enable "Use Query" and paste:
```sql
@concat('SELECT ', item().ColumnList, ' FROM ', item().TableName)
```

---

## Dummy Table Setup

Create a dummy table to satisfy schema validation:

```sql
CREATE TABLE DummyTable (
    DummyCol VARCHAR(10)
);
```

---

## Limitations

- Destination tables must already exist with expected schema
- No schema creation is done automatically in Azure SQL DB
- Dummy table is never used at runtime — it's just for validation

---

## Final Outcome

- Dynamically copies only **selected columns** from **selected tables**
- Entire logic driven by a control table
- No hardcoding — fully dynamic and reusable pipeline
[4.6](/week05/screenshots/img%20task4%20(10).png)
[4.7](/week05/screenshots/img%20task4%20(9).png)
[4.8](/week05/screenshots/img%20task4%20(11).png)

---