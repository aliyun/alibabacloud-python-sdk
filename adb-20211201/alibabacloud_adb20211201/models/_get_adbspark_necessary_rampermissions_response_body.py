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
        # The returned result.
        self.data = data
        # The ID of the request.
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
        # When permission check fails, returns diagnostic information related to permission check failure.
        self.denied_detail = denied_detail
        # Check whether the use has the basic permissions to use Analytic DB for Spark.
        # 
        # *   true: The check is passed and the basic permissions are granted.
        # *   false: The check fails and some permissions are missing.
        self.passed = passed
        # Based on diagnostic information, recommends configurations for customers to perform in the RAM system.
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
        # The name of the RAM action that failed the authentication.
        self.action = action
        # The type of the policy denial. Valid values:
        # 
        # *   ImplicitDeny: Resource owner has not configured relevant permission policies for the current user, default denial of unauthorized operations.
        # *   ExplicitDeny: RAM policies configured by the resource owner explicitly deny the current user access to corresponding resources
        self.no_permission_type = no_permission_type
        # The type of the policy that causes the access denied error.
        # 
        # *   ControlPolicy: control policy
        # *   SessionPolicy: Temporary Token additional permission policy
        # *   AssumeRolePolicy: RAM role trust policy
        # *   AccountLevelIdentityBasedPolicy: Principal policy within account authorization scope, including custom policies and system policies
        # *   ResourceGroupLevelIdentityBasedPolicy: Principal policy within resource group authorization scope, including custom policies and system policies.
        self.policy_type = policy_type
        # The identity type of the current user. Valid values:
        # 
        # *   SubUser: a RAM user
        # *   AssumedRoleUser: a RAM role
        self.principal_type = principal_type
        # Authentication object information, can be the current user\\"s RAM account ID, or the role information corresponding to the current visitor.
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

