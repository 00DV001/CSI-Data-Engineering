# Task 1: On-Premises to Azure SQL Data Migration with Azure Data Factory (ADF)

## Overview

This guide details the process of configuring Azure Data Factory (ADF) with a Self-hosted Integration Runtime (SHIR) to facilitate secure data movement from an on-premises SQL Server instance to an Azure SQL Database. This approach ensures that data residing within your private network can be efficiently and securely transferred to the Azure cloud.

## Steps

Follow these steps to configure and execute your data migration pipeline.

### Step 1: Create a Self-hosted Integration Runtime in ADF

1.  Navigate to the [Azure Portal](https://portal.azure.com/).
2.  Open your **Azure Data Factory** resource.
3.  Click **Launch Studio**.
4.  In ADF Studio, go to the **Manage** tab.
5.  Select **Integration Runtimes**.
6.  Click **+ New**.
7.  Under "Integration Runtime setup," select the **Self-hosted** option.
8.  Provide a name for your SHIR (e.g., `SHIR_LocalServer`).
9.  Click **Create**.
10. After creation, click on your newly created SHIR.
11. **Download the installer** for the Self-hosted Integration Runtime.
12. **Copy the authentication key** displayed. You will need this during the installation process.

### Step 2: Install SHIR on Local Machine

1.  Locate the downloaded SHIR installer (`.exe` file) on your local machine.
2.  **Run the installer** as an administrator.
3.  During the installation wizard, when prompted, choose the option **Register with Azure Data Factory**.
4.  **Paste the authentication key** you copied in Step 1.
5.  Complete the setup wizard.

    Your local machine is now registered as the host for the Self-hosted Integration Runtime, establishing a secure connection to your Azure Data Factory.

### Step 3: Create Linked Services in Azure Data Factory

Linked Services define the connection information for external data stores.

#### a. For On-Prem SQL Server

1.  In ADF Studio, go to the **Manage** tab.
2.  Select **Linked Services**.
3.  Click **+ New**.
4.  Search for and choose **SQL Server**.
5.  Configure the settings:
    * **Integration Runtime:** Select `SHIR_LocalServer` (the SHIR you just installed).
    * **Authentication type:** Choose either **SQL Authentication** (recommended for production) or **Windows Authentication** (if your local SQL Server is configured for it).
    * **Server name:** Enter the name or IP address of your local SQL Server.
    * **Database name:** Enter the name of the database you want to extract data from.
    * Provide **User name** and **Password** if using SQL Authentication.
6.  Click **Test connection** to verify connectivity.
7.  Click **Create**.

#### b. For Azure SQL Database

1.  In ADF Studio, go to the **Manage** tab.
2.  Select **Linked Services**.
3.  Click **+ New**.
4.  Search for and choose **Azure SQL Database**.
5.  Configure the settings:
    * **Authentication type:** Use **SQL Authentication**.
    * **Server name:** Enter the fully qualified server name of your Azure SQL Database (e.g., `yourserver.database.windows.net`).
    * **Database name:** Enter the name of your Azure SQL Database.
    * Provide **User name** and **Password** for your Azure SQL Database.
6.  Click **Test connection** to verify connectivity.
7.  Click **Create**.

### Step 4: Create Datasets

Datasets represent the structure of the data you want to move.

1.  In ADF Studio, go to the **Author** tab.
2.  Select **Datasets**.
3.  Click **+ New Dataset**.
4.  Search for and choose **SQL Server** (for your source data).
5.  Select the **Linked Service** you created for your local SQL Server.
6.  Choose the specific **table** you wish to extract data from.
7.  Click **OK** and then **Create**.

8.  Create a second Dataset:
    * Click **+ New Dataset** again.
    * Search for and choose **Azure SQL Database** (for your sink data).
    * Select the **Linked Service** you created for your Azure SQL Database.
    * Choose an existing destination table or specify a new table name. ADF can often create the table if it doesn't exist, based on the source schema.
    * Click **OK** and then **Create**.

### Step 5: Create Copy Data Pipeline

Pipelines orchestrate the data movement activities.

1.  In ADF Studio, go to the **Author** tab.
2.  Select **Pipelines**.
3.  Click **+ New Pipeline**.
4.  From the "Activities" pane, drag and drop a **Copy Data** activity onto the pipeline canvas.
5.  Select the **Copy Data** activity and go to its **Source** tab:
    * **Source dataset:** Select the dataset you created for your on-premises SQL Server.
6.  Go to the **Sink** tab:
    * **Sink dataset:** Select the dataset you created for your Azure SQL Database.
    * Configure any additional sink settings as needed (e.g., write behavior).

### Step 6: Run and Verify

1.  **Validate and Publish All** your changes in ADF Studio to save your configurations.
2.  To run the pipeline, click **Add Trigger** on your pipeline.
3.  Select **Trigger Now**.
4.  Go to the **Monitor** tab in ADF Studio.
5.  Check the **pipeline run status**. It should show as "Succeeded."
6.  Connect to your **Azure SQL Database** using a tool like Azure Data Studio or SSMS.
7.  **Confirm that the data has been successfully loaded** into your destination table.

## Screenshots:

![1.1](/week06/screenshots/setup.png)
![1.2](/week06/screenshots/task%201-1.png)
![1.3](/week06/screenshots/task%201-2.png)
![1.4](/week06/screenshots/task%201-3.png)

# Task 2: FTP/SFTP to Azure Blob Storage Data Extraction with Azure Data Factory (ADF)

## Overview

This guide details the process of configuring Azure Data Factory (ADF) to connect to an FTP or SFTP server, extract files, and store them in an Azure Storage Account's Blob Storage. This is a common pattern for data ingestion from external sources that provide data via FTP/SFTP protocols.

## Steps

Follow these steps to configure and execute your data extraction pipeline.

### Step 1: Gather FTP/SFTP Credentials

Ensure you have the following information readily available for your FTP/SFTP server:

* **Hostname:** The address of the FTP/SFTP server (e.g., `ftp.example.com` or `sftp.mydomain.net`).
* **Port:** The port number. Default is `21` for FTP and `22` for SFTP.
* **Username & Password:** Credentials for authentication. If using SFTP with key-based authentication, ensure you have the private key.
* **Directory Path:** The specific directory path on the FTP/SFTP server where the files you want to extract are located.

### Step 2: Create Linked Services in Azure Data Factory

Linked Services define the connection information for external data stores.

#### a. FTP/SFTP Linked Service

1.  Open **ADF Studio**.
2.  Go to the **Manage** tab.
3.  Select **Linked Services**.
4.  Click **+ New**.
5.  Search for and choose either **FTP** (for basic FTP servers) or **SFTP** (for Secure FTP servers), depending on your server type.
6.  Fill in the connection details:
    * **Host:** Enter the hostname of your FTP/SFTP server.
    * **Port:** Enter the port number.
    * **Authentication type:**
        * **Basic:** If using username and password. Provide your Username and Password.
        * **SSH Key:** If using SFTP with key-based authentication. Provide your Username and the content of your Private Key.
    * **Path:** Specify the root directory or a specific subdirectory on the FTP/SFTP server.
    * **Integration Runtime:** Select `AutoResolveIntegrationRuntime` if your FTP/SFTP server is publicly accessible. If it's within a private network, select your configured Self-hosted Integration Runtime.
7.  Click **Test connection** to verify connectivity.
8.  Click **Create**.

#### b. Azure Blob Storage Linked Service (if not already created)

If you haven't already set up a Linked Service for your Azure Blob Storage, follow these steps:

1.  Click **+ New** under Linked Services.
2.  Choose **Azure Blob Storage**.
3.  For **Authentication type**, select **Account key**.
4.  Select your **Azure Storage Account** from the dropdown.
5.  Click **Test connection** to verify connectivity.
6.  Click **Create**.

### Step 3: Create Datasets

Datasets represent the structure of the data you want to move.

#### a. Source Dataset (FTP/SFTP)

1.  In ADF Studio, go to the **Author** tab.
2.  Select **Datasets**.
3.  Click **+ New Dataset**.
4.  Choose either **FTP** or **SFTP**, matching your source server.
5.  Select the **Linked Service** you created for your FTP/SFTP connection.
6.  For the **File path**, specify a precise filename (e.g., `data.csv`) or use a wildcard pattern (e.g., `*.csv` to extract all CSV files in a directory).
7.  Set the **format** of the files (e.g., `DelimitedText`, `JSON`, `Excel`, etc.) based on your source files.
8.  Click **OK** and then **Create**.

#### b. Sink Dataset (Blob Storage)

1.  Click **+ New Dataset**.
2.  Choose **DelimitedText** or the appropriate file format that matches the output you desire in Blob Storage.
3.  Select the **Linked Service** for your Azure Blob Storage.
4.  For the **File path**, specify the target container and optionally a folder path within it where you want the files to be stored.
5.  Configure the desired **file name** and other format-specific settings (e.g., column delimiter, first row as header).
6.  Click **OK** and then **Create**.

### Step 4: Create Copy Data Pipeline

Pipelines orchestrate the data movement activities.

1.  In ADF Studio, go to the **Author** tab.
2.  Select **Pipelines**.
3.  Click **+ New Pipeline**.
4.  From the "Activities" pane, drag and drop a **Copy Data** activity onto the pipeline canvas.
5.  Select the **Copy Data** activity and go to its **Source** tab:
    * **Source dataset:** Select the dataset you created for your FTP/SFTP.
    * (Optional) Configure **Wildcard file processing** if you are extracting multiple files (e.g., `*.csv`).
6.  Go to the **Sink** tab:
    * **Sink dataset:** Select the dataset you created for your Azure Blob Storage.
    * (Optional) Configure **skip/overwrite options** as per your requirement for handling existing files in the destination.

### Step 5: Validate and Run Pipeline

1.  Click **Validate All** in ADF Studio to check for any configuration errors. Resolve any reported issues.
2.  Click **Publish All** to save and deploy your pipeline changes.
3.  To initiate the pipeline run, click **Add Trigger** on your pipeline.
4.  Select **Trigger Now**.
5.  Go to the **Monitor** tab in ADF Studio.
6.  Observe the **pipeline run status**. Ensure it shows as "Succeeded."

### Step 6: Verify Output

1.  Navigate to your **Azure Storage Account** in the Azure Portal.
2.  Go to **Containers**.
3.  Open the container you specified as the destination in your sink dataset.
4.  **Verify that the file(s)** downloaded from the FTP/SFTP server now exist in your Azure Blob Storage container and that their content is correct.

## Screenshots:

![2.1](/week06/screenshots/task%202-1.png)
![2.2](/week06/screenshots/task%202-2.png)
![2.3](/week06/screenshots/task%202-3.png)

# Task 3: Incremental Data Load and Daily Automation with Azure Data Factory (ADF)

## Overview

This guide details the creation of an incremental data loading pipeline in Azure Data Factory. Instead of transferring all data during each run, this pipeline identifies and moves only the records that have been newly added or modified since the last successful load. This is achieved by using a "watermark" column (typically a `datetime` column) in the source table and tracking the last processed timestamp. The pipeline is then scheduled to run daily for automated data synchronization.

## Steps

Follow these steps to configure and automate your incremental data load pipeline.

### Step 1: Add a Watermark Column to Source Table

The cornerstone of incremental loading is a watermark column that records the last modification time of a row.

1.  **Identify or add a `datetime` column** to your source table (e.g., `Customers`). This column will track when a record was last inserted or updated.
2.  **Ensure this column is automatically updated** whenever a record is inserted or modified. You can achieve this using a `DEFAULT GETDATE()` constraint for new records and triggers or application logic for updates.

    **Example SQL to add a column (if it doesn't exist):**

    ```sql
    ALTER TABLE Customers ADD UpdatedAt DATETIME DEFAULT GETDATE();
    ```

    *Note: For existing records, you might need to backfill this column with appropriate timestamps.*

### Step 2: Create Watermark Table in ADF Sink (Optional but Recommended)

To track the last successful load timestamp, create a dedicated watermark table in your destination database.

1.  In your destination Azure SQL Database, execute the following SQL command to create the `WatermarkTracking` table:

    ```sql
    CREATE TABLE WatermarkTracking (
        TableName VARCHAR(100),
        LastLoadedTime DATETIME
    );
    ```

2.  **Initialize this table** with an initial timestamp for each source table you plan to incrementally load. This timestamp should be earlier than any data you want to load initially.

    **Example SQL to initialize:**

    ```sql
    INSERT INTO WatermarkTracking VALUES ('Customers', '2023-01-01 00:00:00');
    ```
    *Adjust the date to be before your earliest data, or a very old date if you want to load all historical data on the first run.*

### Step 3: Create Linked Services

Ensure you have the necessary Linked Services configured in Azure Data Factory.

* **Source Database Linked Service:**
    * If your source is an on-premises SQL Server, ensure you have a Linked Service configured using a Self-hosted Integration Runtime (SHIR).
    * If your source is Azure SQL Database, use a standard Azure SQL Database Linked Service.
    * **Test and save** the connection.

* **Azure SQL Database (Destination) Linked Service:**
    * Create or verify a Linked Service for your target Azure SQL Database.
    * **Test and save** the connection.

### Step 4: Create Datasets with Parameters

Create parameterized datasets to allow dynamic filtering based on the watermark value.

#### a. Source Dataset (SQL)

1.  In ADF Studio, go to the **Author** tab.
2.  Select **Datasets**.
3.  Click **+ New Dataset**.
4.  Choose your source database type (e.g., **SQL Server** or **Azure SQL Database**).
5.  Select your **Source Linked Service**.
6.  Instead of selecting a table directly, choose the option to **Edit manually** or **Use query**.
7.  Add a **parameter** to this dataset. In the "Parameters" tab of the dataset, click `+ New` and name it `watermarkValue` with type `String`.
8.  In the "Connection" tab of the dataset, for the query, use dynamic content to filter based on the `watermarkValue` parameter.

    **Example Query:**

    ```sql
    SELECT * FROM Customers WHERE UpdatedAt > '@{dataset().watermarkValue}'
    ```
    *This query will fetch only records where `UpdatedAt` is greater than the `watermarkValue` passed to the dataset.*

#### b. Sink Dataset (Azure SQL Database)

1.  Create a new Dataset for your destination.
2.  Choose **Azure SQL Database**.
3.  Select your **Azure SQL Database Linked Service**.
4.  Specify the target table in your Azure SQL Database.
5.  Configure the dataset to allow **insert/upsert** as required. For incremental loads, you typically want to insert new records and update existing ones (upsert). This configuration is usually done in the Copy Data activity's Sink settings.

### Step 5: Create Pipeline Logic

This pipeline will consist of activities to read the last watermark, copy data, and update the watermark.

1.  In ADF Studio, go to the **Author** tab.
2.  Select **Pipelines**.
3.  Click **+ New Pipeline**.

4.  **Add a Lookup activity:**
    * Drag a **Lookup** activity onto the pipeline canvas.
    * Go to its **Settings** tab.
    * **Source Dataset:** Create an inline dataset pointing to your `WatermarkTracking` table in the destination Azure SQL Database.
    * **Query:** Enter the SQL query to retrieve the `LastLoadedTime` for your specific table:
        ```sql
        SELECT LastLoadedTime FROM WatermarkTracking WHERE TableName = 'Customers';
        ```
    * Ensure "First row only" is checked if you expect only one row for the table.

5.  **Add a Set Variable activity:**
    * Drag a **Set Variable** activity onto the pipeline canvas.
    * Connect the success output of the Lookup activity to this Set Variable activity.
    * Go to its **Settings** tab.
    * **Variables:** Create a new variable named `watermarkValue` (type `String`).
    * **Value:** Use dynamic content to capture the output of the Lookup activity:
        ```
        @activity('Lookup1').output.firstRow.LastLoadedTime
        ```
        *(Replace 'Lookup1' with the actual name of your Lookup activity)*

6.  **Add a Copy Data activity:**
    * Drag a **Copy Data** activity onto the pipeline canvas.
    * Connect the success output of the Set Variable activity to this Copy Data activity.
    * Go to its **Source** tab:
        * **Source Dataset:** Select your parameterized source dataset (e.g., `SQLSourceDataset`).
        * **watermarkValue parameter:** Pass the pipeline variable you just set:
            ```
            @variables('watermarkValue')
            ```
    * Go to its **Sink** tab:
        * **Sink Dataset:** Select your destination Azure SQL Database dataset.
        * Configure **Table option** (e.g., `Auto create table` or `Existing table`).
        * Configure **Write behavior** (e.g., `Insert` for new records, or `Upsert` if you need to update existing records based on a key). For upsert, you'll need to specify the key columns.

7.  **Add a Stored Procedure or Script activity (to update watermark):**
    * Drag a **Stored Procedure** activity (if you prefer to encapsulate the logic in a stored procedure) or a **Script** activity onto the pipeline canvas.
    * Connect the success output of the Copy Data activity to this activity.
    * Go to its **Settings** tab.
    * **Linked Service:** Select your Azure SQL Database Linked Service (the destination).
    * **For Stored Procedure:**
        * **Stored procedure name:** Create a stored procedure in your Azure SQL DB like `UpdateWatermark` that takes `TableName` and `NewWatermarkTime` as parameters.
        * **Stored procedure parameters:** Pass the current timestamp and table name using dynamic content:
            ```json
            {
                "TableName": { "value": "Customers", "type": "String" },
                "NewWatermarkTime": { "value": "@formatDateTime(utcNow(), 'yyyy-MM-dd HH:mm:ss.fff')", "type": "String" }
            }
            ```
    * **For Script Activity (direct SQL):**
        * **Script:** Enter the SQL command to update the `WatermarkTracking` table with the current timestamp.
            ```sql
            UPDATE WatermarkTracking
            SET LastLoadedTime = GETDATE()
            WHERE TableName = 'Customers';
            ```
            *Note: `GETDATE()` will use the time on the Azure SQL DB server. If you need the ADF pipeline's execution time, use `@formatDateTime(pipeline().TriggerTime, 'yyyy-MM-dd HH:mm:ss.fff')`.*

### Step 6: Schedule Daily Execution

Automate the pipeline to run daily.

1.  In ADF Studio, go to the **Triggers** section (under the **Manage** tab or directly from the pipeline view).
2.  Click **+ New**.
3.  Choose **Schedule** as the trigger type.
4.  Provide a meaningful **Name** (e.g., `DailyIncrementalLoad_Customers`).
5.  Set the **Recurrence** to "Every 24 hours" or your desired frequency (e.g., "Every 1 day").
6.  Configure the **Start date** and **time zone**.
7.  **Attach this trigger to your pipeline** by selecting your incremental load pipeline.
8.  **Publish all changes** in ADF Studio to activate the trigger and schedule.

## Screenshots:

![3.1](/week06/screenshots/task%203-1.png)
![3.2](/week06/screenshots/task%203-2.png)
![3.3](/week06/screenshots/task%203-3.png)
![3.4](/week06/screenshots/task%203-4.png)
![3.5](/week06/screenshots/task%203-5.png)

# Task 4: Automating a Pipeline for the Last Saturday of the Month in Azure Data Factory

## Overview

Azure Data Factory's built-in scheduling capabilities do not directly offer a "last Saturday of the month" option. To achieve this, we employ a two-pronged strategy: first, schedule a trigger to run every Saturday, and second, embed conditional logic within the pipeline itself to check if the current execution day is indeed the last Saturday of the month. If it is, the pipeline proceeds with its core activities; otherwise, it gracefully exits.

## Steps

Follow these steps to configure your custom monthly trigger.

### Step 1: Understanding the Limitation

Azure Data Factory's native scheduling options, while robust, do not inherently provide a "last day of the week in a month" recurrence. Therefore, to achieve "Last Saturday of the Month," we must:

* Utilize a standard **Scheduled Trigger** or **Tumbling Window Trigger** that runs more frequently (e.g., every Saturday).
* Implement **conditional logic within the pipeline** to check if the current execution date is the last Saturday of the month. If the condition is met, the pipeline proceeds; otherwise, it skips its primary activities.

### Step 2: Create the Scheduled Trigger (Weekly on Saturdays)

This trigger will initiate your pipeline every Saturday.

1.  Go to **Azure Data Factory Studio**.
2.  Navigate to the **Manage** tab.
3.  Select **Triggers**.
4.  Click **+ New**.
5.  Configure the trigger settings:
    * **Name:** Provide a descriptive name (e.g., `LastSaturdayMonthlyTrigger`).
    * **Type:** Select `Schedule`.
    * **Recurrence:**
        * **Frequency:** `Week`
        * **Interval:** `1` (meaning every week)
        * **Days:** Select **Saturday only**.
    * **Start Date:** Choose an upcoming Saturday (e.g., `2025-07-19T00:00Z`).
    * **Time Zone:** Select your preferred time zone (e.g., `UTC` or `IST`).
6.  Click **Next**.
7.  Under "Attach to pipelines," select your target pipeline (e.g., `MonthlyReportPipeline`).
8.  Click **Finish**.
9.  **Publish All** your changes in ADF Studio to activate the trigger.

At this point, your `MonthlyReportPipeline` will be scheduled to run every Saturday. The next step is to ensure it only executes its core logic on the *last* Saturday.

### Step 3: Add Date Check Logic Inside Pipeline

To ensure the pipeline's core activities only run on the last Saturday of the month, you'll need to add a conditional check. Since ADF's expression language doesn't have a direct `lastSaturdayOfMonth()` function, you'll simulate this using external logic.

**Option 1: Using an Azure Function / Web Activity (Recommended for robustness)**

This method involves calling an external service (like an Azure Function or a simple web service) that can perform the date calculation.

1.  **Create an Azure Function:**
    * Develop a simple Azure Function (e.g., in Python or C#) that takes a date as input (or uses the current date) and returns `true` if it's the last Saturday of the month, `false` otherwise.
    * **Example Python logic snippet for Azure Function:**
        ```python
        import datetime

        def is_last_saturday_of_month(date_str):
            dt_object = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if dt_object.weekday() == 5:  # 5 represents Saturday
                # Check if adding 7 days moves to the next month
                if (dt_object + datetime.timedelta(days=7)).month != dt_object.month:
                    return True
            return False

        # In your Azure Function's main handler:
        # Check if today is the last Saturday
        # result = is_last_saturday_of_month(datetime.date.today().strftime('%Y-%m-%d'))
        # Return {"isLastSaturday": result}
        ```
2.  **Add a Web Activity or Azure Function Activity in ADF:**
    * Drag either an **Azure Function** activity or a **Web** activity onto your pipeline canvas.
    * Configure it to call your Azure Function, passing `@formatDateTime(utcNow(), 'yyyy-MM-dd')` as a parameter.
    * The expected output should be a boolean (e.g., `{"isLastSaturday": true}`).

3.  **Add an If Condition activity:**
    * Drag an **If Condition** activity onto the pipeline canvas.
    * Connect the success output of your Web/Azure Function activity to this If Condition.
    * In the "Activities" tab of the If Condition, set the **Expression** to:
        ```
        @equals(activity('YourWebActivityName').output.isLastSaturday, true)
        ```
        *(Replace 'YourWebActivityName' with the actual name of your Web or Azure Function activity).*
    * **If True Activities:** Place all your core pipeline activities (e.g., Copy Data, Data Flow, Stored Procedure) inside the "If True" branch.
    * **If False Activities (Optional):** You can add a `Set Variable` activity or `Log` activity here to record that the pipeline skipped execution for the current Saturday.

**Option 2: Using a Stored Procedure/Script Activity (SQL-based calculation)**

This method leverages a SQL stored procedure or script within your database to perform the date calculation.

1.  **Create a Stored Procedure in your Azure SQL Database:**
    ```sql
    CREATE PROCEDURE CheckIfLastSaturdayOfMonth
        @InputDate DATE,
        @IsLastSaturday BIT OUTPUT
    AS
    BEGIN
        SET @IsLastSaturday = 0; -- Default to false

        IF DATENAME(dw, @InputDate) = 'Saturday' -- Check if it's a Saturday
        BEGIN
            -- Check if adding 7 days pushes it into the next month
            IF MONTH(DATEADD(day, 7, @InputDate)) != MONTH(@InputDate)
            BEGIN
                SET @IsLastSaturday = 1; -- It's the last Saturday
            END
        END
    END;
    ```
2.  **Add a Stored Procedure Activity in ADF:**
    * Drag a **Stored Procedure** activity onto your pipeline canvas.
    * Configure its **Linked Service** to your Azure SQL Database.
    * **Stored procedure name:** `CheckIfLastSaturdayOfMonth`
    * **Stored procedure parameters:** Pass the current date:
        ```json
        {
            "InputDate": { "value": "@formatDateTime(utcNow(), 'yyyy-MM-dd')", "type": "Date" },
            "IsLastSaturday": { "value": null, "direction": "Output", "type": "Boolean" }
        }
        ```
        *Note: You need to define `@IsLastSaturday` as an output parameter in the Stored Procedure activity.*

3.  **Add an If Condition activity:**
    * Connect the success output of your Stored Procedure activity to this If Condition.
    * In the "Activities" tab of the If Condition, set the **Expression** to:
        ```
        @equals(activity('YourStoredProcedureActivityName').output.parameters.IsLastSaturday, true)
        ```
        *(Replace 'YourStoredProcedureActivityName' with the actual name of your Stored Procedure activity).*
    * **If True Activities:** Place all your core pipeline activities inside the "If True" branch.
    * **If False Activities (Optional):** Add activities to log a skip.

### Step 4: Deploy and Monitor

1.  **Publish All** your changes in ADF Studio. This will ensure your pipeline with the new logic and the scheduled trigger are deployed.
2.  Go to the **Monitor** tab in ADF.
3.  Observe the **Trigger runs** to confirm that the `LastSaturdayMonthlyTrigger` is firing every Saturday as expected.
4.  Monitor the **Pipeline runs** associated with this trigger.
5.  On Saturdays that are *not* the last Saturday of the month, you should see the pipeline run, but the activities within the "If True" branch should not execute. On the last Saturday of the month, all activities should run successfully.

## Screenshots:

![4.1](/week06/screenshots/task%204-1.png)
![4.2](/week06/screenshots/task%204-2.png)
![4.3](/week06/screenshots/task%204-3.png)


# Task 5: Graceful Data Retrieval Failure Handling with Retry and Wait Logic in Azure Data Factory

## Overview

Transient errors, such as temporary network glitches, database timeouts, or API rate limits, are common when interacting with external data sources. If not handled, these short-lived issues can cause pipeline failures, requiring manual intervention. This guide provides strategies to build self-healing pipelines in ADF by incorporating automated retry and intelligent wait mechanisms, enhancing overall pipeline resilience.

## Steps

Follow these steps to implement robust error handling in your ADF pipelines.

### Step 1: Set Built-in Retry Policies for Activities

Most data movement and transformation activities in ADF (e.g., Copy Data, Lookup, Web, Data Flow) come with built-in retry settings. This is the simplest and first line of defense against transient errors.

1.  Select the activity in your pipeline that is prone to transient failures (e.g., a **Copy Data** activity reading from an FTP server).
2.  Go to the **Settings** tab of the selected activity.
3.  Configure the following properties:
    * **Retry:** Set this to a number greater than 0 (e.g., `3`). This defines how many times ADF should automatically re-attempt the activity if it fails.
    * **Retry interval (seconds):** Specify the delay between each retry attempt (e.g., `30` seconds).

    **Example Configuration:**

    ```
    Retry: 3
    Retry interval: 30 seconds
    ```
    This configuration instructs ADF to automatically retry the activity up to 3 times, waiting 30 seconds between each attempt. If all 3 retries fail, the activity will then officially fail.

### Step 2: Add Wait Activity for Controlled Delay

The `Wait` activity introduces a deliberate pause in your pipeline execution. This is useful for cooling off periods after an error or before re-attempting an operation when you anticipate a temporary resource unavailability.

1.  Drag a **Wait** activity from the "General" section of the Activities pane onto your pipeline canvas.
2.  Go to its **Settings** tab.
3.  Set the **Wait time in seconds** (e.g., `10`).
4.  You can chain a Wait activity using dependency conditions. For instance, if an activity fails, you might have a path that first waits, then tries a different approach or logs the failure.

**Example Use Case:** After a `Web` activity fails due to a rate limit, you could have a `Wait` activity for 60 seconds before attempting a custom retry logic for the `Web` activity.

### Step 3: Use If Condition or Switch for Recovery Logic

For more sophisticated error handling, you can use `If Condition` or `Switch` activities to implement custom recovery logic based on the status of a preceding activity.

1.  Drag an **If Condition** activity onto your pipeline canvas.
2.  Connect the potentially failing activity (e.g., `CopyFromFTP`) to the `If Condition` activity using a **Failed** dependency (the red arrow). This means the `If Condition` will only execute if `CopyFromFTP` fails.
3.  In the `If Condition` activity's **Expression** field, use an ADF expression to check the status of the preceding activity.

    **Example Expression:**

    ```
    @equals(activity('CopyFromFTP').Status,'Failed')
    ```
    *(Replace 'CopyFromFTP' with the actual name of your activity)*

4.  **If True Branch:** Inside the `True` branch of the `If Condition`, you can implement your recovery logic. This might include:
    * A `Wait` activity to pause for a longer duration.
    * A `Set Variable` activity to increment a retry counter.
    * Another attempt at the failing activity (though for simple retries, built-in settings are usually preferred).
    * Logging the failure details to a file or database.
5.  **If False Branch:** This branch would contain the activities that execute if the preceding activity succeeded (i.e., the original path of your pipeline).

### Step 4: Implement Custom Retry Using Until Activity (Advanced)

The `Until` activity allows you to run a set of activities repeatedly until a specified condition is met or a timeout occurs. This is powerful for implementing highly customized retry logic.

1.  Drag an **Until** activity from the "Iteration & Conditionals" section onto your pipeline canvas.
2.  Inside the `Until` activity, place the activity that you want to repeatedly retry (e.g., a `Copy Data` activity named `CopyFromAPI`).
3.  Set the **Expression** for the `Until` activity. This expression determines when the loop should stop.

    **Example Condition:**

    ```
    @equals(activity('CopyFromAPI').Status, 'Succeeded')
    ```
    This means the loop will continue until the `CopyFromAPI` activity successfully completes.

4.  **Add a Wait activity inside the Until loop:**
    * It is crucial to include a `Wait` activity (e.g., `Wait 10 seconds`) inside the `Until` loop. This prevents a tight, uncontrolled loop that could quickly consume resources or hit API limits. Connect the `CopyFromAPI` activity's `Failed` output to the `Wait` activity, and then connect the `Wait` activity back to the `CopyFromAPI` activity (allowing it to re-run in the next iteration of the loop).
5.  Configure the `Until` activity's **Timeout** (e.g., `00:05:00` for 5 minutes) and **Count** (maximum iterations). This acts as a circuit breaker to prevent infinite loops.

    **Example Scenario:**
    * `Until` activity wraps a `Web` activity that calls an external API.
    * If the `Web` activity fails, a `Wait` activity pauses for 30 seconds.
    * The `Web` activity is retried in the next iteration of the `Until` loop.
    * The loop continues for a maximum of 10 attempts or until 5 minutes elapse, whichever comes first.

### Step 5: Test and Monitor

Thorough testing is critical to ensure your retry logic behaves as expected.

1.  **Simulate Failures:** Intentionally cause failures in your source system (e.g., temporarily disconnect an FTP server, introduce a network block to a local SQL Server, or configure an API to return error codes).
2.  **Observe Retry Behavior:**
    * Go to the **Monitor** tab in ADF Studio.
    * Examine the pipeline runs and activity runs. You should see the activities retrying.
    * Check the activity output and status to verify that the retry intervals and counts are respected.
3.  **Check Logs and Alerts:** If you have integrated with Azure Monitor or logging solutions, verify that failure details and retry attempts are being logged.

## Screenshots:

![5.1](/week06/screenshots/task%205.png)
