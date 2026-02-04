# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class AddTraficMatchRuleToTrafficMarkingPolicyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_marking_policy_id: str = None,
        traffic_match_rules: List[main_models.AddTraficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules] = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, ClientToken is set to the value of RequestId. The value of RequestId may be different for each request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: performs a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the traffic marking policy.
        # 
        # This parameter is required.
        self.traffic_marking_policy_id = traffic_marking_policy_id
        # The information about the traffic classification rule.
        # 
        # You can specify at most 50 traffic classification rules.
        self.traffic_match_rules = traffic_match_rules

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id

        result['TrafficMatchRules'] = []
        if self.traffic_match_rules is not None:
            for k1 in self.traffic_match_rules:
                result['TrafficMatchRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')

        self.traffic_match_rules = []
        if m.get('TrafficMatchRules') is not None:
            for k1 in m.get('TrafficMatchRules'):
                temp_model = main_models.AddTraficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules()
                self.traffic_match_rules.append(temp_model.from_map(k1))

        return self

class AddTraficMatchRuleToTrafficMarkingPolicyRequestTrafficMatchRules(DaraModel):
    def __init__(
        self,
        dst_cidr: str = None,
        dst_port_range: List[int] = None,
        match_dscp: int = None,
        protocol: str = None,
        src_cidr: str = None,
        src_port_range: List[int] = None,
        traffic_match_rule_description: str = None,
        traffic_match_rule_name: str = None,
    ):
        # The destination CIDR block that is used to match packets.
        # 
        # The traffic classification rule matches the packets whose destination IP addresses fall within the specified destination CIDR block. If you do not set this parameter, packets are considered a match regardless of the DSCP value.
        # 
        # You can specify at most 50 traffic classification rules.
        self.dst_cidr = dst_cidr
        # The destination port range that is used to match packets. Valid values: **-1** and **1** to **65535**.
        # 
        # The traffic classification rule matches the packets whose destination ports fall within the destination port range. If you do not set this parameter, packets are considered a match regardless of the DSCP value.
        # 
        # You can specify at most two ports. Take note of the following rules:
        # 
        # *   If you enter only one port number such as 1, the system matches the packets whose destination port is port 1.
        # *   If you enter two port numbers such as 1 and 200, the system matches the packets whose destination ports fall between 1 and 200.
        # *   If you enter two port numbers and one of them is -1, the other port number must also be -1. In this case, packets are considered a match regardless of the destination port.
        # 
        # You can specify at most 50 traffic classification rules.
        self.dst_port_range = dst_port_range
        # The differentiated services code point (DSCP) value that is used to match packets. Valid values: **0** to **63**.
        # 
        # The traffic classification rule matches the packets that contain the specified DSCP value. If you do not set this parameter, packets are considered a match regardless of the DSCP value.
        # 
        # >  The DSCP value that you specify for this parameter is the DSCP value that packets carry before they are transmitted over the inter-region connection.
        # 
        # You can specify at most 50 traffic classification rules.
        self.match_dscp = match_dscp
        # The protocol that is used to match packets.
        # 
        # Valid values: **HTTP**, **HTTPS**, **TCP**, **UDP**, **SSH**, and **Telnet**. For more information, log on to the [Cloud Enterprise Network (CEN) console](https://cen.console.aliyun.com/cen/list).
        # 
        # You can specify at most 50 traffic classification rules.
        self.protocol = protocol
        # The source CIDR block that is used to match packets.
        # 
        # The traffic classification rule matches the packets whose source IP addresses fall within the specified source CIDR block. If you do not set this parameter, packets are considered a match regardless of the source IP address.
        # 
        # You can specify at most 50 traffic classification rules.
        self.src_cidr = src_cidr
        # The source port range that is used to match packets. Valid values: **-1** and **1** to **65535**.
        # 
        # The traffic classification rule matches the packets whose source ports fall within the source port range. If you do not set this parameter, packets are considered a match regardless of the source port.
        # 
        # You can specify at most two ports. Take note of the following rules:
        # 
        # *   If you enter only one port number such as 1, the system matches the packets whose source port is 1.
        # *   If you enter two port numbers such as 1 and 200, the system matches the packets whose source ports fall between 1 and 200.
        # *   If you enter two port numbers and one of them is -1, the other port number must also be -1. In this case, packets are considered a match regardless of the source port.
        # 
        # You can specify at most 50 traffic classification rules.
        self.src_port_range = src_port_range
        # The description of the traffic classification rule.
        # 
        # The description must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The description must start with a letter.
        # 
        # You can specify at most 50 traffic classification rules.
        self.traffic_match_rule_description = traffic_match_rule_description
        # The name of the traffic classification rule.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        # 
        # You can specify at most 50 traffic classification rules.
        self.traffic_match_rule_name = traffic_match_rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.traffic_match_rule_name is not None:
            result['TrafficMatchRuleName'] = self.traffic_match_rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('TrafficMatchRuleName') is not None:
            self.traffic_match_rule_name = m.get('TrafficMatchRuleName')

        return self

