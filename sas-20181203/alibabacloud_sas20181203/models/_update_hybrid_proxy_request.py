# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHybridProxyRequest(DaraModel):
    def __init__(
        self,
        proxy_uuid: str = None,
    ):
        # The UUID of the Security Center agent.
        # 
        # This parameter is required.
        self.proxy_uuid = proxy_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.proxy_uuid is not None:
            result['ProxyUuid'] = self.proxy_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyUuid') is not None:
            self.proxy_uuid = m.get('ProxyUuid')

        return self

