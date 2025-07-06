-- clear tables from dv01/dv-destination
DELETE FROM Students;
DELETE FROM Teachers;

-- 
CREATE TABLE TableColumnMap (
    TableName NVARCHAR(100),
    ColumnList NVARCHAR(MAX)
);
-- copy tables in tableColumnMap
INSERT INTO TableColumnMap (TableName, ColumnList)
VALUES
('Students', 'StudentID, FirstName'),
('Teachers', 'TeacherID, Subject');

-- lookup > settings > use query > table column map
SELECT TableName, ColumnList FROM TableColumnMap

-- creating dummy table in source dv01-db1
CREATE TABLE DummyTable (
    DummyCol VARCHAR(10)
);

-- override with sql query copy activity in pipeline
@concat('SELECT ', item().ColumnList, ' FROM ', item().TableName)