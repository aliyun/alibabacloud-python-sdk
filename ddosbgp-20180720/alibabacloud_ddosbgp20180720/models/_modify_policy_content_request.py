# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddosbgp20180720 import models as main_models
from darabonba.model import DaraModel

class ModifyPolicyContentRequest(DaraModel):
    def __init__(
        self,
        content: main_models.ModifyPolicyContentRequestContent = None,
        id: str = None,
        name: str = None,
        port_version: str = None,
    ):
        # The policy content.
        self.content = content
        # The policy ID.
        # 
        # This parameter is required.
        self.id = id
        # The policy name.
        self.name = name
        # The version of the port-specific mitigation policy. Valid values:
        # 
        # - **Not specified**: modifies the default surf mitigation engine policy.
        # - **2**: modifies the new stream mitigation engine policy.
        # > Only port-specific mitigation policies are supported.
        self.port_version = port_version

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.port_version is not None:
            result['PortVersion'] = self.port_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.ModifyPolicyContentRequestContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PortVersion') is not None:
            self.port_version = m.get('PortVersion')

        return self

class ModifyPolicyContentRequestContent(DaraModel):
    def __init__(
        self,
        black_ip_list_expire_at: int = None,
        enable_drop_icmp: bool = None,
        enable_intelligence: bool = None,
        enable_l4defense: bool = None,
        finger_print_rule_list: List[main_models.ModifyPolicyContentRequestContentFingerPrintRuleList] = None,
        intelligence_level: str = None,
        l_4rule_list: List[main_models.ModifyPolicyContentRequestContentL4RuleList] = None,
        port_rule_list: List[main_models.ModifyPolicyContentRequestContentPortRuleList] = None,
        reflect_block_udp_port_list: List[int] = None,
        region_block_country_list: List[int] = None,
        region_block_province_list: List[int] = None,
        sip_defense: main_models.ModifyPolicyContentRequestContentSipDefense = None,
        source_block_list: List[main_models.ModifyPolicyContentRequestContentSourceBlockList] = None,
        source_limit: main_models.ModifyPolicyContentRequestContentSourceLimit = None,
        whiten_gfbr_nets: bool = None,
    ):
        # The expiration time of the IP blacklist (UNIX timestamp).
        self.black_ip_list_expire_at = black_ip_list_expire_at
        # Specifies whether to disable the ICMP protocol.
        self.enable_drop_icmp = enable_drop_icmp
        # Specifies whether to enable AI-based intelligent analysis.
        self.enable_intelligence = enable_intelligence
        # Specifies whether to enable port-specific mitigation.
        self.enable_l4defense = enable_l4defense
        # The list of Byte-Match Filter rules.
        self.finger_print_rule_list = finger_print_rule_list
        # The protection level of AI-based intelligent analysis. Valid values:
        # 
        # - **default**: Normal.
        # - **hard**: Strict.
        # - **weak**: Loose.
        self.intelligence_level = intelligence_level
        # The list of port-specific mitigation rules.
        self.l_4rule_list = l_4rule_list
        # The list of port blocking rules.
        self.port_rule_list = port_rule_list
        # The list of ports filtered by the reflection attack prevention feature.
        self.reflect_block_udp_port_list = reflect_block_udp_port_list
        # The list of countries for location blacklist.
        self.region_block_country_list = region_block_country_list
        # The list of provinces for location blacklist.
        self.region_block_province_list = region_block_province_list
        # The SIP Protection Settings.
        self.sip_defense = sip_defense
        # The source rate limiting blacklist.
        self.source_block_list = source_block_list
        # The source rate limiting configuration.
        self.source_limit = source_limit
        # Specifies whether to whitelist the back-to-origin IP addresses of Anti-DDoS Pro and Anti-DDoS Premium (the Chinese mainland and outside the Chinese mainland).
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
        if self.sip_defense:
            self.sip_defense.validate()
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

        if self.reflect_block_udp_port_list is not None:
            result['ReflectBlockUdpPortList'] = self.reflect_block_udp_port_list

        if self.region_block_country_list is not None:
            result['RegionBlockCountryList'] = self.region_block_country_list

        if self.region_block_province_list is not None:
            result['RegionBlockProvinceList'] = self.region_block_province_list

        if self.sip_defense is not None:
            result['SipDefense'] = self.sip_defense.to_map()

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
                temp_model = main_models.ModifyPolicyContentRequestContentFingerPrintRuleList()
                self.finger_print_rule_list.append(temp_model.from_map(k1))

        if m.get('IntelligenceLevel') is not None:
            self.intelligence_level = m.get('IntelligenceLevel')

        self.l_4rule_list = []
        if m.get('L4RuleList') is not None:
            for k1 in m.get('L4RuleList'):
                temp_model = main_models.ModifyPolicyContentRequestContentL4RuleList()
                self.l_4rule_list.append(temp_model.from_map(k1))

        self.port_rule_list = []
        if m.get('PortRuleList') is not None:
            for k1 in m.get('PortRuleList'):
                temp_model = main_models.ModifyPolicyContentRequestContentPortRuleList()
                self.port_rule_list.append(temp_model.from_map(k1))

        if m.get('ReflectBlockUdpPortList') is not None:
            self.reflect_block_udp_port_list = m.get('ReflectBlockUdpPortList')

        if m.get('RegionBlockCountryList') is not None:
            self.region_block_country_list = m.get('RegionBlockCountryList')

        if m.get('RegionBlockProvinceList') is not None:
            self.region_block_province_list = m.get('RegionBlockProvinceList')

        if m.get('SipDefense') is not None:
            temp_model = main_models.ModifyPolicyContentRequestContentSipDefense()
            self.sip_defense = temp_model.from_map(m.get('SipDefense'))

        self.source_block_list = []
        if m.get('SourceBlockList') is not None:
            for k1 in m.get('SourceBlockList'):
                temp_model = main_models.ModifyPolicyContentRequestContentSourceBlockList()
                self.source_block_list.append(temp_model.from_map(k1))

        if m.get('SourceLimit') is not None:
            temp_model = main_models.ModifyPolicyContentRequestContentSourceLimit()
            self.source_limit = temp_model.from_map(m.get('SourceLimit'))

        if m.get('WhitenGfbrNets') is not None:
            self.whiten_gfbr_nets = m.get('WhitenGfbrNets')

        return self

class ModifyPolicyContentRequestContentSourceLimit(DaraModel):
    def __init__(
        self,
        bps: int = None,
        pps: int = None,
        syn_bps: int = None,
        syn_pps: int = None,
    ):
        # The source bandwidth throttling value, in bytes per second (byte/s).
        self.bps = bps
        # The source PPS rate limit, in packets per second (packet/s).
        self.pps = pps
        # The source SYN bandwidth throttling value, in bytes per second (byte/s).
        self.syn_bps = syn_bps
        # The source SYN PPS rate limit, in packets per second (packet/s).
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

class ModifyPolicyContentRequestContentSourceBlockList(DaraModel):
    def __init__(
        self,
        block_expire_seconds: int = None,
        every_seconds: int = None,
        exceed_limit_times: int = None,
        type: int = None,
    ):
        # The duration for which the source IP address is added to the blacklist. Unit: seconds.
        # 
        # This parameter is required.
        self.block_expire_seconds = block_expire_seconds
        # The statistical period for source rate limiting blacklisting. Unit: seconds.
        # 
        # This parameter is required.
        self.every_seconds = every_seconds
        # The number of times the source IP address exceeds the rate limit within one statistical period.
        # 
        # This parameter is required.
        self.exceed_limit_times = exceed_limit_times
        # The source rate limiting type. Valid values:
        # - **3**: Source PPS rate limiting.
        # - **4**: Source bandwidth throttling.
        # - **5**: Source SYN PPS rate limiting.
        # - **6**: Source SYN bandwidth throttling.
        # 
        # This parameter is required.
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

class ModifyPolicyContentRequestContentSipDefense(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        level: str = None,
        sip_defend: bool = None,
        sip_learn: bool = None,
        sip_module: bool = None,
        sip_port: str = None,
        sip_rate: int = None,
        sip_start_mbps: int = None,
        sip_start_pps: int = None,
    ):
        # Specifies whether to enable SIP protection. Valid values:
        # 
        # - **true**: Enabled.
        # - **false**: Disabled.
        self.enable = enable
        # The SIP protection level.
        self.level = level
        # Specifies whether to enable SIP defense mode.
        self.sip_defend = sip_defend
        # Specifies whether to enable SIP learning mode.
        self.sip_learn = sip_learn
        # Specifies whether to enable the SIP source rate limiting module.
        self.sip_module = sip_module
        # The SIP protection port. Valid values: **1** to **65535**.
        self.sip_port = sip_port
        # The SIP source rate limit (PPS).
        self.sip_rate = sip_rate
        # The SIP activation threshold (Mbps).
        self.sip_start_mbps = sip_start_mbps
        # The SIP activation threshold (PPS).
        self.sip_start_pps = sip_start_pps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        if self.level is not None:
            result['Level'] = self.level

        if self.sip_defend is not None:
            result['SipDefend'] = self.sip_defend

        if self.sip_learn is not None:
            result['SipLearn'] = self.sip_learn

        if self.sip_module is not None:
            result['SipModule'] = self.sip_module

        if self.sip_port is not None:
            result['SipPort'] = self.sip_port

        if self.sip_rate is not None:
            result['SipRate'] = self.sip_rate

        if self.sip_start_mbps is not None:
            result['SipStartMbps'] = self.sip_start_mbps

        if self.sip_start_pps is not None:
            result['SipStartPps'] = self.sip_start_pps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('SipDefend') is not None:
            self.sip_defend = m.get('SipDefend')

        if m.get('SipLearn') is not None:
            self.sip_learn = m.get('SipLearn')

        if m.get('SipModule') is not None:
            self.sip_module = m.get('SipModule')

        if m.get('SipPort') is not None:
            self.sip_port = m.get('SipPort')

        if m.get('SipRate') is not None:
            self.sip_rate = m.get('SipRate')

        if m.get('SipStartMbps') is not None:
            self.sip_start_mbps = m.get('SipStartMbps')

        if m.get('SipStartPps') is not None:
            self.sip_start_pps = m.get('SipStartPps')

        return self

class ModifyPolicyContentRequestContentPortRuleList(DaraModel):
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
        # The end value of the destination port range. Valid values: **0** to **65535**.
        # 
        # This parameter is required.
        self.dst_port_end = dst_port_end
        # The start value of the destination port range. Valid values: **0** to **65535**.
        # 
        # This parameter is required.
        self.dst_port_start = dst_port_start
        # The rule ID.
        self.id = id
        # The match action. Valid values:
        # 
        # - **drop**: Drop.
        # 
        # This parameter is required.
        self.match_action = match_action
        # The protocol type. Valid values:
        # 
        # - **tcp**: Transmission Control Protocol.
        # - **udp**: User Datagram Protocol.
        # 
        # This parameter is required.
        self.protocol = protocol
        # The priority of the rule, represented as an integer.
        # >A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.seq_no = seq_no
        # The end value of the source port range. Valid values: **0** to **65535**.
        # 
        # This parameter is required.
        self.src_port_end = src_port_end
        # The start value of the source port range. Valid values: **0** to **65535**.
        # 
        # This parameter is required.
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

class ModifyPolicyContentRequestContentL4RuleList(DaraModel):
    def __init__(
        self,
        action: str = None,
        condition_list: List[main_models.ModifyPolicyContentRequestContentL4RuleListConditionList] = None,
        limited: int = None,
        match: str = None,
        method: str = None,
        name: str = None,
        priority: int = None,
    ):
        # The action.
        self.action = action
        # The list of detection conditions.
        self.condition_list = condition_list
        # The minimum number of bytes in a session flow to trigger rule matching. Valid values: **0** to **2048**.
        self.limited = limited
        # The logical operator. Valid values:
        # 
        # - **0**: executes the action when the rule is matched.
        # 
        # - **1**: executes the action when the rule is not matched.
        self.match = match
        # The rule type. Valid values:
        # 
        # - **char**: string matching.
        # 
        # - **hex**: hexadecimal matching.
        self.method = method
        # The rule name.
        # 
        # This parameter is required.
        self.name = name
        # The rule priority. Valid values: 1 to 100.
        # > A smaller value indicates a higher priority.
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
                temp_model = main_models.ModifyPolicyContentRequestContentL4RuleListConditionList()
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

class ModifyPolicyContentRequestContentL4RuleListConditionList(DaraModel):
    def __init__(
        self,
        arg: str = None,
        content: str = None,
        depth: int = None,
        encode: str = None,
        offset: main_models.ModifyPolicyContentRequestContentL4RuleListConditionListOffset = None,
        pattern: str = None,
        position: int = None,
    ):
        # The detection content.
        # > If the rule type is **char**, the value must be an ASCII string. If the rule type is **hex**, the value must be a hexadecimal string. Maximum length: 2048.
        self.arg = arg
        # The matching content.
        # 
        # 1. When **Encode** is set to **str**, the following requirements must be met:
        # 
        # - The length of **Content** must not exceed 1500.
        # 
        # - **End** - **Start** >= length of **Content**.
        # 
        # 2. When **Encode** is set to **hex**, the following requirements must be met:
        # 
        # - **Content** must be hexadecimal characters.
        # 
        # - The length of **Content** must be an even number.
        # 
        # - The length of **Content** must not exceed 3000.
        # 
        # - **End** - **Start** + 1 >= length of **Content** / 2.
        self.content = content
        # The detection window length. Valid values: **1** to **2048**.
        self.depth = depth
        # The character type. Valid values:
        # 
        # - **str**: string.
        # 
        # - **hex**: hexadecimal.
        self.encode = encode
        # The matching range.
        self.offset = offset
        # The matching pattern. Valid values:
        # 
        # - **contain**: contains.
        # 
        # - **not_contain**: does not contain.
        self.pattern = pattern
        # The detection start position. Valid values: **0** to **2047**.
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
            temp_model = main_models.ModifyPolicyContentRequestContentL4RuleListConditionListOffset()
            self.offset = temp_model.from_map(m.get('Offset'))

        if m.get('Pattern') is not None:
            self.pattern = m.get('Pattern')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

class ModifyPolicyContentRequestContentL4RuleListConditionListOffset(DaraModel):
    def __init__(
        self,
        end: int = None,
        start: int = None,
    ):
        # The end position. Valid values: **0** to **1499**.
        # 
        # > The end position must be greater than or equal to the start position.
        self.end = end
        # The start position. Valid values: **0** to **1499**.
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

class ModifyPolicyContentRequestContentFingerPrintRuleList(DaraModel):
    def __init__(
        self,
        comment: str = None,
        dst_port_end: int = None,
        dst_port_start: int = None,
        id: str = None,
        match_action: str = None,
        max_pkt_len: int = None,
        min_pkt_len: int = None,
        mode: int = None,
        offset: int = None,
        payload_bytes: str = None,
        protocol: str = None,
        rate_value: int = None,
        rule: str = None,
        seq_no: int = None,
        src_port_end: int = None,
        src_port_start: int = None,
        type: int = None,
    ):
        # The rule comment.
        self.comment = comment
        # The end value of the destination port range. Valid values: **0** to **65535**.
        self.dst_port_end = dst_port_end
        # The start value of the destination port range. Valid values: **0** to **65535**.
        self.dst_port_start = dst_port_start
        # The rule ID.
        self.id = id
        # The action to take when the fingerprint is matched. Valid values:
        # 
        # - **permit**: allows traffic that matches the fingerprint.
        # - **drop**: drops traffic that matches the fingerprint.
        # - **ip_rate**: rate-limits the source IP address of traffic that matches the fingerprint. The rate limit is specified by the **RateValue** parameter.
        # - **session_rate**: rate-limits the source session of traffic that matches the fingerprint. The rate limit is specified by the **RateValue** parameter.
        # 
        # This parameter is required.
        self.match_action = match_action
        # The maximum packet length. Valid values: **1** to **1500**.
        self.max_pkt_len = max_pkt_len
        # The minimum packet length. Valid values: **1** to **1500**.
        self.min_pkt_len = min_pkt_len
        # The rule mode.
        self.mode = mode
        # The offset. Valid values: **0** to **1500**.
        self.offset = offset
        # The detection payload. The value is in hexadecimal string format.
        self.payload_bytes = payload_bytes
        # The protocol type. Valid values:
        # 
        # - **tcp**: Transmission Control Protocol.
        # - **udp**: User Datagram Protocol.
        self.protocol = protocol
        # The rate limit. Valid values: **1** to **100000**.
        # 
        # > This parameter is required when the match action is source IP rate limiting or source session rate limiting (**MatchAction** is set to **ip_rate** or **session_rate**).
        self.rate_value = rate_value
        # The rule.
        self.rule = rule
        # The priority of the rule, represented as an integer.
        # >A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.seq_no = seq_no
        # The end value of the source port range. Valid values: **0** to **65535**.
        self.src_port_end = src_port_end
        # The start value of the source port range. Valid values: **0** to **65535**.
        self.src_port_start = src_port_start
        # The type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

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

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.payload_bytes is not None:
            result['PayloadBytes'] = self.payload_bytes

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.rate_value is not None:
            result['RateValue'] = self.rate_value

        if self.rule is not None:
            result['Rule'] = self.rule

        if self.seq_no is not None:
            result['SeqNo'] = self.seq_no

        if self.src_port_end is not None:
            result['SrcPortEnd'] = self.src_port_end

        if self.src_port_start is not None:
            result['SrcPortStart'] = self.src_port_start

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

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

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('PayloadBytes') is not None:
            self.payload_bytes = m.get('PayloadBytes')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RateValue') is not None:
            self.rate_value = m.get('RateValue')

        if m.get('Rule') is not None:
            self.rule = m.get('Rule')

        if m.get('SeqNo') is not None:
            self.seq_no = m.get('SeqNo')

        if m.get('SrcPortEnd') is not None:
            self.src_port_end = m.get('SrcPortEnd')

        if m.get('SrcPortStart') is not None:
            self.src_port_start = m.get('SrcPortStart')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

