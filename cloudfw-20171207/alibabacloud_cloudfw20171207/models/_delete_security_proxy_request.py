# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSecurityProxyRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        proxy_id: str = None,
    ):
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the NAT firewall.
        # 
        # This parameter is required.
        self.proxy_id = proxy_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        return self

