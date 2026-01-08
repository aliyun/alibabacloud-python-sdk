# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class ModifyTrFirewallV2RoutePolicyScopeRequest(DaraModel):
    def __init__(
        self,
        dest_candidate_list: List[main_models.ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList] = None,
        firewall_id: str = None,
        lang: str = None,
        should_recover: str = None,
        src_candidate_list: List[main_models.ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList] = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The secondary traffic redirection instances.
        self.dest_candidate_list = dest_candidate_list
        # The instance ID of the virtual private cloud (VPC) firewall.
        # 
        # This parameter is required.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *  **zh** (default): Chinese
        # *  **en**: English
        self.lang = lang
        # Specifies whether to restore the traffic redirection configurations. Valid values:
        # 
        # *   true: roll back
        # *   false: withdraw
        self.should_recover = should_recover
        # The primary traffic redirection instances.
        self.src_candidate_list = src_candidate_list
        # The ID of the routing policy.
        # 
        # This parameter is required.
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

        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.should_recover is not None:
            result['ShouldRecover'] = self.should_recover

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
                temp_model = main_models.ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList()
                self.dest_candidate_list.append(temp_model.from_map(k1))

        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ShouldRecover') is not None:
            self.should_recover = m.get('ShouldRecover')

        self.src_candidate_list = []
        if m.get('SrcCandidateList') is not None:
            for k1 in m.get('SrcCandidateList'):
                temp_model = main_models.ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList()
                self.src_candidate_list.append(temp_model.from_map(k1))

        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')

        return self

class ModifyTrFirewallV2RoutePolicyScopeRequestSrcCandidateList(DaraModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the traffic redirection instance.
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

class ModifyTrFirewallV2RoutePolicyScopeRequestDestCandidateList(DaraModel):
    def __init__(
        self,
        candidate_id: str = None,
        candidate_type: str = None,
    ):
        # The ID of the traffic redirection instance.
        self.candidate_id = candidate_id
        # The type of the traffic redirection instance.
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

