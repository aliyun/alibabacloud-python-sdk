# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnLinkageRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scheduler_rules: List[main_models.DescribeCdnLinkageRulesResponseBodySchedulerRules] = None,
        total_count: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The traffic scheduling rules.
        self.scheduler_rules = scheduler_rules
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.scheduler_rules:
            for v1 in self.scheduler_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SchedulerRules'] = []
        if self.scheduler_rules is not None:
            for k1 in self.scheduler_rules:
                result['SchedulerRules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scheduler_rules = []
        if m.get('SchedulerRules') is not None:
            for k1 in m.get('SchedulerRules'):
                temp_model = main_models.DescribeCdnLinkageRulesResponseBodySchedulerRules()
                self.scheduler_rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCdnLinkageRulesResponseBodySchedulerRules(DaraModel):
    def __init__(
        self,
        cdn_linkage_enable: int = None,
        cdn_linkage_rule: main_models.DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRule = None,
        domain: str = None,
    ):
        # Specifies whether CDN interaction is enabled. Valid values:
        # 
        # - **0**: Disabled
        # 
        # - **1**: Enabled
        self.cdn_linkage_enable = cdn_linkage_enable
        # The CDN interaction rule.
        self.cdn_linkage_rule = cdn_linkage_rule
        # The domain name.
        self.domain = domain

    def validate(self):
        if self.cdn_linkage_rule:
            self.cdn_linkage_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_linkage_enable is not None:
            result['CdnLinkageEnable'] = self.cdn_linkage_enable

        if self.cdn_linkage_rule is not None:
            result['CdnLinkageRule'] = self.cdn_linkage_rule.to_map()

        if self.domain is not None:
            result['Domain'] = self.domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnLinkageEnable') is not None:
            self.cdn_linkage_enable = m.get('CdnLinkageEnable')

        if m.get('CdnLinkageRule') is not None:
            temp_model = main_models.DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRule()
            self.cdn_linkage_rule = temp_model.from_map(m.get('CdnLinkageRule'))

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        return self

class DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRule(DaraModel):
    def __init__(
        self,
        cname: str = None,
        param: main_models.DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRuleParam = None,
        rule_name: str = None,
        rules: List[main_models.DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRuleRules] = None,
    ):
        # The canonical name of the Anti-DDoS instance that is associated with the domain name.
        self.cname = cname
        # The resource for interaction.
        self.param = param
        # The name of the traffic scheduling rule.
        self.rule_name = rule_name
        # The rule information.
        self.rules = rules

    def validate(self):
        if self.param:
            self.param.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Param') is not None:
            temp_model = main_models.DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRuleParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRuleRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRuleRules(DaraModel):
    def __init__(
        self,
        priority: int = None,
        region_id: str = None,
        status: int = None,
        type: str = None,
        value: str = None,
        value_type: int = None,
    ):
        # The priority of the rule. Valid values: 0 to 100. A larger value indicates a higher priority.
        self.priority = priority
        # The region ID. The default value is empty.
        self.region_id = region_id
        # The status of the rule. Valid values:
        # 
        # - **0**: Inactive
        # 
        # - **1**: Active
        self.status = status
        # The format of the resource address. Valid values:
        # 
        # - **A**: IPv4 address
        # 
        # - **AAAA**: IPv6 address
        # 
        # - **CNAME**: canonical name
        self.type = type
        # The resource address.
        self.value = value
        # The type of the resource address. Valid values:
        # 
        # - **1**: Anti-DDoS IP
        # 
        # - **5**: Accelerated domain name for CDN interaction
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRuleParam(DaraModel):
    def __init__(
        self,
        param_data: main_models.DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRuleParamParamData = None,
        param_type: str = None,
    ):
        # The interaction conditions.
        self.param_data = param_data
        # The type of the resource for interaction. Valid values:
        # 
        # - **cdn**: Alibaba Cloud CDN
        # 
        # - **dcdn**: DCDN
        self.param_type = param_type

    def validate(self):
        if self.param_data:
            self.param_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_data is not None:
            result['ParamData'] = self.param_data.to_map()

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamData') is not None:
            temp_model = main_models.DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRuleParamParamData()
            self.param_data = temp_model.from_map(m.get('ParamData'))

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        return self

class DescribeCdnLinkageRulesResponseBodySchedulerRulesCdnLinkageRuleParamParamData(DaraModel):
    def __init__(
        self,
        access_qps: int = None,
        upstream_qps: int = None,
    ):
        # The QPS threshold that triggers a resource switch.
        self.access_qps = access_qps
        # A reserved field. The default value is 0.
        self.upstream_qps = upstream_qps

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_qps is not None:
            result['AccessQps'] = self.access_qps

        if self.upstream_qps is not None:
            result['UpstreamQps'] = self.upstream_qps

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessQps') is not None:
            self.access_qps = m.get('AccessQps')

        if m.get('UpstreamQps') is not None:
            self.upstream_qps = m.get('UpstreamQps')

        return self

