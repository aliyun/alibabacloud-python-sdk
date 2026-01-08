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
        # The names of the attacked applications. Set the value in the `["AttackApp1","AttackApp2"]` format.
        self.attack_app = attack_app
        # A list of categories of attacked applications, expressed in the format ["AttackAppCategory1","AttackAppCategory2"].
        self.attack_app_category = attack_app_category
        # The attack type of the intrusion events. Valid values:
        # 
        # *   **1**: suspicious connection
        # *   **2**: command execution
        # *   **3**: brute-force attack
        # *   **4**: scanning
        # *   **5**: others
        # *   **6**: information leak
        # *   **7**: DoS attack
        # *   **8**: buffer overflow attack
        # *   **9**: web attack
        # *   **10**: trojan backdoor
        # *   **11**: computer worm
        # *   **12**: mining
        # *   **13**: reverse shell
        # 
        # > If you do not specify this parameter, the intrusion events of all attack types are queried.
        self.attack_type = attack_type
        # The edition of Cloud Firewall that you purchase. Valid values:
        # 
        # *   **2**: Premium Edition
        # *   **3**: Enterprise Edition
        # *   **4**: Ultimate Edition
        # *   **10**: Cloud Firewall that uses the pay-as-you-go billing method
        self.buy_version = buy_version
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The type of the risk events.\\
        # Set the value to **session**, which indicates intrusion events.
        # 
        # This parameter is required.
        self.data_type = data_type
        # The direction of the traffic for the intrusion events. Valid values:
        # 
        # *   **in**: inbound
        # *   **out**: outbound
        # 
        # > If you do not specify this parameter, the intrusion events that are recorded for both inbound and outbound traffic are queried.
        self.direction = direction
        # The destination IP address to query. If you specify this parameter, all intrusion events with the specified destination IP address are queried.
        self.dst_ip = dst_ip
        # The ID of the destination VPC.
        # 
        # > If the FirewallType parameter is set to VpcFirewall, you must specify this parameter.
        self.dst_network_instance_id = dst_network_instance_id
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the intrusion event.
        self.event_name = event_name
        # The type of the firewall. Valid values:
        # 
        # *   **VpcFirewall**: virtual private cloud (VPC) firewall
        # *   **InternetFirewall**: Internet firewall (default)
        self.firewall_type = firewall_type
        # Whether to query only the data that has completed private network tracing.
        self.is_only_private_assoc = is_only_private_assoc
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese (default)
        # *   **en**: English
        self.lang = lang
        # Specifies whether to query the information about the geographical locations of IP addresses.
        # 
        # *   **true**: does not query the information about the geographical locations of IP addresses.
        # *   **false**: queries the information about the geographical locations of IP addresses. This is the default value.
        self.no_location = no_location
        # The order in which you want to sort the results. Valid values:
        # 
        # *   **asc**: the ascending order.
        # *   **desc**: the descending order. This is the default value.
        self.order = order
        # The number of entries to return on each page.
        # 
        # Default value: **6**. Maximum value: **10**.
        self.page_size = page_size
        # The status of the firewall. Valid values:
        # 
        # *   **1**: alerting
        # *   **2**: blocking
        # 
        # > If you do not specify this parameter, all intrusion events that are detected by the firewall are queried, regardless of the firewall status.
        self.rule_result = rule_result
        # The module of the rule that is used to detect the intrusion events. Valid values:
        # 
        # *   **1**: basic protection
        # *   **2**: virtual patching
        # *   **4**: threat intelligence
        # 
        # > If you do not specify this parameter, the intrusion events that are detected by all rules are queried.
        self.rule_source = rule_source
        # The field based on which you want to sort the results. Valid values:
        # 
        # *   **VulLevel**: The results are sorted based on the risk level field. This is the default value.
        # *   **LastTime**: The results are sorted based on the most recent occurrence time.
        self.sort = sort
        # The source IP address to query. If you specify this parameter, all intrusion events with the specified source IP address are queried.
        self.src_ip = src_ip
        # The ID of the source VPC.
        # 
        # > If the FirewallType parameter is set to VpcFirewall, you must specify this parameter.
        self.src_network_instance_id = src_network_instance_id
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The risk level of the intrusion events. Valid values:
        # 
        # *   **1**: low
        # *   **2**: medium
        # *   **3**: high
        # 
        # > If you do not specify this parameter, the intrusion events that are at all risk levels are queried.
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

