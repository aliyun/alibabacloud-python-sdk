# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class ListPolicyResponseBody(DaraModel):
    def __init__(
        self,
        policy_list: List[main_models.ListPolicyResponseBodyPolicyList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The policies.
        self.policy_list = policy_list
        # The request ID.
        self.request_id = request_id
        # The total number of policies.
        self.total = total

    def validate(self):
        if self.policy_list:
            for v1 in self.policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PolicyList'] = []
        if self.policy_list is not None:
            for k1 in self.policy_list:
                result['PolicyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k1 in m.get('PolicyList'):
                temp_model = main_models.ListPolicyResponseBodyPolicyList()
                self.policy_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListPolicyResponseBodyPolicyList(DaraModel):
    def __init__(
        self,
        attached_count: int = None,
        content: main_models.ListPolicyResponseBodyPolicyListContent = None,
        id: str = None,
        name: str = None,
        remark: str = None,
        type: str = None,
    ):
        # The number of protected objects that are added to the policy.
        self.attached_count = attached_count
        # The content of the policy.
        self.content = content
        # The ID of the policy.
        self.id = id
        # The name of the policy.
        self.name = name
        # The remarks of the policy.
        self.remark = remark
        # The type of the policy. Valid values:
        # 
        # *   **default**: the default mitigation policy.
        # *   **l3**: IP-specific mitigation policies.
        # *   **l4**: port-specific mitigation policies.
        self.type = type

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attached_count is not None:
            result['AttachedCount'] = self.attached_count

        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachedCount') is not None:
            self.attached_count = m.get('AttachedCount')

        if m.get('Content') is not None:
            temp_model = main_models.ListPolicyResponseBodyPolicyListContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListPolicyResponseBodyPolicyListContent(DaraModel):
    def __init__(
        self,
        black_ip_list_expire_at: int = None,
        enable_drop_icmp: bool = None,
        enable_intelligence: bool = None,
        enable_l4defense: bool = None,
        finger_print_rule_list: List[main_models.ListPolicyResponseBodyPolicyListContentFingerPrintRuleList] = None,
        intelligence_level: str = None,
        l_4rule_list: List[main_models.ListPolicyResponseBodyPolicyListContentL4RuleList] = None,
        port_rule_list: List[main_models.ListPolicyResponseBodyPolicyListContentPortRuleList] = None,
        port_version: str = None,
        reflect_block_udp_port_list: List[int] = None,
        region_block_country_list: List[int] = None,
        region_block_province_list: List[int] = None,
        source_block_list: List[main_models.ListPolicyResponseBodyPolicyListContentSourceBlockList] = None,
        source_limit: main_models.ListPolicyResponseBodyPolicyListContentSourceLimit = None,
        whiten_gfbr_nets: bool = None,
    ):
        # The validity period of the IP address blacklist. The value is a UNIX timestamp.
        self.black_ip_list_expire_at = black_ip_list_expire_at
        # Indicates whether ICMP blocking is enabled.
        self.enable_drop_icmp = enable_drop_icmp
        # Indicates whether intelligent protection is enabled.
        self.enable_intelligence = enable_intelligence
        # Indicates whether port-specific mitigation is enabled.
        self.enable_l4defense = enable_l4defense
        # The byte-match filter rules.
        self.finger_print_rule_list = finger_print_rule_list
        # The level of intelligent protection. Valid values:
        # 
        # *   **default**: normal.
        # *   **hard**: strict.
        # *   **weak**: loose.
        self.intelligence_level = intelligence_level
        # The port-specific mitigation rules.
        self.l_4rule_list = l_4rule_list
        # The port blocking rules.
        self.port_rule_list = port_rule_list
        self.port_version = port_version
        # The ports whose traffic is filtered out by the filtering policies for UDP reflection attacks.
        self.reflect_block_udp_port_list = reflect_block_udp_port_list
        # The countries in the location blacklist.
        self.region_block_country_list = region_block_country_list
        # The provinces in the location blacklist.
        self.region_block_province_list = region_block_province_list
        # The source IP addresses that are added to the blacklist.
        self.source_block_list = source_block_list
        # The settings for source rate limiting.
        self.source_limit = source_limit
        # Indicates whether back-to-origin CIDR blocks of Anti-DDoS Proxy are added to the whitelist.
        self.whiten_gfbr_nets = whiten_gfbr_nets

    def validate(self):
        if self.finger_print_rule_list:
            for v1 in self.finger_print_rule_list:
                 if v1:
                    v1.validate()
        if self.l_4rule_list:
            for v1 in self.l_4rule_list:
                 if v1:
                    v1.validate()
        if self.port_rule_list:
            for v1 in self.port_rule_list:
                 if v1:
                    v1.validate()
        if self.source_block_list:
            for v1 in self.source_block_list:
                 if v1:
                    v1.validate()
        if self.source_limit:
            self.source_limit.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.black_ip_list_expire_at is not None:
            result['BlackIpListExpireAt'] = self.black_ip_list_expire_at

        if self.enable_drop_icmp is not None:
            result['EnableDropIcmp'] = self.enable_drop_icmp

        if self.enable_intelligence is not None:
            result['EnableIntelligence'] = self.enable_intelligence

        if self.enable_l4defense is not None:
            result['EnableL4Defense'] = self.enable_l4defense

        result['FingerPrintRuleList'] = []
        if self.finger_print_rule_list is not None:
            for k1 in self.finger_print_rule_list:
                result['FingerPrintRuleList'].append(k1.to_map() if k1 else None)

        if self.intelligence_level is not None:
            result['IntelligenceLevel'] = self.intelligence_level

        result['L4RuleList'] = []
        if self.l_4rule_list is not None:
            for k1 in self.l_4rule_list:
                result['L4RuleList'].append(k1.to_map() if k1 else None)

        result['PortRuleList'] = []
        if self.port_rule_list is not None:
            for k1 in self.port_rule_list:
                result['PortRuleList'].append(k1.to_map() if k1 else None)

        if self.port_version is not None:
            result['PortVersion'] = self.port_version

        if self.reflect_block_udp_port_list is not None:
            result['ReflectBlockUdpPortList'] = self.reflect_block_udp_port_list

        if self.region_block_country_list is not None:
            result['RegionBlockCountryList'] = self.region_block_country_list

        if self.region_block_province_list is not None:
            result['RegionBlockProvinceList'] = self.region_block_province_list

        result['SourceBlockList'] = []
        if self.source_block_list is not None:
            for k1 in self.source_block_list:
                result['SourceBlockList'].append(k1.to_map() if k1 else None)

        if self.source_limit is not None:
            result['SourceLimit'] = self.source_limit.to_map()

        if self.whiten_gfbr_nets is not None:
            result['WhitenGfbrNets'] = self.whiten_gfbr_nets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlackIpListExpireAt') is not None:
            self.black_ip_list_expire_at = m.get('BlackIpListExpireAt')

        if m.get('EnableDropIcmp') is not None:
            self.enable_drop_icmp = m.get('EnableDropIcmp')

        if m.get('EnableIntelligence') is not None:
            self.enable_intelligence = m.get('EnableIntelligence')

        if m.get('EnableL4Defense') is not None:
            self.enable_l4defense = m.get('EnableL4Defense')

        self.finger_print_rule_list = []
        if m.get('FingerPrintRuleList') is not None:
            for k1 in m.get('FingerPrintRuleList'):
                temp_model = main_models.ListPolicyResponseBodyPolicyListContentFingerPrintRuleList()
                self.finger_print_rule_list.append(temp_model.from_map(k1))

        if m.get('IntelligenceLevel') is not None:
            self.intelligence_level = m.get('IntelligenceLevel')

        self.l_4rule_list = []
        if m.get('L4RuleList') is not None:
            for k1 in m.get('L4RuleList'):
                temp_model = main_models.ListPolicyResponseBodyPolicyListContentL4RuleList()
                self.l_4rule_list.append(temp_model.from_map(k1))

        self.port_rule_list = []
        if m.get('PortRuleList') is not None:
            for k1 in m.get('PortRuleList'):
                temp_model = main_models.ListPolicyResponseBodyPolicyListContentPortRuleList()
                self.port_rule_list.append(temp_model.from_map(k1))

        if m.get('PortVersion') is not None:
            self.port_version = m.get('PortVersion')

        if m.get('ReflectBlockUdpPortList') is not None:
            self.reflect_block_udp_port_list = m.get('ReflectBlockUdpPortList')

        if m.get('RegionBlockCountryList') is not None:
            self.region_block_country_list = m.get('RegionBlockCountryList')

        if m.get('RegionBlockProvinceList') is not None:
            self.region_block_province_list = m.get('RegionBlockProvinceList')

        self.source_block_list = []
        if m.get('SourceBlockList') is not None:
            for k1 in m.get('SourceBlockList'):
                temp_model = main_models.ListPolicyResponseBodyPolicyListContentSourceBlockList()
                self.source_block_list.append(temp_model.from_map(k1))

        if m.get('SourceLimit') is not None:
            temp_model = main_models.ListPolicyResponseBodyPolicyListContentSourceLimit()
            self.source_limit = temp_model.from_map(m.get('SourceLimit'))

        if m.get('WhitenGfbrNets') is not None:
            self.whiten_gfbr_nets = m.get('WhitenGfbrNets')

        return self

class ListPolicyResponseBodyPolicyListContentSourceLimit(DaraModel):
    def __init__(
        self,
        bps: int = None,
        pps: int = None,
        syn_bps: int = None,
        syn_pps: int = None,
    ):
        # The bandwidth limit on source IP addresses. Unit: bytes per second.
        self.bps = bps
        # The packets per second (PPS) limit on source IP addresses.
        self.pps = pps
        # The bandwidth limit on source SYN packets. Unit: bytes per second.
        self.syn_bps = syn_bps
        # The PPS limit on source SYN packets.
        self.syn_pps = syn_pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bps is not None:
            result['Bps'] = self.bps

        if self.pps is not None:
            result['Pps'] = self.pps

        if self.syn_bps is not None:
            result['SynBps'] = self.syn_bps

        if self.syn_pps is not None:
            result['SynPps'] = self.syn_pps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bps') is not None:
            self.bps = m.get('Bps')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        if m.get('SynBps') is not None:
            self.syn_bps = m.get('SynBps')

        if m.get('SynPps') is not None:
            self.syn_pps = m.get('SynPps')

        return self

class ListPolicyResponseBodyPolicyListContentSourceBlockList(DaraModel):
    def __init__(
        self,
        block_expire_seconds: int = None,
        every_seconds: int = None,
        exceed_limit_times: int = None,
        type: int = None,
    ):
        # The validity period of the blacklist to which the source IP address is added. Unit: seconds.
        self.block_expire_seconds = block_expire_seconds
        # The statistical period during which the system collects data on source IP addresses to determine whether to add the source IP addresses to the blacklist. Unit: seconds.
        self.every_seconds = every_seconds
        # The number of times that the source IP address exceeds a limit in a statistical period.
        self.exceed_limit_times = exceed_limit_times
        # The type of the source rate limit. Valid values:
        # 
        # *   **3**: the PPS limit on source IP addresses.
        # *   **4**: the bandwidth limit on source IP addresses.
        # *   **5**: the PPS limit on source SYN packets.
        # *   **6**: the bandwidth limit on source SYN packets.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block_expire_seconds is not None:
            result['BlockExpireSeconds'] = self.block_expire_seconds

        if self.every_seconds is not None:
            result['EverySeconds'] = self.every_seconds

        if self.exceed_limit_times is not None:
            result['ExceedLimitTimes'] = self.exceed_limit_times

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlockExpireSeconds') is not None:
            self.block_expire_seconds = m.get('BlockExpireSeconds')

        if m.get('EverySeconds') is not None:
            self.every_seconds = m.get('EverySeconds')

        if m.get('ExceedLimitTimes') is not None:
            self.exceed_limit_times = m.get('ExceedLimitTimes')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListPolicyResponseBodyPolicyListContentPortRuleList(DaraModel):
    def __init__(
        self,
        dst_port_end: int = None,
        dst_port_start: int = None,
        id: str = None,
        match_action: str = None,
        protocol: str = None,
        seq_no: int = None,
        src_port_end: int = None,
        src_port_start: int = None,
    ):
        # The end of the destination port range. Valid values: **0** to **65535**.
        self.dst_port_end = dst_port_end
        # The start of the destination port range. Valid values: **0** to **65535**.
        self.dst_port_start = dst_port_start
        # The ID of the rule.
        self.id = id
        # The action triggered if the rule is matched. Valid value:
        # 
        # *   **drop**: The traffic is discarded.
        self.match_action = match_action
        # The protocol type. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.protocol = protocol
        # The sequence number that indicates the order for the rule to take effect. The value is an integer.
        self.seq_no = seq_no
        # The end of the source port range. Valid values: **0** to **65535**.
        self.src_port_end = src_port_end
        # The start of the source port range. Valid values: **0** to **65535**.
        self.src_port_start = src_port_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_port_end is not None:
            result['DstPortEnd'] = self.dst_port_end

        if self.dst_port_start is not None:
            result['DstPortStart'] = self.dst_port_start

        if self.id is not None:
            result['Id'] = self.id

        if self.match_action is not None:
            result['MatchAction'] = self.match_action

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.seq_no is not None:
            result['SeqNo'] = self.seq_no

        if self.src_port_end is not None:
            result['SrcPortEnd'] = self.src_port_end

        if self.src_port_start is not None:
            result['SrcPortStart'] = self.src_port_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPortEnd') is not None:
            self.dst_port_end = m.get('DstPortEnd')

        if m.get('DstPortStart') is not None:
            self.dst_port_start = m.get('DstPortStart')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchAction') is not None:
            self.match_action = m.get('MatchAction')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('SeqNo') is not None:
            self.seq_no = m.get('SeqNo')

        if m.get('SrcPortEnd') is not None:
            self.src_port_end = m.get('SrcPortEnd')

        if m.get('SrcPortStart') is not None:
            self.src_port_start = m.get('SrcPortStart')

        return self

class ListPolicyResponseBodyPolicyListContentL4RuleList(DaraModel):
    def __init__(
        self,
        action: str = None,
        condition_list: List[main_models.ListPolicyResponseBodyPolicyListContentL4RuleListConditionList] = None,
        limited: int = None,
        match: str = None,
        method: str = None,
        name: str = None,
        priority: int = None,
    ):
        # The action that is specified in the rule. Valid value:
        # 
        # *   **2**: The traffic is discarded.
        self.action = action
        # The match conditions.
        self.condition_list = condition_list
        # The minimum number of bytes in a session to trigger matching. Valid values: **0** to **2048**.
        self.limited = limited
        # The condition based on which an action is performed. Valid values:
        # 
        # *   **0**: If the rule is matched, the action specified in the rule is performed.
        # *   **1**: If the rule is not matched, the action specified in the rule is performed.
        self.match = match
        # The type of the rule. Valid values:
        # 
        # *   **char**: string match.
        # *   **hex**: hexadecimal string match.
        self.method = method
        # The name of the rule.
        self.name = name
        # The priority of the rule.
        self.priority = priority

    def validate(self):
        if self.condition_list:
            for v1 in self.condition_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['ConditionList'] = []
        if self.condition_list is not None:
            for k1 in self.condition_list:
                result['ConditionList'].append(k1.to_map() if k1 else None)

        if self.limited is not None:
            result['Limited'] = self.limited

        if self.match is not None:
            result['Match'] = self.match

        if self.method is not None:
            result['Method'] = self.method

        if self.name is not None:
            result['Name'] = self.name

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.condition_list = []
        if m.get('ConditionList') is not None:
            for k1 in m.get('ConditionList'):
                temp_model = main_models.ListPolicyResponseBodyPolicyListContentL4RuleListConditionList()
                self.condition_list.append(temp_model.from_map(k1))

        if m.get('Limited') is not None:
            self.limited = m.get('Limited')

        if m.get('Match') is not None:
            self.match = m.get('Match')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class ListPolicyResponseBodyPolicyListContentL4RuleListConditionList(DaraModel):
    def __init__(
        self,
        arg: str = None,
        content: str = None,
        depth: int = None,
        encode: str = None,
        offset: main_models.ListPolicyResponseBodyPolicyListContentL4RuleListConditionListOffset = None,
        pattern: str = None,
        position: int = None,
    ):
        # The term that is used for matching.
        # 
        # >  If Method is set to **char**, the value of this parameter must be ASCII strings. If Method is set to **hex**, the value of this parameter must be hexadecimal strings. Maximum length: 2,048.
        self.arg = arg
        self.content = content
        # The number of bytes from the start position for matching. Valid values: **1** to **2048**.
        self.depth = depth
        self.encode = encode
        self.offset = offset
        self.pattern = pattern
        # The start position for matching. Valid values: **0** to **2047**.
        self.position = position

    def validate(self):
        if self.offset:
            self.offset.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arg is not None:
            result['Arg'] = self.arg

        if self.content is not None:
            result['Content'] = self.content

        if self.depth is not None:
            result['Depth'] = self.depth

        if self.encode is not None:
            result['Encode'] = self.encode

        if self.offset is not None:
            result['Offset'] = self.offset.to_map()

        if self.pattern is not None:
            result['Pattern'] = self.pattern

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arg') is not None:
            self.arg = m.get('Arg')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Depth') is not None:
            self.depth = m.get('Depth')

        if m.get('Encode') is not None:
            self.encode = m.get('Encode')

        if m.get('Offset') is not None:
            temp_model = main_models.ListPolicyResponseBodyPolicyListContentL4RuleListConditionListOffset()
            self.offset = temp_model.from_map(m.get('Offset'))

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class ListPolicyResponseBodyPolicyListContentL4RuleListConditionListOffset(DaraModel):
    def __init__(
        self,
        end: int = None,
        start: int = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class ListPolicyResponseBodyPolicyListContentFingerPrintRuleList(DaraModel):
    def __init__(
        self,
        dst_port_end: int = None,
        dst_port_start: int = None,
        id: str = None,
        match_action: str = None,
        max_pkt_len: int = None,
        min_pkt_len: int = None,
        offset: int = None,
        payload_bytes: str = None,
        protocol: str = None,
        rate_value: int = None,
        seq_no: int = None,
        src_port_end: int = None,
        src_port_start: int = None,
    ):
        # The end of the destination port range. Valid values: **0** to **65535**.
        self.dst_port_end = dst_port_end
        # The start of the destination port range. Valid values: **0** to **65535**.
        self.dst_port_start = dst_port_start
        # The ID of the rule.
        self.id = id
        # The action triggered if the rule is matched. Valid values:
        # 
        # *   **accept**: allows the traffic that matches the conditions in the byte-match filter rule.
        # *   **drop**: discards the traffic that matches the conditions in the byte-match filter rule.
        # *   **ip_rate**: limits rates on the source IP address whose traffic matches the conditions in the byte-match filter rule. The rate limit is specified by **RateValue**.
        # *   **session_rate**: limits the number of sessions from the source IP address whose traffic matches the conditions in the byte-match filter rule. The rate limit is specified by **RateValue**.
        self.match_action = match_action
        # The maximum packet length. Valid values: **1** to **1500**.
        self.max_pkt_len = max_pkt_len
        # The minimum packet length. Valid values: **1** to **1500**.
        self.min_pkt_len = min_pkt_len
        # The offset. Valid values: **0** to **1500**.
        self.offset = offset
        # The payload. The value is a hexadecimal string.
        self.payload_bytes = payload_bytes
        # The protocol type. Valid values:
        # 
        # *   **tcp**
        # *   **udp**
        self.protocol = protocol
        # The rate limit. Valid values: **1** to **100000**.
        # 
        # >  This parameter is required when **MatchAction** is set to **ip_rate** or **session_rate**.
        self.rate_value = rate_value
        # The sequence number that indicates the order for the rule to take effect. The value is an integer.
        self.seq_no = seq_no
        # The end of the source port range. Valid values: **0** to **65535**.
        self.src_port_end = src_port_end
        # The start of the source port range. Valid values: **0** to **65535**.
        self.src_port_start = src_port_start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dst_port_end is not None:
            result['DstPortEnd'] = self.dst_port_end

        if self.dst_port_start is not None:
            result['DstPortStart'] = self.dst_port_start

        if self.id is not None:
            result['Id'] = self.id

        if self.match_action is not None:
            result['MatchAction'] = self.match_action

        if self.max_pkt_len is not None:
            result['MaxPktLen'] = self.max_pkt_len

        if self.min_pkt_len is not None:
            result['MinPktLen'] = self.min_pkt_len

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.payload_bytes is not None:
            result['PayloadBytes'] = self.payload_bytes

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.rate_value is not None:
            result['RateValue'] = self.rate_value

        if self.seq_no is not None:
            result['SeqNo'] = self.seq_no

        if self.src_port_end is not None:
            result['SrcPortEnd'] = self.src_port_end

        if self.src_port_start is not None:
            result['SrcPortStart'] = self.src_port_start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstPortEnd') is not None:
            self.dst_port_end = m.get('DstPortEnd')

        if m.get('DstPortStart') is not None:
            self.dst_port_start = m.get('DstPortStart')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchAction') is not None:
            self.match_action = m.get('MatchAction')

        if m.get('MaxPktLen') is not None:
            self.max_pkt_len = m.get('MaxPktLen')

        if m.get('MinPktLen') is not None:
            self.min_pkt_len = m.get('MinPktLen')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('PayloadBytes') is not None:
            self.payload_bytes = m.get('PayloadBytes')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RateValue') is not None:
            self.rate_value = m.get('RateValue')

        if m.get('SeqNo') is not None:
            self.seq_no = m.get('SeqNo')

        if m.get('SrcPortEnd') is not None:
            self.src_port_end = m.get('SrcPortEnd')

        if m.get('SrcPortStart') is not None:
            self.src_port_start = m.get('SrcPortStart')

        return self

