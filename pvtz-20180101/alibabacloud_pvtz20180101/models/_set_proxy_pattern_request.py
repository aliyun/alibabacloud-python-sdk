# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetProxyPatternRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        lang: str = None,
        proxy_pattern: str = None,
        user_client_ip: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        # 
        # Default value: en.
        self.lang = lang
        # Specifies whether to enable the recursive resolution proxy for subdomain names. Valid values:
        # 
        # *   **ZONE**: disables the recursive resolution proxy for subdomain names. In this case, NXDOMAIN is returned if the queried subdomain name does not exist in the zone.
        # *   **RECORD**: enables the recursive resolution proxy for subdomain names. In this case, if the queried domain name does not exist in the zone, Domain Name System (DNS) requests are recursively forwarded to the forward module and then to the recursion module until DNS results are returned.
        # 
        # This parameter is required.
        self.proxy_pattern = proxy_pattern
        # The IP address of the client.
        self.user_client_ip = user_client_ip
        # The zone ID. This ID uniquely identifies the zone.
        # 
        # This parameter is required.
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

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern

        if self.user_client_ip is not None:
            result['UserClientIp'] = self.user_client_ip

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')

        if m.get('UserClientIp') is not None:
            self.user_client_ip = m.get('UserClientIp')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

