# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyIpsRulesRequest(DaraModel):
    def __init__(
        self,
        firewall_type: str = None,
        lang: str = None,
        rule_action: str = None,
        rule_type: str = None,
        rules: str = None,
        source_ip: str = None,
    ):
        self.firewall_type = firewall_type
        self.lang = lang
        # This parameter is required.
        self.rule_action = rule_action
        # This parameter is required.
        self.rule_type = rule_type
        # This parameter is required.
        self.rules = rules
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.rules is not None:
            result['Rules'] = self.rules

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

