# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class ListPolicySetsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_sets: List[main_models.ListPolicySetsResponseBodyPolicySets] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.policy_sets = policy_sets
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.policy_sets:
            for v1 in self.policy_sets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PolicySets'] = []
        if self.policy_sets is not None:
            for k1 in self.policy_sets:
                result['PolicySets'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.policy_sets = []
        if m.get('PolicySets') is not None:
            for k1 in m.get('PolicySets'):
                temp_model = main_models.ListPolicySetsResponseBodyPolicySets()
                self.policy_sets.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPolicySetsResponseBodyPolicySets(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        policy_set_arn: str = None,
        policy_set_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.policy_set_arn = policy_set_arn
        self.policy_set_name = policy_set_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.policy_set_arn is not None:
            result['PolicySetArn'] = self.policy_set_arn

        if self.policy_set_name is not None:
            result['PolicySetName'] = self.policy_set_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicySetArn') is not None:
            self.policy_set_arn = m.get('PolicySetArn')

        if m.get('PolicySetName') is not None:
            self.policy_set_name = m.get('PolicySetName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

