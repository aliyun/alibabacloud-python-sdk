# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEventLogRequest(DaraModel):
    def __init__(
        self,
        attack_type: int = None,
        current_page: str = None,
        dst_ip: str = None,
        end_time: str = None,
        firewall_type: str = None,
        lang: str = None,
        log_type: str = None,
        page_size: str = None,
        rule_result: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        start_time: str = None,
    ):
        # The attack type of the intrusion prevention event. Valid values:
        # - **1**: Abnormal connection.
        # - **2**: Command execution.
        # - **3**: Brute-force attack.
        # - **4**: Scanning.
        # - **5**: Other.
        # - **6**: Information leakage.
        # - **7**: DoS attack.
        # - **8**: Overflow attack.
        # - **9**: Web attack.
        # - **10**: Trojan backdoor.
        # - **11**: Viruses and worms.
        # - **12**: Mining behavior.
        # - **13**: Reverse shell.
        # 
        # > If you do not specify this parameter, all attack types are queried.
        self.attack_type = attack_type
        # The page number for a paged query.
        self.current_page = current_page
        # The destination IP address to query. If you specify this parameter, the system queries intrusion prevention events that involve this destination IP address.
        self.dst_ip = dst_ip
        # The end time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of the Cloud Firewall. Valid values:
        # - **VpcFirewall**: virtual private cloud (VPC) firewalls.
        # - **InternetFirewall** (default): the Internet Border firewall.
        self.firewall_type = firewall_type
        # The language of the response message.
        self.lang = lang
        # The log type.
        self.log_type = log_type
        # The number of entries to return on each page.
        # 
        # Default value: **6**, which indicates that 6 entries are returned on each page. Maximum value: **10**.
        self.page_size = page_size
        # The defense status of the Cloud Firewall. Valid values:
        # - **1**: Alert.
        # - **2**: Block.
        # 
        # > If you do not specify this parameter, all defense statuses are queried.
        self.rule_result = rule_result
        # The tracing code.
        # 
        # This parameter is required.
        self.source_code = source_code
        # The source IP address of the requester.
        self.source_ip = source_ip
        # The source IP address to query. If you specify this parameter, the system queries intrusion prevention events that involve this source IP address.
        self.src_ip = src_ip
        # The start time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_type is not None:
            result['LogType'] = self.log_type

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogType') is not None:
            self.log_type = m.get('LogType')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

