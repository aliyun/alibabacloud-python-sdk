# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRiskEventGroupRequest(DaraModel):
    def __init__(
        self,
        attack_app: List[str] = None,
        attack_app_category: List[str] = None,
        attack_type: str = None,
        buy_version: int = None,
        current_page: str = None,
        data_type: str = None,
        direction: str = None,
        dst_ip: str = None,
        dst_network_instance_id: str = None,
        end_time: str = None,
        event_name: str = None,
        firewall_type: str = None,
        is_only_private_assoc: str = None,
        lang: str = None,
        no_location: str = None,
        order: str = None,
        page_size: str = None,
        rule_result: str = None,
        rule_source: str = None,
        sort: str = None,
        src_ip: str = None,
        src_network_instance_id: str = None,
        start_time: str = None,
        vul_level: str = None,
    ):
        # A list of names of the attacked applications. Use the `["AttackApp1","AttackApp2"]` format.
        self.attack_app = attack_app
        # A list of categories of the attacked applications. Use the ["AttackAppCategory1","AttackAppCategory2"] format.
        self.attack_app_category = attack_app_category
        # The type of the attack. Valid values:
        # 
        # - **1**: abnormal connection
        # 
        # - **2**: command execution
        # 
        # - **3**: brute-force attack
        # 
        # - **4**: scan
        # 
        # - **5**: other
        # 
        # - **6**: information leakage
        # 
        # - **7**: DoS attack
        # 
        # - **8**: overflow attack
        # 
        # - **9**: web attack
        # 
        # - **10**: backdoor trojan
        # 
        # - **11**: virus or worm
        # 
        # - **12**: mining behavior
        # 
        # - **13**: reverse shell
        # 
        # > If you do not set this parameter, events of all attack types are queried.
        self.attack_type = attack_type
        # The edition of Cloud Firewall. Valid values:
        # 
        # - **2**: Premium Edition
        # 
        # - **3**: Enterprise Edition
        # 
        # - **4**: Ultimate Edition
        # 
        # - **10**: pay-as-you-go
        self.buy_version = buy_version
        # The page number of the returned data.
        # Default value: **1**.
        self.current_page = current_page
        # The type of the risk event.<br>
        # Set the value to **session**, which indicates intrusion prevention events.<br>
        # 
        # This parameter is required.
        self.data_type = data_type
        # The traffic direction of the intrusion prevention event. Valid values:
        # 
        # - **in**: inbound
        # 
        # - **out**: outbound
        # 
        # > If you do not set this parameter, events in all traffic directions are queried.
        self.direction = direction
        # The destination IP address to query. If you set this parameter, only intrusion prevention events that contain the specified destination IP address are queried.
        self.dst_ip = dst_ip
        # The ID of the destination VPC.
        # 
        # > This parameter is required only when \\`FirewallType\\` is set to \\`VpcFirewall\\`.
        self.dst_network_instance_id = dst_network_instance_id
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the intrusion prevention event.
        self.event_name = event_name
        # The type of the firewall. Valid values:
        # 
        # - **VpcFirewall**: VPC firewall
        # 
        # - **InternetFirewall** (default): Internet firewall
        self.firewall_type = firewall_type
        # Specifies whether to query only the data that is traced to private IP addresses.
        self.is_only_private_assoc = is_only_private_assoc
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # Specifies whether to query the IP address location information. Valid values:
        # 
        # - **true**: Does not query the IP geolocation information.
        # 
        # - **false** (default): Queries the IP geolocation information.
        self.no_location = no_location
        # The sorting order. Valid values:
        # 
        # - **asc**: ascending
        # 
        # - **desc** (default): descending
        self.order = order
        # The number of entries to return on each page.
        # 
        # Default value: **6**. Maximum value: **10**.
        self.page_size = page_size
        # The handling status of Cloud Firewall. Valid values:
        # 
        # - **1**: Alert
        # 
        # - **2**: Block
        # 
        # > If you do not set this parameter, events in all handling statuses are queried.
        self.rule_result = rule_result
        # The source of the rule that is used to detect the intrusion prevention event. Valid values:
        # 
        # - **1**: basic protection
        # 
        # - **2**: virtual patching
        # 
        # - **4**: threat intelligence
        # 
        # > If you do not set this parameter, events detected based on all types of rules are queried.
        self.rule_source = rule_source
        # The field to use for sorting. Valid values:
        # 
        # - **VulLevel** (default): Sorts by risk level.
        # 
        # - **LastTime**: Sorts by the most recent occurrence time.
        self.sort = sort
        # The source IP address to query. If you set this parameter, only intrusion prevention events that contain the specified source IP address are queried.
        self.src_ip = src_ip
        # The ID of the source VPC.
        # 
        # > This parameter is required only when \\`FirewallType\\` is set to \\`VpcFirewall\\`.
        self.src_network_instance_id = src_network_instance_id
        # The start of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The risk level of the intrusion prevention event. Valid values:
        # 
        # - **1**: low
        # 
        # - **2**: medium
        # 
        # - **3**: high
        # 
        # > If you do not set this parameter, events of all risk levels are queried.
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app

        if self.attack_app_category is not None:
            result['AttackAppCategory'] = self.attack_app_category

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.buy_version is not None:
            result['BuyVersion'] = self.buy_version

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.direction is not None:
            result['Direction'] = self.direction

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.dst_network_instance_id is not None:
            result['DstNetworkInstanceId'] = self.dst_network_instance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.is_only_private_assoc is not None:
            result['IsOnlyPrivateAssoc'] = self.is_only_private_assoc

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.no_location is not None:
            result['NoLocation'] = self.no_location

        if self.order is not None:
            result['Order'] = self.order

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result

        if self.rule_source is not None:
            result['RuleSource'] = self.rule_source

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.src_network_instance_id is not None:
            result['SrcNetworkInstanceId'] = self.src_network_instance_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')

        if m.get('AttackAppCategory') is not None:
            self.attack_app_category = m.get('AttackAppCategory')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('BuyVersion') is not None:
            self.buy_version = m.get('BuyVersion')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Direction') is not None:
            self.direction = m.get('Direction')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('DstNetworkInstanceId') is not None:
            self.dst_network_instance_id = m.get('DstNetworkInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('IsOnlyPrivateAssoc') is not None:
            self.is_only_private_assoc = m.get('IsOnlyPrivateAssoc')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NoLocation') is not None:
            self.no_location = m.get('NoLocation')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')

        if m.get('RuleSource') is not None:
            self.rule_source = m.get('RuleSource')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SrcNetworkInstanceId') is not None:
            self.src_network_instance_id = m.get('SrcNetworkInstanceId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        return self

