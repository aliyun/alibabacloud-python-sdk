# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AuthorizeSecurityGroupRequest(DaraModel):
    def __init__(
        self,
        ip_protocol: str = None,
        policy: str = None,
        port_range: str = None,
        priority: int = None,
        security_group_id: str = None,
        source_cidr_ip: str = None,
        source_port_range: str = None,
    ):
        # The transport layer protocol. The values of this parameter are case-sensitive. Valid values:
        # 
        # *   tcp
        # *   udp
        # *   icmp
        # *   gre
        # *   all: All protocols are supported.
        # 
        # This parameter is required.
        self.ip_protocol = ip_protocol
        # The action of security group rule N that determines whether to allow inbound access. Valid values:
        # 
        # *   accept: allows access.
        # *   drop: denies access and returns no responses.
        # 
        # Default value: accept.
        self.policy = policy
        # The range of destination ports that correspond to the transport layer protocol for security group rule N. Valid values:
        # 
        # *   When the IpProtocol parameter is set to tcp or udp, the port number range is **1** to **65535**. The start port number and the end port number are separated by a forward slash (/). Correct example: **1/200**. Incorrect example: **200/1**.
        # *   When the IpProtocol parameter is set to icmp, the port number range is **-1/-1**, which indicates all ports.
        # *   When the IpProtocol parameter is set to gre, the port number range is **-1/-1**, which indicates all ports.
        # *   When the IpProtocol parameter is set to all, the port number range is **-1/-1**, which indicates all ports.
        # 
        # This parameter is required.
        self.port_range = port_range
        # The priority of security group rule N. Valid values: **1** to **100**.
        # 
        # Default value: **1**.
        self.priority = priority
        # The ID of the security group.
        # 
        # This parameter is required.
        self.security_group_id = security_group_id
        # The source IPv4 CIDR block. CIDR blocks and IPv4 addresses are supported.
        # 
        # This parameter is empty by default.
        # 
        # This parameter is required.
        self.source_cidr_ip = source_cidr_ip
        # The range of port numbers that correspond to the transport layer protocol for the source security group. Valid values:
        # 
        # *   When the IpProtocol parameter is set to tcp or udp, the port number range is **1 to 65535**. The start port number and the end port number are separated by a forward slash (/). Correct example: **1/200**. Incorrect example: **200/1**.
        # *   When the IpProtocol parameter is set to icmp, the port number range is **-1/-1**, which indicates all ports.
        # *   When the IpProtocol parameter is set to gre, the port number range is **-1/-1**, which indicates all ports.
        # *   When the IpProtocol parameter is set to all, the port number range is **-1/-1**, which indicates all ports.
        self.source_port_range = source_port_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        return self

