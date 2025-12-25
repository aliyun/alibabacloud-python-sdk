# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListSQLExecAuditLogResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        sqlexec_audit_log_list: main_models.ListSQLExecAuditLogResponseBodySQLExecAuditLogList = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The entries returned.
        self.sqlexec_audit_log_list = sqlexec_audit_log_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.sqlexec_audit_log_list:
            self.sqlexec_audit_log_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sqlexec_audit_log_list is not None:
            result['SQLExecAuditLogList'] = self.sqlexec_audit_log_list.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SQLExecAuditLogList') is not None:
            temp_model = main_models.ListSQLExecAuditLogResponseBodySQLExecAuditLogList()
            self.sqlexec_audit_log_list = temp_model.from_map(m.get('SQLExecAuditLogList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSQLExecAuditLogResponseBodySQLExecAuditLogList(DaraModel):
    def __init__(
        self,
        sqlexec_audit_log: List[main_models.ListSQLExecAuditLogResponseBodySQLExecAuditLogListSQLExecAuditLog] = None,
    ):
        self.sqlexec_audit_log = sqlexec_audit_log

    def validate(self):
        if self.sqlexec_audit_log:
            for v1 in self.sqlexec_audit_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SQLExecAuditLog'] = []
        if self.sqlexec_audit_log is not None:
            for k1 in self.sqlexec_audit_log:
                result['SQLExecAuditLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sqlexec_audit_log = []
        if m.get('SQLExecAuditLog') is not None:
            for k1 in m.get('SQLExecAuditLog'):
                temp_model = main_models.ListSQLExecAuditLogResponseBodySQLExecAuditLogListSQLExecAuditLog()
                self.sqlexec_audit_log.append(temp_model.from_map(k1))

        return self

class ListSQLExecAuditLogResponseBodySQLExecAuditLogListSQLExecAuditLog(DaraModel):
    def __init__(
        self,
        affect_rows: int = None,
        db_id: int = None,
        elapsed_time: int = None,
        exec_state: str = None,
        instance_id: int = None,
        instance_name: str = None,
        logic: bool = None,
        op_time: str = None,
        remark: str = None,
        sql: str = None,
        sqltype: str = None,
        schema_name: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The number of rows affected by the SQL statement. For example, if you execute an SQL statement to query data, the number of retrieved rows is returned.
        self.affect_rows = affect_rows
        # The ID of the database.
        self.db_id = db_id
        # The amount of time consumed by the execution of the SQL statement. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The execution status of the SQL statement. Valid values:
        # 
        # *   **FAIL**: The SQL statement fails to be executed.
        # *   **NOEXE**: The SQL statement has not been executed.
        # *   **RUNNING**: The SQL statement is being executed.
        # *   **CANCEL**: The execution of the SQL statement is canceled.
        # *   **SUCCESS**: The SQL statement is executed.
        self.exec_state = exec_state
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the database.
        # 
        # >  If the SQL statement takes effect on an instance, the name of the instance is returned.
        self.instance_name = instance_name
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is a physical database.
        self.logic = logic
        # The time when the operation specified by the SQL statement was performed on the instance or database.
        self.op_time = op_time
        # The comment on the SQL statement.
        self.remark = remark
        # The SQL statement that was written.
        self.sql = sql
        # The type of the SQL statement. Valid values:
        # 
        # *   **SELECT**: the SQL statement that is used to query data.
        # *   **INSERT**: the SQL statement that is used to insert data.
        # *   **DELETE**: the SQL statement that is used to delete data.
        # *   **CREATE_TABLE**: the SQL statement that is used to create tables.
        # 
        # >  To view more types of SQL statements, log on to the DMS console and click Security and Specifications. In the left-side navigation pane, click **Operation Audit**. Then, you can view all supported types of SQL statements from the **SQL type** drop-down list.
        self.sqltype = sqltype
        # The name of the database.
        self.schema_name = schema_name
        # The ID of the user who wrote the SQL statement.
        self.user_id = user_id
        # The nickname of the user who wrote the SQL statement.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affect_rows is not None:
            result['AffectRows'] = self.affect_rows

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.exec_state is not None:
            result['ExecState'] = self.exec_state

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.op_time is not None:
            result['OpTime'] = self.op_time

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.sql is not None:
            result['SQL'] = self.sql

        if self.sqltype is not None:
            result['SQLType'] = self.sqltype

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffectRows') is not None:
            self.affect_rows = m.get('AffectRows')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('ExecState') is not None:
            self.exec_state = m.get('ExecState')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OpTime') is not None:
            self.op_time = m.get('OpTime')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SQL') is not None:
            self.sql = m.get('SQL')

        if m.get('SQLType') is not None:
            self.sqltype = m.get('SQLType')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

