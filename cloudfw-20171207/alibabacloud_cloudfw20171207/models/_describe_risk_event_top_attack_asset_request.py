# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRiskEventTopAttackAssetRequest(DaraModel):
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
        self.attack_app = attack_app
        self.attack_type = attack_type
        self.buy_version = buy_version
        # This parameter is required.
        self.end_time = end_time
        self.lang = lang
        self.source_ip = source_ip
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

