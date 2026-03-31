# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePolicyDescriptionRequest(DaraModel):
    def __init__(
        self,
        new_description: str = None,
        policy_name: str = None,
    ):
        # The description of the policy.
        # 
        # The description must be 1 to 1,024 characters in length.
        self.new_description = new_description
        # The name of the policy.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.new_description is not None:
            result['NewDescription'] = self.new_description

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NewDescription') is not None:
            self.new_description = m.get('NewDescription')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

