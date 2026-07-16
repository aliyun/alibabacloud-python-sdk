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
        # - **strict**: Strict mode. Defense mode has a risk of false positives. Use Defense mode during critical event protection periods.
        # - **balance**: Balance mode. Defense mode detects more suspicious risks while reducing false positives.
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

