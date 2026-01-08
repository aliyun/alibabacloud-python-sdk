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
        # The destination IP address to query. If you specify this parameter, all intrusion events with the specified destination IP address are queried.
        self.dst_ip = dst_ip
        # The ID of the destination VPC to query. If you specify this parameter, all intrusion events that contain the specified ID of the destination VPC are queried.
        self.dst_vpc_id = dst_vpc_id
        # The end of the time range to query. The value is a timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of the firewall. Valid values:
        # 
        # *   **VpcFirewall**: virtual private cloud (VPC) firewall
        # *   **InternetFirewall** (default): Internet firewall
        self.firewall_type = firewall_type
        # The public IP address. If you specify this parameter, all intrusion events that contain the specified public IP address are queried.
        self.public_ip = public_ip
        # The source IP address to query. If you specify this parameter, all intrusion events from the specified source IP address are queried.
        self.src_ip = src_ip
        # The ID of the source VPC to query. If you specify this parameter, all intrusion events that contain the specified ID of the source VPC are queried.
        self.src_vpc_id = src_vpc_id
        # The beginning of the time range to query. The value is a timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The UUID of the intrusion event.
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

