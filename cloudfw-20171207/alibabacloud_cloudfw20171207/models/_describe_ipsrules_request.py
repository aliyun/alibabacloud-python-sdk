# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeIPSRulesRequest(DaraModel):
    def __init__(
        self,
        attack_app: str = None,
        attack_app_category: List[str] = None,
        attack_apps: List[str] = None,
        attack_type: str = None,
        cve: str = None,
        default_action: str = None,
        firewall_type: str = None,
        lang: str = None,
        order: str = None,
        page_no: int = None,
        page_size: int = None,
        query_modify: str = None,
        rule_action: str = None,
        rule_class: str = None,
        rule_id: str = None,
        rule_level: int = None,
        rule_name: str = None,
        rule_type: str = None,
        sort: str = None,
        source_ip: str = None,
        vpc_firewall_id: str = None,
    ):
        # The application targeted by the attack.
        self.attack_app = attack_app
        # The categories of applications targeted by attacks.
        self.attack_app_category = attack_app_category
        # The applications targeted by attacks.
        self.attack_apps = attack_apps
        # The attack type.
        self.attack_type = attack_type
        # The CVE ID.
        self.cve = cve
        # The status of the rule.
        self.default_action = default_action
        # The type of firewall.
        self.firewall_type = firewall_type
        # The language of the request and response.
        self.lang = lang
        # The sort order.
        self.order = order
        # The page number.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page.
        # 
        # This parameter is required.
        self.page_size = page_size
        # Indicates whether to retrieve only modified rules.
        self.query_modify = query_modify
        # The rule action.
        self.rule_action = rule_action
        # The inspection mode.
        self.rule_class = rule_class
        # The rule ID.
        self.rule_id = rule_id
        # The rule level.
        self.rule_level = rule_level
        # The rule name.
        self.rule_name = rule_name
        # The rule type.
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # The field to sort by.
        self.sort = sort
        # The source IP address of the request.
        self.source_ip = source_ip
        # The instance ID of the VPC firewall.
        self.vpc_firewall_id = vpc_firewall_id

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

        if self.attack_apps is not None:
            result['AttackApps'] = self.attack_apps

        if self.attack_type is not None:
            result['AttackType'] = self.attack_type

        if self.cve is not None:
            result['Cve'] = self.cve

        if self.default_action is not None:
            result['DefaultAction'] = self.default_action

        if self.firewall_type is not None:
            result['FirewallType'] = self.firewall_type

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.order is not None:
            result['Order'] = self.order

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_modify is not None:
            result['QueryModify'] = self.query_modify

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_class is not None:
            result['RuleClass'] = self.rule_class

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_level is not None:
            result['RuleLevel'] = self.rule_level

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.vpc_firewall_id is not None:
            result['VpcFirewallId'] = self.vpc_firewall_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttackApp') is not None:
            self.attack_app = m.get('AttackApp')

        if m.get('AttackAppCategory') is not None:
            self.attack_app_category = m.get('AttackAppCategory')

        if m.get('AttackApps') is not None:
            self.attack_apps = m.get('AttackApps')

        if m.get('AttackType') is not None:
            self.attack_type = m.get('AttackType')

        if m.get('Cve') is not None:
            self.cve = m.get('Cve')

        if m.get('DefaultAction') is not None:
            self.default_action = m.get('DefaultAction')

        if m.get('FirewallType') is not None:
            self.firewall_type = m.get('FirewallType')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryModify') is not None:
            self.query_modify = m.get('QueryModify')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleClass') is not None:
            self.rule_class = m.get('RuleClass')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleLevel') is not None:
            self.rule_level = m.get('RuleLevel')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('VpcFirewallId') is not None:
            self.vpc_firewall_id = m.get('VpcFirewallId')

        return self

