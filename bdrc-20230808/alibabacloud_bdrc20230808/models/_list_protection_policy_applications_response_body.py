# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class ListProtectionPolicyApplicationsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListProtectionPolicyApplicationsResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data.
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
            temp_model = main_models.ListProtectionPolicyApplicationsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProtectionPolicyApplicationsResponseBodyData(DaraModel):
    def __init__(
        self,
        content: List[main_models.ListProtectionPolicyApplicationsResponseBodyDataContent] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        # The response content.
        self.content = content
        # The maximum number of results to return.
        self.max_results = max_results
        # The pagination token for retrieving the next page of results. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The total number of entries.
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
                temp_model = main_models.ListProtectionPolicyApplicationsResponseBodyDataContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListProtectionPolicyApplicationsResponseBodyDataContent(DaraModel):
    def __init__(
        self,
        apply_detail: str = None,
        apply_status: str = None,
        apply_time: int = None,
        product_type: str = None,
        protection_policy_id: str = None,
        resource_arn: str = None,
        resource_id: str = None,
        resource_owner_id: int = None,
        resource_type: str = None,
        sub_protection_policy_type: str = None,
        task_id: str = None,
    ):
        # The error details, returned when the application fails.
        self.apply_detail = apply_detail
        # The policy application status.
        self.apply_status = apply_status
        # The time the policy was applied.
        self.apply_time = apply_time
        # The product type.
        self.product_type = product_type
        # The protection policy ID.
        self.protection_policy_id = protection_policy_id
        # The resource ARN.
        self.resource_arn = resource_arn
        # The resource ID.
        self.resource_id = resource_id
        self.resource_owner_id = resource_owner_id
        # The resource type.
        self.resource_type = resource_type
        # The sub-protection policy type.
        self.sub_protection_policy_type = sub_protection_policy_type
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_detail is not None:
            result['ApplyDetail'] = self.apply_detail

        if self.apply_status is not None:
            result['ApplyStatus'] = self.apply_status

        if self.apply_time is not None:
            result['ApplyTime'] = self.apply_time

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.protection_policy_id is not None:
            result['ProtectionPolicyId'] = self.protection_policy_id

        if self.resource_arn is not None:
            result['ResourceArn'] = self.resource_arn

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sub_protection_policy_type is not None:
            result['SubProtectionPolicyType'] = self.sub_protection_policy_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyDetail') is not None:
            self.apply_detail = m.get('ApplyDetail')

        if m.get('ApplyStatus') is not None:
            self.apply_status = m.get('ApplyStatus')

        if m.get('ApplyTime') is not None:
            self.apply_time = m.get('ApplyTime')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProtectionPolicyId') is not None:
            self.protection_policy_id = m.get('ProtectionPolicyId')

        if m.get('ResourceArn') is not None:
            self.resource_arn = m.get('ResourceArn')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SubProtectionPolicyType') is not None:
            self.sub_protection_policy_type = m.get('SubProtectionPolicyType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

