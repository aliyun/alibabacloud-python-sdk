# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLayer4RuleShrinkRequest(DaraModel):
    def __init__(
        self,
        listeners: str = None,
        proxy_enable: int = None,
        us_timeout_shrink: str = None,
    ):
        # This parameter is required.
        self.listeners = listeners
        self.proxy_enable = proxy_enable
        self.us_timeout_shrink = us_timeout_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.listeners is not None:
            result['Listeners'] = self.listeners

        if self.proxy_enable is not None:
            result['ProxyEnable'] = self.proxy_enable

        if self.us_timeout_shrink is not None:
            result['UsTimeout'] = self.us_timeout_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Listeners') is not None:
            self.listeners = m.get('Listeners')

        if m.get('ProxyEnable') is not None:
            self.proxy_enable = m.get('ProxyEnable')

        if m.get('UsTimeout') is not None:
            self.us_timeout_shrink = m.get('UsTimeout')

        return self

