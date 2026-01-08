# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchSecurityProxyRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        proxy_id: str = None,
        switch: str = None,
    ):
        # The language of the content within the request and the response. Valid values:
        # 
        # *   **zh** (default)
        # *   **en**
        self.lang = lang
        # The ID of the NAT firewall.
        # 
        # This parameter is required.
        self.proxy_id = proxy_id
        # Specifies whether to enable the NAT firewall. Valid values:
        # 
        # *   open: yes
        # *   close: no
        # 
        # This parameter is required.
        self.switch = switch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id

        if self.switch is not None:
            result['Switch'] = self.switch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('Switch') is not None:
            self.switch = m.get('Switch')

        return self

