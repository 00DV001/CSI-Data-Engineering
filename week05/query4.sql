CREATE PROCEDURE dbo.GenerateAndCreateTable
    @TableName NVARCHAR(128)
AS
BEGIN
    DECLARE @SQL NVARCHAR(MAX) = ''

    SELECT @SQL = 'IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = ''' + @TableName + ''')
    BEGIN
        CREATE TABLE [' + @TableName + '] ('

    SELECT @SQL = @SQL +
        COLUMN_NAME + ' ' +
        DATA_TYPE +
        CASE 
            WHEN CHARACTER_MAXIMUM_LENGTH IS NOT NULL AND DATA_TYPE IN ('nvarchar', 'varchar', 'char') THEN '(' + 
                CASE WHEN CHARACTER_MAXIMUM_LENGTH = -1 THEN 'MAX' ELSE CAST(CHARACTER_MAXIMUM_LENGTH AS VARCHAR) END + ')'
            WHEN DATA_TYPE IN ('decimal', 'numeric') THEN '(' + 
                CAST(NUMERIC_PRECISION AS VARCHAR) + ',' + CAST(NUMERIC_SCALE AS VARCHAR) + ')'
            ELSE ''
        END +
        CASE WHEN IS_NULLABLE = 'NO' THEN ' NOT NULL,' ELSE ',' END
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = @TableName

    -- Remove last comma, close the CREATE TABLE
    SET @SQL = LEFT(@SQL, LEN(@SQL) - 1) + ') END'

    EXEC sp_executesql @SQL
END