# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeTrFirewallV2RoutePolicyListResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: str = None,
        tr_firewall_route_policies: List[main_models.DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # The routing policies.
        self.tr_firewall_route_policies = tr_firewall_route_policies

    def validate(self):
        if self.tr_firewall_route_policies:
            for v1 in self.tr_firewall_route_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['TrFirewallRoutePolicies'] = []
        if self.tr_firewall_route_policies is not None:
            for k1 in self.tr_firewall_route_policies:
                result['TrFirewallRoutePolicies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.tr_firewall_route_policies = []
        if m.get('TrFirewallRoutePolicies') is not None:
            for k1 in m.get('TrFirewallRoutePolicies'):
                temp_model = main_models.DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies()
                self.tr_firewall_route_policies.append(temp_model.from_map(k1))

        return self

class DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePolicies(DaraModel):
    def __init__(
        self,
        dest_candidate_list: List[main_models.DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList] = None,
        policy_description: str = None,
        policy_name: str = None,
        policy_status: str = None,
        policy_type: str = None,
        src_candidate_list: List[main_models.DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList] = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The secondary traffic redirection instances.
        self.dest_candidate_list = dest_candidate_list
        # The description of the routing policy.
        self.policy_description = policy_description
        # The name of the routing policy.
        self.policy_name = policy_name
        # The status of the routing policy. Valid values:
        # 
        # *   creating: The policy is being created.
        # *   deleting: The policy is being deleted.
        # *   opening: The policy is being enabled.
        # *   opened: The policy is enabled.
        # *   closing: The policy is being disabled.
        # *   closed: The policy is disabled.
        self.policy_status = policy_status
        # The type of the traffic redirection scenario of the VPC firewall. Valid values:
        # 
        # *   **fullmesh**: interconnected instances
        # *   **one_to_one**: instance to instance
        # *   **end_to_end**: instance to instances
        self.policy_type = policy_type
        # The primary traffic redirection instances.
        self.src_candidate_list = src_candidate_list
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        if self.dest_candidate_list:
            for v1 in self.dest_candidate_list:
                 if v1:
                    v1.validate()
        if self.src_candidate_list:
            for v1 in self.src_candidate_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DestCandidateList'] = []
        if self.dest_candidate_list is not None:
            for k1 in self.dest_candidate_list:
                result['DestCandidateList'].append(k1.to_map() if k1 else None)

        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_status is not None:
            result['PolicyStatus'] = self.policy_status

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        result['SrcCandidateList'] = []
        if self.src_candidate_list is not None:
            for k1 in self.src_candidate_list:
                result['SrcCandidateList'].append(k1.to_map() if k1 else None)

        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dest_candidate_list = []
        if m.get('DestCandidateList') is not None:
            for k1 in m.get('DestCandidateList'):
                temp_model = main_models.DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList()
                self.dest_candidate_list.append(temp_model.from_map(k1))

        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyStatus') is not None:
            self.policy_status = m.get('PolicyStatus')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        self.src_candidate_list = []
        if m.get('SrcCandidateList') is not None:
            for k1 in m.get('SrcCandidateList'):
                temp_model = main_models.DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList()
                self.src_candidate_list.append(temp_model.from_map(k1))

        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')

        return self

class DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesSrcCandidateList(DaraModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the primary traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the primary traffic redirection instance.
        self.candidate_type = candidate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id

        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')

        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')

        return self

class DescribeTrFirewallV2RoutePolicyListResponseBodyTrFirewallRoutePoliciesDestCandidateList(DaraModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the secondary traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the secondary traffic redirection instance.
        self.candidate_type = candidate_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.candidate_id is not None:
            result['CandidateId'] = self.candidate_id

        if self.candidate_type is not None:
            result['CandidateType'] = self.candidate_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateId') is not None:
            self.candidate_id = m.get('CandidateId')

        if m.get('CandidateType') is not None:
            self.candidate_type = m.get('CandidateType')

        return self

