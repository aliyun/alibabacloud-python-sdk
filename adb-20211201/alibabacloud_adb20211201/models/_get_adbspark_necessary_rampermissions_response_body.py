# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class GetADBSparkNecessaryRAMPermissionsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetADBSparkNecessaryRAMPermissionsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetADBSparkNecessaryRAMPermissionsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetADBSparkNecessaryRAMPermissionsResponseBodyData(DaraModel):
    def __init__(
        self,
        denied_detail: main_models.GetADBSparkNecessaryRAMPermissionsResponseBodyDataDeniedDetail = None,
        passed: bool = None,
        suggestion: str = None,
    ):
        # The diagnostic information returned when the permission check fails.
        self.denied_detail = denied_detail
        # Indicates whether the current user has the basic permissions to use ADB Spark. Valid values:
        # 
        # - true: The check is passed. The user has the basic permissions.
        # - false: The check failed. The user is missing some permissions.
        self.passed = passed
        # The recommended RAM configuration based on the diagnostic information.
        self.suggestion = suggestion

    def validate(self):
        if self.denied_detail:
            self.denied_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.denied_detail is not None:
            result['DeniedDetail'] = self.denied_detail.to_map()

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.suggestion is not None:
            result['Suggestion'] = self.suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeniedDetail') is not None:
            temp_model = main_models.GetADBSparkNecessaryRAMPermissionsResponseBodyDataDeniedDetail()
            self.denied_detail = temp_model.from_map(m.get('DeniedDetail'))

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('Suggestion') is not None:
            self.suggestion = m.get('Suggestion')

        return self

class GetADBSparkNecessaryRAMPermissionsResponseBodyDataDeniedDetail(DaraModel):
    def __init__(
        self,
        action: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
        principal_type: str = None,
        resource_auth_target_info: str = None,
        resource_owner_id: str = None,
    ):
        # The name of the RAM action for which authentication failed.
        self.action = action
        # The type of access policy denial. Valid values:
        # - ImplicitDeny: The resource owner has not configured a relevant access policy for the current user. Unauthorized operations are denied by default.
        # - ExplicitDeny: The RAM policy configured by the resource owner explicitly denies the current user authorization to access the corresponding resource.
        self.no_permission_type = no_permission_type
        # The type of the policy that caused the permission denial. Valid values:
        # - ControlPolicy: control policy.
        # - SessionPolicy: an additional permission policy attached to a temporary token.
        # - AssumeRolePolicy: the trust policy of a RAM role.
        # - AccountLevelIdentityBasedPolicy: an identity-access policy at the account authorization scope, including custom policies and system policies.
        # - ResourceGroupLevelIdentityBasedPolicy: an identity-access policy at the resource group authorization scope, including custom policies and system policies.
        self.policy_type = policy_type
        # The identity type of the current user. Valid values:
        # - SubUser: Resource Access Management (RAM) user.
        # - AssumedRoleUser: RAM role.
        self.principal_type = principal_type
        # The information about the authentication target, which can be the Resource Access Management (RAM) users ID of the current user or the role information of the current accessor.
        self.resource_auth_target_info = resource_auth_target_info
        # The ID of the resource owner.
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type

        if self.resource_auth_target_info is not None:
            result['ResourceAuthTargetInfo'] = self.resource_auth_target_info

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')

        if m.get('ResourceAuthTargetInfo') is not None:
            self.resource_auth_target_info = m.get('ResourceAuthTargetInfo')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

