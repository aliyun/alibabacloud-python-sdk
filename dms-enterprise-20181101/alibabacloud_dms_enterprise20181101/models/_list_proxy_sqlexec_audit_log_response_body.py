# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListProxySQLExecAuditLogResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        proxy_sqlexec_audit_log_list: main_models.ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The audit information about the database instance that is provided by the secure access proxy feature.
        self.proxy_sqlexec_audit_log_list = proxy_sqlexec_audit_log_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.proxy_sqlexec_audit_log_list:
            self.proxy_sqlexec_audit_log_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.proxy_sqlexec_audit_log_list is not None:
            result['ProxySQLExecAuditLogList'] = self.proxy_sqlexec_audit_log_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('ProxySQLExecAuditLogList') is not None:
            temp_model = main_models.ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogList()
            self.proxy_sqlexec_audit_log_list = temp_model.from_map(m.get('ProxySQLExecAuditLogList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogList(DaraModel):
    def __init__(
        self,
        proxy_sqlexec_audit_log: List[main_models.ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogListProxySQLExecAuditLog] = None,
    ):
        self.proxy_sqlexec_audit_log = proxy_sqlexec_audit_log

    def validate(self):
        if self.proxy_sqlexec_audit_log:
            for v1 in self.proxy_sqlexec_audit_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProxySQLExecAuditLog'] = []
        if self.proxy_sqlexec_audit_log is not None:
            for k1 in self.proxy_sqlexec_audit_log:
                result['ProxySQLExecAuditLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.proxy_sqlexec_audit_log = []
        if m.get('ProxySQLExecAuditLog') is not None:
            for k1 in m.get('ProxySQLExecAuditLog'):
                temp_model = main_models.ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogListProxySQLExecAuditLog()
                self.proxy_sqlexec_audit_log.append(temp_model.from_map(k1))

        return self

class ListProxySQLExecAuditLogResponseBodyProxySQLExecAuditLogListProxySQLExecAuditLog(DaraModel):
    def __init__(
        self,
        affect_rows: int = None,
        elapsed_time: int = None,
        exec_state: str = None,
        instance_id: int = None,
        instance_name: str = None,
        op_time: str = None,
        remark: str = None,
        sql: str = None,
        sqltype: str = None,
        schema_name: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # Indicates the total number of rows returned after the SQL statement was executed. If an SELECT SQL statement is executed, the return value of this parameter indicates the total number of the queried data rows.
        self.affect_rows = affect_rows
        # The amount of time that is consumed to execute the SQL statement. Unit: milliseconds.
        self.elapsed_time = elapsed_time
        # The execution status of the SQL statement. Valid values:
        # 
        # *   **FAIL**: The execution of the SQL statement fails.
        # *   **CANCEL**: The execution of the SQL statement is canceled.
        # *   **SUCCESS**: The SQL statement is executed.
        self.exec_state = exec_state
        # The ID of the database instance.
        self.instance_id = instance_id
        # The name of the database instance.
        self.instance_name = instance_name
        # The time at which the user executes the SQL statement on the database instance. The value of this parameter must be a timestamp that follows the UNIX time format.
        self.op_time = op_time
        # The description.
        self.remark = remark
        # The SQL statement that was executed.
        self.sql = sql
        # The type of the SQL statement. Valid values:
        # 
        # *   **SELECT**
        # *   **INSERT**
        # *   **DELETE**
        # *   **CREATE_TABLE**
        # 
        # >  You can choose Operation Audit > Secure Access Proxy in the top navigation bar of the DMS console to view more types of SQL statements.
        self.sqltype = sqltype
        # The name of the database.
        self.schema_name = schema_name
        # The ID of the user.
        self.user_id = user_id
        # The nickname of the user.
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

        if self.elapsed_time is not None:
            result['ElapsedTime'] = self.elapsed_time

        if self.exec_state is not None:
            result['ExecState'] = self.exec_state

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

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

        if m.get('ElapsedTime') is not None:
            self.elapsed_time = m.get('ElapsedTime')

        if m.get('ExecState') is not None:
            self.exec_state = m.get('ExecState')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

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

