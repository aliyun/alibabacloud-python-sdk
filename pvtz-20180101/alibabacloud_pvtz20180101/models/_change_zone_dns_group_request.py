# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChangeZoneDnsGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dns_group: str = None,
        zone_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see How to ensure idempotence.
        self.client_token = client_token
        # The logical location of the built-in authoritative module in which the zone is added. Valid values:
        # 
        # *   Normal zone: regular module
        # *   Fast Zone: acceleration module
        # 
        # This parameter is required.
        self.dns_group = dns_group
        # The global ID of the zone.
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

        if self.dns_group is not None:
            result['DnsGroup'] = self.dns_group

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DnsGroup') is not None:
            self.dns_group = m.get('DnsGroup')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

