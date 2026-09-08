# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class CreateTrafficMarkingPolicyRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        marking_dscp: int = None,
        owner_account: str = None,
        owner_id: int = None,
        priority: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        traffic_marking_policy_description: str = None,
        traffic_marking_policy_name: str = None,
        traffic_match_rules: List[main_models.CreateTrafficMarkingPolicyRequestTrafficMatchRules] = None,
        transit_router_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run. The system checks the required parameters, request syntax, and business restrictions. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # - **false** (default): performs a dry run and sends the request. If the request passes the dry run, the traffic marking policy is created.
        self.dry_run = dry_run
        # The DSCP value to be added to traffic packets that match the traffic classification rules. Valid values: **0** to **63**.
        # 
        # The DSCP value of each traffic marking policy under a transit router instance must be unique.
        # 
        # This parameter is required.
        self.marking_dscp = marking_dscp
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The priority of the traffic marking policy. Valid values: **1** to **100**.
        # 
        # The priority of each traffic marking policy under a transit router instance must be unique. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.priority = priority
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The description of the traffic marking policy.
        # 
        # The description can be empty or 1 to 256 characters in length, and cannot start with http:// or https://.
        self.traffic_marking_policy_description = traffic_marking_policy_description
        # The name of the traffic marking policy.
        # 
        # The name can be empty or 1 to 128 characters in length, and cannot start with http:// or https://.
        self.traffic_marking_policy_name = traffic_marking_policy_name
        # The list of traffic classification rules for the traffic marking policy.
        # 
        # Traffic packets that match the traffic classification rules are marked with the DSCP value of the traffic marking policy.
        # 
        # You can create up to 50 traffic classification rules at a time.
        self.traffic_match_rules = traffic_match_rules
        # The instance ID of the forward routing transit router.
        # 
        # This parameter is required.
        self.transit_router_id = transit_router_id

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

        if self.marking_dscp is not None:
            result['MarkingDscp'] = self.marking_dscp

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.traffic_marking_policy_description is not None:
            result['TrafficMarkingPolicyDescription'] = self.traffic_marking_policy_description

        if self.traffic_marking_policy_name is not None:
            result['TrafficMarkingPolicyName'] = self.traffic_marking_policy_name

        result['TrafficMatchRules'] = []
        if self.traffic_match_rules is not None:
            for k1 in self.traffic_match_rules:
                result['TrafficMatchRules'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('MarkingDscp') is not None:
            self.marking_dscp = m.get('MarkingDscp')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TrafficMarkingPolicyDescription') is not None:
            self.traffic_marking_policy_description = m.get('TrafficMarkingPolicyDescription')

        if m.get('TrafficMarkingPolicyName') is not None:
            self.traffic_marking_policy_name = m.get('TrafficMarkingPolicyName')

        self.traffic_match_rules = []
        if m.get('TrafficMatchRules') is not None:
            for k1 in m.get('TrafficMatchRules'):
                temp_model = main_models.CreateTrafficMarkingPolicyRequestTrafficMatchRules()
                self.traffic_match_rules.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

class CreateTrafficMarkingPolicyRequestTrafficMatchRules(DaraModel):
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
        # The address type. Valid values: IPv4, IPv6, or empty.
        self.address_family = address_family
        # The destination CIDR block of traffic packets. IPv4 and IPv6 addresses are supported.
        # 
        # The traffic classification rule matches traffic whose destination IP address falls within the destination CIDR block. If you do not set this parameter, the traffic classification rule matches traffic with any destination IP address.
        # 
        # You can create up to 50 traffic classification rules at a time, and each traffic classification rule can specify one destination CIDR block.
        self.dst_cidr = dst_cidr
        # The destination port of traffic packets. Valid values: **-1** and **1** to **65535**.
        # 
        # The traffic classification rule matches traffic whose destination port falls within the destination port range. If you do not set this parameter, the traffic classification rule matches traffic with any destination port.
        # 
        # This parameter supports up to two port numbers. The input format is described as follows:
        # 
        # - If you enter only one port number, such as 1, the system matches traffic whose destination port is 1 by default. If the value is -1, the system matches traffic with any destination port.
        # - If you enter two port numbers, such as 1 and 200, the system matches traffic whose destination port is in the range of 1 to 200 by default.
        # - If you enter two port numbers and one of them is -1, the other port number must also be -1, which indicates matching traffic with any destination port.
        # 
        # You can create up to 50 traffic classification rules at a time, and each traffic classification rule can specify one destination port range.
        self.dst_port_range = dst_port_range
        # The DSCP value of traffic packets. Valid values: **0** to **63**.
        # 
        # The traffic classification rule matches traffic that contains the specified DSCP value. If you do not set this parameter, the traffic classification rule matches traffic with any DSCP value.
        # 
        # > The DSCP value refers to the DSCP value that the traffic packets already carry before entering the inter-region connection.
        # 
        # You can create up to 50 traffic classification rules at a time, and each traffic classification rule can match one DSCP value.
        self.match_dscp = match_dscp
        # The protocol type of traffic packets.
        # 
        # The traffic marking policy supports matching traffic of multiple protocol types such as **HTTP**, **HTTPS**, **TCP**, **UDP**, **SSH**, and **Telnet**. For more protocol types, log on to the [Cloud Enterprise Network (CEN) console](https://cen.console.aliyun.com/cen/list).
        # <details>
        # <summary>Some protocols have fixed ports. Click to view port details.</summary>
        # 
        # - If the protocol type is **ICMP**, the destination port must be set to **-1**.
        # - If the protocol type is **GRE**, the destination port must be set to **-1**.
        # - If the protocol type is **SSH**, the destination port must be set to **22**.
        # - If the protocol type is **Telnet**, the destination port must be set to **23**.
        # - If the protocol type is **HTTP**, the destination port must be set to **80**.
        # - If the protocol type is **HTTPS**, the destination port must be set to **443**.
        # - If the protocol type is **MS SQL**, the destination port must be set to **1443**.
        # - If the protocol type is **Oracle**, the destination port must be set to **1521**.
        # - If the protocol type is **Mysql**, the destination port must be set to **3306**.
        # - If the protocol type is **RDP**, the destination port must be set to **3389**.
        # - If the protocol type is **Postgre SQL**, the destination port must be set to **5432**.
        # - If the protocol type is **Redis**, the destination port must be set to **6379**.
        # 
        # </details>
        # 
        # You can create up to 50 traffic classification rules at a time, and each traffic classification rule can match one protocol type.
        self.protocol = protocol
        # The source CIDR block of traffic packets. IPv6 and IPv4 addresses are supported.
        # 
        # The traffic classification rule matches traffic whose source IP address falls within the source CIDR block. If you do not set this parameter, the traffic classification rule matches traffic with any source IP address.
        # 
        # You can create up to 50 traffic classification rules at a time, and each traffic classification rule can match one source CIDR block.
        self.src_cidr = src_cidr
        # The source port of traffic packets. Valid values: **-1** and **1** to **65535**.
        # 
        # The traffic classification rule matches traffic whose source port falls within the source port range. If you do not set this parameter, the traffic classification rule matches traffic with any source port.
        # 
        # This parameter supports up to two port numbers. The input format is described as follows:
        # 
        # - If you enter only one port number, such as 1, the system matches traffic whose source port is 1 by default. If the value is -1, the system matches traffic with any source port.
        # - If you enter two port numbers, such as 1 and 200, the system matches traffic whose source port is in the range of 1 to 200 by default.
        # - If you enter two port numbers and one of them is -1, the other port number must also be -1, which indicates matching traffic with any source port.
        # 
        # You can create up to 50 traffic classification rules at a time, and each traffic classification rule can specify one source port range.
        self.src_port_range = src_port_range
        # The description of the traffic classification rule.
        # 
        # You can create up to 50 traffic classification rules at a time, and each traffic classification rule can have one description.
        # 
        # The description can be empty or 1 to 256 characters in length, and cannot start with http:// or https://.
        self.traffic_match_rule_description = traffic_match_rule_description
        # The name of the traffic classification rule.
        # 
        # You can create up to 50 traffic classification rules at a time, and each traffic classification rule can have one name.
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

