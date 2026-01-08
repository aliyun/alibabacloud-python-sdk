# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyIpsRulesToDefaultRequest(DaraModel):
    def __init__(
        self,
        attack_app: str = None,
        firewall_type: str = None,
        lang: str = None,
        rule_type: str = None,
        rules: str = None,
        source_ip: str = None,
    ):
        self.attack_app = attack_app
        self.firewall_type = firewall_type
        self.lang = lang
        # This parameter is required.
        self.rule_type = rule_type
        self.rules = rules
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attack_app is not None:
            result['AttackApp'] = self.attack_app

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.rules is not None:
            result['Rules'] = self.rules

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

