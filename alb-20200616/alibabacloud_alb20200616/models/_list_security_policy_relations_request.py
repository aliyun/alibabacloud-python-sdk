# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListSecurityPolicyRelationsRequest(DaraModel):
    def __init__(
        self,
        security_policy_ids: List[str] = None,
    ):
        # The security policy IDs. You can specify up to five IDs.
        # 
        # This parameter is required.
        self.security_policy_ids = security_policy_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_policy_ids is not None:
            result['SecurityPolicyIds'] = self.security_policy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityPolicyIds') is not None:
            self.security_policy_ids = m.get('SecurityPolicyIds')

        return self

