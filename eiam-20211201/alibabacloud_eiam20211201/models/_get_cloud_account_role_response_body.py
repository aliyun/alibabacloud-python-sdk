# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class GetCloudAccountRoleResponseBody(DaraModel):
    def __init__(
        self,
        cloud_account_role: main_models.GetCloudAccountRoleResponseBodyCloudAccountRole = None,
        request_id: str = None,
    ):
        self.cloud_account_role = cloud_account_role
        self.request_id = request_id

    def validate(self):
        if self.cloud_account_role:
            self.cloud_account_role.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_role is not None:
            result['CloudAccountRole'] = self.cloud_account_role.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountRole') is not None:
            temp_model = main_models.GetCloudAccountRoleResponseBodyCloudAccountRole()
            self.cloud_account_role = temp_model.from_map(m.get('CloudAccountRole'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCloudAccountRoleResponseBodyCloudAccountRole(DaraModel):
    def __init__(
        self,
        cloud_account_id: str = None,
        cloud_account_role_external_id: str = None,
        cloud_account_role_health: str = None,
        cloud_account_role_health_check_result: main_models.GetCloudAccountRoleResponseBodyCloudAccountRoleCloudAccountRoleHealthCheckResult = None,
        cloud_account_role_id: str = None,
        cloud_account_role_name: str = None,
        cloud_account_role_type: str = None,
        cloud_account_role_usage_type: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        status: str = None,
        update_time: int = None,
    ):
        # 云账号ID
        self.cloud_account_id = cloud_account_id
        # 云账号角色外部唯一ID
        self.cloud_account_role_external_id = cloud_account_role_external_id
        # 云账号角色可用性
        self.cloud_account_role_health = cloud_account_role_health
        # 云账号角色验证结果
        self.cloud_account_role_health_check_result = cloud_account_role_health_check_result
        # 云账号角色ID
        self.cloud_account_role_id = cloud_account_role_id
        # 云账号名称
        self.cloud_account_role_name = cloud_account_role_name
        # 云账号角色用途
        self.cloud_account_role_type = cloud_account_role_type
        # 云账号角色类型
        self.cloud_account_role_usage_type = cloud_account_role_usage_type
        self.create_time = create_time
        self.description = description
        # IDaaS EIAM 实例Id
        self.instance_id = instance_id
        # 云账号角色状态
        self.status = status
        self.update_time = update_time

    def validate(self):
        if self.cloud_account_role_health_check_result:
            self.cloud_account_role_health_check_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.cloud_account_role_external_id is not None:
            result['CloudAccountRoleExternalId'] = self.cloud_account_role_external_id

        if self.cloud_account_role_health is not None:
            result['CloudAccountRoleHealth'] = self.cloud_account_role_health

        if self.cloud_account_role_health_check_result is not None:
            result['CloudAccountRoleHealthCheckResult'] = self.cloud_account_role_health_check_result.to_map()

        if self.cloud_account_role_id is not None:
            result['CloudAccountRoleId'] = self.cloud_account_role_id

        if self.cloud_account_role_name is not None:
            result['CloudAccountRoleName'] = self.cloud_account_role_name

        if self.cloud_account_role_type is not None:
            result['CloudAccountRoleType'] = self.cloud_account_role_type

        if self.cloud_account_role_usage_type is not None:
            result['CloudAccountRoleUsageType'] = self.cloud_account_role_usage_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('CloudAccountRoleExternalId') is not None:
            self.cloud_account_role_external_id = m.get('CloudAccountRoleExternalId')

        if m.get('CloudAccountRoleHealth') is not None:
            self.cloud_account_role_health = m.get('CloudAccountRoleHealth')

        if m.get('CloudAccountRoleHealthCheckResult') is not None:
            temp_model = main_models.GetCloudAccountRoleResponseBodyCloudAccountRoleCloudAccountRoleHealthCheckResult()
            self.cloud_account_role_health_check_result = temp_model.from_map(m.get('CloudAccountRoleHealthCheckResult'))

        if m.get('CloudAccountRoleId') is not None:
            self.cloud_account_role_id = m.get('CloudAccountRoleId')

        if m.get('CloudAccountRoleName') is not None:
            self.cloud_account_role_name = m.get('CloudAccountRoleName')

        if m.get('CloudAccountRoleType') is not None:
            self.cloud_account_role_type = m.get('CloudAccountRoleType')

        if m.get('CloudAccountRoleUsageType') is not None:
            self.cloud_account_role_usage_type = m.get('CloudAccountRoleUsageType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetCloudAccountRoleResponseBodyCloudAccountRoleCloudAccountRoleHealthCheckResult(DaraModel):
    def __init__(
        self,
        error_reason: main_models.GetCloudAccountRoleResponseBodyCloudAccountRoleCloudAccountRoleHealthCheckResultErrorReason = None,
        last_check_time: int = None,
        result: str = None,
    ):
        # 错误原因
        self.error_reason = error_reason
        # 检测时间
        self.last_check_time = last_check_time
        # 结果
        self.result = result

    def validate(self):
        if self.error_reason:
            self.error_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_reason is not None:
            result['ErrorReason'] = self.error_reason.to_map()

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorReason') is not None:
            temp_model = main_models.GetCloudAccountRoleResponseBodyCloudAccountRoleCloudAccountRoleHealthCheckResultErrorReason()
            self.error_reason = temp_model.from_map(m.get('ErrorReason'))

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class GetCloudAccountRoleResponseBodyCloudAccountRoleCloudAccountRoleHealthCheckResultErrorReason(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
    ):
        # 错误码
        self.error_code = error_code
        # 错误信息
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

