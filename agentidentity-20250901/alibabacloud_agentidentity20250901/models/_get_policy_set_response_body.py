# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentidentity20250901 import models as main_models
from darabonba.model import DaraModel

class GetPolicySetResponseBody(DaraModel):
    def __init__(
        self,
        policy_set: main_models.GetPolicySetResponseBodyPolicySet = None,
        request_id: str = None,
    ):
        self.policy_set = policy_set
        self.request_id = request_id

    def validate(self):
        if self.policy_set:
            self.policy_set.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_set is not None:
            result['PolicySet'] = self.policy_set.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicySet') is not None:
            temp_model = main_models.GetPolicySetResponseBodyPolicySet()
            self.policy_set = temp_model.from_map(m.get('PolicySet'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPolicySetResponseBodyPolicySet(DaraModel):
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

