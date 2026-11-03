# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRiskEventPayloadRequest(DaraModel):
    def __init__(
        self,
        dst_ip: str = None,
        dst_vpc_id: str = None,
        end_time: str = None,
        firewall_type: str = None,
        public_ip: str = None,
        src_ip: str = None,
        src_vpc_id: str = None,
        start_time: str = None,
        uuid: str = None,
    ):
        # The destination IP address to query. If you specify this parameter, the query returns intrusion prevention events that involve this destination IP address.
        self.dst_ip = dst_ip
        # The destination VPC ID to query. If you specify this parameter, the query returns intrusion prevention events that involve this destination VPC ID.
        self.dst_vpc_id = dst_vpc_id
        # Specifies the end time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of Cloud Firewall. Valid values:
        # - **VpcFirewall**: virtual private cloud (VPC) firewalls.
        # - **InternetFirewall** (default): the Internet Border firewall.
        self.firewall_type = firewall_type
        # The IP address of the public asset to query. If you specify this parameter, the query returns compromise detection events that involve this asset IP address.
        self.public_ip = public_ip
        # The source IP address to query. If you specify this parameter, the query returns intrusion prevention events that involve this source IP address.
        self.src_ip = src_ip
        # The source VPC ID to query. If you specify this parameter, the query returns intrusion prevention events that involve this source VPC ID.
        self.src_vpc_id = src_vpc_id
        # Specifies the start time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The UUID of the intrusion prevention event.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.dst_vpc_id is not None:
            result['DstVpcId'] = self.dst_vpc_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.public_ip is not None:
            result['PublicIP'] = self.public_ip

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.uuid is not None:
            result['UUID'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('DstVpcId') is not None:
            self.dst_vpc_id = m.get('DstVpcId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('PublicIP') is not None:
            self.public_ip = m.get('PublicIP')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('UUID') is not None:
            self.uuid = m.get('UUID')

        return self

