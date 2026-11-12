# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class CreateFirewallTemplateRulesRequest(DaraModel):
    def __init__(
        self,
        firewall_rule: List[main_models.CreateFirewallTemplateRulesRequestFirewallRule] = None,
        firewall_template_id: str = None,
        region_id: str = None,
    ):
        # The firewall rules.
        # 
        # This parameter is required.
        self.firewall_rule = firewall_rule
        # The ID of the firewall template.
        # 
        # This parameter is required.
        self.firewall_template_id = firewall_template_id
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the available regions for Simple Application Server.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.firewall_rule:
            for v1 in self.firewall_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FirewallRule'] = []
        if self.firewall_rule is not None:
            for k1 in self.firewall_rule:
                result['FirewallRule'].append(k1.to_map() if k1 else None)

        if self.firewall_template_id is not None:
            result['FirewallTemplateId'] = self.firewall_template_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.firewall_rule = []
        if m.get('FirewallRule') is not None:
            for k1 in m.get('FirewallRule'):
                temp_model = main_models.CreateFirewallTemplateRulesRequestFirewallRule()
                self.firewall_rule.append(temp_model.from_map(k1))

        if m.get('FirewallTemplateId') is not None:
            self.firewall_template_id = m.get('FirewallTemplateId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateFirewallTemplateRulesRequestFirewallRule(DaraModel):
    def __init__(
        self,
        port: str = None,
        remark: str = None,
        rule_protocol: str = None,
        source_cidr_ip: str = None,
    ):
        # The port range. Valid values: 1 to 65535. Separate the start port and the end port with a forward slash (/). For example, `1024/1055` indicates the port range from 1024 to 1055.
        # 
        # > If you set the protocol to ICMP, the port must be set to -1/-1.
        # 
        # This parameter is required.
        self.port = port
        # The description of the firewall rule.
        self.remark = remark
        # The transport layer protocol. Valid values:
        # 
        # - TCP: TCP.
        # - UDP: UDP.
        # - TCP+UDP: TCP and UDP.
        # - ICMP: ICMP.
        # 
        # This parameter is required.
        self.rule_protocol = rule_protocol
        # The source IPv4 CIDR address range for which you want to configure access Settings. Address ranges in CIDR format and IPv4 format are supported.
        # 
        # This parameter is required.
        self.source_cidr_ip = source_cidr_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleProtocol') is not None:
            self.rule_protocol = m.get('RuleProtocol')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        return self

