# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGatewayQuotaRuleStatusRequest(DaraModel):
    def __init__(
        self,
        clear_history: bool = None,
        enable: bool = None,
    ):
        self.clear_history = clear_history
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.clear_history is not None:
            result['clearHistory'] = self.clear_history

        if self.enable is not None:
            result['enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clearHistory') is not None:
            self.clear_history = m.get('clearHistory')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        return self

