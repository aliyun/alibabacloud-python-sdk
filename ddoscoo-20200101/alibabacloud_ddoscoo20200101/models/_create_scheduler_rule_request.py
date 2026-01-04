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
        # The details of the CDN interaction rule. This parameter is a JSON string. The following list describes the fields in the value of the parameter:
        # 
        # *   **ParamType**: the type of the scheduling rule. This field is required and must be of the string type. Set the value to **cdn**. This indicates that you want to modify a CDN interaction rule.
        # 
        # *   **ParamData**: the values of parameters that you want to modify for the CDN interaction rule. This field is required and must be of the map type. ParamData contains the following parameters:
        # 
        #     *   **Domain**: the accelerated domain in CDN. This parameter is required and must be of the string type.
        #     *   **Cname**: the CNAME that is assigned to the accelerated domain. This parameter is required and must be of the string type.
        #     *   **AccessQps**: the queries per second (QPS) threshold that is used to switch service traffic to Anti-DDoS Pro or Anti-DDoS Premium. This parameter is required and must be of the integer type.
        #     *   **UpstreamQps**: the QPS threshold that is used to switch service traffic to CDN. This parameter is optional and must be of the integer type.
        self.param = param
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The type of the rule. Valid values:
        # 
        # *   **2**: tiered protection
        # *   **3**: network acceleration
        # *   **5**: Alibaba Cloud CDN (CDN) interaction
        # *   **6**: cloud service interaction
        # *   **8**: secure acceleration
        # 
        # This parameter is required.
        self.rule_type = rule_type
        # The details of the scheduling rule. This parameter is a JSON string. The following list describes the fields in the value of the parameter:
        # 
        # *   **Type**: the address type of the interaction resource that you want to use in the scheduling rule. This field is required and must be of the string type. Valid values:
        # 
        #     *   **A**: IP address
        #     *   **CNAME**: domain name
        # 
        # *   **Value**: the address of the interaction resource that you want to use in the scheduling rule. This field is required and must be of the string type.
        # 
        # *   **Priority**: the priority of the scheduling rule. This field is required and must be of the integer type. Valid values: **0** to **100**. A larger value indicates a higher priority.
        # 
        # *   **ValueType**: the type of the interaction resource that you want to use in the scheduling rule. This field is required and must be of the integer type. Valid values:
        # 
        #     *   **1**: the IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance
        #     *   **2**: the IP address of the interaction resource in the tiered protection scenario
        #     *   **3**: the IP address that is used to accelerate access in the network acceleration scenario
        #     *   **5**: the domain name that is configured in Alibaba Cloud CDN (CDN) in the CDN interaction scenario
        #     *   **6** the IP address of the interaction resource in the cloud service interaction scenario
        # 
        # *   **RegionId**: the region where the interaction resource is deployed. This parameter must be specified when **ValueType** is set to **2**. The value must be of the string type.
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

