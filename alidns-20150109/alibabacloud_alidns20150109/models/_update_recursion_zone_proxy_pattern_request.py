# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateRecursionZoneProxyPatternRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        proxy_pattern: str = None,
        zone_id: str = None,
    ):
        self.client_token = client_token
        self.proxy_pattern = proxy_pattern
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

