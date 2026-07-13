# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class GetProtectionPolicyResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetProtectionPolicyResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The unique ID of the request.
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
            temp_model = main_models.GetProtectionPolicyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetProtectionPolicyResponseBodyData(DaraModel):
    def __init__(
        self,
        bound_resource_category_ids: List[str] = None,
        latest_apply_time: int = None,
        latest_task_id: str = None,
        protection_policy_id: str = None,
        protection_policy_name: str = None,
        protection_policy_region_id: str = None,
        sub_protection_policies: List[main_models.GetProtectionPolicyResponseBodyDataSubProtectionPolicies] = None,
    ):
        # The list of associated resource category IDs.
        self.bound_resource_category_ids = bound_resource_category_ids
        # The time when the policy was last applied.
        self.latest_apply_time = latest_apply_time
        # The ID of the latest application task.
        self.latest_task_id = latest_task_id
        # The protection policy ID.
        self.protection_policy_id = protection_policy_id
        # The protection policy name.
        self.protection_policy_name = protection_policy_name
        # The region ID of the protection policy.
        self.protection_policy_region_id = protection_policy_region_id
        # The list of configured sub-protection policies.
        self.sub_protection_policies = sub_protection_policies

    def validate(self):
        if self.sub_protection_policies:
            for v1 in self.sub_protection_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound_resource_category_ids is not None:
            result['BoundResourceCategoryIds'] = self.bound_resource_category_ids

        if self.latest_apply_time is not None:
            result['LatestApplyTime'] = self.latest_apply_time

        if self.latest_task_id is not None:
            result['LatestTaskId'] = self.latest_task_id

        if self.protection_policy_id is not None:
            result['ProtectionPolicyId'] = self.protection_policy_id

        if self.protection_policy_name is not None:
            result['ProtectionPolicyName'] = self.protection_policy_name

        if self.protection_policy_region_id is not None:
            result['ProtectionPolicyRegionId'] = self.protection_policy_region_id

        result['SubProtectionPolicies'] = []
        if self.sub_protection_policies is not None:
            for k1 in self.sub_protection_policies:
                result['SubProtectionPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundResourceCategoryIds') is not None:
            self.bound_resource_category_ids = m.get('BoundResourceCategoryIds')

        if m.get('LatestApplyTime') is not None:
            self.latest_apply_time = m.get('LatestApplyTime')

        if m.get('LatestTaskId') is not None:
            self.latest_task_id = m.get('LatestTaskId')

        if m.get('ProtectionPolicyId') is not None:
            self.protection_policy_id = m.get('ProtectionPolicyId')

        if m.get('ProtectionPolicyName') is not None:
            self.protection_policy_name = m.get('ProtectionPolicyName')

        if m.get('ProtectionPolicyRegionId') is not None:
            self.protection_policy_region_id = m.get('ProtectionPolicyRegionId')

        self.sub_protection_policies = []
        if m.get('SubProtectionPolicies') is not None:
            for k1 in m.get('SubProtectionPolicies'):
                temp_model = main_models.GetProtectionPolicyResponseBodyDataSubProtectionPolicies()
                self.sub_protection_policies.append(temp_model.from_map(k1))

        return self

class GetProtectionPolicyResponseBodyDataSubProtectionPolicies(DaraModel):
    def __init__(
        self,
        config: str = None,
        sub_protection_policy_type: str = None,
    ):
        # The sub-protection policy configuration.
        self.config = config
        # The sub-protection policy type.
        self.sub_protection_policy_type = sub_protection_policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['Config'] = self.config

        if self.sub_protection_policy_type is not None:
            result['SubProtectionPolicyType'] = self.sub_protection_policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('SubProtectionPolicyType') is not None:
            self.sub_protection_policy_type = m.get('SubProtectionPolicyType')

        return self

