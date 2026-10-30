# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizeSecurityGroupEgressRequest(DaraModel):
    def __init__(
        self,
        dest_cidr_ip: str = None,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        security_group_id: str = None,
        source_port_range: str = None,
    ):
        # The destination IP address range. CIDR blocks and IPv4 address ranges are supported.
        # 
        # Default value: none.
        # 
        # This parameter is required.
        self.dest_cidr_ip = dest_cidr_ip
        # The transport layer protocol. The value is case-sensitive. Valid values:
        # 
        # - tcp: TCP.
        # - udp: UDP.
        # - icmp: ICMP.
        # - gre: GRE.
        # - all: All protocols.
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        # Settings for access permissions. Valid values:
        # 
        # - accept (default): accept access.
        # - drop: deny access without returning a deny message.
        self.policy = policy
        # The range of ports enabled for the transport layer protocol in the security group. Valid values:
        # - For TCP or UDP: **1** to **65535**. Use a forward slash (/) to separate the start port and the end port. Correct example: **1/200**. Incorrect example: **200/1**.
        # - For ICMP: **-1/-1**.
        # - For GRE: **-1/-1**.
        # - If IpProtocol is set to all: **-1/-1**.
        # 
        # This parameter is required.
        self.port_range = port_range
        # The priority of the security group rule. Valid values: **1** to **100**. Default value: **1**.
        self.priority = priority
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The range of ports enabled for the transport layer protocol in the source security group. Valid values:
        # 
        # - For TCP or UDP: **1** to **65535**. Use a forward slash (/) to separate the start port and the end port. Correct example: **1/200**. Incorrect example: **200/1**.
        # - For ICMP: **-1/-1**.
        # - For GRE: **-1/-1**.
        # - If IpProtocol is set to all: **-1/-1**.
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_cidr_ip is not None:
            result['DestCidrIp'] = self.dest_cidr_ip

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port_range is not None:
            result['PortRange'] = self.port_range

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCidrIp') is not None:
            self.dest_cidr_ip = m.get('DestCidrIp')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PortRange') is not None:
            self.port_range = m.get('PortRange')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

