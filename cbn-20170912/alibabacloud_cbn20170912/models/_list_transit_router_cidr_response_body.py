# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRouterCidrResponseBody(DaraModel):
    def __init__(
        self,
        cidr_lists: List[main_models.ListTransitRouterCidrResponseBodyCidrLists] = None,
        request_id: str = None,
    ):
        # The information about the CIDR block.
        self.cidr_lists = cidr_lists
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.cidr_lists:
            for v1 in self.cidr_lists:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CidrLists'] = []
        if self.cidr_lists is not None:
            for k1 in self.cidr_lists:
                result['CidrLists'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cidr_lists = []
        if m.get('CidrLists') is not None:
            for k1 in m.get('CidrLists'):
                temp_model = main_models.ListTransitRouterCidrResponseBodyCidrLists()
                self.cidr_lists.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListTransitRouterCidrResponseBodyCidrLists(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
        family: str = None,
        name: str = None,
        publish_cidr_route: bool = None,
        transit_router_cidr_id: str = None,
        transit_router_id: str = None,
    ):
        # The CIDR block of the transit router.
        self.cidr = cidr
        # The description of the CIDR block.
        self.description = description
        # The type of the CIDR block.
        # 
        # The value is **IPv4**, which indicates that the CIDR block is of the IPv4 type.
        self.family = family
        # The name of the CIDR block.
        self.name = name
        # Indicates whether the system is allowed to automatically add a route to the route table of the transit router. Valid values:
        # 
        # *   **true**
        # 
        #     A value of **true** indicates that after you create a private VPN connection and enable route learning for the connection, the system automatically adds a blackhole route to the route table of the transit router to which the VPN connection is attached.
        # 
        #     The destination CIDR block of the blackhole route is the CIDR block of the transit router. The CIDR block of the transit router refers to the CIDR block from which gateway IP addresses are allocated to IPsec-VPN connections.
        # 
        #     The blackhole route is advertised only to the route table of the virtual border router (VBR) that is connected to the transit router.
        # 
        # *   **false**
        self.publish_cidr_route = publish_cidr_route
        # The ID of the transit router CIDR block.
        self.transit_router_cidr_id = transit_router_cidr_id
        # The transit router ID.
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['Cidr'] = self.cidr

        if self.description is not None:
            result['Description'] = self.description

        if self.family is not None:
            result['Family'] = self.family

        if self.name is not None:
            result['Name'] = self.name

        if self.publish_cidr_route is not None:
            result['PublishCidrRoute'] = self.publish_cidr_route

        if self.transit_router_cidr_id is not None:
            result['TransitRouterCidrId'] = self.transit_router_cidr_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Family') is not None:
            self.family = m.get('Family')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishCidrRoute') is not None:
            self.publish_cidr_route = m.get('PublishCidrRoute')

        if m.get('TransitRouterCidrId') is not None:
            self.transit_router_cidr_id = m.get('TransitRouterCidrId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

