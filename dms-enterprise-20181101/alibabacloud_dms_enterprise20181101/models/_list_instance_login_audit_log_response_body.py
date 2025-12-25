# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListInstanceLoginAuditLogResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        instance_login_audit_log_list: main_models.ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The logon records of the instance.
        self.instance_login_audit_log_list = instance_login_audit_log_list
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
        if self.instance_login_audit_log_list:
            self.instance_login_audit_log_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_login_audit_log_list is not None:
            result['InstanceLoginAuditLogList'] = self.instance_login_audit_log_list.to_map()

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

        if m.get('InstanceLoginAuditLogList') is not None:
            temp_model = main_models.ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogList()
            self.instance_login_audit_log_list = temp_model.from_map(m.get('InstanceLoginAuditLogList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogList(DaraModel):
    def __init__(
        self,
        instance_login_audit_log: List[main_models.ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogListInstanceLoginAuditLog] = None,
    ):
        self.instance_login_audit_log = instance_login_audit_log

    def validate(self):
        if self.instance_login_audit_log:
            for v1 in self.instance_login_audit_log:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InstanceLoginAuditLog'] = []
        if self.instance_login_audit_log is not None:
            for k1 in self.instance_login_audit_log:
                result['InstanceLoginAuditLog'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instance_login_audit_log = []
        if m.get('InstanceLoginAuditLog') is not None:
            for k1 in m.get('InstanceLoginAuditLog'):
                temp_model = main_models.ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogListInstanceLoginAuditLog()
                self.instance_login_audit_log.append(temp_model.from_map(k1))

        return self

class ListInstanceLoginAuditLogResponseBodyInstanceLoginAuditLogListInstanceLoginAuditLog(DaraModel):
    def __init__(
        self,
        db_user: str = None,
        instance_id: int = None,
        instance_name: str = None,
        op_time: str = None,
        request_ip: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The database account that is used to log on to the instance.
        self.db_user = db_user
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance.
        self.instance_name = instance_name
        # The time when the user performed an operation on the instance.
        self.op_time = op_time
        # The source IP address of the request.
        self.request_ip = request_ip
        # The ID of the user.
        self.user_id = user_id
        # The alias of the user.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_user is not None:
            result['DbUser'] = self.db_user

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.op_time is not None:
            result['OpTime'] = self.op_time

        if self.request_ip is not None:
            result['RequestIp'] = self.request_ip

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbUser') is not None:
            self.db_user = m.get('DbUser')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('OpTime') is not None:
            self.op_time = m.get('OpTime')

        if m.get('RequestIp') is not None:
            self.request_ip = m.get('RequestIp')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

