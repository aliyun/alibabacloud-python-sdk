# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePolicyV2ShrinkRequest(DaraModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_id: str = None,
        policy_name: str = None,
        rules_shrink: str = None,
    ):
        # The description of the backup policy.
        self.policy_description = policy_description
        # The ID of the backup policy.
        self.policy_id = policy_id
        # The name of the backup policy.
        self.policy_name = policy_name
        # The rules in the backup policy.
        self.rules_shrink = rules_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.rules_shrink is not None:
            result['Rules'] = self.rules_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('Rules') is not None:
            self.rules_shrink = m.get('Rules')

        return self

