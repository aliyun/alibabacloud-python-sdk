# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeTrFirewallPolicyBackUpAssociationListRequest(DaraModel):
    def __init__(
        self,
        candidate_list: List[main_models.DescribeTrFirewallPolicyBackUpAssociationListRequestCandidateList] = None,
        firewall_id: str = None,
        lang: str = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The traffic redirection instances.
        self.candidate_list = candidate_list
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

    def validate(self):
        if self.candidate_list:
            for v1 in self.candidate_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CandidateList'] = []
        if self.candidate_list is not None:
            for k1 in self.candidate_list:
                result['CandidateList'].append(k1.to_map() if k1 else None)

        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.candidate_list = []
        if m.get('CandidateList') is not None:
            for k1 in m.get('CandidateList'):
                temp_model = main_models.DescribeTrFirewallPolicyBackUpAssociationListRequestCandidateList()
                self.candidate_list.append(temp_model.from_map(k1))

        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')

        return self

class DescribeTrFirewallPolicyBackUpAssociationListRequestCandidateList(DaraModel):
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

