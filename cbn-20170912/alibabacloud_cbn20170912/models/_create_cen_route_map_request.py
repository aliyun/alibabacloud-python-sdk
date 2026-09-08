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
        # - **Include**: fuzzy match. A match is successful if the AS path in the match condition overlaps with the AS path of the route being matched. 
        # 
        # - **Complete**: exact match. A match is successful only if the AS path in the match condition is the same as the AS path of the route being matched.
        self.as_path_match_mode = as_path_match_mode
        # The instance ID of the Cloud Enterprise Network (CEN).
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The ID of the region to which the routing policy is applied.
        # 
        # You can call [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) to query region IDs.
        # 
        # This parameter is required.
        self.cen_region_id = cen_region_id
        # The match mode of the prefix list. Valid values:
        # 
        # - **Include**: fuzzy match. A match is successful if the route prefix in the match condition contains the route prefix of the route being matched.
        # 
        #  For example, a policy that defines 10.10.0.0/16 can fuzzy match the route 10.10.1.0/24.
        # 
        # - **Complete**: exact match. A match is successful only if the route prefix in the match condition is the same as the route prefix of the route being matched. 
        # 
        #  For example, a policy that defines 10.10.0.0/16 can only exact match the route 10.10.0.0/16.
        self.cidr_match_mode = cidr_match_mode
        # The match mode of the Community. Valid values:
        # 
        # - **Include**: fuzzy match. A match is successful if the Community in the match condition overlaps with the Community of the route being matched. 
        # 
        # - **Complete**: exact match. A match is successful only if the Community in the match condition is the same as the Community of the route being matched.
        # 
        # - **Contain**: inclusive match. A match is successful only if the Community of the route being matched contains all the Communities specified in the match condition.
        self.community_match_mode = community_match_mode
        # The action to perform on the Community. Valid values:
        # 
        # - **Additive**: adds a Community to the route.
        # 
        # - **Replace**: replaces the existing Community of the route.
        # 
        # This parameter specifies the action to perform after a route matches the condition.
        self.community_operate_mode = community_operate_mode
        # The description of the routing policy.
        # 
        # The description can be empty or 1 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The list of destination instance types that the route must match. The following instance types are supported:
        # 
        # - **VPC**: VPC instance.
        # 
        # - **VBR**: VBR instance.
        # 
        # - **CCN**: CCN instance.
        # 
        # - **VPN**: IPsec connection.
        # 
        #     > If an IPsec connection or SSL server is bound to a VPN gateway instance and is connected to a transit router instance through the VPC associated with the VPN gateway instance, this parameter does not take effect. This parameter takes effect only when an IPsec connection is directly bound to a transit router instance.
        # 
        # You can specify multiple instance types.
        # 
        # >The destination instance type list takes effect only when the routing policy direction is outbound from the regional gateway and the destination instance types are instance types in the local region.
        self.destination_child_instance_types = destination_child_instance_types
        # The prefix list that the route must match.
        # 
        # IP address ranges in the prefix list are in CIDR format. You can specify up to 64 IP address ranges.
        # 
        # Both IPv4 and IPv6 formats are supported.
        self.destination_cidr_blocks = destination_cidr_blocks
        # The list of destination instance IDs that the route must match. The following types of instance IDs are supported:
        # 
        # - Virtual Private Cloud (VPC) instance ID
        # - Virtual Border Router (VBR) instance ID
        # - Cloud Connect Network (CCN) instance ID
        # - Smart Access Gateway instance ID
        # - IPsec connection ID
        # 
        # You can specify up to 64 instance IDs.
        # 
        # >The destination instance ID list takes effect only when the routing policy direction is outbound from the regional gateway and the destination instance IDs are instance IDs in the local region.
        self.destination_instance_ids = destination_instance_ids
        # Specifies whether to use the exclude matching mode for the destination instance ID list. Valid values:
        # 
        # - **false** (default): no. A match is successful if the destination instance ID of the route is in the **DestinationInstanceIds.N** list.
        # 
        # - **true**: yes. A match is successful if the destination instance ID of the route is not in the **DestinationInstanceIds.N** list.
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        # The list of destination region IDs that the route must match. You can specify up to 64 region IDs.
        self.destination_region_ids = destination_region_ids
        # The list of destination route table IDs that the route must match. You can specify up to 64 route table IDs.
        # 
        # >The destination route table ID list takes effect only when the routing policy direction is outbound from the regional gateway and the destination route table IDs are route table IDs of network instances in the local region.
        self.destination_route_table_ids = destination_route_table_ids
        # The action to perform after all conditions are matched. Valid values:
        # 
        # - **Permit**: permits the matched routes.
        # 
        # - **Deny**: denies the matched routes.
        # 
        # This parameter is required.
        self.map_result = map_result
        # The IP address type that the route must match. Valid values:
        # 
        # - **IPv4**: matches only IPv4 routes.
        # - **IPv6**: matches only IPv6 routes.
        # 
        # This parameter can be left empty, which indicates that all types of routes are matched.
        self.match_address_type = match_address_type
        # The AS path list that the route must match.
        # 
        # You can specify up to 64 AS numbers.
        # 
        # > Only AS SEQUENCE is supported. AS SET, AS CONFED SEQUENCE, and AS CONFED SET are not supported. This means that only AS number lists are supported, not sets or sublists.
        self.match_asns = match_asns
        # The Community set that the route must match.
        # 
        # Each Community is in the n:m format, where the value ranges of n and m are **1** to **65535**. Communities must comply with RFC 1997. Large Communities (RFC 8092) are not supported.
        # 
        # You can specify up to 64 Communities.
        # 
        # > Incorrect Community configurations may cause routes to fail to be advertised to on-premises data centers.
        self.match_community_set = match_community_set
        # Policy priority of the next associated routing policy.
        # 
        # - You can set policy priority of the next associated routing policy only when **MapResult** is set to **Permit**. Only routes that are permitted continue to match the next associated routing policy.
        # - The next associated routing policy must have the same region and direction as the current routing policy.
        # - Policy priority of the next associated routing policy must be lower than policy priority of the current routing policy.
        self.next_priority = next_priority
        # The Community set to be executed.
        # 
        # Each Community is in the n:m format, where the value ranges of n and m are **1** to **65535**. Communities must comply with RFC 1997. Large Communities (RFC 8092) are not supported.
        # 
        # You can specify up to 32 Communities.
        # 
        # > Incorrect Community configurations may cause routes to fail to be advertised to on-premises data centers.
        self.operate_community_set = operate_community_set
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The modified priority of the route.
        # 
        # Valid values: **1** to **100**. The default priority of a route is **50**. A smaller value indicates a higher priority.
        # 
        # This parameter specifies the action to perform after a route matches the condition.
        self.preference = preference
        # The AS path that is prepended when the regional gateway receives or publishes route entries.
        # 
        # The requirements for configuring the prepended AS path vary based on the routing policy direction:
        # 
        # - When the direction is inbound to the regional gateway, the match condition must include the source instance ID list and source region, and the source region must be the same as the region to which the routing policy is applied.
        # 
        # - When the direction is outbound from the regional gateway, the match condition must include the destination instance ID list.
        # 
        # 
        # This parameter specifies the action to execute after a route matches the condition. You can specify up to 32 AS numbers.
        self.prepend_as_path = prepend_as_path
        # Policy priority of the routing policy. Valid values: **1** to **100**. A smaller value indicates a higher priority.
        # 
        # > Policy priority of routing policies in the same region and with the same direction must be unique. When a routing policy is executed, the system starts matching conditional statements from the routing policy with the smallest priority value. Specify policy priority based on the expected matching order.
        # 
        # This parameter is required.
        self.priority = priority
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The list of routing types that the route must match. The following routing types are supported:
        # 
        # - **System**: system routes that are automatically generated by the system.
        # 
        # - **Custom**: custom routes that are manually added by users.
        # 
        # - **BGP**: BGP routes that are propagated through the BGP routing protocol.
        # 
        # You can specify multiple routing types.
        self.route_types = route_types
        # The list of source instance types that the route must match. The following instance types are supported:
        # 
        # - **VPC**: VPC instance.
        # 
        # - **VBR**: virtual border router instance.
        # 
        # - **CCN**: CCN instance.
        # 
        # - **VPN**: VPN gateway instance or IPsec connection.
        # 
        #     - If an IPsec connection or SSL server is attached to a VPN gateway instance, the VPC associated with the VPN gateway instance must be connected to a transit router instance, and the VPN gateway instance must run the BGP dynamic routing protocol for this parameter to take effect.
        #     - If an IPsec connection is directly attached to a transit router instance, this parameter takes effect.
        # 
        # You can specify multiple instance types.
        self.source_child_instance_types = source_child_instance_types
        # The list of source instance IDs that the route must match. The following types of instance IDs are supported:
        # 
        # - Virtual Private Cloud (VPC) instance ID
        # - Virtual Border Router (VBR) instance ID
        # - Cloud Connect Network (CCN) instance ID
        # - Smart Access Gateway instance ID
        # - IPsec connection ID
        # 
        # You can specify up to 64 instance IDs.
        self.source_instance_ids = source_instance_ids
        # Specifies whether to use the exclude matching mode for the source instance ID list. Valid values:
        # 
        # - **false** (default): no. A match is successful if the source instance ID of the route is in the **SourceInstanceIds.N** list.
        # 
        # - **true**: yes. A match is successful if the source instance ID of the route is not in the **SourceInstanceIds.N** list.
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        # The list of source region IDs that the route must match. You can specify up to 64 region IDs.
        # 
        # You can call [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) to query region IDs.
        self.source_region_ids = source_region_ids
        # The list of source route table IDs that the route must match. You can specify up to 64 route table IDs.
        self.source_route_table_ids = source_route_table_ids
        # The route table ID of the transit router.
        # 
        # If you do not specify a route table ID, the routing policy is automatically associated with the default route table of the transit router.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The direction in which the routing policy is applied. Valid values:
        # 
        # - **RegionIn**: the inbound direction of the regional gateway. Routes are transmitted to the CEN regional gateway.
        # 
        #  For example, a route is advertised from a network instance in the local region to the local regional gateway, or a route is advertised from another region to the local regional gateway.
        # 
        # - **RegionOut**: the outbound direction of the regional gateway. Routes are transmitted from the CEN regional gateway.
        # 
        #  For example, a route is advertised from the local regional gateway to a network instance in the local region, or to a regional gateway in another region.
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

