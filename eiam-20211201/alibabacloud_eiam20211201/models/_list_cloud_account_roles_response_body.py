# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListCloudAccountRolesResponseBody(DaraModel):
    def __init__(
        self,
        cloud_account_roles: List[main_models.ListCloudAccountRolesResponseBodyCloudAccountRoles] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of cloud roles.
        self.cloud_account_roles = cloud_account_roles
        # The number of entries returned per page.
        self.max_results = max_results
        # The query token returned in this call.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.cloud_account_roles:
            for v1 in self.cloud_account_roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudAccountRoles'] = []
        if self.cloud_account_roles is not None:
            for k1 in self.cloud_account_roles:
                result['CloudAccountRoles'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_account_roles = []
        if m.get('CloudAccountRoles') is not None:
            for k1 in m.get('CloudAccountRoles'):
                temp_model = main_models.ListCloudAccountRolesResponseBodyCloudAccountRoles()
                self.cloud_account_roles.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCloudAccountRolesResponseBodyCloudAccountRoles(DaraModel):
    def __init__(
        self,
        cloud_account_id: str = None,
        cloud_account_role_external_id: str = None,
        cloud_account_role_health: str = None,
        cloud_account_role_health_check_result: main_models.ListCloudAccountRolesResponseBodyCloudAccountRolesCloudAccountRoleHealthCheckResult = None,
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
        # The ID of the Alibaba Cloud account.
        self.cloud_account_id = cloud_account_id
        # The external ID for the cloud role.
        self.cloud_account_role_external_id = cloud_account_role_external_id
        # The health status of the cloud role. Valid values:
        # 
        # - healthy: The role is healthy.
        # 
        # - unhealthy: The role is unhealthy.
        # 
        # - unknown: The health status is unknown.
        self.cloud_account_role_health = cloud_account_role_health
        # The result of the health check for the cloud role.
        self.cloud_account_role_health_check_result = cloud_account_role_health_check_result
        # The ID of the cloud role.
        self.cloud_account_role_id = cloud_account_role_id
        # The name of the cloud role.
        self.cloud_account_role_name = cloud_account_role_name
        # The type of the cloud role. The format of the role type varies based on the type of the cloud account. The following value is supported:
        # 
        # - role: This value applies to Alibaba Cloud accounts.
        self.cloud_account_role_type = cloud_account_role_type
        # The usage type of the cloud role. Valid values:
        # 
        # - system: The role is used by the system.
        # 
        # - user: The role is used by a user.
        self.cloud_account_role_usage_type = cloud_account_role_usage_type
        # The time when the role was created. This is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The description of the cloud role.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The status of the cloud role. Valid values:
        # 
        # - enabled: The role is enabled.
        # 
        # - disabled: The role is disabled.
        self.status = status
        # The time when the role was last updated. This is a UNIX timestamp. Unit: milliseconds.
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
            temp_model = main_models.ListCloudAccountRolesResponseBodyCloudAccountRolesCloudAccountRoleHealthCheckResult()
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

class ListCloudAccountRolesResponseBodyCloudAccountRolesCloudAccountRoleHealthCheckResult(DaraModel):
    def __init__(
        self,
        error_reason: main_models.ListCloudAccountRolesResponseBodyCloudAccountRolesCloudAccountRoleHealthCheckResultErrorReason = None,
        last_check_time: int = None,
        result: str = None,
    ):
        # The reason for the error. This parameter is returned when the health check status is unhealthy.
        self.error_reason = error_reason
        # The time of the last health check. This is a UNIX timestamp. Unit: milliseconds.
        self.last_check_time = last_check_time
        # The result of the health check. Valid values:
        # 
        # - success: The health check was successful.
        # 
        # - failed: The health check failed.
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
            temp_model = main_models.ListCloudAccountRolesResponseBodyCloudAccountRolesCloudAccountRoleHealthCheckResultErrorReason()
            self.error_reason = temp_model.from_map(m.get('ErrorReason'))

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class ListCloudAccountRolesResponseBodyCloudAccountRolesCloudAccountRoleHealthCheckResultErrorReason(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
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

