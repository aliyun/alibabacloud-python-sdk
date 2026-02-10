# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenSensitiveFileScanRequest(DaraModel):
    def __init__(
        self,
        switch_on: str = None,
    ):
        # Specifies whether to enable or disable sensitive file scan. Valid values:
        # 
        # *   **on**: enables sensitive file scan
        # *   **off**: disables sensitive file scan
        self.switch_on = switch_on

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.switch_on is not None:
            result['SwitchOn'] = self.switch_on

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SwitchOn') is not None:
            self.switch_on = m.get('SwitchOn')

        return self

