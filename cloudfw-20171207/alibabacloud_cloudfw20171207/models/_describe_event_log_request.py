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
        rule_id: str = None,
        rule_result: str = None,
        source_code: str = None,
        source_ip: str = None,
        src_ip: str = None,
        ssl_handshake_res: str = None,
        start_time: str = None,
    ):
        # The attack type of the intrusion prevention event. Valid values:
        # - **1**: Abnormal connection.
        # - **2**: execute commands.
        # - **3**: brute-force attacks.
        # - **4**: Scan.
        # - **5**: Other.
        # - **6**: Information leak.
        # - **7**: DoS attack.
        # - **8**: Overflow attack.
        # - **9**: Web attack.
        # - **10**: Trojan backdoor.
        # - **11**: Virus and worm.
        # - **12**: Mining behavior.
        # - **13**: Reverse shell.
        # 
        # > If you do not specify the Settings for this parameter, events of all attack types are queried.
        self.attack_type = attack_type
        # The page number for paging in a paged query.
        self.current_page = current_page
        # The destination IP address to query. If you specify this parameter, the intrusion prevention events that involve this destination IP address are queried.
        self.dst_ip = dst_ip
        # The end time of the query. The value is a UNIX timestamp in seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of Cloud Firewall. Valid values:
        # - **VpcFirewall**: virtual private cloud (VPC) firewalls at the border.
        # - **InternetFirewall** (default): the Internet Border firewall.
        self.firewall_type = firewall_type
        # The language for receiving messages.
        self.lang = lang
        # The log type.
        self.log_type = log_type
        # Specifies the number of results per page for a paginated query.
        # 
        # Default value: **6**, which indicates that 6 results are returned per page. Maximum value: **10**.
        self.page_size = page_size
        # Filters event logs by rule hits. The value must be the same as the RuleId value in the response. If LogType is set to ips, pass the UUID of the IPS rule (the RuleUuid value returned by DescribeIPSRules) instead of the numeric format (font style) of the RuleId. If both RuleId and AttackType are specified, records that meet both conditions are returned. This parameter takes effect for ips, app_ctl, web_filter, and threat_intelligence. If LogType is set to tls and this parameter is specified, a parameter fault is returned. If no matching records are found, TotalCount is 0. If you do not specify this parameter, event logs are not filtered by rule hit.
        self.rule_id = rule_id
        # The defense status of Cloud Firewall. Valid values:
        # - **1**: Alert.
        # - **2**: Block.
        # 
        # > If you do not specify this parameter, events of all defense statuses are queried.
        self.rule_result = rule_result
        # The tracing code.
        # 
        # This parameter is required.
        self.source_code = source_code
        # The source IP address of the visitor.
        self.source_ip = source_ip
        # The source IP address to query. If you specify this parameter, the intrusion prevention events that involve this source IP address are queried.
        self.src_ip = src_ip
        # Filters by the exact TLS handshake result. This parameter takes effect only when LogType is set to tls and is ignored for other types. Valid values: bypass, alert, and failed (handshake failure). If this parameter is not specified, records of the bypass, alert, and failed types are returned, and normal traffic with successful handshakes (success) is not returned.
        self.ssl_handshake_res = ssl_handshake_res
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

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_result is not None:
            result['RuleResult'] = self.rule_result

        if self.source_code is not None:
            result['SourceCode'] = self.source_code

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.ssl_handshake_res is not None:
            result['SslHandshakeRes'] = self.ssl_handshake_res

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

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleResult') is not None:
            self.rule_result = m.get('RuleResult')

        if m.get('SourceCode') is not None:
            self.source_code = m.get('SourceCode')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SslHandshakeRes') is not None:
            self.ssl_handshake_res = m.get('SslHandshakeRes')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

