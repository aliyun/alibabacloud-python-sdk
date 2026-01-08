# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyFirewallV2RoutePolicySwitchRequest(DaraModel):
    def __init__(
        self,
        firewall_id: str = None,
        lang: str = None,
        should_recover: str = None,
        tr_firewall_route_policy_id: str = None,
        tr_firewall_route_policy_switch_status: str = None,
    ):
        # The instance ID of the virtual private cloud (VPC) firewall.
        self.firewall_id = firewall_id
        # The language of the content within the response. Valid values:
        # 
        # *   **zh** (default): Chinese
        # *   **en**: English
        self.lang = lang
        # Specifies whether to restore the traffic redirection configurations. Valid values:
        # 
        # *   true: roll back
        # *   false: withdraw
        self.should_recover = should_recover
        # The ID of the routing policy.
        self.tr_firewall_route_policy_id = tr_firewall_route_policy_id
        # The status of the routing policy. Valid values:
        # 
        # *   open: enabled
        # *   close: disabled
        self.tr_firewall_route_policy_switch_status = tr_firewall_route_policy_switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firewall_id is not None:
            result['FirewallId'] = self.firewall_id

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.should_recover is not None:
            result['ShouldRecover'] = self.should_recover

        if self.tr_firewall_route_policy_id is not None:
            result['TrFirewallRoutePolicyId'] = self.tr_firewall_route_policy_id

        if self.tr_firewall_route_policy_switch_status is not None:
            result['TrFirewallRoutePolicySwitchStatus'] = self.tr_firewall_route_policy_switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallId') is not None:
            self.firewall_id = m.get('FirewallId')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('ShouldRecover') is not None:
            self.should_recover = m.get('ShouldRecover')

        if m.get('TrFirewallRoutePolicyId') is not None:
            self.tr_firewall_route_policy_id = m.get('TrFirewallRoutePolicyId')

        if m.get('TrFirewallRoutePolicySwitchStatus') is not None:
            self.tr_firewall_route_policy_switch_status = m.get('TrFirewallRoutePolicySwitchStatus')

        return self

