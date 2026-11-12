# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class CreateFirewallTemplateRulesResponseBody(DaraModel):
    def __init__(
        self,
        firewall_template_rules: List[main_models.CreateFirewallTemplateRulesResponseBodyFirewallTemplateRules] = None,
        request_id: str = None,
    ):
        # The firewall template rules.
        self.firewall_template_rules = firewall_template_rules
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.firewall_template_rules:
            for v1 in self.firewall_template_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FirewallTemplateRules'] = []
        if self.firewall_template_rules is not None:
            for k1 in self.firewall_template_rules:
                result['FirewallTemplateRules'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.firewall_template_rules = []
        if m.get('FirewallTemplateRules') is not None:
            for k1 in m.get('FirewallTemplateRules'):
                temp_model = main_models.CreateFirewallTemplateRulesResponseBodyFirewallTemplateRules()
                self.firewall_template_rules.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateFirewallTemplateRulesResponseBodyFirewallTemplateRules(DaraModel):
    def __init__(
        self,
        firewall_template_rule_id: str = None,
        port: str = None,
        remark: str = None,
        rule_protocol: str = None,
        source_cidr_ip: str = None,
    ):
        # The ID of the firewall template rule.
        self.firewall_template_rule_id = firewall_template_rule_id
        # The port range. Valid values: 1 to 65535. Separate the start port and the end port with a forward slash (/). For example, `1024/1055` indicates the port range from 1024 to 1055.
        # 
        # > If you set the protocol to ICMP, the port must be set to -1/-1.
        self.port = port
        # The description of the firewall rule.
        self.remark = remark
        # The transport layer protocol. Valid values:
        # 
        # - TCP: TCP.
        # - UDP: UDP.
        # - TCP+UDP: TCP and UDP.
        # - ICMP: ICMP.
        self.rule_protocol = rule_protocol
        # The source IPv4 CIDR address range for which you want to configure access Settings. Address ranges in CIDR format and IPv4 format are supported.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firewall_template_rule_id is not None:
            result['FirewallTemplateRuleId'] = self.firewall_template_rule_id

        if self.port is not None:
            result['Port'] = self.port

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_protocol is not None:
            result['RuleProtocol'] = self.rule_protocol

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallTemplateRuleId') is not None:
            self.firewall_template_rule_id = m.get('FirewallTemplateRuleId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleProtocol') is not None:
            self.rule_protocol = m.get('RuleProtocol')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        return self

