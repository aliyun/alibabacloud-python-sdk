# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class ListPoliciesForUserResponseBody(DaraModel):
    def __init__(
        self,
        policies: main_models.ListPoliciesForUserResponseBodyPolicies = None,
        request_id: str = None,
    ):
        self.policies = policies
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.policies:
            self.policies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policies is not None:
            result['Policies'] = self.policies.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policies') is not None:
            temp_model = main_models.ListPoliciesForUserResponseBodyPolicies()
            self.policies = temp_model.from_map(m.get('Policies'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPoliciesForUserResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        policy: List[main_models.ListPoliciesForUserResponseBodyPoliciesPolicy] = None,
    ):
        self.policy = policy

    def validate(self):
        if self.policy:
            for v1 in self.policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Policy'] = []
        if self.policy is not None:
            for k1 in self.policy:
                result['Policy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy = []
        if m.get('Policy') is not None:
            for k1 in m.get('Policy'):
                temp_model = main_models.ListPoliciesForUserResponseBodyPoliciesPolicy()
                self.policy.append(temp_model.from_map(k1))

        return self

class ListPoliciesForUserResponseBodyPoliciesPolicy(DaraModel):
    def __init__(
        self,
        attach_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        self.attach_date = attach_date
        self.default_version = default_version
        self.description = description
        self.policy_name = policy_name
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_date is not None:
            result['AttachDate'] = self.attach_date

        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.description is not None:
            result['Description'] = self.description

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachDate') is not None:
            self.attach_date = m.get('AttachDate')

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

