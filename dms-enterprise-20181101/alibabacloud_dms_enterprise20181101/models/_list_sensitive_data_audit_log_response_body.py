# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListSensitiveDataAuditLogResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        sensitive_data_audit_log_list: List[main_models.ListSensitiveDataAuditLogResponseBodySensitiveDataAuditLogList] = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The audit logs for sensitive data.
        self.sensitive_data_audit_log_list = sensitive_data_audit_log_list
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.sensitive_data_audit_log_list:
            for v1 in self.sensitive_data_audit_log_list:
                 if v1:
                    v1.validate()

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

        result['SensitiveDataAuditLogList'] = []
        if self.sensitive_data_audit_log_list is not None:
            for k1 in self.sensitive_data_audit_log_list:
                result['SensitiveDataAuditLogList'].append(k1.to_map() if k1 else None)

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

        self.sensitive_data_audit_log_list = []
        if m.get('SensitiveDataAuditLogList') is not None:
            for k1 in m.get('SensitiveDataAuditLogList'):
                temp_model = main_models.ListSensitiveDataAuditLogResponseBodySensitiveDataAuditLogList()
                self.sensitive_data_audit_log_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSensitiveDataAuditLogResponseBodySensitiveDataAuditLogList(DaraModel):
    def __init__(
        self,
        db_display_name: str = None,
        instance_id: int = None,
        module_name: str = None,
        op_time: str = None,
        sensitive_data_log: List[main_models.ListSensitiveDataAuditLogResponseBodySensitiveDataAuditLogListSensitiveDataLog] = None,
        target_name: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The name of the database that stores the sensitive data.
        self.db_display_name = db_display_name
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the function module whose audit logs were queried.
        self.module_name = module_name
        # The time when the operation was performed. The time is in the yyyy-MM-DD HH:mm:ss format.
        self.op_time = op_time
        # The logs for sensitive data.
        self.sensitive_data_log = sensitive_data_log
        # The details of the object on which the operation was performed. The value of this parameter is in one of the following formats:
        # 
        # *   Object name - object ID
        # *   Object name (object ID)
        self.target_name = target_name
        # The user ID of the requester.
        self.user_id = user_id
        # The username of the requester.
        self.user_name = user_name

    def validate(self):
        if self.sensitive_data_log:
            for v1 in self.sensitive_data_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_display_name is not None:
            result['DbDisplayName'] = self.db_display_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.module_name is not None:
            result['ModuleName'] = self.module_name

        if self.op_time is not None:
            result['OpTime'] = self.op_time

        result['SensitiveDataLog'] = []
        if self.sensitive_data_log is not None:
            for k1 in self.sensitive_data_log:
                result['SensitiveDataLog'].append(k1.to_map() if k1 else None)

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbDisplayName') is not None:
            self.db_display_name = m.get('DbDisplayName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')

        if m.get('OpTime') is not None:
            self.op_time = m.get('OpTime')

        self.sensitive_data_log = []
        if m.get('SensitiveDataLog') is not None:
            for k1 in m.get('SensitiveDataLog'):
                temp_model = main_models.ListSensitiveDataAuditLogResponseBodySensitiveDataAuditLogListSensitiveDataLog()
                self.sensitive_data_log.append(temp_model.from_map(k1))

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class ListSensitiveDataAuditLogResponseBodySensitiveDataAuditLogListSensitiveDataLog(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        column_permission_type: str = None,
        desensitization_rule: str = None,
        security_level: str = None,
        table_name: str = None,
    ):
        # The name of the column that contains sensitive data.
        self.column_name = column_name
        # The permission that the user has on the column. Valid values:
        # 
        # *   **No permission**
        # *   **Partial redaction**
        # *   **Plaintext**
        # *   **Change**
        # *   **Enable data masking**
        # *   **Disable data masking**
        self.column_permission_type = column_permission_type
        # The algorithm used for data masking.
        self.desensitization_rule = desensitization_rule
        # The sensitivity level of the data. Valid values:
        # 
        # *   **Low**
        # *   **Medium**
        # *   **High**
        self.security_level = security_level
        # The name of the table that stores the sensitive data.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_permission_type is not None:
            result['ColumnPermissionType'] = self.column_permission_type

        if self.desensitization_rule is not None:
            result['DesensitizationRule'] = self.desensitization_rule

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnPermissionType') is not None:
            self.column_permission_type = m.get('ColumnPermissionType')

        if m.get('DesensitizationRule') is not None:
            self.desensitization_rule = m.get('DesensitizationRule')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

