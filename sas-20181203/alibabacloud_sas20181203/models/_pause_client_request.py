# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PauseClientRequest(DaraModel):
    def __init__(
        self,
        uuids: str = None,
        value: str = None,
    ):
        # The UUIDs of servers for which you want to enable or disable the Security Center agent.
        # 
        # This parameter is required.
        self.uuids = uuids
        # The status of the Security Center agent. Valid values:
        # 
        # *   **0**: disabled
        # *   **1**: enabled
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uuids is not None:
            result['Uuids'] = self.uuids

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

