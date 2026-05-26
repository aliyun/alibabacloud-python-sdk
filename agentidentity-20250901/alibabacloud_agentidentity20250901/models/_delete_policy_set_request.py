# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletePolicySetRequest(DaraModel):
    def __init__(
        self,
        policy_set_name: str = None,
    ):
        self.policy_set_name = policy_set_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_set_name is not None:
            result['PolicySetName'] = self.policy_set_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicySetName') is not None:
            self.policy_set_name = m.get('PolicySetName')

        return self

