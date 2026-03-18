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
        # The type of the action. Valid values:
        # 
        # *   **10**: modifies the name. If you specify this value, `Name` is required.
        # *   **11**: modifies the blacklist validity period. If you specify this value, `BlackIpListExpireAt` is required. Only IP-specific mitigation policies support this value.
        # *   **12**: changes the status of the feature of adding back-to-origin CIDR blocks of Anti-DDoS Proxy to the whitelist. If you specify this value, `WhitenGfbrNets` is required. Only IP-specific mitigation policies support this value.
        # *   **13**: changes the status of the ICMP blocking feature. If you specify this value, `EnableDropIcmp` is required. Only IP-specific mitigation policies support this value.
        # *   **20**: adds IP addresses to the blacklist or the whitelist. If you specify this value, you must specify at least one of `WhiteIpList` and `BlackIpList`. Only IP-specific mitigation policies support this value.
        # *   **21**: removes IP addresses from the blacklist or the whitelist. If you specify this value, at least one of `WhiteIpList` and `BlackIpList` is required. Only IP-specific mitigation policies support this value.
        # *   **22**: clears the whitelist. Only IP-specific mitigation policies support this value.
        # *   **23**: clears the blacklist. Only IP-specific mitigation policies support this value.
        # *   **30**: modifies the status and level of intelligent protection. If you specify this value, `EnableIntelligence` and `IntelligenceLevel` are required. Only IP-specific mitigation policies support this value.
        # *   **31**: modifies the location blacklist settings. If you specify this value, one of `RegionBlockCountryList` and `RegionBlockProvinceList` is required. Only IP-specific mitigation policies support this value.
        # *   **32**: modifies the settings for source rate limiting. If you specify this value, `SourceLimit` and `SourceBlockList` are required. Only IP-specific mitigation policies support this value.
        # *   **33**: modifies the settings for reflection attack filtering. If you specify this value, `ReflectBlockUdpPortList` is required. Only IP-specific mitigation policies support this value.
        # *   **40**: creates a port blocking rule. If you specify this value, `PortRuleList` is required. Only IP-specific mitigation policies support this value.
        # *   **41**: modifies the port blocking rule. If you specify this value, `PortRuleList` is required. Only IP-specific mitigation policies support this value.
        # *   **42**: deletes the port blocking rule. If you specify this value, `PortRuleList` is required. Only IP-specific mitigation policies support this value.
        # *   **50**: creates a byte-match filter rule. If you specify this value, `FingerPrintRuleList` is required. Only IP-specific mitigation policies support this value.
        # *   **51**: modifies the byte-match filter rule. If you specify this value, `FingerPrintRuleList` is required. Only IP-specific mitigation policies support this value.
        # *   **52**: deletes the byte-match filter rule. If you specify this value, `FingerPrintRuleList` is required. Only IP-specific mitigation policies support this value.
        # *   **60**: changes the status of the port-specific mitigation feature. If you specify this value, `EnableL4Defense` is required. Only port-specific mitigation policies support this value.
        # *   **61**: creates a port-specific mitigation rule. If you specify this value, `L4RuleList` is required. Only port-specific mitigation policies support this value.
        # *   **62**: modifies the port-specific mitigation rule. If you specify this value, `L4RuleList` is required. Only port-specific mitigation policies support this value.
        # *   **63**: deletes the port-specific mitigation rule. If you specify this value, `L4RuleList` is required. Only port-specific mitigation policies support this value.
        # 
        # This parameter is required.
        self.action_type = action_type
        # The policy content.
        self.content_shrink = content_shrink
        # The ID of the policy.
        # 
        # This parameter is required.
        self.id = id
        # The name of the policy.
        self.name = name
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

