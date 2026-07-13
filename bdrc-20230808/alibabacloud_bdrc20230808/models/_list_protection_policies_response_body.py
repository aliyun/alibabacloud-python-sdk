# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class ListProtectionPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListProtectionPoliciesResponseBodyData = None,
        request_id: str = None,
    ):
        # The data returned.
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
            temp_model = main_models.ListProtectionPoliciesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProtectionPoliciesResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListProtectionPoliciesResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The response parameters.
        self.content = content
        # The maximum number of results requested.
        self.max_results = max_results
        # The paging token.
        self.next_token = next_token
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.ListProtectionPoliciesResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProtectionPoliciesResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        bound_resource_category_ids: List[str] = None,
        latest_apply_summary: main_models.ListProtectionPoliciesResponseBodyDataContentLatestApplySummary = None,
        latest_apply_time: int = None,
        latest_task_id: str = None,
        protection_policy_id: str = None,
        protection_policy_name: str = None,
        protection_policy_region_id: str = None,
        sub_protection_policies: List[main_models.ListProtectionPoliciesResponseBodyDataContentSubProtectionPolicies] = None,
    ):
        # The attached resource category IDs.
        self.bound_resource_category_ids = bound_resource_category_ids
        # The summary of the latest application result.
        self.latest_apply_summary = latest_apply_summary
        # The time when the policy was last applied.
        self.latest_apply_time = latest_apply_time
        # The task ID of the latest policy application.
        self.latest_task_id = latest_task_id
        # The protection policy ID.
        self.protection_policy_id = protection_policy_id
        # The protection policy name.
        self.protection_policy_name = protection_policy_name
        # The region ID of the protection policy.
        self.protection_policy_region_id = protection_policy_region_id
        # The sub-protection policies.
        self.sub_protection_policies = sub_protection_policies

    def validate(self):
        if self.latest_apply_summary:
            self.latest_apply_summary.validate()
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

        if self.latest_apply_summary is not None:
            result['LatestApplySummary'] = self.latest_apply_summary.to_map()

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

        if m.get('LatestApplySummary') is not None:
            temp_model = main_models.ListProtectionPoliciesResponseBodyDataContentLatestApplySummary()
            self.latest_apply_summary = temp_model.from_map(m.get('LatestApplySummary'))

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
                temp_model = main_models.ListProtectionPoliciesResponseBodyDataContentSubProtectionPolicies()
                self.sub_protection_policies.append(temp_model.from_map(k1))

        return self

class ListProtectionPoliciesResponseBodyDataContentSubProtectionPolicies(DaraModel):
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

class ListProtectionPoliciesResponseBodyDataContentLatestApplySummary(DaraModel):
    def __init__(
        self,
        apply_status_count: List[main_models.ListProtectionPoliciesResponseBodyDataContentLatestApplySummaryApplyStatusCount] = None,
        complete_time: int = None,
        resource_count: List[main_models.ListProtectionPoliciesResponseBodyDataContentLatestApplySummaryResourceCount] = None,
    ):
        # The count statistics of application status.
        self.apply_status_count = apply_status_count
        # The time when the task was completed. Unix timestamp format, in seconds.
        self.complete_time = complete_time
        # The count of resources by type.
        self.resource_count = resource_count

    def validate(self):
        if self.apply_status_count:
            for v1 in self.apply_status_count:
                 if v1:
                    v1.validate()
        if self.resource_count:
            for v1 in self.resource_count:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApplyStatusCount'] = []
        if self.apply_status_count is not None:
            for k1 in self.apply_status_count:
                result['ApplyStatusCount'].append(k1.to_map() if k1 else None)

        if self.complete_time is not None:
            result['CompleteTime'] = self.complete_time

        result['ResourceCount'] = []
        if self.resource_count is not None:
            for k1 in self.resource_count:
                result['ResourceCount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.apply_status_count = []
        if m.get('ApplyStatusCount') is not None:
            for k1 in m.get('ApplyStatusCount'):
                temp_model = main_models.ListProtectionPoliciesResponseBodyDataContentLatestApplySummaryApplyStatusCount()
                self.apply_status_count.append(temp_model.from_map(k1))

        if m.get('CompleteTime') is not None:
            self.complete_time = m.get('CompleteTime')

        self.resource_count = []
        if m.get('ResourceCount') is not None:
            for k1 in m.get('ResourceCount'):
                temp_model = main_models.ListProtectionPoliciesResponseBodyDataContentLatestApplySummaryResourceCount()
                self.resource_count.append(temp_model.from_map(k1))

        return self

class ListProtectionPoliciesResponseBodyDataContentLatestApplySummaryResourceCount(DaraModel):
    def __init__(
        self,
        count: int = None,
        resource_type: str = None,
    ):
        # The count of resources by type.
        self.count = count
        # The resource type.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

class ListProtectionPoliciesResponseBodyDataContentLatestApplySummaryApplyStatusCount(DaraModel):
    def __init__(
        self,
        apply_status: str = None,
        count: int = None,
    ):
        # The application status.
        self.apply_status = apply_status
        # The count of resources by type.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_status is not None:
            result['ApplyStatus'] = self.apply_status

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyStatus') is not None:
            self.apply_status = m.get('ApplyStatus')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

