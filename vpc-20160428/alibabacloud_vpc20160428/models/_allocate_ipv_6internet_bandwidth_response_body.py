# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateIpv6InternetBandwidthResponseBody(DaraModel):
    def __init__(
        self,
        internet_bandwidth_id: str = None,
        ipv_6address_id: str = None,
        request_id: str = None,
    ):
        # The ID of the Internet bandwidth that you purchased for the IPv6 gateway.
        self.internet_bandwidth_id = internet_bandwidth_id
        # The ID of the IPv6 address.
        self.ipv_6address_id = ipv_6address_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.internet_bandwidth_id is not None:
            result['InternetBandwidthId'] = self.internet_bandwidth_id

        if self.ipv_6address_id is not None:
            result['Ipv6AddressId'] = self.ipv_6address_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InternetBandwidthId') is not None:
            self.internet_bandwidth_id = m.get('InternetBandwidthId')

        if m.get('Ipv6AddressId') is not None:
            self.ipv_6address_id = m.get('Ipv6AddressId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

