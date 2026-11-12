# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class DescribeFirewallTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        firewall_templates: List[main_models.DescribeFirewallTemplatesResponseBodyFirewallTemplates] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the queried firewall templates.
        self.firewall_templates = firewall_templates
        # The page number.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.firewall_templates:
            for v1 in self.firewall_templates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FirewallTemplates'] = []
        if self.firewall_templates is not None:
            for k1 in self.firewall_templates:
                result['FirewallTemplates'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.firewall_templates = []
        if m.get('FirewallTemplates') is not None:
            for k1 in m.get('FirewallTemplates'):
                temp_model = main_models.DescribeFirewallTemplatesResponseBodyFirewallTemplates()
                self.firewall_templates.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeFirewallTemplatesResponseBodyFirewallTemplates(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        creation_time: str = None,
        description: str = None,
        firewall_template_id: str = None,
        firewall_template_rules: List[main_models.DescribeFirewallTemplatesResponseBodyFirewallTemplatesFirewallTemplateRules] = None,
        name: str = None,
    ):
        # The time when the firewall template was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        # 
        # >  The time displayed in the Simple Application Server console is in the format of UTC+8.
        self.create_time = create_time
        # The time when the firewall template was created. The time follows the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the firewall template.
        self.description = description
        # The ID of the firewall template.
        self.firewall_template_id = firewall_template_id
        # The details of the firewall template rules.
        self.firewall_template_rules = firewall_template_rules
        # The name of the firewall template.
        self.name = name

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.firewall_template_id is not None:
            result['FirewallTemplateId'] = self.firewall_template_id

        result['FirewallTemplateRules'] = []
        if self.firewall_template_rules is not None:
            for k1 in self.firewall_template_rules:
                result['FirewallTemplateRules'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FirewallTemplateId') is not None:
            self.firewall_template_id = m.get('FirewallTemplateId')

        self.firewall_template_rules = []
        if m.get('FirewallTemplateRules') is not None:
            for k1 in m.get('FirewallTemplateRules'):
                temp_model = main_models.DescribeFirewallTemplatesResponseBodyFirewallTemplatesFirewallTemplateRules()
                self.firewall_template_rules.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class DescribeFirewallTemplatesResponseBodyFirewallTemplatesFirewallTemplateRules(DaraModel):
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
        # The port range. Valid values: 1 to 65535. Specify a port range in the format of \\<start port number>/\\<end port number>. Example: `1024/1055`, which indicates that the port range of 1024 to 1055.
        # 
        # >  If you set RuleProtocol to ICMP, you must set Port to -1/-1.
        self.port = port
        # The remarks of the firewall template rule.
        self.remark = remark
        # The transport layer protocol that the rule supports. Valid values:
        # 
        # *   TCP
        # *   UDP
        # *   TCP+UDP
        # *   ICMP
        self.rule_protocol = rule_protocol
        # The source address to which you want to grant access permissions. CIDR blocks and IPv4 addresses are supported.
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

