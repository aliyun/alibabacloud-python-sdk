# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class GenerateServicePolicyResponseBody(DaraModel):
    def __init__(
        self,
        missing_policy: List[main_models.GenerateServicePolicyResponseBodyMissingPolicy] = None,
        policy: str = None,
        request_id: str = None,
    ):
        # The policies that are missing.
        self.missing_policy = missing_policy
        # The RAM policy.
        self.policy = policy
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.missing_policy:
            for v1 in self.missing_policy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MissingPolicy'] = []
        if self.missing_policy is not None:
            for k1 in self.missing_policy:
                result['MissingPolicy'].append(k1.to_map() if k1 else None)

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.missing_policy = []
        if m.get('MissingPolicy') is not None:
            for k1 in m.get('MissingPolicy'):
                temp_model = main_models.GenerateServicePolicyResponseBodyMissingPolicy()
                self.missing_policy.append(temp_model.from_map(k1))

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GenerateServicePolicyResponseBodyMissingPolicy(DaraModel):
    def __init__(
        self,
        action: List[str] = None,
        resource: str = None,
        service_name: str = None,
    ):
        # Operations on specific resources.
        self.action = action
        # The specific objects authorized. An asterisk (*) denotes all resources.
        self.resource = resource
        # The name of the service.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        return self

