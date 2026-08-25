# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudsso20210515 import models as main_models
from darabonba.model import DaraModel

class ListPermissionPoliciesInAccessConfigurationResponseBody(DaraModel):
    def __init__(
        self,
        permission_policies: List[main_models.ListPermissionPoliciesInAccessConfigurationResponseBodyPermissionPolicies] = None,
        request_id: str = None,
        total_counts: int = None,
    ):
        # The policies.
        self.permission_policies = permission_policies
        # The request ID.
        self.request_id = request_id
        # The total number of policies.
        self.total_counts = total_counts

    def validate(self):
        if self.permission_policies:
            for v1 in self.permission_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PermissionPolicies'] = []
        if self.permission_policies is not None:
            for k1 in self.permission_policies:
                result['PermissionPolicies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_counts is not None:
            result['TotalCounts'] = self.total_counts

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.permission_policies = []
        if m.get('PermissionPolicies') is not None:
            for k1 in m.get('PermissionPolicies'):
                temp_model = main_models.ListPermissionPoliciesInAccessConfigurationResponseBodyPermissionPolicies()
                self.permission_policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCounts') is not None:
            self.total_counts = m.get('TotalCounts')

        return self

class ListPermissionPoliciesInAccessConfigurationResponseBodyPermissionPolicies(DaraModel):
    def __init__(
        self,
        add_time: str = None,
        permission_policy_document: str = None,
        permission_policy_name: str = None,
        permission_policy_type: str = None,
    ):
        # The time when the policy was created for the access configuration.
        self.add_time = add_time
        # The configurations of the inline policy.
        # 
        # >  This parameter is returned only when the value of the PermissionPolicyType parameter is Inline.
        self.permission_policy_document = permission_policy_document
        # The name of the policy.
        self.permission_policy_name = permission_policy_name
        # The type of the policy.
        self.permission_policy_type = permission_policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_time is not None:
            result['AddTime'] = self.add_time

        if self.permission_policy_document is not None:
            result['PermissionPolicyDocument'] = self.permission_policy_document

        if self.permission_policy_name is not None:
            result['PermissionPolicyName'] = self.permission_policy_name

        if self.permission_policy_type is not None:
            result['PermissionPolicyType'] = self.permission_policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddTime') is not None:
            self.add_time = m.get('AddTime')

        if m.get('PermissionPolicyDocument') is not None:
            self.permission_policy_document = m.get('PermissionPolicyDocument')

        if m.get('PermissionPolicyName') is not None:
            self.permission_policy_name = m.get('PermissionPolicyName')

        if m.get('PermissionPolicyType') is not None:
            self.permission_policy_type = m.get('PermissionPolicyType')

        return self

