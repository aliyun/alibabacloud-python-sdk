# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeRouteEntryListResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        route_entrys: main_models.DescribeRouteEntryListResponseBodyRouteEntrys = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If no value is returned for **NextToken**, no next queries are sent.
        # *   If a value is returned for **NextToken**, the value is used to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the routes.
        self.route_entrys = route_entrys

    def validate(self):
        if self.route_entrys:
            self.route_entrys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.route_entrys is not None:
            result['RouteEntrys'] = self.route_entrys.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteEntrys') is not None:
            temp_model = main_models.DescribeRouteEntryListResponseBodyRouteEntrys()
            self.route_entrys = temp_model.from_map(m.get('RouteEntrys'))

        return self

class DescribeRouteEntryListResponseBodyRouteEntrys(DaraModel):
    def __init__(
        self,
        route_entry: List[main_models.DescribeRouteEntryListResponseBodyRouteEntrysRouteEntry] = None,
    ):
        self.route_entry = route_entry

    def validate(self):
        if self.route_entry:
            for v1 in self.route_entry:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouteEntry'] = []
        if self.route_entry is not None:
            for k1 in self.route_entry:
                result['RouteEntry'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_entry = []
        if m.get('RouteEntry') is not None:
            for k1 in m.get('RouteEntry'):
                temp_model = main_models.DescribeRouteEntryListResponseBodyRouteEntrysRouteEntry()
                self.route_entry.append(temp_model.from_map(k1))

        return self

class DescribeRouteEntryListResponseBodyRouteEntrysRouteEntry(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_block: str = None,
        gmt_modified: str = None,
        ip_version: str = None,
        next_hops: main_models.DescribeRouteEntryListResponseBodyRouteEntrysRouteEntryNextHops = None,
        origin: str = None,
        route_entry_id: str = None,
        route_entry_name: str = None,
        route_table_id: str = None,
        service_type: str = None,
        status: str = None,
        type: str = None,
    ):
        # The description of the route.
        self.description = description
        # The destination CIDR block of the route.
        self.destination_cidr_block = destination_cidr_block
        # The time when the route was modified. The time follows the ISO 8601 standard in the `YYYY-MM-DDThh:mm:ssZ` format. The time is displayed in UTC.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modified = gmt_modified
        # The IP version. Valid values: Valid values:
        # 
        # *   **ipv4**
        # *   **ipv6**
        self.ip_version = ip_version
        # The information about the next hops.
        self.next_hops = next_hops
        # The route origin. Valid values:
        # * **RoutePropagation**: The route is created by a dynamic propagation source.
        # * **SystemCreate**: The route is created by the system.
        # * **CustomCreate**: The route is created by a user.
        self.origin = origin
        # The ID of the route.
        self.route_entry_id = route_entry_id
        # The name of the route.
        self.route_entry_name = route_entry_name
        # The ID of the route table.
        self.route_table_id = route_table_id
        # Indicates whether the route is hosted. If the parameter is empty, the route is not hosted.
        # 
        # If **TR** is returned, the route is hosted by a transit router.
        self.service_type = service_type
        # The status of the route entry. Valid values:
        # 
        # *   **Pending**
        # *   **Available**
        # *   **Modifying**
        # *   **Deleting**
        self.status = status
        # The route type. Valid values:
        # 
        # *   **Custom**: custom routes.
        # *   **System**: system routes.
        # *   **BGP**: BGP routes.
        # *   **CEN**: CEN routes.
        # *   **ECR**: ECR routes.
        self.type = type

    def validate(self):
        if self.next_hops:
            self.next_hops.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.next_hops is not None:
            result['NextHops'] = self.next_hops.to_map()

        if self.origin is not None:
            result['Origin'] = self.origin

        if self.route_entry_id is not None:
            result['RouteEntryId'] = self.route_entry_id

        if self.route_entry_name is not None:
            result['RouteEntryName'] = self.route_entry_name

        if self.route_table_id is not None:
            result['RouteTableId'] = self.route_table_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('NextHops') is not None:
            temp_model = main_models.DescribeRouteEntryListResponseBodyRouteEntrysRouteEntryNextHops()
            self.next_hops = temp_model.from_map(m.get('NextHops'))

        if m.get('Origin') is not None:
            self.origin = m.get('Origin')

        if m.get('RouteEntryId') is not None:
            self.route_entry_id = m.get('RouteEntryId')

        if m.get('RouteEntryName') is not None:
            self.route_entry_name = m.get('RouteEntryName')

        if m.get('RouteTableId') is not None:
            self.route_table_id = m.get('RouteTableId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeRouteEntryListResponseBodyRouteEntrysRouteEntryNextHops(DaraModel):
    def __init__(
        self,
        next_hop: List[main_models.DescribeRouteEntryListResponseBodyRouteEntrysRouteEntryNextHopsNextHop] = None,
    ):
        self.next_hop = next_hop

    def validate(self):
        if self.next_hop:
            for v1 in self.next_hop:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NextHop'] = []
        if self.next_hop is not None:
            for k1 in self.next_hop:
                result['NextHop'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.next_hop = []
        if m.get('NextHop') is not None:
            for k1 in m.get('NextHop'):
                temp_model = main_models.DescribeRouteEntryListResponseBodyRouteEntrysRouteEntryNextHopsNextHop()
                self.next_hop.append(temp_model.from_map(k1))

        return self

class DescribeRouteEntryListResponseBodyRouteEntrysRouteEntryNextHopsNextHop(DaraModel):
    def __init__(
        self,
        enabled: int = None,
        next_hop_id: str = None,
        next_hop_region_id: str = None,
        next_hop_related_info: main_models.DescribeRouteEntryListResponseBodyRouteEntrysRouteEntryNextHopsNextHopNextHopRelatedInfo = None,
        next_hop_type: str = None,
        weight: int = None,
    ):
        # Indicates whether the route is available. Valid values:
        # 
        # *   **0**: unavailable
        # *   **1**: available
        # 
        # >  This parameter is returned when the next hop type is set to **RouterInterface**.
        self.enabled = enabled
        # The ID of the next hop.
        self.next_hop_id = next_hop_id
        # The ID of the region where the next hop is deployed.
        # 
        # >  This parameter is returned when the next hop type is set to **RouterInterface**.
        self.next_hop_region_id = next_hop_region_id
        # The information about the next hop.
        self.next_hop_related_info = next_hop_related_info
        # The next hop type. Valid values:
        # 
        # *   **Instance**: an ECS instance.
        # *   **HaVip**: an HaVip.
        # *   **VpnGateway**: a VPN gateway.
        # *   **NatGateway**: a NAT gateway.
        # *   **NetworkInterface**: a secondary ENI.
        # *   **RouterInterface**: a router interface.
        # *   **IPv6Gateway**: an IPv6 gateway.
        # *   **Attachment**: a transit router.
        # *   **Ipv4Gateway**: an IPv4 gateway.
        # *   **GatewayEndpoint**: a gateway endpoint.
        # *   **CenBasic**: CEN does not support transit routers.
        # *   **Ecr**: ECR.
        self.next_hop_type = next_hop_type
        # The weight of the route.
        # 
        # >  This parameter is returned when the next hop type is set to **RouterInterface**.
        self.weight = weight

    def validate(self):
        if self.next_hop_related_info:
            self.next_hop_related_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.next_hop_id is not None:
            result['NextHopId'] = self.next_hop_id

        if self.next_hop_region_id is not None:
            result['NextHopRegionId'] = self.next_hop_region_id

        if self.next_hop_related_info is not None:
            result['NextHopRelatedInfo'] = self.next_hop_related_info.to_map()

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

        if m.get('NextHopRegionId') is not None:
            self.next_hop_region_id = m.get('NextHopRegionId')

        if m.get('NextHopRelatedInfo') is not None:
            temp_model = main_models.DescribeRouteEntryListResponseBodyRouteEntrysRouteEntryNextHopsNextHopNextHopRelatedInfo()
            self.next_hop_related_info = temp_model.from_map(m.get('NextHopRelatedInfo'))

        if m.get('NextHopType') is not None:
            self.next_hop_type = m.get('NextHopType')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class DescribeRouteEntryListResponseBodyRouteEntrysRouteEntryNextHopsNextHopNextHopRelatedInfo(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
    ):
        # The ID of the instance that is associated with the next hop.
        self.instance_id = instance_id
        # The type of the instance associated with the next hop. Valid values:
        # 
        # *   **VPC**: a VPC
        # *   **VBR**: a VBR
        # *   **PCONN**: an Express Connect circuit
        self.instance_type = instance_type
        # The region ID of the instance associated with the next hop. Valid values:
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

