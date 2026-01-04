# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListGatewayRouteTableEntriesResponseBody(DaraModel):
    def __init__(
        self,
        gateway_route_entry_models: List[main_models.ListGatewayRouteTableEntriesResponseBodyGatewayRouteEntryModels] = None,
        next_token: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The details of the routes in the gateway route table.
        self.gateway_route_entry_models = gateway_route_entry_models
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If a value is returned for **NextToken**, the value is used to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.gateway_route_entry_models:
            for v1 in self.gateway_route_entry_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GatewayRouteEntryModels'] = []
        if self.gateway_route_entry_models is not None:
            for k1 in self.gateway_route_entry_models:
                result['GatewayRouteEntryModels'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gateway_route_entry_models = []
        if m.get('GatewayRouteEntryModels') is not None:
            for k1 in m.get('GatewayRouteEntryModels'):
                temp_model = main_models.ListGatewayRouteTableEntriesResponseBodyGatewayRouteEntryModels()
                self.gateway_route_entry_models.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListGatewayRouteTableEntriesResponseBodyGatewayRouteEntryModels(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_block: str = None,
        name: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        next_hops: List[main_models.ListGatewayRouteTableEntriesResponseBodyGatewayRouteEntryModelsNextHops] = None,
        status: str = None,
    ):
        # The name of the route entry.
        self.description = description
        # The destination CIDR block of the route.
        self.destination_cidr_block = destination_cidr_block
        # The name of the route entry.
        # 
        # The name must be 2 to 128 characters in length and can contain letter, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The ID of the next hop.
        self.next_hop_id = next_hop_id
        # The type of the next hop. Valid values:
        # 
        # *   **EcsInstance**: Elastic Compute Service (ECS) instance
        # *   **NetworkInterface**: elastic network interfaces (ENIs).
        # *   **Local**: local next hop
        self.next_hop_type = next_hop_type
        # The information about the next hop.
        self.next_hops = next_hops
        # The status of the route entry. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        # *   **Modifying**
        self.status = status

    def validate(self):
        if self.next_hops:
            for v1 in self.next_hops:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.name is not None:
            result['Name'] = self.name

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        result['NextHops'] = []
        if self.next_hops is not None:
            for k1 in self.next_hops:
                result['NextHops'].append(k1.to_map() if k1 else None)

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        self.next_hops = []
        if m.get('NextHops') is not None:
            for k1 in m.get('NextHops'):
                temp_model = main_models.ListGatewayRouteTableEntriesResponseBodyGatewayRouteEntryModelsNextHops()
                self.next_hops.append(temp_model.from_map(k1))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListGatewayRouteTableEntriesResponseBodyGatewayRouteEntryModelsNextHops(DaraModel):
    def __init__(
        self,
        enabled: str = None,
        next_hop_id: str = None,
        next_hop_type: str = None,
        weight: str = None,
    ):
        # Indicates whether the route is available. Valid values:
        # 
        # *   **0**: unavailable
        # *   **1**: available
        self.enabled = enabled
        # The ID of the next hop.
        self.next_hop_id = next_hop_id
        # The type of the next hop. Valid values:
        # 
        # *   **Instance** (default): an ECS instance
        # *   **HaVip**: a high-availability virtual IP address (HaVip).
        # *   **VpnGateway**: a VPN gateway
        # *   **NatGateway**: a NAT gateway
        # *   **NetworkInterface**: a secondary ENI
        # *   **RouterInterface**: a router interface
        # *   **IPv6Gateway**: an IPv6 gateway
        # *   **Attachment**: a transit router
        self.next_hop_type = next_hop_type
        # The weight of the route.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_type is not None:
            result['NextHopType'] = self.next_hop_type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('NextHopId') is not None:
            self.next_hop_id = m.get('NextHopId')

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

