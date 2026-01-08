# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class CreateTrFirewallV2RoutePolicyRequest(DaraModel):
    def __init__(
        self,
        dest_candidate_list: List[main_models.CreateTrFirewallV2RoutePolicyRequestDestCandidateList] = None,
        firewall_id: str = None,
        lang: str = None,
        policy_description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        src_candidate_list: List[main_models.CreateTrFirewallV2RoutePolicyRequestSrcCandidateList] = None,
    ):
        # The secondary traffic redirection instances.
        self.dest_candidate_list = dest_candidate_list
        # The instance ID of the VPC firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # The description of the traffic redirection instance.
        self.policy_description = policy_description
        # The name of the traffic redirection instance.
        self.policy_name = policy_name
        # The type of the traffic redirection scenario of the VPC firewall. Valid values:
        # 
        # *   **fullmesh**: interconnected instances
        # *   **one_to_one**: instance to instance
        # *   **end_to_end**: instance to instances
        self.policy_type = policy_type
        # The primary traffic redirection instances.
        self.src_candidate_list = src_candidate_list

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

        if self.policy_description is not None:
            result['PolicyDescription'] = self.policy_description

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        result['SrcCandidateList'] = []
        if self.src_candidate_list is not None:
            for k1 in self.src_candidate_list:
                result['SrcCandidateList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dest_candidate_list = []
        if m.get('DestCandidateList') is not None:
            for k1 in m.get('DestCandidateList'):
                temp_model = main_models.CreateTrFirewallV2RoutePolicyRequestDestCandidateList()
                self.dest_candidate_list.append(temp_model.from_map(k1))

        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PolicyDescription') is not None:
            self.policy_description = m.get('PolicyDescription')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        self.src_candidate_list = []
        if m.get('SrcCandidateList') is not None:
            for k1 in m.get('SrcCandidateList'):
                temp_model = main_models.CreateTrFirewallV2RoutePolicyRequestSrcCandidateList()
                self.src_candidate_list.append(temp_model.from_map(k1))

        return self

class CreateTrFirewallV2RoutePolicyRequestSrcCandidateList(DaraModel):
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

class CreateTrFirewallV2RoutePolicyRequestDestCandidateList(DaraModel):
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

