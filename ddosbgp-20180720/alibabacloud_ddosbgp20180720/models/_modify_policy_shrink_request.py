# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPolicyShrinkRequest(DaraModel):
    def __init__(
        self,
        action_type: int = None,
        content_shrink: str = None,
        id: str = None,
        name: str = None,
        port_version: str = None,
    ):
        # The action type. Valid values:
        # 
        # - **10**: modifies the name (Name is required).
        # - **11**: modifies the blacklist timeout period (BlackIpListExpireAt is required). Only IP-specific mitigation policy is supported.
        # - **12**: modifies the switch for whitelisting back-to-origin IP addresses of Anti-DDoS Pro and Anti-DDoS Premium (WhitenGfbrNets is required). Only IP-specific mitigation policy is supported.
        # - **13**: modifies the switch for ICMP Blocking (EnableDropIcmp is required). Only IP-specific mitigation policy is supported.
        # - **20**: adds entries to blacklists and whitelists (WhiteIpList and BlackIpList are optional). Only IP-specific mitigation policy is supported.
        # - **21**: deletes entries from blacklists and whitelists (WhiteIpList and BlackIpList are optional). Only IP-specific mitigation policy is supported.
        # - **22**: clears the whitelist. Only IP-specific mitigation policy is supported.
        # - **23**: clears the blacklist. Only IP-specific mitigation policy is supported.
        # - **30**: modifies the AI-based intelligent protection switch and level (EnableIntelligence and IntelligenceLevel are required). Only IP-specific mitigation policy is supported.
        # - **31**: modifies the Location Blacklist configuration (RegionBlockCountryList and RegionBlockProvinceList are optional). Only IP-specific mitigation policy is supported.
        # - **32**: modifies the source rate limiting configuration (SourceLimit and SourceBlockList are required). Only IP-specific mitigation policy is supported.
        # - **33**: modifies the reflection attack port filtering (ReflectBlockUdpPortList is required). Only IP-specific mitigation policy is supported.
        # - **40**: creates a port blocking rule (PortRuleList is required). Only IP-specific mitigation policy is supported.
        # - **41**: modifies a port blocking rule (PortRuleList is required). Only IP-specific mitigation policy is supported.
        # - **42**: deletes a port blocking rule (PortRuleList is required). Only IP-specific mitigation policy is supported.
        # - **50**: creates a byte-match filter rule (FingerPrintRuleList is required). Only IP-specific mitigation policy is supported.
        # - **51**: modifies a byte-match filter rule (FingerPrintRuleList is required). Only IP-specific mitigation policy is supported.
        # - **52**: deletes a byte-match filter rule (FingerPrintRuleList is required). Only IP-specific mitigation policy is supported.
        # - **60**: modifies the port-specific mitigation switch (EnableL4Defense is required). Only port-specific mitigation policy is supported.
        # - **61**: creates a port-specific mitigation rule (L4RuleList is required). Only port-specific mitigation policy is supported.
        # - **62**: modifies a port-specific mitigation rule (L4RuleList is required). Only port-specific mitigation policy is supported.
        # - **63**: deletes a port-specific mitigation rule (L4RuleList is required). Only port-specific mitigation policy is supported.
        # 
        # This parameter is required.
        self.action_type = action_type
        # The policy content.
        self.content_shrink = content_shrink
        # The policy ID.
        # 
        # This parameter is required.
        self.id = id
        # The policy name.
        self.name = name
        # The version of the port-specific mitigation policy. Valid values:
        # 
        # - **Not specified**: Modifies the default surf mitigation engine policy.
        # - **2**: Modifies the new stream mitigation engine policy.
        # > Only port-specific mitigation policies are supported.
        self.port_version = port_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.content_shrink is not None:
            result['Content'] = self.content_shrink

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.port_version is not None:
            result['PortVersion'] = self.port_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('Content') is not None:
            self.content_shrink = m.get('Content')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PortVersion') is not None:
            self.port_version = m.get('PortVersion')

        return self

