# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeTransitRouterPolicyBasedRoutesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        policy_based_routes: List[main_models.DescribeTransitRouterPolicyBasedRoutesResponseBodyPolicyBasedRoutes] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned per page. Default value: **20**.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If **NextToken** is empty, no next query is available.
        # - If **NextToken** returns a value, the value is the token used to start the next query.
        self.next_token = next_token
        # The list of policy-based route rules.
        self.policy_based_routes = policy_based_routes
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.policy_based_routes:
            for v1 in self.policy_based_routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PolicyBasedRoutes'] = []
        if self.policy_based_routes is not None:
            for k1 in self.policy_based_routes:
                result['PolicyBasedRoutes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.policy_based_routes = []
        if m.get('PolicyBasedRoutes') is not None:
            for k1 in m.get('PolicyBasedRoutes'):
                temp_model = main_models.DescribeTransitRouterPolicyBasedRoutesResponseBodyPolicyBasedRoutes()
                self.policy_based_routes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTransitRouterPolicyBasedRoutesResponseBodyPolicyBasedRoutes(DaraModel):
    def __init__(
        self,
        address_family: str = None,
        description: str = None,
        dest_port_range: str = None,
        destination_cidr: str = None,
        dscp: str = None,
        name: str = None,
        policy_based_route_id: str = None,
        policy_table_id: str = None,
        priority: int = None,
        protocol: str = None,
        source_cidr: str = None,
        source_port_range: str = None,
        status: str = None,
        target_route_table_id: str = None,
    ):
        # The address family. Valid values:
        # 
        # - IPv4
        # - IPv6
        self.address_family = address_family
        # The description of the policy-based route table.
        self.description = description
        # The destination port. Valid values: **-1** or **1** to **65535**.
        # 
        # Matches traffic whose port numbers fall within the destination port range. If this parameter is not specified, traffic to any destination port is matched.
        # 
        # The port range format is described as follows:
        # 
        # - 80: port 80.
        # - 80/80: port 80.
        # - 1/200: ports 1 to 200.
        # - -1/-1: all ports.
        self.dest_port_range = dest_port_range
        # The destination CIDR block.
        self.destination_cidr = destination_cidr
        # The Differentiated Services Code Point (DSCP) value of the traffic packets to match. Valid values: **0** to **63**.
        # 
        # The DSCP value format is described as follows:
        # 
        # - 1: matches traffic with a DSCP value of 1.
        # - 1/10: matches traffic with DSCP values from 1 to 10.
        # - -1/-1: matches traffic with any DSCP value.
        self.dscp = dscp
        # The name of the policy-based route rule.
        # 
        # The name can be empty or 1 to 128 characters in length. It cannot start with http:// or https://.
        self.name = name
        # The instance ID of the policy-based routing rule.
        self.policy_based_route_id = policy_based_route_id
        # The instance ID of the policy-based routing table.
        self.policy_table_id = policy_table_id
        # The priority of the policy-based route. Valid values: **1** to **100**.
        # 
        # The priority of each policy-based route in a policy-based route table of a transit router must be unique. A smaller value indicates a higher priority.
        self.priority = priority
        # The protocol type of the traffic packets.
        # 
        # Traffic classification rules support matching traffic of various protocol types, such as **HTTP**, **HTTPS**, **TCP**, **UDP**, **SSH**, and **Telnet**. For more protocol types, log on to the [Cloud Enterprise Network (CEN) console](https://cen.console.aliyun.com/cen/list).
        self.protocol = protocol
        # The source CIDR block.
        self.source_cidr = source_cidr
        # The source port. Valid values: **-1** or **1** to **65535**.
        # 
        # Matches traffic whose port numbers fall within the source port range. If this parameter is not specified, traffic from any source port is matched.
        # 
        # The port range format is described as follows:
        # 
        # - 80: port 80.
        # - 80/80: port 80.
        # - 1/200: ports 1 to 200.
        # - -1/-1: all ports.
        self.source_port_range = source_port_range
        # The status of the policy-based route. Valid values:
        # 
        # - **Creating**: The policy-based route is being created.
        # - **Active**: The policy-based route is available.
        # - **Deleting**: The policy-based route is being deleted.
        self.status = status
        # The destination route table.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.dest_port_range is not None:
            result['DestPortRange'] = self.dest_port_range

        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.dscp is not None:
            result['Dscp'] = self.dscp

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_based_route_id is not None:
            result['PolicyBasedRouteId'] = self.policy_based_route_id

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

        if self.status is not None:
            result['Status'] = self.status

        if self.target_route_table_id is not None:
            result['TargetRouteTableId'] = self.target_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressFamily') is not None:
            self.address_family = m.get('AddressFamily')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestPortRange') is not None:
            self.dest_port_range = m.get('DestPortRange')

        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('Dscp') is not None:
            self.dscp = m.get('Dscp')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyBasedRouteId') is not None:
            self.policy_based_route_id = m.get('PolicyBasedRouteId')

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

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TargetRouteTableId') is not None:
            self.target_route_table_id = m.get('TargetRouteTableId')

        return self

