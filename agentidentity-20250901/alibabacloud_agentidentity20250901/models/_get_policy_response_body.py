# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetPolicyResponseBody(DaraModel):
    def __init__(
        self,
        policy: main_models.GetPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        self.policy = policy
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        definition: main_models.Definition = None,
        description: str = None,
        policy_arn: str = None,
        policy_name: str = None,
        policy_set_name: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.definition = definition
        self.description = description
        self.policy_arn = policy_arn
        self.policy_name = policy_name
        self.policy_set_name = policy_set_name
        self.update_time = update_time

    def validate(self):
        if self.definition:
            self.definition.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.definition is not None:
            result['Definition'] = self.definition.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.policy_arn is not None:
            result['PolicyArn'] = self.policy_arn

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_set_name is not None:
            result['PolicySetName'] = self.policy_set_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Definition') is not None:
            temp_model = main_models.Definition()
            self.definition = temp_model.from_map(m.get('Definition'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyArn') is not None:
            self.policy_arn = m.get('PolicyArn')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicySetName') is not None:
            self.policy_set_name = m.get('PolicySetName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

