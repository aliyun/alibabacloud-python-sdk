# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class CreateFirewallRulesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        firewall_rules: List[main_models.CreateFirewallRulesRequestFirewallRules] = None,
        instance_id: str = None,
        region_id: str = None,
        tag: List[main_models.CreateFirewallRulesRequestTag] = None,
    ):
        # The client token.
        self.client_token = client_token
        # The array of firewall rules.
        self.firewall_rules = firewall_rules
        # The instance ID of the specified simple application server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query the regions where simple application servers are available.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of tags. The list can contain up to 20 tags.
        self.tag = tag

    def validate(self):
        if self.firewall_rules:
            for v1 in self.firewall_rules:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['FirewallRules'] = []
        if self.firewall_rules is not None:
            for k1 in self.firewall_rules:
                result['FirewallRules'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.firewall_rules = []
        if m.get('FirewallRules') is not None:
            for k1 in m.get('FirewallRules'):
                temp_model = main_models.CreateFirewallRulesRequestFirewallRules()
                self.firewall_rules.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateFirewallRulesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateFirewallRulesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key that is specified for the firewall rule. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string. It can be up to 64 characters in length, cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The tag value that is specified for the firewall rule. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain http:// or https://.
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

class CreateFirewallRulesRequestFirewallRules(DaraModel):
    def __init__(
        self,
        port: str = None,
        remark: str = None,
        rule_protocol: str = None,
        source_cidr_ip: str = None,
    ):
        # The port number.
        # - TCP or UDP: Valid values are 1 to 65535. Use a forward slash (/) to separate the start port and the end port. Example: 1/200.
        # - ICMP: -1/-1.
        self.port = port
        # The remark.
        self.remark = remark
        # The transport layer protocol. Valid values:
        # 
        # - TCP: TCP.
        # - UDP: UDP.
        # - TCP+UDP: TCP and UDP.
        # - ICMP: ICMP.
        self.rule_protocol = rule_protocol
        # The source IP address or CIDR block.
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

