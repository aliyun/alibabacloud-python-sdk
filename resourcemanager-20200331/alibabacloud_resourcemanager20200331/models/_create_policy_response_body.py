# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class CreatePolicyResponseBody(DaraModel):
    def __init__(
        self,
        policy: main_models.CreatePolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        # The information about the permission policy.
        self.policy = policy
        # The request ID.
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
            temp_model = main_models.CreatePolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreatePolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        default_version: str = None,
        description: str = None,
        policy_name: str = None,
        policy_type: str = None,
    ):
        # The time when the permission policy was created.
        self.create_date = create_date
        # The version number of the permission policy. Default value: v1.
        self.default_version = default_version
        # The description of the permission policy.
        self.description = description
        # The name of the permission policy.
        self.policy_name = policy_name
        # The type of the permission policy. Valid values:
        # 
        # *   Custom
        # *   System
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

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
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self

