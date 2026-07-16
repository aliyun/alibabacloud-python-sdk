# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        definition_shrink: str = None,
        description: str = None,
        policy_name: str = None,
        policy_set_name: str = None,
    ):
        self.definition_shrink = definition_shrink
        self.description = description
        self.policy_name = policy_name
        self.policy_set_name = policy_set_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.definition_shrink is not None:
            result['Definition'] = self.definition_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_set_name is not None:
            result['PolicySetName'] = self.policy_set_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Definition') is not None:
            self.definition_shrink = m.get('Definition')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicySetName') is not None:
            self.policy_set_name = m.get('PolicySetName')

        return self

