# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeSagRouteListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        routes: List[main_models.DescribeSagRouteListResponseBodyRoutes] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The routes.
        self.routes = routes

    def validate(self):
        if self.routes:
            for v1 in self.routes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['Routes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.routes = []
        if m.get('Routes') is not None:
            for k1 in m.get('Routes'):
                temp_model = main_models.DescribeSagRouteListResponseBodyRoutes()
                self.routes.append(temp_model.from_map(k1))

        return self

class DescribeSagRouteListResponseBodyRoutes(DaraModel):
    def __init__(
        self,
        conflict_cidrs: List[str] = None,
        cost: str = None,
        destination_cidr: str = None,
        next_hop: str = None,
        port_name: str = None,
        route_protocol: str = None,
    ):
        # The list of CIDR blocks that overlap with each other.
        self.conflict_cidrs = conflict_cidrs
        # The cost of the route.
        # 
        # The number on the left side of the forward slash (/) indicates the administrative distance (AD) of the routing protocol.
        # 
        # The number on the right side of the forward slash (/) indicates the metric value.
        self.cost = cost
        # The destination CIDR block.
        self.destination_cidr = destination_cidr
        # The next hop.
        self.next_hop = next_hop
        # The name of the port. If the port name is -1, data is transferred through a VPN tunnel to Alibaba Cloud.
        self.port_name = port_name
        # The routing protocol. Valid values:
        # 
        # *   **STATIC**: a static routing protocol.
        # *   **OSPF**: the Open Shortest Path First (OSPF) dynamic routing protocol.
        # *   **BGP**: the Border Gateway Protocol (BGP) dynamic routing protocol.
        self.route_protocol = route_protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflict_cidrs is not None:
            result['ConflictCidrs'] = self.conflict_cidrs

        if self.cost is not None:
            result['Cost'] = self.cost

        if self.destination_cidr is not None:
            result['DestinationCidr'] = self.destination_cidr

        if self.next_hop is not None:
            result['NextHop'] = self.next_hop

        if self.port_name is not None:
            result['PortName'] = self.port_name

        if self.route_protocol is not None:
            result['RouteProtocol'] = self.route_protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConflictCidrs') is not None:
            self.conflict_cidrs = m.get('ConflictCidrs')

        if m.get('Cost') is not None:
            self.cost = m.get('Cost')

        if m.get('DestinationCidr') is not None:
            self.destination_cidr = m.get('DestinationCidr')

        if m.get('NextHop') is not None:
            self.next_hop = m.get('NextHop')

        if m.get('PortName') is not None:
            self.port_name = m.get('PortName')

        if m.get('RouteProtocol') is not None:
            self.route_protocol = m.get('RouteProtocol')

        return self

