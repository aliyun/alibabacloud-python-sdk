# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSchedulerRuleRequest(DaraModel):
    def __init__(
        self,
        param: str = None,
        resource_group_id: str = None,
        rule_name: str = None,
        rule_type: int = None,
        rules: str = None,
    ):
        # The details of the CDN interaction rule. This parameter is a JSON format character string. The following list describes the structure:
        # - **ParamType**: Required. String type. The type of CDN interaction. Valid values: **cdn**, which indicates CDN interaction.
        # - **ParamData**: Required. Map type. The CDN interaction parameters. The following list describes the structure:
        #     - **Domain**: Required. String type. The CDN-accelerated domain name.
        #     - **Cname**: Required. String type. The CNAME of the accelerated domain name.
        #     - **AccessQps**: Required. Integer type. The access QPS threshold. If the QPS exceeds this threshold, traffic is switched to Anti-DDoS Pro and Anti-DDoS Premium.
        #     - **UpstreamQps**: Optional. Integer type. The back-to-origin QPS threshold. If the QPS is lower than this threshold, traffic is switched to CDN.
        self.param = param
        # The ID of the resource group to which the Anti-DDoS Pro or Anti-DDoS Premium instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The type of the rule. Valid values:
        # - **2**: tiered protection
        # - **3**: acceleration for China-to-global traffic
        # - **5**: CDN interaction
        # - **6**: cloud service interaction
        # - **8**: secure acceleration
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # The details of the general interaction rule. This parameter is a JSON string that consists of the following characters. The following list describes the structure:
        # - **Type**: String type. Required. The format of the Resource for Interaction address. Valid values:
        #     - **A**: IP address
        #     - **CNAME**: domain name
        # - **Value**: String type. Required. The address of the Resource for Interaction.
        # - **Priority**: Integer type. Required. The priority of the rule. Valid values: **0** to **100**. A larger value indicates a higher priority.
        # - **ValueType**: Integer type. Required. The type of the Resource for Interaction. Valid values:
        #     - **1**: IP Address of Anti-DDoS Proxy instance 
        #     - **2**: (Tiered protection) IP addresses of cloud resources
        #     - **3**: (Sec-acceleration for China-to-global traffic) acceleration line IP address
        #     - **5**: (CDN interaction) acceleration domain name
        #     - **6**: (Cloud service interaction) IP addresses of cloud resources
        # - **RegionId**: String type. Optional (required when **ValueType** is **2**). The region ID.
        # 
        # This parameter is required.
        self.rules = rules

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param is not None:
            result['Param'] = self.param

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.rules is not None:
            result['Rules'] = self.rules

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Param') is not None:
            self.param = m.get('Param')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Rules') is not None:
            self.rules = m.get('Rules')

        return self

