# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddZoneRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dns_group: str = None,
        lang: str = None,
        proxy_pattern: str = None,
        resource_group_id: str = None,
        zone_name: str = None,
        zone_tag: str = None,
        zone_type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The logical location type of the built-in authoritative module in which the zone is added. Valid values:
        # 
        # *   **NORMAL_ZONE**: the regular module. DNS results are stored in the cache module and DNS requests are sent to the regular module if the DNS requests do not match the DNS records in the cache module. DNS record updates take effect based on the time to live (TTL) value. The regular module does not support DNS resolution over user-defined lines or based on weight values.
        # *   **FAST_ZONE**: the acceleration module. It directly responds to DNS requests with the lowest latency and updates DNS records in real time. The acceleration module supports DNS resolution over user-defined lines or based on weight values.
        # 
        # Default value: **NORMAL_ZONE**.
        # 
        # >  The DNS results returned by the built-in authoritative acceleration module are not stored in the cache module because the built-in authoritative acceleration module is located before the cache module. As a result, you are charged more for DNS requests.
        self.dns_group = dns_group
        # The language of the response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        # 
        # Default value: **en**.
        self.lang = lang
        # Specifies whether to enable the recursive resolution proxy for subdomain names. Valid values:
        # 
        # *   **ZONE**: disables the recursive resolution proxy for subdomain names. In this case, NXDOMAIN is returned if the queried subdomain name does not exist in the zone.
        # *   **RECORD**: enables the recursive resolution proxy for subdomain names. In this case, if the queried subdomain name does not exist in the zone, DNS requests are recursively forwarded to the forward module and then to the recursion module until DNS results are returned.
        # 
        # Default value: **ZONE**.
        self.proxy_pattern = proxy_pattern
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the zone to be added.
        self.zone_name = zone_name
        # This parameter is not available. You can ignore it.
        self.zone_tag = zone_tag
        # This parameter is not available. You can ignore it.
        self.zone_type = zone_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.proxy_pattern is not None:
            result['ProxyPattern'] = self.proxy_pattern

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        if self.zone_tag is not None:
            result['ZoneTag'] = self.zone_tag

        if self.zone_type is not None:
            result['ZoneType'] = self.zone_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ProxyPattern') is not None:
            self.proxy_pattern = m.get('ProxyPattern')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        if m.get('ZoneTag') is not None:
            self.zone_tag = m.get('ZoneTag')

        if m.get('ZoneType') is not None:
            self.zone_type = m.get('ZoneType')

        return self

