# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRiskEventStatisticRequest(DaraModel):
    def __init__(
        self,
        attack_app: List[str] = None,
        attack_type: str = None,
        buy_version: str = None,
        end_time: str = None,
        lang: str = None,
        source_ip: str = None,
        start_time: str = None,
    ):
        # The attacked application.
        self.attack_app = attack_app
        # The attack type of the intrusion prevention event. Valid values:
        # 
        # - **1**: anomalous connection
        # 
        # - **2**: command execution
        # 
        # - **3**: brute-force attack
        # 
        # - **4**: scanning
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
        # - **10**: trojan backdoor
        # 
        # - **11**: virus and worm
        # 
        # - **12**: mining
        # 
        # - **13**: reverse shell
        # 
        # > If you do not specify this parameter, all attack types are queried.
        self.attack_type = attack_type
        # The edition of Cloud Firewall.
        self.buy_version = buy_version
        # The end time. The value is a UNIX timestamp. Unit: seconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The language of the response.
        self.lang = lang
        # The source IP address of the visitor.
        self.source_ip = source_ip
        # The start time. The value is a UNIX timestamp. Unit: seconds.
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
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.buy_version is not None:
            result['BuyVersion'] = self.buy_version

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('BuyVersion') is not None:
            self.buy_version = m.get('BuyVersion')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

