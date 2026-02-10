# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListClientAlertModeRequest(DaraModel):
    def __init__(
        self,
        mode: str = None,
    ):
        # The protection mode. Valid values:
        # 
        # *   **strict**: The strict mode. False positives may be generated. We recommend that you enable this mode during major events.
        # *   **balance**: The balanced mode. More risks can be detected with less false positives in this mode.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

