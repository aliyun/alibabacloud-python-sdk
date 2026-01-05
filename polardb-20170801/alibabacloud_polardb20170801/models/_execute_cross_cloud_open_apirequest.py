# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteCrossCloudOpenAPIRequest(DaraModel):
    def __init__(
        self,
        proxy_info: str = None,
    ):
        self.proxy_info = proxy_info

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.proxy_info is not None:
            result['ProxyInfo'] = self.proxy_info

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProxyInfo') is not None:
            self.proxy_info = m.get('ProxyInfo')

        return self

