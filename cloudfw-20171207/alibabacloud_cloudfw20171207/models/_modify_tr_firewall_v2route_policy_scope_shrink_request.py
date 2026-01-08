# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTrFirewallV2RoutePolicyScopeShrinkRequest(DaraModel):
    def __init__(
        self,
        dest_candidate_list_shrink: str = None,
        firewall_id: str = None,
        lang: str = None,
        should_recover: str = None,
        src_candidate_list_shrink: str = None,
        tr_firewall_route_policy_id: str = None,
    ):
        # The secondary traffic redirection instances.
        self.dest_candidate_list_shrink = dest_candidate_list_shrink
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
        self.src_candidate_list_shrink = src_candidate_list_shrink
        # The ID of the routing policy.
        # 
        # This parameter is required.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id

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

        if self.should_recover is not None:
            result['ShouldRecover'] = self.should_recover

        if self.src_candidate_list_shrink is not None:
            result['SrcCandidateList'] = self.src_candidate_list_shrink

        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCandidateList') is not None:
            self.dest_candidate_list_shrink = m.get('DestCandidateList')

        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ShouldRecover') is not None:
            self.should_recover = m.get('ShouldRecover')

        if m.get('SrcCandidateList') is not None:
            self.src_candidate_list_shrink = m.get('SrcCandidateList')

        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')

        return self

