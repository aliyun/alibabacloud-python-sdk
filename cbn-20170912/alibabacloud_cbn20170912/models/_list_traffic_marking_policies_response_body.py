# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ListTrafficMarkingPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        traffic_marking_policies: List[main_models.ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPolicies] = None,
    ):
        # The number of entries returned on each page.
        self.max_results = max_results
        # The token that determines the start point of the query.
        # 
        # *   If **NextToken** was not returned in the previous query, it indicates that no additional results exist.
        # *   If **NextToken** was returned in the previous query, specify the value to obtain the next set of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count
        # The information about the traffic marking policy.
        self.traffic_marking_policies = traffic_marking_policies

    def validate(self):
        if self.traffic_marking_policies:
            for v1 in self.traffic_marking_policies:
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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TrafficMarkingPolicies'] = []
        if self.traffic_marking_policies is not None:
            for k1 in self.traffic_marking_policies:
                result['TrafficMarkingPolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.traffic_marking_policies = []
        if m.get('TrafficMarkingPolicies') is not None:
            for k1 in m.get('TrafficMarkingPolicies'):
                temp_model = main_models.ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPolicies()
                self.traffic_marking_policies.append(temp_model.from_map(k1))

        return self

class ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPolicies(DaraModel):
    def __init__(
        self,
        marking_dscp: int = None,
        priority: int = None,
        traffic_marking_policy_description: str = None,
        traffic_marking_policy_id: str = None,
        traffic_marking_policy_name: str = None,
        traffic_marking_policy_status: str = None,
        traffic_match_rules: List[main_models.ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPoliciesTrafficMatchRules] = None,
        transit_router_id: str = None,
    ):
        # The Differentiated Service Code Point (DSCP) value of the traffic marking policy.
        self.marking_dscp = marking_dscp
        # The priority of the traffic marking policy.
        # 
        # A lower value indicates a higher priority.
        self.priority = priority
        # The description of the traffic marking policy.
        self.traffic_marking_policy_description = traffic_marking_policy_description
        # The ID of the traffic marking policy.
        self.traffic_marking_policy_id = traffic_marking_policy_id
        # The name of the traffic marking policy.
        self.traffic_marking_policy_name = traffic_marking_policy_name
        # The status of the traffic marking policy. Valid values:
        # 
        # *   **Creating**: The policy is being created.
        # *   **Active**: The policy is available.
        # *   **Modifying**: The policy is being modified.
        # *   **Deleting**: The policy is being deleted.
        self.traffic_marking_policy_status = traffic_marking_policy_status
        # The traffic classification rules.
        self.traffic_match_rules = traffic_match_rules
        # The ID of the transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        if self.traffic_match_rules:
            for v1 in self.traffic_match_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.marking_dscp is not None:
            result['MarkingDscp'] = self.marking_dscp

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.traffic_marking_policy_description is not None:
            result['TrafficMarkingPolicyDescription'] = self.traffic_marking_policy_description

        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id

        if self.traffic_marking_policy_name is not None:
            result['TrafficMarkingPolicyName'] = self.traffic_marking_policy_name

        if self.traffic_marking_policy_status is not None:
            result['TrafficMarkingPolicyStatus'] = self.traffic_marking_policy_status

        result['TrafficMatchRules'] = []
        if self.traffic_match_rules is not None:
            for k1 in self.traffic_match_rules:
                result['TrafficMatchRules'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarkingDscp') is not None:
            self.marking_dscp = m.get('MarkingDscp')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('TrafficMarkingPolicyDescription') is not None:
            self.traffic_marking_policy_description = m.get('TrafficMarkingPolicyDescription')

        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')

        if m.get('TrafficMarkingPolicyName') is not None:
            self.traffic_marking_policy_name = m.get('TrafficMarkingPolicyName')

        if m.get('TrafficMarkingPolicyStatus') is not None:
            self.traffic_marking_policy_status = m.get('TrafficMarkingPolicyStatus')

        self.traffic_match_rules = []
        if m.get('TrafficMatchRules') is not None:
            for k1 in m.get('TrafficMatchRules'):
                temp_model = main_models.ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPoliciesTrafficMatchRules()
                self.traffic_match_rules.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class ListTrafficMarkingPoliciesResponseBodyTrafficMarkingPoliciesTrafficMatchRules(DaraModel):
    def __init__(
        self,
        address_family: str = None,
        dst_cidr: str = None,
        dst_port_range: List[int] = None,
        match_dscp: int = None,
        protocol: str = None,
        src_cidr: str = None,
        src_port_range: List[int] = None,
        traffic_match_rule_description: str = None,
        traffic_match_rule_id: str = None,
        traffic_match_rule_name: str = None,
        traffic_match_rule_status: str = None,
    ):
        # The address family. You can set the value to IPv4 or IPv6, or leave the value empty.
        self.address_family = address_family
        # The destination CIDR block of packets. IPv4 and IPv6 addresses are supported.
        self.dst_cidr = dst_cidr
        # The destination port range used to match data packets.
        self.dst_port_range = dst_port_range
        # The DSCP value used to match data packets.
        # 
        # >  If the value of the **MatchDscp** parameter is -1, data packets are considered a match regardless of the DSCP value.
        self.match_dscp = match_dscp
        # The protocol that is used to match packets.
        # 
        # >  Traffic marking policies support multiple protocols. For more information, see the documentation of CEN.
        self.protocol = protocol
        # The source CIDR block of packets. IPv6 and IPv4 addresses are supported.
        self.src_cidr = src_cidr
        # The source port range used to match data packets.
        self.src_port_range = src_port_range
        # The description of the traffic classification rule.
        self.traffic_match_rule_description = traffic_match_rule_description
        # The ID of the traffic classification rule.
        self.traffic_match_rule_id = traffic_match_rule_id
        # The name of the traffic classification rule.
        self.traffic_match_rule_name = traffic_match_rule_name
        # The status of the traffic classification rule. Valid values:
        # 
        # *   **Creating**: The rule is being created.
        # *   **Active**: The rule is available.
        # *   **Deleting**: The rule is being deleted.
        self.traffic_match_rule_status = traffic_match_rule_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_family is not None:
            result['AddressFamily'] = self.address_family

        if self.dst_cidr is not None:
            result['DstCidr'] = self.dst_cidr

        if self.dst_port_range is not None:
            result['DstPortRange'] = self.dst_port_range

        if self.match_dscp is not None:
            result['MatchDscp'] = self.match_dscp

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.src_cidr is not None:
            result['SrcCidr'] = self.src_cidr

        if self.src_port_range is not None:
            result['SrcPortRange'] = self.src_port_range

        if self.traffic_match_rule_description is not None:
            result['TrafficMatchRuleDescription'] = self.traffic_match_rule_description

        if self.traffic_match_rule_id is not None:
            result['TrafficMatchRuleId'] = self.traffic_match_rule_id

        if self.traffic_match_rule_name is not None:
            result['TrafficMatchRuleName'] = self.traffic_match_rule_name

        if self.traffic_match_rule_status is not None:
            result['TrafficMatchRuleStatus'] = self.traffic_match_rule_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressFamily') is not None:
            self.address_family = m.get('AddressFamily')

        if m.get('DstCidr') is not None:
            self.dst_cidr = m.get('DstCidr')

        if m.get('DstPortRange') is not None:
            self.dst_port_range = m.get('DstPortRange')

        if m.get('MatchDscp') is not None:
            self.match_dscp = m.get('MatchDscp')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SrcCidr') is not None:
            self.src_cidr = m.get('SrcCidr')

        if m.get('SrcPortRange') is not None:
            self.src_port_range = m.get('SrcPortRange')

        if m.get('TrafficMatchRuleDescription') is not None:
            self.traffic_match_rule_description = m.get('TrafficMatchRuleDescription')

        if m.get('TrafficMatchRuleId') is not None:
            self.traffic_match_rule_id = m.get('TrafficMatchRuleId')

        if m.get('TrafficMatchRuleName') is not None:
            self.traffic_match_rule_name = m.get('TrafficMatchRuleName')

        if m.get('TrafficMatchRuleStatus') is not None:
            self.traffic_match_rule_status = m.get('TrafficMatchRuleStatus')

        return self

