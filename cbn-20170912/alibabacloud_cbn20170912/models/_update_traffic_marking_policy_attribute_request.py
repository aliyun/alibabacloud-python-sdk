# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class UpdateTrafficMarkingPolicyAttributeRequest(DaraModel):
    def __init__(
        self,
        add_traffic_match_rules: List[main_models.UpdateTrafficMarkingPolicyAttributeRequestAddTrafficMatchRules] = None,
        client_token: str = None,
        delete_traffic_match_rules: List[main_models.UpdateTrafficMarkingPolicyAttributeRequestDeleteTrafficMatchRules] = None,
        dry_run: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_marking_policy_description: str = None,
        traffic_marking_policy_id: str = None,
        traffic_marking_policy_name: str = None,
    ):
        # The traffic classification rules to be added to the traffic marking policy.
        # 
        # You can add at most 50 traffic classification rules in each call.
        self.add_traffic_match_rules = add_traffic_match_rules
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The traffic classification rules to be deleted from the traffic marking policy.
        # 
        # >  Specify detailed information about the traffic classification rule, such as the source CIDR block, destination CIDR block, source port, destination port, and DSCP value. If you do not specify sufficient information, the system may fail to match the traffic classification rule that you want to delete.
        self.delete_traffic_match_rules = delete_traffic_match_rules
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: preforms a dry run. The system checks the required parameters, request syntax, and limits. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and sends the request.
        self.dry_run = dry_run
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The new description of the traffic marking policy.
        # 
        # The description must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). The description must start with a letter.
        self.traffic_marking_policy_description = traffic_marking_policy_description
        # The ID of the traffic marking policy.
        # 
        # This parameter is required.
        self.traffic_marking_policy_id = traffic_marking_policy_id
        # The new name of the traffic marking policy.
        # 
        # The name must be 2 to 128 characters in length, and can contain letters, digits, underscores (_), and hyphens (-). It must start with a letter.
        self.traffic_marking_policy_name = traffic_marking_policy_name

    def validate(self):
        if self.add_traffic_match_rules:
            for v1 in self.add_traffic_match_rules:
                 if v1:
                    v1.validate()
        if self.delete_traffic_match_rules:
            for v1 in self.delete_traffic_match_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddTrafficMatchRules'] = []
        if self.add_traffic_match_rules is not None:
            for k1 in self.add_traffic_match_rules:
                result['AddTrafficMatchRules'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['DeleteTrafficMatchRules'] = []
        if self.delete_traffic_match_rules is not None:
            for k1 in self.delete_traffic_match_rules:
                result['DeleteTrafficMatchRules'].append(k1.to_map() if k1 else None)

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

        if self.traffic_marking_policy_description is not None:
            result['TrafficMarkingPolicyDescription'] = self.traffic_marking_policy_description

        if self.traffic_marking_policy_id is not None:
            result['TrafficMarkingPolicyId'] = self.traffic_marking_policy_id

        if self.traffic_marking_policy_name is not None:
            result['TrafficMarkingPolicyName'] = self.traffic_marking_policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.add_traffic_match_rules = []
        if m.get('AddTrafficMatchRules') is not None:
            for k1 in m.get('AddTrafficMatchRules'):
                temp_model = main_models.UpdateTrafficMarkingPolicyAttributeRequestAddTrafficMatchRules()
                self.add_traffic_match_rules.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.delete_traffic_match_rules = []
        if m.get('DeleteTrafficMatchRules') is not None:
            for k1 in m.get('DeleteTrafficMatchRules'):
                temp_model = main_models.UpdateTrafficMarkingPolicyAttributeRequestDeleteTrafficMatchRules()
                self.delete_traffic_match_rules.append(temp_model.from_map(k1))

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

        if m.get('TrafficMarkingPolicyDescription') is not None:
            self.traffic_marking_policy_description = m.get('TrafficMarkingPolicyDescription')

        if m.get('TrafficMarkingPolicyId') is not None:
            self.traffic_marking_policy_id = m.get('TrafficMarkingPolicyId')

        if m.get('TrafficMarkingPolicyName') is not None:
            self.traffic_marking_policy_name = m.get('TrafficMarkingPolicyName')

        return self

class UpdateTrafficMarkingPolicyAttributeRequestDeleteTrafficMatchRules(DaraModel):
    def __init__(
        self,
        address_family: str = None,
        dst_cidr: str = None,
        dst_port_range: List[int] = None,
        match_dscp: int = None,
        protocol: str = None,
        src_cidr: str = None,
        src_port_range: List[int] = None,
        traffic_match_rule_description: str = None,
        traffic_match_rule_name: str = None,
    ):
        # The address family. Valid values: You can set the value to IPv4 or IPv6, or leave the value empty.
        self.address_family = address_family
        # The destination CIDR block of packets. IPv4 and IPv6 addresses are supported.
        self.dst_cidr = dst_cidr
        # The destination port range that is used to match packets.
        self.dst_port_range = dst_port_range
        # The DSCP value that is used to match packets.
        self.match_dscp = match_dscp
        # The protocol that is used to match packets.
        # 
        # You can call the [ListTrafficMarkingPolicies](https://help.aliyun.com/document_detail/468322.html) operation to query the details about a traffic classification rule.
        self.protocol = protocol
        # The source CIDR block of packets. IPv4 and IPv6 addresses are supported.
        self.src_cidr = src_cidr
        # The source port range that is used to match packets.
        self.src_port_range = src_port_range
        # The description of the traffic classification rule.
        # 
        # This parameter is optional. If you enter a description, it must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.traffic_match_rule_description = traffic_match_rule_description
        # The name of the traffic classification rule.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.traffic_match_rule_name = traffic_match_rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_family is not None:
            result['AddressFamily'] = self.address_family

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
        if m.get('AddressFamily') is not None:
            self.address_family = m.get('AddressFamily')

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

class UpdateTrafficMarkingPolicyAttributeRequestAddTrafficMatchRules(DaraModel):
    def __init__(
        self,
        address_family: str = None,
        dst_cidr: str = None,
        dst_port_range: List[int] = None,
        match_dscp: int = None,
        protocol: str = None,
        src_cidr: str = None,
        src_port_range: List[int] = None,
        traffic_match_rule_description: str = None,
        traffic_match_rule_name: str = None,
    ):
        # The address family. Valid values: You can set the value to IPv4 or IPv6, or leave the value empty.
        self.address_family = address_family
        # The destination CIDR block of packets. IPv4 and IPv6 addresses are supported.
        # 
        # Packets whose destination IP addresses fall into the specified destination CIDR block meet the traffic classification rule. If you do not specify a destination CIDR block, all packets meet the traffic classification rule.
        # 
        # You can create up to 50 traffic classification rules in each call. You can specify a destination CIDR block for each traffic classification rule.
        self.dst_cidr = dst_cidr
        # The destination port range that is used to match packets. Valid values: **-1** and **1** to **65535**.
        # 
        # Packets whose destination ports fall within the specified destination port range are considered a match. If you do not specify a destination port range, packets are considered a match regardless of the destination port.
        # 
        # You can enter up to two port numbers. Take note of the following rules:
        # 
        # *   If you enter only one port number, such as 1, packets whose destination port is 1 match the traffic classification rule. A value of -1 specifies all destination ports.
        # *   If you enter two port numbers, such as 1 and 200, packets whose destination ports fall into 1 and 200 are considered a match.
        # *   If you enter two port numbers and one of them is -1, the other port number must also be -1. In this case, all packets meet the traffic classification rule.
        # 
        # You can create up to 50 traffic classification rules in each call. You can specify a destination port range for each traffic classification rule.
        self.dst_port_range = dst_port_range
        # The Differentiated Service Code Point (DSCP) value that is used to match packets. Valid values: **0** to **63**.
        # 
        # Requests that carry the specified DSCP value are considered a match. If you do not specify a DSCP value, packets are considered a match regardless of the DSCP value.
        # 
        # >  The DSCP value that you specify for this parameter is the DSCP value that packets carry before they are transmitted over the inter-region connection.
        # 
        # You can create up to 50 traffic classification rules in each call. You can specify a DSCP value for each traffic classification rule.
        self.match_dscp = match_dscp
        # The protocol that is used to match packets.
        # 
        # Traffic classification rules support the following protocols: **HTTP**, **HTTPS**, **TCP**, **UDP**, **SSH**, and **Telnet**. For more information, log on to the [CEN console](https://cen.console.aliyun.com/cen/list).
        # 
        # **Some protocols use a fixed port. Click to view the protocols and ports.**
        # 
        # *   If the protocol is **ICMP**, set the destination port to **-1**.
        # *   If the protocol is **GRE**, set the destination port to **-1**.
        # *   If the protocol is **SSH**, set the destination port to **22**.
        # *   If the protocol is **Telnet**, set the destination port to **23**.
        # *   If the protocol is **HTTP**, set the destination port to **80**.
        # *   If the protocol is **HTTPS**, set the destination port to **443**.
        # *   If the protocol is **MS SQL**, set the destination port to **1443**.
        # *   If the protocol is **Oracle**, set the destination port to **1521**.
        # *   If the protocol is **Mysql**, set the destination port to **3306**.
        # *   If the protocol is **RDP**, set the destination port to **3389**.
        # *   If the protocol is **Postgre SQL**, set the destination port to **5432**.
        # *   If the protocol is **Redis**, the destination port must be **6379**.
        # 
        # You can create up to 50 traffic classification rules in each call. You can specify a protocol for each traffic classification rule.
        self.protocol = protocol
        # The source CIDR block of packets. IPv4 and IPv6 addresses are supported.
        # 
        # Packets whose source IP addresses fall into the specified source CIDR block meet the traffic classification rule. If you do not specify a source CIDR block, all packets meet the traffic classification rule.
        # 
        # You can create up to 50 traffic classification rules in each call. You can specify a source CIDR block for each traffic classification rule.
        self.src_cidr = src_cidr
        # The source port range that is used to match packets. Valid values: **-1** and **1** to **65535**.
        # 
        # The traffic classification rule matches the packets whose source ports fall within the source port range. If you do not specify this parameter, packets are considered a match regardless of the source port.
        # 
        # You can enter up to two port numbers. Take note of the following rules:
        # 
        # *   If you enter only one port number, such as 1, packets whose source port is 1 are considered a match. A value of -1 specifies all source ports.
        # *   If you enter two port numbers, such as 1 and 200, packets whose source ports fall into 1 and 200 are considered a match.
        # *   If you enter two port numbers and one of them is -1, the other port number must also be -1. In this case, all packets meet the traffic classification rule.
        # 
        # You can create up to 50 traffic classification rules in each call. You can specify a source port range for each traffic classification rule.
        self.src_port_range = src_port_range
        # The description of the traffic classification rule.
        # 
        # You can create up to 50 traffic classification rules in each call. You can specify a description for each traffic classification rule.
        # 
        # This parameter is optional. If you enter a description, it must be 1 to 256 characters in length and cannot start with http:// or https://.
        self.traffic_match_rule_description = traffic_match_rule_description
        # The name of the traffic classification rule.
        # 
        # You can create up to 50 traffic classification rules in each call. You can specify a name for each traffic classification rule.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.traffic_match_rule_name = traffic_match_rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_family is not None:
            result['AddressFamily'] = self.address_family

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
        if m.get('AddressFamily') is not None:
            self.address_family = m.get('AddressFamily')

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

