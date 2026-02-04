# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenRouteMapsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        route_maps: main_models.DescribeCenRouteMapsResponseBodyRouteMaps = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The information about the routing policy.
        self.route_maps = route_maps
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.route_maps:
            self.route_maps.validate()

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

        if self.route_maps is not None:
            result['RouteMaps'] = self.route_maps.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RouteMaps') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMaps()
            self.route_maps = temp_model.from_map(m.get('RouteMaps'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCenRouteMapsResponseBodyRouteMaps(DaraModel):
    def __init__(
        self,
        route_map: List[main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMap] = None,
    ):
        self.route_map = route_map

    def validate(self):
        if self.route_map:
            for v1 in self.route_map:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RouteMap'] = []
        if self.route_map is not None:
            for k1 in self.route_map:
                result['RouteMap'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.route_map = []
        if m.get('RouteMap') is not None:
            for k1 in m.get('RouteMap'):
                temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMap()
                self.route_map.append(temp_model.from_map(k1))

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMap(DaraModel):
    def __init__(
        self,
        as_path_match_mode: str = None,
        cen_id: str = None,
        cen_region_id: str = None,
        cidr_match_mode: str = None,
        community_match_mode: str = None,
        community_operate_mode: str = None,
        description: str = None,
        destination_child_instance_types: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes = None,
        destination_cidr_blocks: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks = None,
        destination_instance_ids: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds = None,
        destination_instance_ids_reverse_match: bool = None,
        destination_region_ids: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRegionIds = None,
        destination_route_table_ids: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds = None,
        map_result: str = None,
        match_address_type: str = None,
        match_asns: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns = None,
        match_community_set: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet = None,
        next_priority: int = None,
        operate_community_set: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet = None,
        preference: int = None,
        prepend_as_path: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath = None,
        priority: int = None,
        route_map_id: str = None,
        route_types: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes = None,
        source_child_instance_types: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes = None,
        source_instance_ids: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds = None,
        source_instance_ids_reverse_match: bool = None,
        source_region_ids: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds = None,
        source_route_table_ids: main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds = None,
        status: str = None,
        transit_router_route_table_id: str = None,
        transmit_direction: str = None,
    ):
        # The match method that is used to match routes based on the AS path.
        # 
        # *   **Include**: fuzzy match. A route is a match if the AS path of the route overlaps with the AS path specified in the match condition.
        # *   **Complete**: exact match. A route is a match only if the AS path of the route is the same as an AS path specified in the match condition.
        self.as_path_match_mode = as_path_match_mode
        # The CEN instance ID.
        self.cen_id = cen_id
        # The region ID of the routing policy.
        self.cen_region_id = cen_region_id
        # The match method that is used to evaluate routes based on the prefix. Valid values:
        # 
        # *   **Include**: fuzzy match. A route is a match if the route prefix is included in the match conditions.
        # 
        # For example, if you set the match condition to 10.10.0.0/16 and fuzzy match is applied, the route whose prefix is 10.10.1.0/24 meets the match condition.
        # 
        # *   **Complete**: exact match. A route is a match only if the route prefix is the same as the prefix specified in the match condition.
        # 
        # For example, if you set the match condition to 10.10.0.0/16 and exact match is enabled, a route is a match only if the prefix is 10.10.0.0/16.
        self.cidr_match_mode = cidr_match_mode
        # The match method that is used to match routes against the community.
        # 
        # *   **Include**: fuzzy match. A route is a match if the community of the route overlaps with the community specified in the match condition.
        # *   **Complete**: exact match. A route meets the match condition only if the community of the route is the same as the community specified in the match condition.
        self.community_match_mode = community_match_mode
        # The action that is performed on the community of the route.
        # 
        # *   **Additive**: adds the community to the route.
        # *   **Replace**: replaces the original community of the route.
        # 
        # This parameter specifies the action to be performed when a route meets the match condition.
        self.community_operate_mode = community_operate_mode
        # The description of the routing policy.
        self.description = description
        # The types of destination network instances to which the routes belong.
        # 
        # *   **VPC**
        # *   **VBR**
        # *   **CCN**
        # *   **VPN**
        # 
        # >  The destination route tables take effect only if the routing policy is applied to the egress gateway direction, and the type of the destination route tables is the same as that of the network instance in the current region.
        self.destination_child_instance_types = destination_child_instance_types
        # The prefix list against which routes are matched.
        # 
        # IPv4 and IPv6 addresses are supported.
        self.destination_cidr_blocks = destination_cidr_blocks
        # The IDs of the destination network instances to which the routes point.
        # 
        # >  The destination route tables take effect only if the routing policy is applied to the egress gateway direction, and the ID the destination instance is the same as that of the network instance in the current region.
        self.destination_instance_ids = destination_instance_ids
        # Indicates whether the destination network instance IDs are excluded.
        # 
        # *   **false** (default): A route is a match if its destination network instance ID is in the list specified by **DestinationInstanceIds.N**.
        # *   **true**: A route is a match if its destination network instance ID is not in the list specified by **DestinationInstanceIds.N**.
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        # The IDs of the destination regions for the routing policy.
        self.destination_region_ids = destination_region_ids
        # The IDs of the destination route tables to which the routes belong. You can enter at most 32 route table IDs.
        # 
        # >  The destination route tables take effect only if the routing policy is applied to the egress gateway direction, and the destination route table IDs are in the current region.
        self.destination_route_table_ids = destination_route_table_ids
        # The action performed on a route that meets the match conditions.
        # 
        # *   **Permit**: the route is permitted.
        # *   **Deny**: the route is denied.
        self.map_result = map_result
        # The type of IP address to be matched against the match condition. Valid values:
        # 
        # *   **IPv4**: IPv4 addresses
        # *   **IPv6**: IPv6 addresses
        # *   If no value is returned, both IPv4 and IPv6 addresses are matched against the match condition.
        self.match_address_type = match_address_type
        # The AS paths against which routes are matched.
        self.match_asns = match_asns
        # The community set against which routes are matched.
        self.match_community_set = match_community_set
        # The priority of the routing policy that you want to associate with the current one.
        self.next_priority = next_priority
        # The community set on which actions are performed.
        self.operate_community_set = operate_community_set
        # The new priority of the route.
        # 
        # A smaller value indicates a higher priority.
        # 
        # This parameter indicates the action to be performed when a route meets the match condition.
        self.preference = preference
        # The AS paths that are prepended by using an action statement when regional gateways receive or advertise routes.
        # 
        # This parameter indicates the action to be performed when a route meets the match condition.
        self.prepend_as_path = prepend_as_path
        # The priority of the routing policy. A smaller value indicates a higher priority.
        self.priority = priority
        # The routing policy ID.
        self.route_map_id = route_map_id
        # The type of route that is compared. Valid values:
        # 
        # *   **System**: system routes that are automatically generated by the system.
        # *   **Custom**: custom routes that are manually added.
        # *   **BGP**: routes that are advertised over BGP.
        self.route_types = route_types
        # The types of source network instances to which the routes belong.
        # 
        # *   **VPC**
        # *   **VBR**
        # *   **CCN**
        # *   **VPN**
        self.source_child_instance_types = source_child_instance_types
        # The IDs of the source network instances to which the routes belong.
        self.source_instance_ids = source_instance_ids
        # Indicates whether the source network instance IDs are excluded.
        # 
        # *   **false** (default): A route is a match if its source network instance ID is in the list specified by **SourceInstanceIds.N**.
        # *   **true**: A route is match if its source network instance ID is not in the list specified by **SourceInstanceIds.N**.
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        # The IDs of the source regions to which the routes belong.
        self.source_region_ids = source_region_ids
        # The IDs of the source route tables to which the routes belong.
        self.source_route_table_ids = source_route_table_ids
        # The status of the routing policy. Valid values:
        # 
        # *   **Creating**
        # *   **Active**
        # *   **Deleting**
        self.status = status
        # The route table ID of the transit router with which the routing policy is associated.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The direction in which the routing policy is applied.
        self.transmit_direction = transmit_direction

    def validate(self):
        if self.destination_child_instance_types:
            self.destination_child_instance_types.validate()
        if self.destination_cidr_blocks:
            self.destination_cidr_blocks.validate()
        if self.destination_instance_ids:
            self.destination_instance_ids.validate()
        if self.destination_region_ids:
            self.destination_region_ids.validate()
        if self.destination_route_table_ids:
            self.destination_route_table_ids.validate()
        if self.match_asns:
            self.match_asns.validate()
        if self.match_community_set:
            self.match_community_set.validate()
        if self.operate_community_set:
            self.operate_community_set.validate()
        if self.prepend_as_path:
            self.prepend_as_path.validate()
        if self.route_types:
            self.route_types.validate()
        if self.source_child_instance_types:
            self.source_child_instance_types.validate()
        if self.source_instance_ids:
            self.source_instance_ids.validate()
        if self.source_region_ids:
            self.source_region_ids.validate()
        if self.source_route_table_ids:
            self.source_route_table_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_path_match_mode is not None:
            result['AsPathMatchMode'] = self.as_path_match_mode

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cen_region_id is not None:
            result['CenRegionId'] = self.cen_region_id

        if self.cidr_match_mode is not None:
            result['CidrMatchMode'] = self.cidr_match_mode

        if self.community_match_mode is not None:
            result['CommunityMatchMode'] = self.community_match_mode

        if self.community_operate_mode is not None:
            result['CommunityOperateMode'] = self.community_operate_mode

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_child_instance_types is not None:
            result['DestinationChildInstanceTypes'] = self.destination_child_instance_types.to_map()

        if self.destination_cidr_blocks is not None:
            result['DestinationCidrBlocks'] = self.destination_cidr_blocks.to_map()

        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids.to_map()

        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match

        if self.destination_region_ids is not None:
            result['DestinationRegionIds'] = self.destination_region_ids.to_map()

        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids.to_map()

        if self.map_result is not None:
            result['MapResult'] = self.map_result

        if self.match_address_type is not None:
            result['MatchAddressType'] = self.match_address_type

        if self.match_asns is not None:
            result['MatchAsns'] = self.match_asns.to_map()

        if self.match_community_set is not None:
            result['MatchCommunitySet'] = self.match_community_set.to_map()

        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority

        if self.operate_community_set is not None:
            result['OperateCommunitySet'] = self.operate_community_set.to_map()

        if self.preference is not None:
            result['Preference'] = self.preference

        if self.prepend_as_path is not None:
            result['PrependAsPath'] = self.prepend_as_path.to_map()

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        if self.route_types is not None:
            result['RouteTypes'] = self.route_types.to_map()

        if self.source_child_instance_types is not None:
            result['SourceChildInstanceTypes'] = self.source_child_instance_types.to_map()

        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids.to_map()

        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match

        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids.to_map()

        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.transit_router_route_table_id is not None:
            result['TransitRouterRouteTableId'] = self.transit_router_route_table_id

        if self.transmit_direction is not None:
            result['TransmitDirection'] = self.transmit_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPathMatchMode') is not None:
            self.as_path_match_mode = m.get('AsPathMatchMode')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CenRegionId') is not None:
            self.cen_region_id = m.get('CenRegionId')

        if m.get('CidrMatchMode') is not None:
            self.cidr_match_mode = m.get('CidrMatchMode')

        if m.get('CommunityMatchMode') is not None:
            self.community_match_mode = m.get('CommunityMatchMode')

        if m.get('CommunityOperateMode') is not None:
            self.community_operate_mode = m.get('CommunityOperateMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationChildInstanceTypes') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes()
            self.destination_child_instance_types = temp_model.from_map(m.get('DestinationChildInstanceTypes'))

        if m.get('DestinationCidrBlocks') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks()
            self.destination_cidr_blocks = temp_model.from_map(m.get('DestinationCidrBlocks'))

        if m.get('DestinationInstanceIds') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds()
            self.destination_instance_ids = temp_model.from_map(m.get('DestinationInstanceIds'))

        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')

        if m.get('DestinationRegionIds') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRegionIds()
            self.destination_region_ids = temp_model.from_map(m.get('DestinationRegionIds'))

        if m.get('DestinationRouteTableIds') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds()
            self.destination_route_table_ids = temp_model.from_map(m.get('DestinationRouteTableIds'))

        if m.get('MapResult') is not None:
            self.map_result = m.get('MapResult')

        if m.get('MatchAddressType') is not None:
            self.match_address_type = m.get('MatchAddressType')

        if m.get('MatchAsns') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns()
            self.match_asns = temp_model.from_map(m.get('MatchAsns'))

        if m.get('MatchCommunitySet') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet()
            self.match_community_set = temp_model.from_map(m.get('MatchCommunitySet'))

        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')

        if m.get('OperateCommunitySet') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet()
            self.operate_community_set = temp_model.from_map(m.get('OperateCommunitySet'))

        if m.get('Preference') is not None:
            self.preference = m.get('Preference')

        if m.get('PrependAsPath') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath()
            self.prepend_as_path = temp_model.from_map(m.get('PrependAsPath'))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        if m.get('RouteTypes') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes()
            self.route_types = temp_model.from_map(m.get('RouteTypes'))

        if m.get('SourceChildInstanceTypes') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes()
            self.source_child_instance_types = temp_model.from_map(m.get('SourceChildInstanceTypes'))

        if m.get('SourceInstanceIds') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds()
            self.source_instance_ids = temp_model.from_map(m.get('SourceInstanceIds'))

        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')

        if m.get('SourceRegionIds') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds()
            self.source_region_ids = temp_model.from_map(m.get('SourceRegionIds'))

        if m.get('SourceRouteTableIds') is not None:
            temp_model = main_models.DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds()
            self.source_route_table_ids = temp_model.from_map(m.get('SourceRouteTableIds'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')

        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRouteTableIds(DaraModel):
    def __init__(
        self,
        source_route_table_id: List[str] = None,
    ):
        self.source_route_table_id = source_route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_route_table_id is not None:
            result['SourceRouteTableId'] = self.source_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceRouteTableId') is not None:
            self.source_route_table_id = m.get('SourceRouteTableId')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceRegionIds(DaraModel):
    def __init__(
        self,
        source_region_id: List[str] = None,
    ):
        self.source_region_id = source_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_region_id is not None:
            result['SourceRegionId'] = self.source_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceRegionId') is not None:
            self.source_region_id = m.get('SourceRegionId')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceInstanceIds(DaraModel):
    def __init__(
        self,
        source_instance_id: List[str] = None,
    ):
        self.source_instance_id = source_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapSourceChildInstanceTypes(DaraModel):
    def __init__(
        self,
        source_child_instance_type: List[str] = None,
    ):
        self.source_child_instance_type = source_child_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_child_instance_type is not None:
            result['SourceChildInstanceType'] = self.source_child_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceChildInstanceType') is not None:
            self.source_child_instance_type = m.get('SourceChildInstanceType')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapRouteTypes(DaraModel):
    def __init__(
        self,
        route_type: List[str] = None,
    ):
        self.route_type = route_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_type is not None:
            result['RouteType'] = self.route_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapPrependAsPath(DaraModel):
    def __init__(
        self,
        as_path: List[str] = None,
    ):
        self.as_path = as_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_path is not None:
            result['AsPath'] = self.as_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPath') is not None:
            self.as_path = m.get('AsPath')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapOperateCommunitySet(DaraModel):
    def __init__(
        self,
        operate_community: List[str] = None,
    ):
        self.operate_community = operate_community

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate_community is not None:
            result['OperateCommunity'] = self.operate_community

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperateCommunity') is not None:
            self.operate_community = m.get('OperateCommunity')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchCommunitySet(DaraModel):
    def __init__(
        self,
        match_community: List[str] = None,
    ):
        self.match_community = match_community

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_community is not None:
            result['MatchCommunity'] = self.match_community

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchCommunity') is not None:
            self.match_community = m.get('MatchCommunity')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapMatchAsns(DaraModel):
    def __init__(
        self,
        match_asn: List[str] = None,
    ):
        self.match_asn = match_asn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match_asn is not None:
            result['MatchAsn'] = self.match_asn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchAsn') is not None:
            self.match_asn = m.get('MatchAsn')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRouteTableIds(DaraModel):
    def __init__(
        self,
        destination_route_table_id: List[str] = None,
    ):
        self.destination_route_table_id = destination_route_table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_route_table_id is not None:
            result['DestinationRouteTableId'] = self.destination_route_table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRouteTableId') is not None:
            self.destination_route_table_id = m.get('DestinationRouteTableId')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationRegionIds(DaraModel):
    def __init__(
        self,
        destination_region_id: List[str] = None,
    ):
        self.destination_region_id = destination_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationInstanceIds(DaraModel):
    def __init__(
        self,
        destination_instance_id: List[str] = None,
    ):
        self.destination_instance_id = destination_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_instance_id is not None:
            result['DestinationInstanceId'] = self.destination_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationInstanceId') is not None:
            self.destination_instance_id = m.get('DestinationInstanceId')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationCidrBlocks(DaraModel):
    def __init__(
        self,
        destination_cidr_block: List[str] = None,
    ):
        self.destination_cidr_block = destination_cidr_block

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        return self

class DescribeCenRouteMapsResponseBodyRouteMapsRouteMapDestinationChildInstanceTypes(DaraModel):
    def __init__(
        self,
        destination_child_instance_type: List[str] = None,
    ):
        self.destination_child_instance_type = destination_child_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_child_instance_type is not None:
            result['DestinationChildInstanceType'] = self.destination_child_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationChildInstanceType') is not None:
            self.destination_child_instance_type = m.get('DestinationChildInstanceType')

        return self

