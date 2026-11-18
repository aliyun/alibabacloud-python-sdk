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
        proxy_id: str = None,
        rule_type: str = None,
        rules: str = None,
        source_ip: str = None,
    ):
        # The attack application.
        self.attack_app = attack_app
        # The Cloud Firewall type. Valid values:
        # - **VpcFirewall**: virtual private cloud (VPC) firewall
        # - **InternetFirewall** (default): the Internet firewall
        self.firewall_type = firewall_type
        # The language type. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # Instance ID of the NAT firewall instance. This parameter is required only when FirewallType is set to **NatFirewall**. In this case, the scope is the rules under this instance. This parameter is ignored for Internet and VPC firewalls. You can call the [ListNatFirewallIpsConfigs](https://help.aliyun.com/document_detail/2879296.html) operation to query instance ID.
        self.proxy_id = proxy_id
        # The rule type. Valid values:
        # - **basicRule**
        # - **customize**
        self.rule_type = rule_type
        # The list of rules. This parameter is conditionally required: when RuleType is set to customize, you must specify at least one of this parameter or AttackApp. If you specify only RuleType without Rules or AttackApp, the API returns an ErrorParameters error.
        self.rules = rules
        # The source IP address of the requester.
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

        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id

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

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

