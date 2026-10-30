# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateRouteMapRuleRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        match_conditions: main_models.CreateRouteMapRuleRequestMatchConditions = None,
        name: str = None,
        priority: int = None,
        route_map_id: str = None,
        set_actions: main_models.CreateRouteMapRuleRequestSetActions = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the parameter value on your client. Make sure that the token is unique across different requests. The client token supports only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request may be different.
        self.client_token = client_token
        # The detailed description of the rule. The description can be empty or 1 to 256 characters in length, and cannot start with http:// or https://.
        self.description = description
        # Specifies whether to only precheck the request. Valid values:
        # 
        # - **true**: Prechecks the request without creating the route map rule. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): Sends the request. After the request passes the precheck, the route map rule is created.
        self.dry_run = dry_run
        # The match conditions of the route map rule. The system executes the actions defined in **SetActions** only when a route meets all the match conditions defined in this parameter.
        self.match_conditions = match_conditions
        # The name of the rule for easy identification. The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.name = name
        # The priority of the rule. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.priority = priority
        # The ID of the route map.
        # 
        # This parameter is required.
        self.route_map_id = route_map_id
        # The actions to execute for the route map rule. After a route meets all the match conditions defined in **MatchConditions**, the system processes the route based on the actions defined in this parameter.
        self.set_actions = set_actions

    def validate(self):
        if self.match_conditions:
            self.match_conditions.validate()
        if self.set_actions:
            self.set_actions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.match_conditions is not None:
            result['MatchConditions'] = self.match_conditions.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        if self.set_actions is not None:
            result['SetActions'] = self.set_actions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('MatchConditions') is not None:
            temp_model = main_models.CreateRouteMapRuleRequestMatchConditions()
            self.match_conditions = temp_model.from_map(m.get('MatchConditions'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        if m.get('SetActions') is not None:
            temp_model = main_models.CreateRouteMapRuleRequestSetActions()
            self.set_actions = temp_model.from_map(m.get('SetActions'))

        return self

class CreateRouteMapRuleRequestSetActions(DaraModel):
    def __init__(
        self,
        as_path_prepend: List[int] = None,
        as_path_replace: List[int] = None,
        community_add: List[str] = None,
        community_replace: List[str] = None,
        next_priority: int = None,
        route_action: str = None,
    ):
        # The AS path to prepend when the regional gateway receives a route or executes a publish route entry. You can specify up to 64 AS numbers.
        # 
        # This parameter is mutually exclusive with **AsPathReplace**. You cannot specify both parameters at the same time.
        # 
        # This parameter specifies the action to execute after a route meets the match conditions.
        self.as_path_prepend = as_path_prepend
        # The AS path to replace when the regional gateway receives a route or executes a publish route entry. The original AS path of the route is replaced with the list of AS numbers specified in this parameter. You can specify up to 64 AS numbers.
        # 
        # This parameter is mutually exclusive with **AsPathPrepend**. You cannot specify both parameters at the same time.
        # 
        # This parameter specifies the action to execute after a route meets the match conditions.
        self.as_path_replace = as_path_replace
        # The community set to add to the route. You can specify up to 64 communities.
        # 
        # Each community is in the format of n:m, where n and m range from **1** to **65535**. The community must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # This parameter is mutually exclusive with **CommunityReplace**. You cannot specify both parameters at the same time.
        # 
        # This parameter specifies the action to execute after a route meets the match conditions.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.community_add = community_add
        # The community set to replace the original community of the route. You can specify up to 64 communities.
        # 
        # Each community is in the format of n:m, where n and m range from **1** to **65535**. The community must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # This parameter is mutually exclusive with **CommunityAdd**. You cannot specify both parameters at the same time.
        # 
        # This parameter specifies the action to execute after a route meets the match conditions.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.community_replace = community_replace
        # Policy priority of the associated next route map rule.
        # 
        # - You can set policy priority of the associated route map rule only when **RouteAction** is set to **Permit**. Only the routes that are permitted continue to match the associated next route map rule.
        # - Policy priority of the associated next route map rule must be lower than policy priority of the current route map rule.
        self.next_priority = next_priority
        # The policy action after all conditions are met. Valid values:
        # 
        # - **Permit**: Permits the matched routes.
        # 
        # - **Deny**: Denies the matched routes.
        self.route_action = route_action

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.as_path_prepend is not None:
            result['AsPathPrepend'] = self.as_path_prepend

        if self.as_path_replace is not None:
            result['AsPathReplace'] = self.as_path_replace

        if self.community_add is not None:
            result['CommunityAdd'] = self.community_add

        if self.community_replace is not None:
            result['CommunityReplace'] = self.community_replace

        if self.next_priority is not None:
            result['NextPriority'] = self.next_priority

        if self.route_action is not None:
            result['RouteAction'] = self.route_action

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsPathPrepend') is not None:
            self.as_path_prepend = m.get('AsPathPrepend')

        if m.get('AsPathReplace') is not None:
            self.as_path_replace = m.get('AsPathReplace')

        if m.get('CommunityAdd') is not None:
            self.community_add = m.get('CommunityAdd')

        if m.get('CommunityReplace') is not None:
            self.community_replace = m.get('CommunityReplace')

        if m.get('NextPriority') is not None:
            self.next_priority = m.get('NextPriority')

        if m.get('RouteAction') is not None:
            self.route_action = m.get('RouteAction')

        return self

class CreateRouteMapRuleRequestMatchConditions(DaraModel):
    def __init__(
        self,
        address_prefixes_include: List[str] = None,
        address_prefixes_match: List[str] = None,
        as_paths_include: List[int] = None,
        as_paths_match: List[int] = None,
        community_set_include: List[str] = None,
        community_set_match: List[str] = None,
        destination_instance_ids: List[str] = None,
        destination_instance_ids_reverse_match: bool = None,
        destination_instance_types: List[str] = None,
        destination_region_ids: List[str] = None,
        destination_route_table_ids: List[str] = None,
        match_address_type: str = None,
        route_types: List[str] = None,
        source_instance_ids: List[str] = None,
        source_instance_ids_reverse_match: bool = None,
        source_instance_types: List[str] = None,
        source_region_ids: List[str] = None,
        source_route_table_ids: List[str] = None,
    ):
        # The route prefix list for fuzzy match. You can specify up to 64 IP address blocks.
        # 
        # A match is successful if the route prefix in the match condition contains the route prefix of the matched route.
        # 
        # For example, a policy defined with 10.0.0.0/8 can fuzzy match a route with 10.10.10.0/24.
        # 
        # IP address blocks use the CIDR format and support IPv4 and IPv6.
        # 
        # This parameter is mutually exclusive with **AddressPrefixesMatch**. You cannot specify both parameters at the same time.
        self.address_prefixes_include = address_prefixes_include
        # The route prefix list for exact match. You can specify up to 64 IP address blocks.
        # 
        # A match is successful only if the route prefix in the match condition is exactly the same as the route prefix of the matched route.
        # 
        # For example, a policy defined with 10.0.0.0/8 can only exactly match a route with 10.0.0.0/8.
        # 
        # IP address blocks use the CIDR format and support IPv4 and IPv6.
        # 
        # This parameter is mutually exclusive with **AddressPrefixesInclude**. You cannot specify both parameters at the same time.
        self.address_prefixes_match = address_prefixes_match
        # The list of AS paths for fuzzy match. You can specify up to 64 AS numbers.
        # 
        # A match is successful if the AS path in the match condition overlaps with the AS path of the matched route.
        # 
        # This parameter is mutually exclusive with **AsPathsMatch**. You cannot specify both parameters at the same time.
        # 
        # > Only AS SEQUENCE is supported. AS SET, AS CONFED SEQUENCE, and AS CONFED SET are not supported. This means only a list of AS numbers is supported, and sets and sublists are not supported.
        self.as_paths_include = as_paths_include
        # The list of AS paths for exact match. You can specify up to 64 AS numbers.
        # 
        # A match is successful only if the AS path in the match condition is exactly the same as the AS path of the matched route.
        # 
        # This parameter is mutually exclusive with **AsPathsInclude**. You cannot specify both parameters at the same time.
        # 
        # > Only AS SEQUENCE is supported. AS SET, AS CONFED SEQUENCE, and AS CONFED SET are not supported. This means only a list of AS numbers is supported, and sets and sublists are not supported.
        self.as_paths_match = as_paths_match
        # The community set for fuzzy match. You can specify up to 64 communities.
        # 
        # A match is successful if the community in the match condition overlaps with the community of the matched route.
        # 
        # Each community is in the format of n:m, where n and m range from **1** to **65535**. The community must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # This parameter is mutually exclusive with **CommunitySetMatch**. You cannot specify both parameters at the same time.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.community_set_include = community_set_include
        # The community set for exact match. You can specify up to 64 communities.
        # 
        # A match is successful only if the community in the match condition is exactly the same as the community of the matched route.
        # 
        # Each community is in the format of n:m, where n and m range from **1** to **65535**. The community must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # This parameter is mutually exclusive with **CommunitySetInclude**. You cannot specify both parameters at the same time.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.community_set_match = community_set_match
        # The list of destination instance IDs to match. You can specify the following types of instance IDs:
        # 
        # - Virtual Private Cloud (VPC) instance IDs
        # - Virtual Border Router (VBR) instance IDs
        # 
        # You can specify up to 64 instance IDs.
        # 
        # > The list of destination instance IDs takes effect only when the direction of the route map is outbound.
        self.destination_instance_ids = destination_instance_ids
        # Specifies whether to use the exclusion match mode for the list of destination instance IDs. Valid values:
        # 
        # - **false** (default): No. A match is successful if the destination instance ID of the route is in **DestinationInstanceIds.N**.
        # 
        # - **true**: Yes. A match is successful if the destination instance ID of the route is not in **DestinationInstanceIds.N**.
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        # The list of destination instance types to match. The following instance types are supported:
        # 
        # - **VPC**: VPC instance.
        # 
        # - **VBR**: VBR instance.
        # 
        # 
        # You can specify multiple instance types.
        # 
        # > The list of destination instance types takes effect only when the direction of the route map is outbound.
        self.destination_instance_types = destination_instance_types
        # The list of destination region IDs to match. You can specify up to 64 region IDs.
        self.destination_region_ids = destination_region_ids
        # The list of destination route table IDs to match. You can specify up to 64 route table IDs.
        # 
        # > The list of destination route table IDs takes effect only when the direction of the route map is outbound.
        self.destination_route_table_ids = destination_route_table_ids
        # The IP address type of the routes to match. Valid values:
        # 
        # - **IPv4**: Matches only IPv4 routes.
        # - **IPv6**: Matches only IPv6 routes.
        # 
        # You can leave this parameter empty to match routes of all types.
        self.match_address_type = match_address_type
        # The list of route types to match. The following route types are supported:
        # 
        # - **System**: system route, which is automatically generated by the system.
        # 
        # - **Custom**: custom route, which is manually added by the user.
        # 
        # - **BGP**: BGP route, which is propagated through the BGP routable protocol.
        # 
        # You can specify multiple route types.
        self.route_types = route_types
        # The list of source instance IDs to match. You can specify the following types of instance IDs:
        # 
        # - Virtual Private Cloud (VPC) instance IDs
        # - Virtual Border Router (VBR) instance IDs
        # 
        # 
        # You can specify up to 64 instance IDs.
        self.source_instance_ids = source_instance_ids
        # Specifies whether to use the exclusion match mode for the list of source instance IDs. Valid values:
        # 
        # - **false** (default): No. A match is successful if the source instance ID of the route is in **SourceInstanceIds.N**.
        # 
        # - **true**: Yes. A match is successful if the source instance ID of the route is not in **SourceInstanceIds.N**.
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        # The list of source instance types to match. The following instance types are supported:
        # 
        # - **VPC**: VPC instance.
        # 
        # - **VBR**: VBR instance.
        # 
        # 
        # You can specify multiple instance types.
        self.source_instance_types = source_instance_types
        # The list of source region IDs to match. You can specify up to 64 region IDs.
        self.source_region_ids = source_region_ids
        # The list of source route table IDs to match. You can specify up to 64 route table IDs.
        self.source_route_table_ids = source_route_table_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_prefixes_include is not None:
            result['AddressPrefixesInclude'] = self.address_prefixes_include

        if self.address_prefixes_match is not None:
            result['AddressPrefixesMatch'] = self.address_prefixes_match

        if self.as_paths_include is not None:
            result['AsPathsInclude'] = self.as_paths_include

        if self.as_paths_match is not None:
            result['AsPathsMatch'] = self.as_paths_match

        if self.community_set_include is not None:
            result['CommunitySetInclude'] = self.community_set_include

        if self.community_set_match is not None:
            result['CommunitySetMatch'] = self.community_set_match

        if self.destination_instance_ids is not None:
            result['DestinationInstanceIds'] = self.destination_instance_ids

        if self.destination_instance_ids_reverse_match is not None:
            result['DestinationInstanceIdsReverseMatch'] = self.destination_instance_ids_reverse_match

        if self.destination_instance_types is not None:
            result['DestinationInstanceTypes'] = self.destination_instance_types

        if self.destination_region_ids is not None:
            result['DestinationRegionIds'] = self.destination_region_ids

        if self.destination_route_table_ids is not None:
            result['DestinationRouteTableIds'] = self.destination_route_table_ids

        if self.match_address_type is not None:
            result['MatchAddressType'] = self.match_address_type

        if self.route_types is not None:
            result['RouteTypes'] = self.route_types

        if self.source_instance_ids is not None:
            result['SourceInstanceIds'] = self.source_instance_ids

        if self.source_instance_ids_reverse_match is not None:
            result['SourceInstanceIdsReverseMatch'] = self.source_instance_ids_reverse_match

        if self.source_instance_types is not None:
            result['SourceInstanceTypes'] = self.source_instance_types

        if self.source_region_ids is not None:
            result['SourceRegionIds'] = self.source_region_ids

        if self.source_route_table_ids is not None:
            result['SourceRouteTableIds'] = self.source_route_table_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressPrefixesInclude') is not None:
            self.address_prefixes_include = m.get('AddressPrefixesInclude')

        if m.get('AddressPrefixesMatch') is not None:
            self.address_prefixes_match = m.get('AddressPrefixesMatch')

        if m.get('AsPathsInclude') is not None:
            self.as_paths_include = m.get('AsPathsInclude')

        if m.get('AsPathsMatch') is not None:
            self.as_paths_match = m.get('AsPathsMatch')

        if m.get('CommunitySetInclude') is not None:
            self.community_set_include = m.get('CommunitySetInclude')

        if m.get('CommunitySetMatch') is not None:
            self.community_set_match = m.get('CommunitySetMatch')

        if m.get('DestinationInstanceIds') is not None:
            self.destination_instance_ids = m.get('DestinationInstanceIds')

        if m.get('DestinationInstanceIdsReverseMatch') is not None:
            self.destination_instance_ids_reverse_match = m.get('DestinationInstanceIdsReverseMatch')

        if m.get('DestinationInstanceTypes') is not None:
            self.destination_instance_types = m.get('DestinationInstanceTypes')

        if m.get('DestinationRegionIds') is not None:
            self.destination_region_ids = m.get('DestinationRegionIds')

        if m.get('DestinationRouteTableIds') is not None:
            self.destination_route_table_ids = m.get('DestinationRouteTableIds')

        if m.get('MatchAddressType') is not None:
            self.match_address_type = m.get('MatchAddressType')

        if m.get('RouteTypes') is not None:
            self.route_types = m.get('RouteTypes')

        if m.get('SourceInstanceIds') is not None:
            self.source_instance_ids = m.get('SourceInstanceIds')

        if m.get('SourceInstanceIdsReverseMatch') is not None:
            self.source_instance_ids_reverse_match = m.get('SourceInstanceIdsReverseMatch')

        if m.get('SourceInstanceTypes') is not None:
            self.source_instance_types = m.get('SourceInstanceTypes')

        if m.get('SourceRegionIds') is not None:
            self.source_region_ids = m.get('SourceRegionIds')

        if m.get('SourceRouteTableIds') is not None:
            self.source_route_table_ids = m.get('SourceRouteTableIds')

        return self

