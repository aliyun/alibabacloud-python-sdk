# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListRouteMapRulesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        route_map_rules: List[main_models.ListRouteMapRulesResponseBodyRouteMapRules] = None,
        total_count: int = None,
    ):
        # The number of entries returned on each page in a paginated query.
        self.max_results = max_results
        # The token for the next query. Valid values:
        # 
        # - If **NextToken** is empty, no next query is available.
        # - If **NextToken** has a return value, the value indicates the token for the next query.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The list of route map rules.
        self.route_map_rules = route_map_rules
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.route_map_rules:
            for v1 in self.route_map_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['RouteMapRules'] = []
        if self.route_map_rules is not None:
            for k1 in self.route_map_rules:
                result['RouteMapRules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.route_map_rules = []
        if m.get('RouteMapRules') is not None:
            for k1 in m.get('RouteMapRules'):
                temp_model = main_models.ListRouteMapRulesResponseBodyRouteMapRules()
                self.route_map_rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRouteMapRulesResponseBodyRouteMapRules(DaraModel):
    def __init__(
        self,
        description: str = None,
        match_conditions: main_models.ListRouteMapRulesResponseBodyRouteMapRulesMatchConditions = None,
        name: str = None,
        priority: int = None,
        route_map_id: str = None,
        route_map_rule_id: str = None,
        set_actions: main_models.ListRouteMapRulesResponseBodyRouteMapRulesSetActions = None,
        status: str = None,
    ):
        # The description of the rule.
        self.description = description
        # The match conditions of the route map rule. The system executes the actions defined in **SetActions** only when a route meets all the match conditions defined in this parameter.
        self.match_conditions = match_conditions
        # The name of the rule.
        self.name = name
        # The priority of the rule. A smaller value indicates a higher priority.
        self.priority = priority
        # The ID of the route map.
        self.route_map_id = route_map_id
        # The ID of the route map rule.
        self.route_map_rule_id = route_map_rule_id
        # The actions to execute for the route map rule. After a route meets all the match conditions defined in **MatchConditions**, the system processes the route based on the actions defined in this parameter.
        self.set_actions = set_actions
        # The status of the route map rule. Valid values:
        # 
        # - **Creating**: The rule is being created.
        # - **Updating**: The rule is being updated.
        # - **Active**: The rule is available.
        # - **Deleting**: The rule is being deleted.
        # - **Deleted**: The rule is deleted.
        self.status = status

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
        if self.description is not None:
            result['Description'] = self.description

        if self.match_conditions is not None:
            result['MatchConditions'] = self.match_conditions.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.route_map_id is not None:
            result['RouteMapId'] = self.route_map_id

        if self.route_map_rule_id is not None:
            result['RouteMapRuleId'] = self.route_map_rule_id

        if self.set_actions is not None:
            result['SetActions'] = self.set_actions.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MatchConditions') is not None:
            temp_model = main_models.ListRouteMapRulesResponseBodyRouteMapRulesMatchConditions()
            self.match_conditions = temp_model.from_map(m.get('MatchConditions'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RouteMapId') is not None:
            self.route_map_id = m.get('RouteMapId')

        if m.get('RouteMapRuleId') is not None:
            self.route_map_rule_id = m.get('RouteMapRuleId')

        if m.get('SetActions') is not None:
            temp_model = main_models.ListRouteMapRulesResponseBodyRouteMapRulesSetActions()
            self.set_actions = temp_model.from_map(m.get('SetActions'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListRouteMapRulesResponseBodyRouteMapRulesSetActions(DaraModel):
    def __init__(
        self,
        as_path_prepend: List[int] = None,
        as_path_replace: List[int] = None,
        community_add: List[str] = None,
        community_replace: List[str] = None,
        next_priority: int = None,
        route_action: str = None,
    ):
        # The AS path to prepend when the regional gateway receives or advertises routes.
        # 
        # This parameter and **AsPathReplace** are mutually exclusive and cannot be specified at the same time.
        # 
        # This parameter specifies the action to execute after a route meets the match conditions.
        self.as_path_prepend = as_path_prepend
        # The AS path to replace when the regional gateway receives or advertises routes. The original AS path of the route is replaced with the list of AS numbers specified in this parameter.
        # 
        # This parameter and **AsPathPrepend** are mutually exclusive and cannot be specified at the same time.
        # 
        # This parameter specifies the action to execute after a route meets the match conditions.
        self.as_path_replace = as_path_replace
        # The community set to add to the route.
        # 
        # Each community is in the format of n:m, where n and m range from **1** to **65535**. The community must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # This parameter and **CommunityReplace** are mutually exclusive and cannot be specified at the same time.
        # 
        # This parameter specifies the action to execute after a route meets the match conditions.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.community_add = community_add
        # The community set to replace the original community of the route.
        # 
        # Each community is in the format of n:m, where n and m range from **1** to **65535**. The community must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # This parameter and **CommunityAdd** are mutually exclusive and cannot be specified at the same time.
        # 
        # This parameter specifies the action to execute after a route meets the match conditions.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.community_replace = community_replace
        # Policy priority of the associated next route map rule.
        # 
        # - You can set policy priority of the associated route map rule only when **RouteAction** is set to **Permit**. Only the permitted routes continue to match the associated next route map rule.
        # - Policy priority of the associated next route map rule must be lower than policy priority of the current route map rule.
        self.next_priority = next_priority
        # The policy action after all conditions are met. Valid values:
        # 
        # - **Permit**: permits the matched routes.
        # - **Deny**: denies the matched routes.
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

class ListRouteMapRulesResponseBodyRouteMapRulesMatchConditions(DaraModel):
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
        # The route prefix list for fuzzy matching.
        # 
        # A match succeeds if the route prefix in the match condition contains the route prefix of the matched route.
        # 
        # For example, a policy defined with 10.0.0.0/8 can fuzzy match a route with 10.10.10.0/24.
        # 
        # IP address ranges use the CIDR format. Both IPv4 and IPv6 are supported.
        # 
        # This parameter and **AddressPrefixesMatch** are mutually exclusive and cannot be specified at the same time.
        self.address_prefixes_include = address_prefixes_include
        # The route prefix list for exact matching.
        # 
        # A match succeeds only when the route prefix in the match condition is exactly the same as the route prefix of the matched route.
        # 
        # For example, a policy defined with 10.0.0.0/8 can only exactly match a route with 10.0.0.0/8.
        # 
        # IP address ranges use the CIDR format. Both IPv4 and IPv6 are supported.
        # 
        # This parameter and **AddressPrefixesInclude** are mutually exclusive and cannot be specified at the same time.
        self.address_prefixes_match = address_prefixes_match
        # The list of AS paths for fuzzy matching.
        # 
        # A match succeeds if the AS path in the match condition overlaps with the AS path of the matched route.
        # 
        # This parameter and **AsPathsMatch** are mutually exclusive and cannot be specified at the same time.
        # 
        # > Only AS SEQUENCE is supported. AS SET, AS CONFED SEQUENCE, and AS CONFED SET are not supported. This means only a list of AS numbers is supported, and sets and sub-lists are not supported.
        self.as_paths_include = as_paths_include
        # The list of AS paths for exact matching.
        # 
        # A match succeeds only when the AS path in the match condition is exactly the same as the AS path of the matched route.
        # 
        # This parameter and **AsPathsInclude** are mutually exclusive and cannot be specified at the same time.
        # 
        # > Only AS SEQUENCE is supported. AS SET, AS CONFED SEQUENCE, and AS CONFED SET are not supported. This means only a list of AS numbers is supported, and sets and sub-lists are not supported.
        self.as_paths_match = as_paths_match
        # The community set for fuzzy matching.
        # 
        # A match succeeds if the community in the match condition overlaps with the community of the matched route.
        # 
        # Each community is in the format of n:m, where n and m range from **1** to **65535**. The community must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # This parameter and **CommunitySetMatch** are mutually exclusive and cannot be specified at the same time.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.community_set_include = community_set_include
        # The community set for exact matching.
        # 
        # A match succeeds only when the community in the match condition is exactly the same as the community of the matched route.
        # 
        # Each community is in the format of n:m, where n and m range from **1** to **65535**. The community must comply with RFC 1997. Large communities (RFC 8092) are not supported.
        # 
        # This parameter and **CommunitySetInclude** are mutually exclusive and cannot be specified at the same time.
        # 
        # > Incorrect community configurations may prevent routes from being advertised to the on-premises data center.
        self.community_set_match = community_set_match
        # The list of destination instance IDs to match. The following instance types are supported:
        # 
        # - Virtual private cloud (VPC) instance IDs
        # - Virtual border router (VBR) instance IDs
        # 
        # > The list of destination instance IDs takes effect only when the direction of the route map is outbound.
        self.destination_instance_ids = destination_instance_ids
        # Specifies whether to use the exclude matching mode for the list of destination instance IDs. Valid values:
        # 
        # - **false** (default): no. A match succeeds when the destination instance ID of the route is in **DestinationInstanceIds.N**.
        # - **true**: yes. A match succeeds when the destination instance ID of the route is not in **DestinationInstanceIds.N**.
        self.destination_instance_ids_reverse_match = destination_instance_ids_reverse_match
        # The list of destination instance types to match. The following instance types are supported:
        # 
        # - **VPC**: VPC instance.
        # - **VBR**: VBR instance.
        # 
        # > The list of destination instance types takes effect only when the direction of the route map is outbound.
        self.destination_instance_types = destination_instance_types
        # The list of destination region IDs to match.
        self.destination_region_ids = destination_region_ids
        # The list of destination route table IDs to match.
        # 
        # > The list of destination route table IDs takes effect only when the direction of the route map is outbound.
        self.destination_route_table_ids = destination_route_table_ids
        # The IP address type to match. Valid values:
        # 
        # - **IPv4**: matches only IPv4 routes.
        # - **IPv6**: matches only IPv6 routes.
        # 
        # You can leave this parameter empty to match routes of all types.
        self.match_address_type = match_address_type
        # The list of route types to match. The following route types are supported:
        # 
        # - **System**: system route, which is automatically generated by the system.
        # - **Custom**: custom route, which is manually added by a user.
        # - **BGP**: BGP route, which is propagated through the BGP routable protocol.
        # 
        # You can specify multiple route types.
        self.route_types = route_types
        # The list of source instance IDs to match. The following instance types are supported:
        # 
        # - Virtual private cloud (VPC) instance IDs
        # - Virtual border router (VBR) instance IDs
        self.source_instance_ids = source_instance_ids
        # Specifies whether to use the exclude matching mode for the list of source instance IDs. Valid values:
        # 
        # - **false** (default): no. A match succeeds when the source instance ID of the route is in **SourceInstanceIds.N**.
        # - **true**: yes. A match succeeds when the source instance ID of the route is not in **SourceInstanceIds.N**.
        self.source_instance_ids_reverse_match = source_instance_ids_reverse_match
        # The list of source instance types to match. The following instance types are supported:
        # 
        # - **VPC**: VPC instance.
        # - **VBR**: VBR instance.
        self.source_instance_types = source_instance_types
        # The list of source region IDs to match.
        self.source_region_ids = source_region_ids
        # The list of source route table IDs to match.
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

