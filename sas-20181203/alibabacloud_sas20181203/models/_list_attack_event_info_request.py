# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAttackEventInfoRequest(DaraModel):
    def __init__(
        self,
        attack_instance: str = None,
        attack_type: str = None,
        current_page: int = None,
        dst_port: str = None,
        end_time: int = None,
        lang: str = None,
        page_size: int = None,
        src_ip: str = None,
        start_time: int = None,
    ):
        # Attacked asset. You can fill in the machine instance name, public IP, or private IP.
        self.attack_instance = attack_instance
        # Attack type. Values:
        # - 9: SQL Server brute force attack
        # - 5: SSH brute force attack
        # - 6: RDP brute force attack
        # - 101: Java Struts2 attack interception
        # - 102: Redis attack interception
        # - 103: Chinese AntSword WebShell communication
        # - 104: Chinese Chopper WebShell communication
        # - 133: XISE WebShell communication
        # - 161: WebShell upload
        # - 209: PHP WebShell upload
        # - 210: JSP WebShell upload
        # - 211: ASP WebShell upload
        # - 215: Special suffix WebShell upload
        # - ai_webshell: Intelligent defense for WebShell upload
        # - java_common_rce: Java common RCE vulnerability interception
        # - alinet_webrce: Adaptive web attack defense
        self.attack_type = attack_type
        # Page number to display in a paginated query.
        self.current_page = current_page
        # Target port of the attack.
        self.dst_port = dst_port
        # Timestamp of the end time.
        self.end_time = end_time
        # Set the language type for request and response messages. Default is **zh**. Values:
        # 
        # - **zh**: Chinese
        # - **en**: English
        self.lang = lang
        # Maximum number of records per page in a paginated query.
        self.page_size = page_size
        # Source IP of the attack.
        self.src_ip = src_ip
        # Timestamp of the start time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_instance is not None:
            result['AttackInstance'] = self.attack_instance

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.dst_port is not None:
            result['DstPort'] = self.dst_port

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackInstance') is not None:
            self.attack_instance = m.get('AttackInstance')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('DstPort') is not None:
            self.dst_port = m.get('DstPort')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

