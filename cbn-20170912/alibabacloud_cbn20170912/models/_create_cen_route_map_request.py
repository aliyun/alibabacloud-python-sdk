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
        # The match method that is used to match routes based on the AS path. Valid values:
        # 
        # *   **Include**: fuzzy match. A route is a match if the AS path of the route overlaps with the AS path in the match conditions.
        # *   **Complete**: exact match. A route is a match only if the AS path of the route matches the AS path in the match conditions.
        self.as_path_match_mode = as_path_match_mode
        # The ID of the CEN instance.
        # 
        # This parameter is required.
        self.cen_id = cen_id
        # The ID of the region in which the routing policy is applied.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.cen_region_id = cen_region_id
        # The match method that is used to match routes against the prefix list. Valid values:
        # 
        # *   **Include**: fuzzy match. A route is a match if the route prefix is included in the match conditions.
        # 
        # For example, if you set the match condition to 1.1.0.0/16 and fuzzy match is applied, the route whose prefix is 1.1.1.0/24 meets the match condition.
        # 
        # *   **Complete**: exact match. A route is a match only if the route prefix is the same as the prefix specified in the match condition.
        # 
        # For example, if you set the match condition to 1.1.0.0/16 and exact match is applied, only the route whose prefix is 1.1.0.0/16 meets the match condition.
        self.cidr_match_mode = cidr_match_mode
        # The match method that is used to match routes based on the community. Valid values:
        # 
        # *   **Include**: fuzzy match. A route is a match if the community of the route overlaps with the community in the match conditions.
        # *   **Complete**: exact match. A route is a match only if the community of the route matches the community in the match conditions.
        self.community_match_mode = community_match_mode
        # The action to be performed on the community. Valid values:
        # 
        # *   **Additive**: adds the community to the route.
        # *   **Replace**: replaces the original community of the route.
        # 
        # This parameter specifies the action to be performed when a route meets the match condition.
        self.community_operate_mode = community_operate_mode
        # The description of the routing policy.
        # 
        # This parameter is optional. If you enter a description, it must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The types of destination network instance to which the routes belong. The following types of network instances are supported:
        # 
        # *   **VPC**: VPC
        # 
        # *   **VBR**: VBR
        # 
        # *   **CCN**: CCN instance
        # 
        # *   **VPN**: IPsec connection
        # 
        #     >This parameter does not take effect if the IPsec-VPN connection or SSL client is associated with a transit router through a VPN gateway and a VPC. This parameter takes effect only if the IPsec connection is directly connected to the transit router.
        # 
        # You can specify one or more network instance types.
        # 
        # > The destination network instance types are valid only if the routing policy is applied to scenarios where routes are advertised from the gateway in the current region to network instances in the current region.
        self.destination_child_instance_types = destination_child_instance_types
        # The prefix list against which routes are matched.
        # 
        # Specify IP addresses in CIDR notations. You can specify at most 32 CIDR blocks.
        # 
        # IPv4 and IPv4 addresses are supported.
        self.destination_cidr_blocks = destination_cidr_blocks
        # The IDs of the destination network instances to which the routes belong. The following network instance types are supported:
        # 
        # *   VPC
        # *   VBR
        # *   CCN instance
        # *   SAG instance
        # *   The ID of the IPsec-VPN connection.
        # 
        # You can enter at most 32 IDs.
        # 
        # > The destination instance IDs take effect only when Direction is set to Export from Regional Gateway and the destination instances are deployed in the current region.
        self.destination_instance_ids = destination_instance_ids
        # Specifies whether to exclude destination instance IDs. Valid values:
        # 
        # *   **false** (default): A route is a match if the destination instance ID is included in the list specified by **SourceInstanceIds.N**.
        # *   **true**: A route is a match if the destination network instance ID is not in the list specified by **SourceInstanceIds.N**.
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        # The destination region IDs of the route. You can specify at most 32 region IDs.
        self.destination_region_ids = destination_region_ids
        # The IDs of the destination route tables to which routes are evaluated. You can enter at most 32 route table IDs.
        # 
        # > The destination route table IDs take effect only when Direction is set to Export from Regional Gateway and the destination route tables belong to network instances deployed in the current region.
        self.destination_route_table_ids = destination_route_table_ids
        # The action to be performed on a route that meets all the match conditions. Valid values:
        # 
        # *   **Permit**: the route is permitted.
        # *   **Deny**: the route is denied.
        # 
        # This parameter is required.
        self.map_result = map_result
        # The type of IP address in the match condition. Valid values:
        # 
        # *   **IPv4**: IPv4 address
        # *   **IPv6**: IPv6 address
        # 
        # This parameter can be empty. If no value is specified, all types of IP address are a match.
        self.match_address_type = match_address_type
        # The AS paths based on which routes are compared.
        # 
        # You can specify at most 32 AS numbers.
        # 
        # > Only the AS-SEQUENCE parameter is supported. The AS-SET, AS-CONFED-SEQUENCE, and AS-CONFED-SET parameters are not supported. In other words, only the AS number list is supported. Sets and sub-lists are not supported.
        self.match_asns = match_asns
        # The community set based on which routes are compared.
        # 
        # Specify the community in the format of n:m. Valid values of n and m: **1** to **65535**. Each community must comply with the RFC 1997 standard. The RFC 8092 standard that defines Border Gateway Protocol (BGP) large communities is not supported.
        # 
        # You can specify at most 32 communities.
        # 
        # > If the configurations of the communities are incorrect, routes may fail to be advertised to your data center.
        self.match_community_set = match_community_set
        # The priority of the routing policy that you want to associate with the current one.
        # 
        # *   This parameter takes effect only when the **MapResult** parameter is set to **Permit**. This way, the permitted route is matched against the next routing policy.
        # *   The region and direction of the routing policy to be associated must be the same as those of the current routing policy.
        # *   The priority of the next routing policy must be lower than the priority of the current routing policy.
        self.next_priority = next_priority
        # The community set on which actions are performed.
        # 
        # Specify the community in the format of n:m. Valid values of n and m: **1** to **65535**. Each community must comply with RFC 1997. The RFC 8092 standard that defines BGP large communities is not supported.
        # 
        # You can specify at most 32 communities.
        # 
        # > If the configurations of the communities are incorrect, routes may fail to be advertised to your data center.
        self.operate_community_set = operate_community_set
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The new priority of the route.
        # 
        # Valid values: **1** to **100**. The default priority is **50**. A smaller value indicates a higher priority.
        # 
        # This parameter specifies the action to be performed when a route meets the match condition.
        self.preference = preference
        # The AS paths that are prepended by using an action statement when regional gateways receive or advertise routes.
        # 
        # The AS paths vary based on the direction in which the routing policy is applied:
        # 
        # *   If AS paths are prepended to a routing policy that is applied in the inbound direction, you must specify source network instance IDs and the source region in the match condition. In addition, the source region must be the same as the region where the routing policy is applied.
        # *   If AS paths are prepended to a routing policy that is applied in the outbound direction, you must specify destination network instance IDs in the match condition.
        # 
        # This parameter specifies the action to be performed when a route meets the match condition. You can specify at most 32 AS numbers.
        self.prepend_as_path = prepend_as_path
        # The priority of the routing policy. Valid values: **1** to **100**. A smaller value indicates a higher priority.
        # 
        # > You cannot specify the same priority for routing policies that apply in the same region and direction. The system matches routes against the match conditions of routing policies in descending order of priority. A smaller value indicates a higher priority. You must set the priorities to proper values.
        # 
        # This parameter is required.
        self.priority = priority
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of route to be compared. Valid values: The following route types are supported:
        # 
        # *   **System**: system routes that are automatically generated by the system.
        # *   **Custom**: custom routes that are manually added.
        # *   **BGP**: routes that are advertised over BGP.
        # 
        # You can specify multiple route types.
        self.route_types = route_types
        # The types of source network instance to which the routes belong. The following types of network instances are supported:
        # 
        # *   **VPC**: VPC
        # 
        # *   **VBR**: VBR
        # 
        # *   **CCN**: CCN instance
        # 
        # *   **VPN**: VPN gateway or IPsec connection
        # 
        #     *   If the IPsec-VPN connection or SSL client is associated with a VPN gateway, the VPC associated with the VPN gateway must be connected to a transit router, and the VPN gateway must use BGP dynamic routing. Otherwise, this parameter cannot take effect.
        #     *   This parameter takes effect if the IPsec connection is directly connected to a transit router.
        # 
        # You can specify one or more network instance types.
        self.source_child_instance_types = source_child_instance_types
        # The IDs of the source network instances to which the routes belong. The following network instance types are supported:
        # 
        # *   Virtual private cloud (VPC)
        # *   Virtual border router (VBR)
        # *   Cloud Connect Network (CCN) instance
        # *   Smart Access Gateway (SAG) instance
        # *   The ID of the IPsec-VPN connection.
        # 
        # You can enter at most 32 IDs.
        self.source_instance_ids = source_instance_ids
        # Specifies whether to exclude source instance IDs. Valid values:
        # 
        # *   **false** (default): A route is a match if the source instance ID is included in the list specified by **SourceInstanceIds.N**.
        # *   **true**: A route is a match if the source network instance ID is not in the list specified by **SourceInstanceIds.N**.
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        # The IDs of the source regions from which routes are evaluated. You can enter at most 32 region IDs.
        # 
        # You can call the [DescribeChildInstanceRegions](https://help.aliyun.com/document_detail/132080.html) operation to query the most recent region list.
        self.source_region_ids = source_region_ids
        # The IDs of the source route tables from which routes are evaluated. You can enter at most 32 route table IDs.
        self.source_route_table_ids = source_route_table_ids
        # The ID of the route table of the transit router.
        # 
        # If you do not specify a route table ID, the routing policy is automatically associated with the default route table of the transit router.
        self.transit_router_route_table_id = transit_router_route_table_id
        # The direction in which the routing policy is applied. Valid values:
        # 
        # *   **RegionIn**: Routes are advertised to the gateways in the regions that are connected by the CEN instance.
        # 
        # For example, routes are advertised from network instances deployed in the current region or other regions to the gateway deployed in the current region.
        # 
        # *   **RegionOut**: Routes are advertised from the gateways in the regions that are connected by the CEN instance.
        # 
        # For example, routes are advertised from the gateway deployed in the current region to network instances deployed in the same region, or to gateways deployed in other regions.
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

