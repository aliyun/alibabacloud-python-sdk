# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListPolicyGroupsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_group_ids: List[str] = None,
        policy_group_name: str = None,
        policy_type: str = None,
    ):
        # The maximum number of entries per page. Value range: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the request to retrieve a new page of results. If the parameter is left empty, the data is queried from the first entry.
        self.next_token = next_token
        # The IDs of the policies.
        self.policy_group_ids = policy_group_ids
        # The name of the policy.
        self.policy_group_name = policy_group_name
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.policy_group_ids is not None:
            result['PolicyGroupIds'] = self.policy_group_ids

        if self.policy_group_name is not None:
            result['PolicyGroupName'] = self.policy_group_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PolicyGroupIds') is not None:
            self.policy_group_ids = m.get('PolicyGroupIds')

        if m.get('PolicyGroupName') is not None:
            self.policy_group_name = m.get('PolicyGroupName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

