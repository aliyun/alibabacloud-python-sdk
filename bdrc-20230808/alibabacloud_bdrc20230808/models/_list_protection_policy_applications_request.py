# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProtectionPolicyApplicationsRequest(DaraModel):
    def __init__(
        self,
        apply_status: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_type: str = None,
        sub_protection_policy_type: str = None,
        task_id: str = None,
    ):
        # The application status.
        self.apply_status = apply_status
        # The maximum number of results to return in a single page.
        self.max_results = max_results
        # The pagination token. The response returns a `NextToken` value only when more results are available. To retrieve the next page, include the `NextToken` from the previous response in your request. If the response does not include a `NextToken` value, all results have been retrieved.
        self.next_token = next_token
        # The resource type.
        self.resource_type = resource_type
        # The sub-protection policy type.
        self.sub_protection_policy_type = sub_protection_policy_type
        # The task ID. You can call the DescribeTasks operation to query task IDs.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_status is not None:
            result['ApplyStatus'] = self.apply_status

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sub_protection_policy_type is not None:
            result['SubProtectionPolicyType'] = self.sub_protection_policy_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyStatus') is not None:
            self.apply_status = m.get('ApplyStatus')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SubProtectionPolicyType') is not None:
            self.sub_protection_policy_type = m.get('SubProtectionPolicyType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

