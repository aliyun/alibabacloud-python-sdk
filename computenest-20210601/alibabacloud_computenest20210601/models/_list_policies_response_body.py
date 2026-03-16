# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class ListPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policies: List[main_models.ListPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
    ):
        # 分页大小。
        self.max_results = max_results
        # Next Token
        self.next_token = next_token
        # Permission policy list
        self.policies = policies
        # Request ID
        self.request_id = request_id

    def validate(self):
        if self.policies:
            for v1 in self.policies:
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

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        description: str = None,
        policy_document: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # Permission policy description.
        self.description = description
        # Policy content.
        self.policy_document = policy_document
        # Permission policy name.
        self.policy_name = policy_name
        # Permission policy type.
        # 
        # - Custom: Custom policy.
        # - System: System policy.
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.policy_document is not None:
            result['PolicyDocument'] = self.policy_document

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyDocument') is not None:
            self.policy_document = m.get('PolicyDocument')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

