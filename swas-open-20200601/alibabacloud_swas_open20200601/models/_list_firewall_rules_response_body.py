# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListFirewallRulesResponseBody(DaraModel):
    def __init__(
        self,
        firewall_rules: List[main_models.ListFirewallRulesResponseBodyFirewallRules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of firewall rules.
        self.firewall_rules = firewall_rules
        # The page number of the firewall rule list.
        self.page_number = page_number
        # The paging Settings for the number of entries per page in a paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of firewall rules.
        self.total_count = total_count

    def validate(self):
        if self.firewall_rules:
            for v1 in self.firewall_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FirewallRules'] = []
        if self.firewall_rules is not None:
            for k1 in self.firewall_rules:
                result['FirewallRules'].append(k1.to_map() if k1 else None)

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
        self.firewall_rules = []
        if m.get('FirewallRules') is not None:
            for k1 in m.get('FirewallRules'):
                temp_model = main_models.ListFirewallRulesResponseBodyFirewallRules()
                self.firewall_rules.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListFirewallRulesResponseBodyFirewallRules(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        policy: str = None,
        port: str = None,
        remark: str = None,
        rule_id: str = None,
        rule_protocol: str = None,
        source_cidr_ip: str = None,
        tags: List[main_models.ListFirewallRulesResponseBodyFirewallRulesTags] = None,
    ):
        # The ID of the simple application server to which the firewall rule belongs.
        self.instance_id = instance_id
        # The firewall policy. Valid values:
        # 
        # - accept: Allow.
        # 
        # - drop: Deny.
        self.policy = policy
        # The port range.
        self.port = port
        # The remark of the firewall rule.
        self.remark = remark
        # The ID of the firewall rule.
        self.rule_id = rule_id
        # The transport layer protocol. Valid values:
        # 
        # - TCP: TCP.
        # - UDP: UDP.
        # - TCP+UDP: TCP and UDP.
        self.rule_protocol = rule_protocol
        # The source CIDR block.
        self.source_cidr_ip = source_cidr_ip
        # The tags of the firewall rules.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.port is not None:
            result['Port'] = self.port

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_protocol is not None:
            result['RuleProtocol'] = self.rule_protocol

        if self.source_cidr_ip is not None:
            result['SourceCidrIp'] = self.source_cidr_ip

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleProtocol') is not None:
            self.rule_protocol = m.get('RuleProtocol')

        if m.get('SourceCidrIp') is not None:
            self.source_cidr_ip = m.get('SourceCidrIp')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListFirewallRulesResponseBodyFirewallRulesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListFirewallRulesResponseBodyFirewallRulesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the firewall rule.
        self.key = key
        # The tag value of the firewall rule.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

