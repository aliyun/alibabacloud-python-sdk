# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateClientAlertModeRequest(DaraModel):
    def __init__(
        self,
        mode: str = None,
        uuids: List[str] = None,
    ):
        # The protection mode. Valid values:
        # 
        # *   **strict**: The strict mode. False positives may be generated. We recommend that you enable this mode during major events.
        # *   **balance**: The balanced mode. More risks can be detected with less false positives in this mode.
        self.mode = mode
        # The UUIDs of servers.
        self.uuids = uuids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        return self

