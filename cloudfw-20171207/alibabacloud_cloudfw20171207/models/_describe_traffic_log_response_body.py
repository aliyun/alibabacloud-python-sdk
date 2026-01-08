# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeTrafficLogResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeTrafficLogResponseBodyDataList] = None,
        page_info: main_models.DescribeTrafficLogResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        self.data_list = data_list
        self.page_info = page_info
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeTrafficLogResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeTrafficLogResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTrafficLogResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTrafficLogResponseBodyDataList(DaraModel):
    def __init__(
        self,
        acl_pre_rule_id: str = None,
        acl_pre_rule_name: str = None,
        acl_pre_state: str = None,
        app_dpi_state: str = None,
        app_id: int = None,
        app_name: str = None,
        attack_app: str = None,
        attack_type: int = None,
        city_id: str = None,
        close_reason: str = None,
        cloud_instance_id: str = None,
        country_id: str = None,
        direction: str = None,
        domain_name: str = None,
        domain_url: str = None,
        dst_ip: str = None,
        dst_port: int = None,
        dst_vpc: main_models.DescribeTrafficLogResponseBodyDataListDstVpc = None,
        end_time: int = None,
        ext: str = None,
        in_bytes: str = None,
        in_packets: str = None,
        ip_protocol: str = None,
        isp: str = None,
        isp_id: str = None,
        location: str = None,
        member_uid: str = None,
        out_bytes: str = None,
        out_packets: str = None,
        packet_bytes: int = None,
        packet_count: int = None,
        private_ip: str = None,
        private_port: int = None,
        region_id: str = None,
        rule_id: str = None,
        rule_name: str = None,
        rule_result: int = None,
        rule_source: str = None,
        rules: List[main_models.DescribeTrafficLogResponseBodyDataListRules] = None,
        src_ip: str = None,
        src_port: int = None,
        src_private_ip: str = None,
        src_vpc: main_models.DescribeTrafficLogResponseBodyDataListSrcVpc = None,
        start_time: int = None,
        tls_rule_id: str = None,
        tls_rule_name: str = None,
        tls_scope_id: str = None,
        vpc_firewall_id: str = None,
        vul_level: int = None,
    ):
        self.acl_pre_rule_id = acl_pre_rule_id
        self.acl_pre_rule_name = acl_pre_rule_name
        self.acl_pre_state = acl_pre_state
        self.app_dpi_state = app_dpi_state
        self.app_id = app_id
        self.app_name = app_name
        self.attack_app = attack_app
        self.attack_type = attack_type
        self.city_id = city_id
        self.close_reason = close_reason
        self.cloud_instance_id = cloud_instance_id
        self.country_id = country_id
        self.direction = direction
        self.domain_name = domain_name
        self.domain_url = domain_url
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.dst_vpc = dst_vpc
        self.end_time = end_time
        self.ext = ext
        self.in_bytes = in_bytes
        self.in_packets = in_packets
        self.ip_protocol = ip_protocol
        self.isp = isp
        self.isp_id = isp_id
        self.location = location
        self.member_uid = member_uid
        self.out_bytes = out_bytes
        self.out_packets = out_packets
        self.packet_bytes = packet_bytes
        self.packet_count = packet_count
        self.private_ip = private_ip
        self.private_port = private_port
        self.region_id = region_id
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.rule_result = rule_result
        self.rule_source = rule_source
        self.rules = rules
        self.src_ip = src_ip
        self.src_port = src_port
        self.src_private_ip = src_private_ip
        self.src_vpc = src_vpc
        self.start_time = start_time
        self.tls_rule_id = tls_rule_id
        self.tls_rule_name = tls_rule_name
        self.tls_scope_id = tls_scope_id
        self.vpc_firewall_id = vpc_firewall_id
        self.vul_level = vul_level

    def validate(self):
        if self.dst_vpc:
            self.dst_vpc.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.src_vpc:
            self.src_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_pre_rule_id is not None:
            result['AclPreRuleId'] = self.acl_pre_rule_id

        if self.acl_pre_rule_name is not None:
            result['AclPreRuleName'] = self.acl_pre_rule_name

        if self.acl_pre_state is not None:
            result['AclPreState'] = self.acl_pre_state

        if self.app_dpi_state is not None:
            result['AppDpiState'] = self.app_dpi_state

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.city_id is not None:
            result['CityId'] = self.city_id

        if self.close_reason is not None:
            result['CloseReason'] = self.close_reason

        if self.cloud_instance_id is not None:
            result['CloudInstanceId'] = self.cloud_instance_id

        if self.country_id is not None:
            result['CountryId'] = self.country_id

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.domain_url is not None:
            result['DomainUrl'] = self.domain_url

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.dst_vpc is not None:
            result['DstVpc'] = self.dst_vpc.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ext is not None:
            result['Ext'] = self.ext

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.in_packets is not None:
            result['InPackets'] = self.in_packets

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.isp_id is not None:
            result['IspId'] = self.isp_id

        if self.location is not None:
            result['Location'] = self.location

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.out_packets is not None:
            result['OutPackets'] = self.out_packets

        if self.packet_bytes is not None:
            result['PacketBytes'] = self.packet_bytes

        if self.packet_count is not None:
            result['PacketCount'] = self.packet_count

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.private_port is not None:
            result['PrivatePort'] = self.private_port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result

        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.src_port is not None:
            result['SrcPort'] = self.src_port

        if self.src_private_ip is not None:
            result['SrcPrivateIP'] = self.src_private_ip

        if self.src_vpc is not None:
            result['SrcVpc'] = self.src_vpc.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tls_rule_id is not None:
            result['TlsRuleId'] = self.tls_rule_id

        if self.tls_rule_name is not None:
            result['TlsRuleName'] = self.tls_rule_name

        if self.tls_scope_id is not None:
            result['TlsScopeId'] = self.tls_scope_id

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclPreRuleId') is not None:
            self.acl_pre_rule_id = m.get('AclPreRuleId')

        if m.get('AclPreRuleName') is not None:
            self.acl_pre_rule_name = m.get('AclPreRuleName')

        if m.get('AclPreState') is not None:
            self.acl_pre_state = m.get('AclPreState')

        if m.get('AppDpiState') is not None:
            self.app_dpi_state = m.get('AppDpiState')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('CityId') is not None:
            self.city_id = m.get('CityId')

        if m.get('CloseReason') is not None:
            self.close_reason = m.get('CloseReason')

        if m.get('CloudInstanceId') is not None:
            self.cloud_instance_id = m.get('CloudInstanceId')

        if m.get('CountryId') is not None:
            self.country_id = m.get('CountryId')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('DomainUrl') is not None:
            self.domain_url = m.get('DomainUrl')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('DstVpc') is not None:
            temp_model = main_models.DescribeTrafficLogResponseBodyDataListDstVpc()
            self.dst_vpc = temp_model.from_map(m.get('DstVpc'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('InPackets') is not None:
            self.in_packets = m.get('InPackets')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('IspId') is not None:
            self.isp_id = m.get('IspId')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('OutPackets') is not None:
            self.out_packets = m.get('OutPackets')

        if m.get('PacketBytes') is not None:
            self.packet_bytes = m.get('PacketBytes')

        if m.get('PacketCount') is not None:
            self.packet_count = m.get('PacketCount')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('PrivatePort') is not None:
            self.private_port = m.get('PrivatePort')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')

        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeTrafficLogResponseBodyDataListRules()
                self.rules.append(temp_model.from_map(k1))

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')

        if m.get('SrcPrivateIP') is not None:
            self.src_private_ip = m.get('SrcPrivateIP')

        if m.get('SrcVpc') is not None:
            temp_model = main_models.DescribeTrafficLogResponseBodyDataListSrcVpc()
            self.src_vpc = temp_model.from_map(m.get('SrcVpc'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TlsRuleId') is not None:
            self.tls_rule_id = m.get('TlsRuleId')

        if m.get('TlsRuleName') is not None:
            self.tls_rule_name = m.get('TlsRuleName')

        if m.get('TlsScopeId') is not None:
            self.tls_scope_id = m.get('TlsScopeId')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        return self

class DescribeTrafficLogResponseBodyDataListSrcVpc(DaraModel):
    def __init__(
        self,
        region_no: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.region_no = region_no
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeTrafficLogResponseBodyDataListRules(DaraModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
    ):
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class DescribeTrafficLogResponseBodyDataListDstVpc(DaraModel):
    def __init__(
        self,
        region_no: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.region_no = region_no
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

