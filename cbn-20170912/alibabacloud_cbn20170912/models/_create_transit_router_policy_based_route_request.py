# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTransitRouterPolicyBasedRouteRequest(DaraModel):
    def __init__(
        self,
        address_family: str = None,
        client_token: str = None,
        description: str = None,
        dest_port_range: str = None,
        destination_cidr: str = None,
        dry_run: bool = None,
        dscp: str = None,
        name: str = None,
        policy_table_id: str = None,
        priority: int = None,
        protocol: str = None,
        source_cidr: str = None,
        source_port_range: str = None,
        target_route_table_id: str = None,
    ):
        # The address family. Valid values:
        # 
        # - IPv4
        # - IPv6
        self.address_family = address_family
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The description of the policy-based route.
        self.description = description
        # The destination port. Valid values: **-1** or **1** to **65535**.
        # 
        # This parameter matches traffic whose port numbers fall within the destination port range. If you do not specify this parameter, traffic to any destination port is matched.
        # 
        # The port range is specified in the following formats:
        # 
        # - 80: port 80.
        # - 80/80: port 80.
        # - 1/200: ports 1 to 200.
        # - -1/-1: all ports.
        self.dest_port_range = dest_port_range
        # The destination CIDR block of the route entry. Both IPv4 and IPv6 addresses are supported.
        self.destination_cidr = destination_cidr
        # Specifies whether to only precheck the request. Valid values:
        # 
        # - **true**: prechecks the request without creating the routing rule entry in the policy route table. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): sends the request. After the request passes the precheck, the routing rule entry is created in the policy route table.
        self.dry_run = dry_run
        # The Differentiated Services Code Point (DSCP) value of the traffic packet to be matched. Valid values: **0** to **63**.
        # 
        # The DSCP range is specified in the following formats:
        # 
        # - 1: traffic with a DSCP value of 1.
        # - 1/10: traffic with a DSCP value from 1 to 10.
        # - -1/-1: traffic with any DSCP value.
        self.dscp = dscp
        # The name of the policy-based route.
        self.name = name
        # The instance ID of the policy routing table.
        # 
        # This parameter is required.
        self.policy_table_id = policy_table_id
        # The priority of the policy-based route. Valid values: **1** to **100**.
        # 
        # The priority of each policy-based route in a policy route table of a transit router must be unique. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.priority = priority
        # The protocol type of the traffic packet.
        # 
        # Traffic classification rules support matching traffic of various protocol types, such as **HTTP**, **HTTPS**, **TCP**, **UDP**, **SSH**, and **Telnet**. For more protocol types, log on to the [Cloud Enterprise Network (CEN) console](https://cen.console.aliyun.com/cen/list).
        self.protocol = protocol
        # The source CIDR block. The source CIDR block must be in CIDR format. Example: 192.168.1.0/24.
        self.source_cidr = source_cidr
        # The source port. Valid values: **-1** or **1** to **65535**.
        # 
        # This parameter matches traffic whose port numbers fall within the source port range. If you do not specify this parameter, traffic from any source port is matched.
        # 
        # The port range is specified in the following formats:
        # 
        # - 80: port 80.
        # - 80/80: port 80.
        # - 1/200: ports 1 to 200.
        # - -1/-1: all ports.
        self.source_port_range = source_port_range
        # The destination route table.
        # 
        # This parameter is required.
        self.target_route_table_id = target_route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_family is not None:
            result['AddressFamily'] = self.address_family

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dest_port_range is not None:
            result['DestPortRange'] = self.dest_port_range

        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.dscp is not None:
            result['Dscp'] = self.dscp

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_table_id is not None:
            result['PolicyTableId'] = self.policy_table_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.target_route_table_id is not None:
            result['TargetRouteTableId'] = self.target_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressFamily') is not None:
            self.address_family = m.get('AddressFamily')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestPortRange') is not None:
            self.dest_port_range = m.get('DestPortRange')

        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Dscp') is not None:
            self.dscp = m.get('Dscp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyTableId') is not None:
            self.policy_table_id = m.get('PolicyTableId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('TargetRouteTableId') is not None:
            self.target_route_table_id = m.get('TargetRouteTableId')

        return self

