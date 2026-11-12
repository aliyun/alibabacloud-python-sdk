# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ModifyFirewallTemplateRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        firewall_template_id: str = None,
        firewall_template_rule: List[main_models.ModifyFirewallTemplateRequestFirewallTemplateRule] = None,
        name: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, and you must make sure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the firewall template.
        self.description = description
        # The ID of the firewall template.
        # 
        # This parameter is required.
        self.firewall_template_id = firewall_template_id
        # The firewall rules.
        self.firewall_template_rule = firewall_template_rule
        # The name of the firewall template.
        self.name = name
        # The region ID of the Simple Application Server instance. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the list of supported Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.firewall_template_rule:
            for v1 in self.firewall_template_rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.firewall_template_id is not None:
            result['FirewallTemplateId'] = self.firewall_template_id

        result['FirewallTemplateRule'] = []
        if self.firewall_template_rule is not None:
            for k1 in self.firewall_template_rule:
                result['FirewallTemplateRule'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FirewallTemplateId') is not None:
            self.firewall_template_id = m.get('FirewallTemplateId')

        self.firewall_template_rule = []
        if m.get('FirewallTemplateRule') is not None:
            for k1 in m.get('FirewallTemplateRule'):
                temp_model = main_models.ModifyFirewallTemplateRequestFirewallTemplateRule()
                self.firewall_template_rule.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyFirewallTemplateRequestFirewallTemplateRule(DaraModel):
    def __init__(
        self,
        firewall_template_rule_id: str = None,
        port: str = None,
        remark: str = None,
        rule_protocol: str = None,
        source_cidr_ip: str = None,
    ):
        # The ID of the firewall template rule.
        # 
        # This parameter is required.
        self.firewall_template_rule_id = firewall_template_rule_id
        # The port range. Valid values: 1 to 65535. Use a forward slash (/) to separate the start port and the end port. For example, `1024/1055` indicates a port range from 1024 to 1055.
        # 
        # > If you set the protocol to ICMP, the port must be set to -1/-1.
        self.port = port
        # The remark of the firewall rule.
        self.remark = remark
        # The transport layer protocol. Valid values:
        # 
        # - TCP: TCP
        # - UDP: UDP
        # - TCP+UDP: TCP and UDP
        # - ICMP: ICMP
        self.rule_protocol = rule_protocol
        # The source IPv4 CIDR block for which you want to configure access permissions. You can specify an IP address range in CIDR format or IPv4 format.
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

