# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeTrafficLogRequest(DaraModel):
    def __init__(
        self,
        acl_pre_rule_id: str = None,
        acl_pre_state: str = None,
        app_dpi_state: str = None,
        app_id: str = None,
        asset_region: str = None,
        attack_type: str = None,
        current_page: str = None,
        direction: str = None,
        domain_name: str = None,
        domain_url: str = None,
        dst_ip: str = None,
        dst_port: str = None,
        dst_vpc_id: str = None,
        dst_vpc_region_no: str = None,
        end_time: str = None,
        firewall_type: str = None,
        flow_type: str = None,
        ip_protocol: str = None,
        ip_version: str = None,
        isp: str = None,
        lang: str = None,
        location: str = None,
        member_uid: int = None,
        nat_firewall_id: str = None,
        nat_gateway_id: str = None,
        page_size: str = None,
        rule_id: str = None,
        rule_result: str = None,
        rule_source: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        src_port: str = None,
        src_private_ip: str = None,
        src_vpc_id: str = None,
        src_vpc_region_no: str = None,
        start_time: str = None,
        tls_scope_id: str = None,
        vpc_firewall_id: str = None,
        vul_level: str = None,
    ):
        self.acl_pre_rule_id = acl_pre_rule_id
        self.acl_pre_state = acl_pre_state
        self.app_dpi_state = app_dpi_state
        self.app_id = app_id
        self.asset_region = asset_region
        self.attack_type = attack_type
        self.current_page = current_page
        self.direction = direction
        self.domain_name = domain_name
        self.domain_url = domain_url
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.dst_vpc_id = dst_vpc_id
        self.dst_vpc_region_no = dst_vpc_region_no
        # This parameter is required.
        self.end_time = end_time
        self.firewall_type = firewall_type
        self.flow_type = flow_type
        self.ip_protocol = ip_protocol
        self.ip_version = ip_version
        self.isp = isp
        self.lang = lang
        self.location = location
        self.member_uid = member_uid
        self.nat_firewall_id = nat_firewall_id
        self.nat_gateway_id = nat_gateway_id
        self.page_size = page_size
        self.rule_id = rule_id
        self.rule_result = rule_result
        self.rule_source = rule_source
        # This parameter is required.
        self.source_code = source_code
        self.source_ip = source_ip
        self.src_ip = src_ip
        self.src_port = src_port
        self.src_private_ip = src_private_ip
        self.src_vpc_id = src_vpc_id
        self.src_vpc_region_no = src_vpc_region_no
        # This parameter is required.
        self.start_time = start_time
        self.tls_scope_id = tls_scope_id
        self.vpc_firewall_id = vpc_firewall_id
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_pre_rule_id is not None:
            result['AclPreRuleId'] = self.acl_pre_rule_id

        if self.acl_pre_state is not None:
            result['AclPreState'] = self.acl_pre_state

        if self.app_dpi_state is not None:
            result['AppDpiState'] = self.app_dpi_state

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.asset_region is not None:
            result['AssetRegion'] = self.asset_region

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

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

        if self.dst_vpc_id is not None:
            result['DstVpcId'] = self.dst_vpc_id

        if self.dst_vpc_region_no is not None:
            result['DstVpcRegionNo'] = self.dst_vpc_region_no

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.location is not None:
            result['Location'] = self.location

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.nat_firewall_id is not None:
            result['NatFirewallId'] = self.nat_firewall_id

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result

        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.src_port is not None:
            result['SrcPort'] = self.src_port

        if self.src_private_ip is not None:
            result['SrcPrivateIP'] = self.src_private_ip

        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id

        if self.src_vpc_region_no is not None:
            result['SrcVpcRegionNo'] = self.src_vpc_region_no

        if self.start_time is not None:
            result['StartTime'] = self.start_time

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

        if m.get('AclPreState') is not None:
            self.acl_pre_state = m.get('AclPreState')

        if m.get('AppDpiState') is not None:
            self.app_dpi_state = m.get('AppDpiState')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AssetRegion') is not None:
            self.asset_region = m.get('AssetRegion')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

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

        if m.get('DstVpcId') is not None:
            self.dst_vpc_id = m.get('DstVpcId')

        if m.get('DstVpcRegionNo') is not None:
            self.dst_vpc_region_no = m.get('DstVpcRegionNo')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NatFirewallId') is not None:
            self.nat_firewall_id = m.get('NatFirewallId')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')

        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SrcPort') is not None:
            self.src_port = m.get('SrcPort')

        if m.get('SrcPrivateIP') is not None:
            self.src_private_ip = m.get('SrcPrivateIP')

        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')

        if m.get('SrcVpcRegionNo') is not None:
            self.src_vpc_region_no = m.get('SrcVpcRegionNo')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TlsScopeId') is not None:
            self.tls_scope_id = m.get('TlsScopeId')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        return self

