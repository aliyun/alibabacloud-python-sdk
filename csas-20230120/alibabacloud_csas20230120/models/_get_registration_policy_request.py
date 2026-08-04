# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRegistrationPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # The ID of the device registration policy. Valid values are obtained from the following sources:
        # - [ListRegistrationPolicies](~~ListRegistrationPolicies~~): Queries device registration policies in batches.
        # - [GetRegistrationPolicy](~~GetRegistrationPolicy~~): Queries the details of a device registration policy.
        # - [CreateRegistrationPolicy](~~CreateRegistrationPolicy~~): Creates a device registration policy.
        # - [UpdateRegistrationPolicy](~~UpdateRegistrationPolicy~~): Updates a device registration policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        return self

