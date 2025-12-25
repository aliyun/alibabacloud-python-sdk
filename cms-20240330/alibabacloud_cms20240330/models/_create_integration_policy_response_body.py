# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreateIntegrationPolicyResponseBody(DaraModel):
    def __init__(
        self,
        created: bool = None,
        policy: main_models.CreateIntegrationPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        # Whether it is created.
        self.created = created
        # Uploaded policy.
        self.policy = policy
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['created'] = self.created

        if self.policy is not None:
            result['policy'] = self.policy.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('policy') is not None:
            temp_model = main_models.CreateIntegrationPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('policy'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreateIntegrationPolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        entity_group_id: str = None,
        policy_id: str = None,
        policy_name: str = None,
        policy_type: str = None,
        region_id: str = None,
        user_id: str = None,
        workspace: str = None,
    ):
        # Entity group ID.
        self.entity_group_id = entity_group_id
        # Policy ID.
        self.policy_id = policy_id
        # Policy name.
        self.policy_name = policy_name
        # Policy type.
        self.policy_type = policy_type
        # Region ID.
        self.region_id = region_id
        # User ID.
        self.user_id = user_id
        # The workspace where the Policy resides.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_group_id is not None:
            result['entityGroupId'] = self.entity_group_id

        if self.policy_id is not None:
            result['policyId'] = self.policy_id

        if self.policy_name is not None:
            result['policyName'] = self.policy_name

        if self.policy_type is not None:
            result['policyType'] = self.policy_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityGroupId') is not None:
            self.entity_group_id = m.get('entityGroupId')

        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')

        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')

        if m.get('policyType') is not None:
            self.policy_type = m.get('policyType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

