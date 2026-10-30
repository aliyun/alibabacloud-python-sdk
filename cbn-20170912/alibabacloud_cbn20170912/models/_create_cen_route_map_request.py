# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateCenRouteMapRequest(DaraModel):
    def __init__(
        self,
        as_path_match_mode: str = None,
        cen_id: str = None,
        cen_region_id: str = None,
        cidr_match_mode: str = None,
        community_match_mode: str = None,
        community_operate_mode: str = None,
        description: str = None,
        destination_child_instance_types: List[str] = None,
        destination_cidr_blocks: List[str] = None,
        destination_instance_ids: List[str] = None,
        destination_instance_ids_reverse_match: bool = None,
        destination_region_ids: List[str] = None,
        destination_route_table_ids: List[str] = None,
        map_result: str = None,
        match_address_type: str = None,
        match_asns: List[int] = None,
        match_community_set: List[str] = None,
        next_priority: int = None,
        operate_community_set: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        preference: int = None,
        prepend_as_path: List[int] = None,
        priority: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_types: List[str] = None,
        source_child_instance_types: List[str] = None,
        source_instance_ids: List[str] = None,
        source_instance_ids_reverse_match: bool = None,
        source_region_ids: List[str] = None,
        source_route_table_ids: List[str] = None,
        transit_router_route_table_id: str = None,
        transmit_direction: str = None,
    ):
        # The match mode of the AS path list. Valid values:
        # 
        # - **Include**: fuzzy match. A route meets the match condition if the AS path in the match condition overlaps with the AS path of the route. 
        # 
        # - **Complete**: exact match. A route meets the match condition only if the AS path in the match condition is exactly the same as the AS path of the route.
        self.as_path_match_mode = as_path_match_mode
        # The Cloud Enterprise Network (CEN) instance ID.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The ID of the region where the route map is applied.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query region IDs.
        # 
        # This parameter is required.
        self.cen_region_id = cen_region_id
        # The match mode of the prefix list. Valid values:
        # 
        # - **Include**: fuzzy match. A route meets the match condition if the route prefix in the match condition contains the prefix of the route.
        # 
        #  For example, if the match condition is 10.10.0.0/16, a route with the prefix 10.10.1.0/24 meets the condition.
        # 
        # - **Complete**: exact match. A route meets the match condition only if the route prefix in the match condition is exactly the same as the prefix of the route. 
        # 
        #  For example, if the match condition is 10.10.0.0/16, only a route with the prefix 10.10.0.0/16 meets the condition.
        self.cidr_match_mode = cidr_match_mode
        # The match mode of the community. Valid values:
        # 
        # - **Include**: fuzzy match. A route meets the match condition if the community in the match condition overlaps with the community of the route. 
        # 
        # - **Complete**: exact match. A route meets the match condition only if the community in the match condition is exactly the same as the community of the route.
        # 
        # - **Contain**: contain match. A route meets the match condition only if the community of the route contains all communities specified in the match condition.
        self.community_match_mode = community_match_mode
        # The action mode of the community. Valid values:
        # 
        # - **Additive**: adds a community to the route.
        # 
        # - **Replace**: replaces the existing community of the route.
        # 
        # This parameter specifies the action to be performed after a route meets the match conditions.
        self.community_operate_mode = community_operate_mode
        # The description of the route map. The description must be 1 to 256 characters in length, and cannot start with http:// or https://. The description can be left empty.
        self.description = description
        # The list of destination instance types to be matched. The following instance types are supported:
        # 
        # - **VPC**: VPC instance.
        # 
        # - **VBR**: VBR instance.
        # 
        # - **CCN**: CCN instance.
        # 
        # - **VPN**: IPsec connection.
        # 
        #     > If an IPsec connection or SSL server is associated with a VPN gateway instance and connected to a transit router instance through the VPC associated with the VPN gateway instance, this parameter does not take effect. This parameter takes effect only when an IPsec connection is directly associated with a transit router instance.
        # 
        # You can enter multiple instance types.
        # 
        # > The destination instance type list takes effect only when the application direction of the route map is set to RegionOut and the destination instance types are the types of instances in the local region.
        self.destination_child_instance_types = destination_child_instance_types
        # The prefix list to be matched.
        # 
        # The CIDR blocks in the prefix list must be in CIDR format. You can enter up to 64 CIDR blocks.
        # 
        # Both IPv4 and IPv6 formats are supported.
        self.destination_cidr_blocks = destination_cidr_blocks
        # The list of destination instance IDs to be matched. You can enter the IDs of the following types of instances:
        # 
        # - Virtual Private Cloud (VPC) instance IDs
        # - Virtual Border Router (VBR) instance IDs
        # - Cloud Connect Network (CCN) instance IDs
        # - Smart Access Gateway (SAG) instance IDs
        # - IPsec connection IDs
        # 
        # You can enter up to 64 instance IDs.
        # 
        # > The destination instance ID list takes effect only when the application direction of the route map is set to RegionOut and the destination instance IDs are the IDs of instances in the local region.
        self.destination_instance_ids = destination_instance_ids
        # Specifies whether to use the exclude match mode for the destination instance ID list. Valid values:
        # 
        # - **false** (default): no. A route meets the match condition if the destination instance ID of the route is in **DestinationInstanceIds.N**.
        # 
        # - **true**: yes. A route meets the match condition if the destination instance ID of the route is not in **DestinationInstanceIds.N**.
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        # The list of destination region IDs to be matched. You can enter up to 64 region IDs.
        self.destination_region_ids = destination_region_ids
        # The list of destination route table IDs to be matched. You can enter up to 64 route table IDs.
        # 
        # > The destination route table ID list takes effect only when the application direction of the route map is set to RegionOut and the destination route table IDs are the IDs of route tables of network instances in the local region.
        self.destination_route_table_ids = destination_route_table_ids
        # The action to be performed when a route meets all match conditions. Valid values:
        # 
        # - **Permit**: permits the matched route.
        # 
        # - **Deny**: denies the matched route.
        # 
        # This parameter is required.
        self.map_result = map_result
        # The IP address type of the routes to be matched. Valid values:
        # 
        # - **IPv4**: matches only IPv4 routes.
        # - **IPv6**: matches only IPv6 routes.
        # 
        # If this parameter is left empty, all types of routes are matched.
        self.match_address_type = match_address_type
        # The AS path list to be matched.
        # 
        # You can enter up to 64 AS numbers.
        # 
        # > Only AS SEQUENCE is supported. AS SET, AS CONFED SEQUENCE, and AS CONFED SET are not supported. This means only AS number lists are supported, and sets and sub-lists are not supported.
        self.match_asns = match_asns
        # The community set to be matched.
        # 
        # Each community must be in the format of n:m, where n and m are integers from **1** to **65535**. Communities must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # You can enter up to 64 communities.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.match_community_set = match_community_set
        # Policy priority of the next route map to be associated.
        # 
        # - You can set this parameter only when **MapResult** is set to **Permit**. Only permitted routes are matched against the next associated route map.
        # - The next route map to be associated must be applied to the same region and in the same direction as the current route map.
        # - Policy priority of the next route map to be associated must be lower than that of the current route map.
        self.next_priority = next_priority
        # The community set to be operated.
        # 
        # Each community must be in the format of n:m, where n and m are integers from **1** to **65535**. Communities must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # You can enter up to 32 communities.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.operate_community_set = operate_community_set
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The priority of the route to be modified.
        # 
        # Valid values: **1** to **100**. The default priority of a route is **50**. A smaller value indicates a higher priority.
        # 
        # This parameter specifies the action to be performed after a route meets the match conditions.
        self.preference = preference
        # The AS path to be prepended when the regional gateway receives or performs publish route entry.
        # 
        # The requirements for configuring the prepended AS path vary based on the application direction of the policy:
        # 
        # - If the application direction is RegionIn, you must configure the source instance ID list and source region in the match conditions, and the source region must be the same as the region where the policy is applied.
        # 
        # - If the application direction is RegionOut, you must configure the destination instance ID list in the match conditions.
        # 
        # 
        # This parameter specifies the action to be executed after routing meets the match conditions. You can enter up to 32 AS numbers.
        self.prepend_as_path = prepend_as_path
        # The policy priority of the route map. Valid values: **1** to **100**. A smaller value indicates a higher priority.
        # 
        # > The policy priority of each route map applied to the same region in the same direction must be unique. When the policy is executed, the system matches routing against the conditional statements of the policy with the smallest priority value first. Therefore, specify the policy priority based on the expected match order.
        # 
        # This parameter is required.
        self.priority = priority
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of route types to be matched. The following route types are supported:
        # 
        # - **System**: system routing, which is automatically generated by the system.
        # 
        # - **Custom**: custom routing, which is manually added by a user.
        # 
        # - **BGP**: BGP routing, which is propagated through the BGP routable protocol.
        # 
        # You can enter multiple route types.
        self.route_types = route_types
        # The list of source instance types to be matched. The following instance types are supported:
        # 
        # - **VPC**: VPC instance.
        # 
        # - **VBR**: border router instance.
        # 
        # - **CCN**: CCN instance.
        # 
        # - **VPN**: VPN gateway instance or IPsec connection.
        # 
        #     - If an IPsec connection or SSL server is attached to a VPN gateway instance, the VPC associated with the VPN gateway instance must be connected to a forward router instance, and the VPN gateway instance must run the BGP dynamic routing routable protocol for this parameter to take effect.
        #     - If an IPsec connection is directly attached to a forward router instance, this parameter takes effect.
        # 
        # You can enter multiple instance types.
        self.source_child_instance_types = source_child_instance_types
        # The list of source instance IDs to be matched. You can enter the IDs of the following types of instances:
        # 
        # - Virtual Private Cloud (VPC) instance IDs
        # - Virtual Border Router (VBR) instance IDs
        # - Cloud Connect Network (CCN) instance IDs
        # - Smart Access Gateway (SAG) instance IDs
        # - IPsec connection IDs
        # 
        # You can enter up to 64 instance IDs.
        self.source_instance_ids = source_instance_ids
        # Specifies whether to use the exclude match mode for the source instance ID list. Valid values:
        # 
        # - **false** (default): no. A route meets the match condition if the source instance ID of the route is in **SourceInstanceIds.N**.
        # 
        # - **true**: yes. A route meets the match condition if the source instance ID of the route is not in **SourceInstanceIds.N**.
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        # The list of source region IDs to be matched. You can enter up to 64 region IDs.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query region IDs.
        self.source_region_ids = source_region_ids
        # The list of source route table IDs to be matched. You can enter up to 64 route table IDs.
        self.source_route_table_ids = source_route_table_ids
        # The ID of the route table of the transit router.
        # 
        # If you do not specify a route table ID, the route map is automatically associated with the default route table of the transit router.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The application direction of the route map. Valid values:
        # 
        # - **RegionIn**: the direction in which routes are transmitted to the regional gateway of the CEN instance. For example, routes are advertised from a network instance in a region to the regional gateway in the same region, or routes are advertised from another region to the regional gateway.
        # 
        # - **RegionOut**: the direction in which routes are transmitted from the regional gateway of the CEN instance. For example, routes are advertised from the regional gateway to a network instance in the same region, or to a regional gateway in another region.
        # 
        # This parameter is required.
        self.transmit_direction = transmit_direction

    def validate(self):
        pass

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
            result['DestinationChildInstanceTypes'] = self.destination_child_instance_types

        if self.destination_cidr_blocks is not None:
            result['DestinationCidrBlocks'] = self.destination_cidr_blocks

        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids

        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match

        if self.destination_region_ids is not None:
            result['DestinationRegionIds'] = self.destination_region_ids

        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids

        if self.map_result is not None:
            result['MapResult'] = self.map_result

        if self.match_address_type is not None:
            result['MatchAddressType'] = self.match_address_type

        if self.match_asns is not None:
            result['MatchAsns'] = self.match_asns

        if self.match_community_set is not None:
            result['MatchCommunitySet'] = self.match_community_set

        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority

        if self.operate_community_set is not None:
            result['OperateCommunitySet'] = self.operate_community_set

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.preference is not None:
            result['Preference'] = self.preference

        if self.prepend_as_path is not None:
            result['PrependAsPath'] = self.prepend_as_path

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_types is not None:
            result['RouteTypes'] = self.route_types

        if self.source_child_instance_types is not None:
            result['SourceChildInstanceTypes'] = self.source_child_instance_types

        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids

        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match

        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids

        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids

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
            self.destination_child_instance_types = m.get('DestinationChildInstanceTypes')

        if m.get('DestinationCidrBlocks') is not None:
            self.destination_cidr_blocks = m.get('DestinationCidrBlocks')

        if m.get('DestinationInstanceIds') is not None:
            self.destination_instance_ids = m.get('DestinationInstanceIds')

        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')

        if m.get('DestinationRegionIds') is not None:
            self.destination_region_ids = m.get('DestinationRegionIds')

        if m.get('DestinationRouteTableIds') is not None:
            self.destination_route_table_ids = m.get('DestinationRouteTableIds')

        if m.get('MapResult') is not None:
            self.map_result = m.get('MapResult')

        if m.get('MatchAddressType') is not None:
            self.match_address_type = m.get('MatchAddressType')

        if m.get('MatchAsns') is not None:
            self.match_asns = m.get('MatchAsns')

        if m.get('MatchCommunitySet') is not None:
            self.match_community_set = m.get('MatchCommunitySet')

        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')

        if m.get('OperateCommunitySet') is not None:
            self.operate_community_set = m.get('OperateCommunitySet')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Preference') is not None:
            self.preference = m.get('Preference')

        if m.get('PrependAsPath') is not None:
            self.prepend_as_path = m.get('PrependAsPath')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteTypes') is not None:
            self.route_types = m.get('RouteTypes')

        if m.get('SourceChildInstanceTypes') is not None:
            self.source_child_instance_types = m.get('SourceChildInstanceTypes')

        if m.get('SourceInstanceIds') is not None:
            self.source_instance_ids = m.get('SourceInstanceIds')

        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')

        if m.get('SourceRegionIds') is not None:
            self.source_region_ids = m.get('SourceRegionIds')

        if m.get('SourceRouteTableIds') is not None:
            self.source_route_table_ids = m.get('SourceRouteTableIds')

        if m.get('TransitRouterRouteTableId') is not None:
            self.transit_router_route_table_id = m.get('TransitRouterRouteTableId')

        if m.get('TransmitDirection') is not None:
            self.transmit_direction = m.get('TransmitDirection')

        return self

