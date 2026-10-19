# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateNetworkCidrBlockRequest(DaraModel):
    def __init__(
        self,
        ip_version: str = None,
        ipv_6isp: str = None,
        network_id: str = None,
        secondary_cidr_block: str = None,
    ):
        # The IP address version. Valid values:
        # - IPV4: IPv4 address.
        # - IPV6: IPv6 address.
        self.ip_version = ip_version
        # The ISP of the IPv6 CIDR block. Valid values:
        # - cmcc
        # - unicom
        # - telecom
        self.ipv_6isp = ipv_6isp
        # The network ID.
        # 
        # This parameter is required.
        self.network_id = network_id
        # The secondary IPv4 CIDR block to be added. The CIDR block must meet the following requirements:
        # - The CIDR block must be within the 10.0.0.0/8, 172.16.0.0/12, or 192.168.0.0/16 range.
        # - The secondary CIDR block must not overlap with the primary CIDR block or existing secondary CIDR blocks of the network.
        self.secondary_cidr_block = secondary_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.ipv_6isp is not None:
            result['Ipv6Isp'] = self.ipv_6isp

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.secondary_cidr_block is not None:
            result['SecondaryCidrBlock'] = self.secondary_cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Ipv6Isp') is not None:
            self.ipv_6isp = m.get('Ipv6Isp')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('SecondaryCidrBlock') is not None:
            self.secondary_cidr_block = m.get('SecondaryCidrBlock')

        return self

