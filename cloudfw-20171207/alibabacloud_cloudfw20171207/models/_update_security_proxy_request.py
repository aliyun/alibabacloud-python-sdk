# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSecurityProxyRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        proxy_id: str = None,
        proxy_name: str = None,
        strict_mode: int = None,
    ):
        # The language of the content within the response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The ID of the NAT firewall.
        # 
        # This parameter is required.
        self.proxy_id = proxy_id
        # The name of the NAT firewall. The name can contain uppercase and lowercase letters, Chinese characters, digits, and underscores (_). The name must be 4 to 50 characters in length and cannot start with an underscore.
        # 
        # This parameter is required.
        self.proxy_name = proxy_name
        # Specifies whether to enable strict mode. Valid values:
        # 
        # - 1: strict mode.
        # - 0: loose mode.
        self.strict_mode = strict_mode

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

        if self.proxy_name is not None:
            result['ProxyName'] = self.proxy_name

        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('ProxyName') is not None:
            self.proxy_name = m.get('ProxyName')

        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

        return self

