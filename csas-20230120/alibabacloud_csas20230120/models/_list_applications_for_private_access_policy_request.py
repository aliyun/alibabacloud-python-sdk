# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListApplicationsForPrivateAccessPolicyRequest(DaraModel):
    def __init__(
        self,
        policy_ids: List[str] = None,
    ):
        # This parameter is required.
        self.policy_ids = policy_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        return self

