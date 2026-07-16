# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddRecursionZoneRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        proxy_pattern: str = None,
        zone_name: str = None,
    ):
        # A client token that ensures the idempotence of the request. You can specify a custom value. Make sure that the value is unique among different requests. The value can contain up to 64 ASCII characters.
        self.client_token = client_token
        # Specifies whether to enable recursive proxy for subdomains. Valid values:
        # 
        # zone: Disables recursive proxy. An NXDOMAIN response is returned for non-existent subdomains. record: Enables recursive proxy. For non-existent subdomains, the system queries the forwarding and recursion modules in sequence and returns the final result.
        self.proxy_pattern = proxy_pattern
        # The name of the zone.
        self.zone_name = zone_name

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

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

