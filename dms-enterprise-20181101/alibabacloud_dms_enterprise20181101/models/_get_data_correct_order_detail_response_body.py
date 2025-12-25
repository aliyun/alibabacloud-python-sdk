# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetDataCorrectOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        data_correct_order_detail: main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetail = None,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The information about the data change ticket.
        self.data_correct_order_detail = data_correct_order_detail
        # The error code returned if the request fails.
        self.error_code = error_code
        # The error message returned if the request fails.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data_correct_order_detail:
            self.data_correct_order_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_correct_order_detail is not None:
            result['DataCorrectOrderDetail'] = self.data_correct_order_detail.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataCorrectOrderDetail') is not None:
            temp_model = main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetail()
            self.data_correct_order_detail = temp_model.from_map(m.get('DataCorrectOrderDetail'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetail(DaraModel):
    def __init__(
        self,
        config_detail: main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailConfigDetail = None,
        database_list: main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseList = None,
        exec_mode: str = None,
        order_detail: main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailOrderDetail = None,
        pre_check_detail: main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetail = None,
        status: str = None,
    ):
        # The configurations of the ticket. This parameter is used to store the configuration information specific to a data change ticket type.
        self.config_detail = config_detail
        # The information about the database in which data is changed.
        self.database_list = database_list
        # The execution mode of the ticket after the ticket is approved. Valid values:
        # 
        # - **COMMITOR**: The data change is performed by the user who submits the ticket.
        # - **AUTO**: The data change is automatically performed after the ticket is approved.
        # - **LAST_AUDITOR**: The data change is performed by the last approver of the ticket.
        self.exec_mode = exec_mode
        # The details of the ticket.
        self.order_detail = order_detail
        # The precheck details of the ticket.
        self.pre_check_detail = pre_check_detail
        # The specific state of the data change ticket. Valid values:
        # 
        # >  The state of the ticket is not exactly equivalent to the status code for the ticket. To query the status code of the ticket, you can call the [GetOrderBaseInfo](https://help.aliyun.com/document_detail/465868.html) operation and check the value of StatusCode in the response.
        # 
        # *   **new**: The ticket is created.
        # *   **precheck**: The ticket is in the pre-check phase.
        # *   **precheckFailed**: The ticket failed to pass the precheck.
        # *   **precheck_success**: The ticket passes the precheck and waits to be submitted for approval.
        # *   **toaudit**: The ticket is being reviewed.
        # *   **Approved**: The ticket is approved.
        # *   **reject**: The ticket is rejected.
        # *   **waiting**: The task is submitted and waits to be scheduled.
        # *   **processing**: The task is being executed.
        # *   **Success**: The task is successful.
        self.status = status

    def validate(self):
        if self.config_detail:
            self.config_detail.validate()
        if self.database_list:
            self.database_list.validate()
        if self.order_detail:
            self.order_detail.validate()
        if self.pre_check_detail:
            self.pre_check_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_detail is not None:
            result['ConfigDetail'] = self.config_detail.to_map()

        if self.database_list is not None:
            result['DatabaseList'] = self.database_list.to_map()

        if self.exec_mode is not None:
            result['ExecMode'] = self.exec_mode

        if self.order_detail is not None:
            result['OrderDetail'] = self.order_detail.to_map()

        if self.pre_check_detail is not None:
            result['PreCheckDetail'] = self.pre_check_detail.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigDetail') is not None:
            temp_model = main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailConfigDetail()
            self.config_detail = temp_model.from_map(m.get('ConfigDetail'))

        if m.get('DatabaseList') is not None:
            temp_model = main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseList()
            self.database_list = temp_model.from_map(m.get('DatabaseList'))

        if m.get('ExecMode') is not None:
            self.exec_mode = m.get('ExecMode')

        if m.get('OrderDetail') is not None:
            temp_model = main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailOrderDetail()
            self.order_detail = temp_model.from_map(m.get('OrderDetail'))

        if m.get('PreCheckDetail') is not None:
            temp_model = main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetail()
            self.pre_check_detail = temp_model.from_map(m.get('PreCheckDetail'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetail(DaraModel):
    def __init__(
        self,
        task_check_do: List[main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetailTaskCheckDO] = None,
    ):
        self.task_check_do = task_check_do

    def validate(self):
        if self.task_check_do:
            for v1 in self.task_check_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TaskCheckDO'] = []
        if self.task_check_do is not None:
            for k1 in self.task_check_do:
                result['TaskCheckDO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_check_do = []
        if m.get('TaskCheckDO') is not None:
            for k1 in m.get('TaskCheckDO'):
                temp_model = main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetailTaskCheckDO()
                self.task_check_do.append(temp_model.from_map(k1))

        return self

class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailPreCheckDetailTaskCheckDO(DaraModel):
    def __init__(
        self,
        check_status: str = None,
        check_step: str = None,
        user_tip: str = None,
    ):
        # The state of the precheck. Valid values:
        # 
        # *   **WAITING**: The ticket is pending precheck.
        # *   **RUNNING**: The ticket is being prechecked.
        # *   **SUCCESS**: The ticket passes the precheck.
        # *   **FAIL**: The ticket fails the precheck.
        self.check_status = check_status
        # The check step of the precheck. Valid values:
        # 
        # *   **SQL_PARSE**: The system checks the syntax of the SQL statement.
        # *   **SQL_TYPE_CHECK**: The system checks the type of the SQL statement.
        # *   **PERMISSION_CHECK**: The system checks the permissions required for the data change.
        # *   **ROW_CHECK**: The system checks the number of affected rows.
        self.check_step = check_step
        # The message that appears when a check step is executed.
        self.user_tip = user_tip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_status is not None:
            result['CheckStatus'] = self.check_status

        if self.check_step is not None:
            result['CheckStep'] = self.check_step

        if self.user_tip is not None:
            result['UserTip'] = self.user_tip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatus') is not None:
            self.check_status = m.get('CheckStatus')

        if m.get('CheckStep') is not None:
            self.check_step = m.get('CheckStep')

        if m.get('UserTip') is not None:
            self.user_tip = m.get('UserTip')

        return self

class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailOrderDetail(DaraModel):
    def __init__(
        self,
        actual_affect_rows: int = None,
        attachment_name: str = None,
        classify: str = None,
        estimate_affect_rows: int = None,
        exe_sql: str = None,
        ignore_affect_rows: bool = None,
        ignore_affect_rows_reason: str = None,
        rb_attachment_name: str = None,
        rb_sql: str = None,
        rb_sqltype: str = None,
        sql_type: str = None,
    ):
        # The number of affected rows that is obtained by the precheck.
        self.actual_affect_rows = actual_affect_rows
        # The name of the attachment that contains the SQL statements used to change data.
        self.attachment_name = attachment_name
        # The category of the reason for the data change.
        self.classify = classify
        # The estimated number of affected rows.
        self.estimate_affect_rows = estimate_affect_rows
        # The executed SQL statements.
        self.exe_sql = exe_sql
        # Indicates whether the precheck result is ignored. Valid values:
        # 
        # - **true**: The precheck result is ignored.
        # - **false**: The precheck result is not ignored.
        self.ignore_affect_rows = ignore_affect_rows
        # The reason why the precheck result is ignored.
        self.ignore_affect_rows_reason = ignore_affect_rows_reason
        # The name of the attachment that contains the SQL statements used to roll back the data change.
        self.rb_attachment_name = rb_attachment_name
        # The SQL statements used to roll back the data change.
        self.rb_sql = rb_sql
        # The format of the SQL statements used to roll back the data change. Valid values:
        # 
        # - **TEXT**: text
        # - **ATTACHMENT**: attachment
        self.rb_sqltype = rb_sqltype
        # The format of the SQL statements used to change data. Valid values:
        # 
        # - **TEXT**: text
        # - **ATTACHMENT**: attachment
        self.sql_type = sql_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_affect_rows is not None:
            result['ActualAffectRows'] = self.actual_affect_rows

        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name

        if self.classify is not None:
            result['Classify'] = self.classify

        if self.estimate_affect_rows is not None:
            result['EstimateAffectRows'] = self.estimate_affect_rows

        if self.exe_sql is not None:
            result['ExeSQL'] = self.exe_sql

        if self.ignore_affect_rows is not None:
            result['IgnoreAffectRows'] = self.ignore_affect_rows

        if self.ignore_affect_rows_reason is not None:
            result['IgnoreAffectRowsReason'] = self.ignore_affect_rows_reason

        if self.rb_attachment_name is not None:
            result['RbAttachmentName'] = self.rb_attachment_name

        if self.rb_sql is not None:
            result['RbSQL'] = self.rb_sql

        if self.rb_sqltype is not None:
            result['RbSQLType'] = self.rb_sqltype

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualAffectRows') is not None:
            self.actual_affect_rows = m.get('ActualAffectRows')

        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')

        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('EstimateAffectRows') is not None:
            self.estimate_affect_rows = m.get('EstimateAffectRows')

        if m.get('ExeSQL') is not None:
            self.exe_sql = m.get('ExeSQL')

        if m.get('IgnoreAffectRows') is not None:
            self.ignore_affect_rows = m.get('IgnoreAffectRows')

        if m.get('IgnoreAffectRowsReason') is not None:
            self.ignore_affect_rows_reason = m.get('IgnoreAffectRowsReason')

        if m.get('RbAttachmentName') is not None:
            self.rb_attachment_name = m.get('RbAttachmentName')

        if m.get('RbSQL') is not None:
            self.rb_sql = m.get('RbSQL')

        if m.get('RbSQLType') is not None:
            self.rb_sqltype = m.get('RbSQLType')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        return self

class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseList(DaraModel):
    def __init__(
        self,
        database: List[main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseListDatabase] = None,
    ):
        self.database = database

    def validate(self):
        if self.database:
            for v1 in self.database:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Database'] = []
        if self.database is not None:
            for k1 in self.database:
                result['Database'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.database = []
        if m.get('Database') is not None:
            for k1 in m.get('Database'):
                temp_model = main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseListDatabase()
                self.database.append(temp_model.from_map(k1))

        return self

class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailDatabaseListDatabase(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        search_name: str = None,
    ):
        # The database ID.
        self.db_id = db_id
        # The engine of the database.
        self.db_type = db_type
        # The type of the environment to which the database belongs. Valid values:
        # 
        # *   product: production environment.
        # *   dev: development environment.
        # *   pre: pre-release environment.
        # *   test: test environment.
        # *   sit: system integration testing (SIT) environment
        # *   uat: user acceptance testing (UAT) environment.
        # *   pet: stress testing environment.
        # *   stag: staging environment.
        self.env_type = env_type
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true.**: The database is a logical database.
        # *   **false**: The database is a physical database.
        self.logic = logic
        # The name that is used to search for the database.
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailConfigDetail(DaraModel):
    def __init__(
        self,
        cron: bool = None,
        cron_call_times: int = None,
        cron_ext_config: main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailConfigDetailCronExtConfig = None,
        cron_format: str = None,
        cron_last_call_start_time: str = None,
        cron_next_call_time: str = None,
        cron_status: str = None,
        csv_table_name: str = None,
        current_task_id: int = None,
        detail_type: str = None,
        duration: int = None,
        file_encoding: str = None,
        file_type: str = None,
        import_ext_config: main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailConfigDetailImportExtConfig = None,
    ):
        # Indicates whether the task is a scheduled task for historical data cleanup. This parameter is a reserved parameter and is valid only if the value of DetailType is CRON_CLEAR_DATA.
        self.cron = cron
        # The number of times the scheduled task is run. This parameter is valid only if the value of DetailType is CRON_CLEAR_DATA.
        self.cron_call_times = cron_call_times
        # The additional configuration information about historical data cleanup. This parameter is valid only if the value of DetailType is CRON_CLEAR_DATA.
        self.cron_ext_config = cron_ext_config
        # The CRON expression of the scheduled task. This parameter is valid only if the value of DetailType is CRON_CLEAR_DATA.
        self.cron_format = cron_format
        # The time when the task was last run.
        self.cron_last_call_start_time = cron_last_call_start_time
        # The time when the task is run next time. This parameter is returned only if the value of CronStatus is SUCCESS.
        self.cron_next_call_time = cron_next_call_time
        # The state of the scheduled task. If this parameter is empty, the task is not run. Valid values:
        # 
        # *   PAUSE: The task is suspended.
        # *   WAITING: The task is waiting to be run.
        # *   SUCCESS: The task is run.
        self.cron_status = cron_status
        # The name of the table to which data is to be imported. This parameter is valid only if the value of DetailType is BIG_FILE. If the value of FileType is SQL, this parameter is empty.
        self.csv_table_name = csv_table_name
        # The ID of the current data change task. This is a reserved parameter and can be ignored.
        self.current_task_id = current_task_id
        # The type of the ticket. Valid values:
        # 
        # *   COMMON: regular data change.
        # *   CHUNK_DML: lock-free data change.
        # *   BIG_FILE: large data import.
        # *   CRON_CLEAR_DATA: historical data cleanup.
        # *   PROCEDURE: programmable object change.
        self.detail_type = detail_type
        # The execution duration of the scheduled task. Unit: hour. This parameter is valid only if the value of DetailType is CRON_CLEAR_DATA. If the value is greater than 0, an execution duration is set.
        self.duration = duration
        # The encoding method of the file. This parameter may be empty, which indicates the value of AUTO. Valid values:
        # 
        # *   **AUTO**: automatic identification.
        # *   **UTF-8**: UTF-8 encoding.
        # *   **GBK**: GBK encoding.
        # *   **ISO-8859-1**: ISO-8859-1 encoding.
        self.file_encoding = file_encoding
        # The type of the file to be imported. This parameter is valid if the value of DetailType is BIG_FILE. Valid values:
        # 
        # *   **SQL**: an SQL file.
        # *   **CSV**: a CSV file.
        # *   **EXCEL**: an Excel file.
        # *   **JSON**: a JSON file, which is supported only by MongoDB databases.
        self.file_type = file_type
        # The additional configuration information about data import. This parameter is valid if the value of DetailType is BIG_FILE.
        self.import_ext_config = import_ext_config

    def validate(self):
        if self.cron_ext_config:
            self.cron_ext_config.validate()
        if self.import_ext_config:
            self.import_ext_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cron is not None:
            result['Cron'] = self.cron

        if self.cron_call_times is not None:
            result['CronCallTimes'] = self.cron_call_times

        if self.cron_ext_config is not None:
            result['CronExtConfig'] = self.cron_ext_config.to_map()

        if self.cron_format is not None:
            result['CronFormat'] = self.cron_format

        if self.cron_last_call_start_time is not None:
            result['CronLastCallStartTime'] = self.cron_last_call_start_time

        if self.cron_next_call_time is not None:
            result['CronNextCallTime'] = self.cron_next_call_time

        if self.cron_status is not None:
            result['CronStatus'] = self.cron_status

        if self.csv_table_name is not None:
            result['CsvTableName'] = self.csv_table_name

        if self.current_task_id is not None:
            result['CurrentTaskId'] = self.current_task_id

        if self.detail_type is not None:
            result['DetailType'] = self.detail_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.file_encoding is not None:
            result['FileEncoding'] = self.file_encoding

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.import_ext_config is not None:
            result['ImportExtConfig'] = self.import_ext_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')

        if m.get('CronCallTimes') is not None:
            self.cron_call_times = m.get('CronCallTimes')

        if m.get('CronExtConfig') is not None:
            temp_model = main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailConfigDetailCronExtConfig()
            self.cron_ext_config = temp_model.from_map(m.get('CronExtConfig'))

        if m.get('CronFormat') is not None:
            self.cron_format = m.get('CronFormat')

        if m.get('CronLastCallStartTime') is not None:
            self.cron_last_call_start_time = m.get('CronLastCallStartTime')

        if m.get('CronNextCallTime') is not None:
            self.cron_next_call_time = m.get('CronNextCallTime')

        if m.get('CronStatus') is not None:
            self.cron_status = m.get('CronStatus')

        if m.get('CsvTableName') is not None:
            self.csv_table_name = m.get('CsvTableName')

        if m.get('CurrentTaskId') is not None:
            self.current_task_id = m.get('CurrentTaskId')

        if m.get('DetailType') is not None:
            self.detail_type = m.get('DetailType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FileEncoding') is not None:
            self.file_encoding = m.get('FileEncoding')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('ImportExtConfig') is not None:
            temp_model = main_models.GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailConfigDetailImportExtConfig()
            self.import_ext_config = temp_model.from_map(m.get('ImportExtConfig'))

        return self

class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailConfigDetailImportExtConfig(DaraModel):
    def __init__(
        self,
        csv_first_row_is_column_def: bool = None,
        ignore_error: bool = None,
        import_mode: str = None,
        insert_type: str = None,
    ):
        # Indicates whether the first row of the CSV file contains field names. Valid values:
        # 
        # *   **true**: The first row in the CSV file contains field names.
        # *   **false**: The first row in the CSV file contains data.
        # 
        # >  This parameter is valid if the value of **FileType** is **CSV** or **EXCEL**.
        self.csv_first_row_is_column_def = csv_first_row_is_column_def
        # Indicates whether an error that occurs is ignored. Valid values:
        # 
        # *   **true**: If an error occurs when SQL statements are being executed, DMS skips the current SQL statement and continues to execute subsequent SQL statements.
        # *   **false**: If an error occurs when SQL statements are being executed, DMS stops executing subsequent SQL statements.
        self.ignore_error = ignore_error
        # The import mode. Valid values:
        # 
        # *   **FAST_MODE**: fast mode. In the Execute step, the uploaded file is read and SQL statements are executed to import data to the specified destination database. Compared with the security mode, this mode can be used to import data in a less secure but more efficient manner.
        # *   **SAFE_MODE**: security mode. In the Precheck step, the uploaded file is parsed, and SQL statements or CSV file data is cached. In the Execute step, the cached SQL statements are read and executed to import data, or the cached CSV file data is read and imported to the specified destination database. Compared with the fast mode, this mode can be used to import data in a more secure but less efficient manner.
        self.import_mode = import_mode
        # The mode in which data is to be imported to the destination table. Valid values:
        # 
        # *   **INSERT**: The database checks the primary key during data insertion. If the primary key is duplicated, an error is reported.
        # *   **INSERT_IGNORE**: If the imported data contains data records that are the same as those in the destination table, the new data records are ignored.
        # *   **REPLACE_INTO**: If the imported data contains a row that has the same value for the primary key or unique index as an existing row in the destination table, the system deletes the existing row and inserts the new row into the destination table.
        # 
        # >  This parameter is valid if the value of FileType is CSV or EXCEL.
        self.insert_type = insert_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.csv_first_row_is_column_def is not None:
            result['CsvFirstRowIsColumnDef'] = self.csv_first_row_is_column_def

        if self.ignore_error is not None:
            result['IgnoreError'] = self.ignore_error

        if self.import_mode is not None:
            result['ImportMode'] = self.import_mode

        if self.insert_type is not None:
            result['InsertType'] = self.insert_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CsvFirstRowIsColumnDef') is not None:
            self.csv_first_row_is_column_def = m.get('CsvFirstRowIsColumnDef')

        if m.get('IgnoreError') is not None:
            self.ignore_error = m.get('IgnoreError')

        if m.get('ImportMode') is not None:
            self.import_mode = m.get('ImportMode')

        if m.get('InsertType') is not None:
            self.insert_type = m.get('InsertType')

        return self

class GetDataCorrectOrderDetailResponseBodyDataCorrectOrderDetailConfigDetailCronExtConfig(DaraModel):
    def __init__(
        self,
        current_clear_task_count: int = None,
        optimize_table_after_every_clear_times: int = None,
    ):
        # The number of times defragmentation is performed. This parameter is valid only if the value of OptimizeTableAfterEveryClearTimes is greater than 0.
        self.current_clear_task_count = current_clear_task_count
        # Indicates whether the Periodically Optimize Table feature is enabled. Valid values:
        # 
        # *   **0** (default): The feature is disabled.
        # *   **A value greater than 0**: The feature is enabled. The value indicates the number of cleanups after which the system performs defragmentation.
        self.optimize_table_after_every_clear_times = optimize_table_after_every_clear_times

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_clear_task_count is not None:
            result['CurrentClearTaskCount'] = self.current_clear_task_count

        if self.optimize_table_after_every_clear_times is not None:
            result['OptimizeTableAfterEveryClearTimes'] = self.optimize_table_after_every_clear_times

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentClearTaskCount') is not None:
            self.current_clear_task_count = m.get('CurrentClearTaskCount')

        if m.get('OptimizeTableAfterEveryClearTimes') is not None:
            self.optimize_table_after_every_clear_times = m.get('OptimizeTableAfterEveryClearTimes')

        return self

