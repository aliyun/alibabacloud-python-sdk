# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTransitRoutersResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        transit_routers: List[main_models.ListTransitRoutersResponseBodyTransitRouters] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # A list of transit routers.
        self.transit_routers = transit_routers

    def validate(self):
        if self.transit_routers:
            for v1 in self.transit_routers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TransitRouters'] = []
        if self.transit_routers is not None:
            for k1 in self.transit_routers:
                result['TransitRouters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.transit_routers = []
        if m.get('TransitRouters') is not None:
            for k1 in m.get('TransitRouters'):
                temp_model = main_models.ListTransitRoutersResponseBodyTransitRouters()
                self.transit_routers.append(temp_model.from_map(k1))

        return self

class ListTransitRoutersResponseBodyTransitRouters(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        cen_id: str = None,
        creation_time: str = None,
        region_id: str = None,
        status: str = None,
        support_multicast: bool = None,
        tags: List[main_models.ListTransitRoutersResponseBodyTransitRoutersTags] = None,
        transit_router_cidr_list: List[main_models.ListTransitRoutersResponseBodyTransitRoutersTransitRouterCidrList] = None,
        transit_router_description: str = None,
        transit_router_id: str = None,
        transit_router_name: str = None,
        type: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the CEN instance belongs.
        self.ali_uid = ali_uid
        # The ID of the CEN instance.
        self.cen_id = cen_id
        # The time when the transit router was created.
        # 
        # The time is displayed in the `YYYY-MM-DDThh:mmZ` format in UTC.
        self.creation_time = creation_time
        # The ID of the region where the transit router is deployed.
        self.region_id = region_id
        # The status of the transit router.
        # 
        # - **Creating**: The transit router is being created.
        # 
        # - **Active**: The transit router is available.
        # 
        # - **Modifying**: The transit router is being modified.
        # 
        # - **Deleting**: The transit router is being deleted.
        # 
        # - **Upgrading**: The transit router is being upgraded.
        self.status = status
        # Indicates whether the multicast feature is enabled for the transit router.
        # 
        # - **true**: enabled.
        # 
        # - **false**: disabled.
        self.support_multicast = support_multicast
        # A list of tags.
        self.tags = tags
        # A list of CIDR blocks of the transit router.
        self.transit_router_cidr_list = transit_router_cidr_list
        # The description of the transit router.
        self.transit_router_description = transit_router_description
        # The ID of the transit router.
        self.transit_router_id = transit_router_id
        # The name of the transit router.
        self.transit_router_name = transit_router_name
        # The type of the transit router.
        # 
        # - **Enterprise**: Enterprise Edition.
        # 
        # - **Basic**: Basic Edition.
        self.type = type

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.transit_router_cidr_list:
            for v1 in self.transit_router_cidr_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.support_multicast is not None:
            result['SupportMulticast'] = self.support_multicast

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['TransitRouterCidrList'] = []
        if self.transit_router_cidr_list is not None:
            for k1 in self.transit_router_cidr_list:
                result['TransitRouterCidrList'].append(k1.to_map() if k1 else None)

        if self.transit_router_description is not None:
            result['TransitRouterDescription'] = self.transit_router_description

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.transit_router_name is not None:
            result['TransitRouterName'] = self.transit_router_name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupportMulticast') is not None:
            self.support_multicast = m.get('SupportMulticast')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListTransitRoutersResponseBodyTransitRoutersTags()
                self.tags.append(temp_model.from_map(k1))

        self.transit_router_cidr_list = []
        if m.get('TransitRouterCidrList') is not None:
            for k1 in m.get('TransitRouterCidrList'):
                temp_model = main_models.ListTransitRoutersResponseBodyTransitRoutersTransitRouterCidrList()
                self.transit_router_cidr_list.append(temp_model.from_map(k1))

        if m.get('TransitRouterDescription') is not None:
            self.transit_router_description = m.get('TransitRouterDescription')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('TransitRouterName') is not None:
            self.transit_router_name = m.get('TransitRouterName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListTransitRoutersResponseBodyTransitRoutersTransitRouterCidrList(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        description: str = None,
        name: str = None,
        publish_cidr_route: bool = None,
        transit_router_cidr_id: str = None,
    ):
        # The CIDR block of the transit router.
        self.cidr = cidr
        # The description of the CIDR block.
        self.description = description
        # The name of the CIDR block.
        self.name = name
        # Indicates whether the system automatically adds a route for the transit router CIDR block to the route table of the transit router.
        # 
        # - **true**: Yes.
        # 
        #   If this parameter is set to **true**, after you create a VPN connection of the private gateway type and enable route learning for the VPN connection, the system automatically adds a blackhole route to the route table of the transit router that is in a route learning correlation with the VPN connection.
        # 
        #   The destination CIDR block of the blackhole route is the CIDR block of the transit router. The CIDR block of the transit router is the CIDR block from which an IP address is allocated to the IPsec-VPN connection.
        # 
        #   This blackhole route is advertised only to the route tables of the virtual border routers (VBRs) that are connected to the transit router.
        # 
        # - **false**: No.
        self.publish_cidr_route = publish_cidr_route
        # The ID of the CIDR block.
        self.transit_router_cidr_id = transit_router_cidr_id

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

        if self.name is not None:
            result['Name'] = self.name

        if self.publish_cidr_route is not None:
            result['PublishCidrRoute'] = self.publish_cidr_route

        if self.transit_router_cidr_id is not None:
            result['TransitRouterCidrId'] = self.transit_router_cidr_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cidr') is not None:
            self.cidr = m.get('Cidr')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PublishCidrRoute') is not None:
            self.publish_cidr_route = m.get('PublishCidrRoute')

        if m.get('TransitRouterCidrId') is not None:
            self.transit_router_cidr_id = m.get('TransitRouterCidrId')

        return self

class ListTransitRoutersResponseBodyTransitRoutersTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

