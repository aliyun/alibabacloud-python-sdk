# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetAccessKeyPolicyForAccountRequest(DaraModel):
    def __init__(
        self,
        access_key_policy: str = None,
    ):
        # The network access restriction policy. The value is a JSON-formatted string. For more information, see the AccessKeyPolicy structure description in the SetAccessKeyPolicy documentation.
        # 
        # This parameter is required.
        self.access_key_policy = access_key_policy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key_policy is not None:
            result['AccessKeyPolicy'] = self.access_key_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKeyPolicy') is not None:
            self.access_key_policy = m.get('AccessKeyPolicy')

        return self

