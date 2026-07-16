# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTrFirewallV2RoutePolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        dest_candidate_list_shrink: str = None,
        firewall_id: str = None,
        lang: str = None,
        policy_description: str = None,
        policy_name: str = None,
        policy_type: str = None,
        src_candidate_list_shrink: str = None,
    ):
        # The list of secondary traffic redirection instances.
        self.dest_candidate_list_shrink = dest_candidate_list_shrink
        # The VPC border firewall instance ID.
        self.firewall_id = firewall_id
        # The language type for receiving messages. Valid values:
        # 
        # - **zh** (default): Chinese
        # - **en**: English
        self.lang = lang
        # The traffic redirection description.
        self.policy_description = policy_description
        # The traffic redirection name.
        self.policy_name = policy_name
        # The traffic redirection scenario type for the VPC border firewall with Cloud Enterprise Network Enterprise Edition. Valid values:
        # 
        # - **fullmesh**: Multi-point interconnection
        # 
        # - **one_to_one**: Point-to-point
        # 
        # - **end_to_end**: Point-to-multipoint
        self.policy_type = policy_type
        # The list of primary traffic redirection instances.
        self.src_candidate_list_shrink = src_candidate_list_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_candidate_list_shrink is not None:
            result['DestCandidateList'] = self.dest_candidate_list_shrink

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

        if self.src_candidate_list_shrink is not None:
            result['SrcCandidateList'] = self.src_candidate_list_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCandidateList') is not None:
            self.dest_candidate_list_shrink = m.get('DestCandidateList')

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

        if m.get('SrcCandidateList') is not None:
            self.src_candidate_list_shrink = m.get('SrcCandidateList')

        return self

