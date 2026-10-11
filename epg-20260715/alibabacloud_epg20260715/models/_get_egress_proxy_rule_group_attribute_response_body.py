# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class GetEgressProxyRuleGroupAttributeResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        egress_proxy_ip_pool_id: str = None,
        egress_proxy_rule_group_id: str = None,
        egress_proxy_rule_group_name: str = None,
        egress_proxy_rules: main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRules = None,
        request_id: str = None,
        resource_group_id: str = None,
        status: str = None,
        tags: List[main_models.GetEgressProxyRuleGroupAttributeResponseBodyTags] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.egress_proxy_ip_pool_id = egress_proxy_ip_pool_id
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        self.egress_proxy_rule_group_name = egress_proxy_rule_group_name
        self.egress_proxy_rules = egress_proxy_rules
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.status = status
        self.tags = tags

    def validate(self):
        if self.egress_proxy_rules:
            self.egress_proxy_rules.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_ip_pool_id is not None:
            result['EgressProxyIpPoolId'] = self.egress_proxy_ip_pool_id

        if self.egress_proxy_rule_group_id is not None:
            result['EgressProxyRuleGroupId'] = self.egress_proxy_rule_group_id

        if self.egress_proxy_rule_group_name is not None:
            result['EgressProxyRuleGroupName'] = self.egress_proxy_rule_group_name

        if self.egress_proxy_rules is not None:
            result['EgressProxyRules'] = self.egress_proxy_rules.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyIpPoolId') is not None:
            self.egress_proxy_ip_pool_id = m.get('EgressProxyIpPoolId')

        if m.get('EgressProxyRuleGroupId') is not None:
            self.egress_proxy_rule_group_id = m.get('EgressProxyRuleGroupId')

        if m.get('EgressProxyRuleGroupName') is not None:
            self.egress_proxy_rule_group_name = m.get('EgressProxyRuleGroupName')

        if m.get('EgressProxyRules') is not None:
            temp_model = main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRules()
            self.egress_proxy_rules = temp_model.from_map(m.get('EgressProxyRules'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetEgressProxyRuleGroupAttributeResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetEgressProxyRuleGroupAttributeResponseBodyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRules(DaraModel):
    def __init__(
        self,
        post_response: List[main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPostResponse] = None,
        pre_dns: List[main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreDns] = None,
        pre_request: List[main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreRequest] = None,
    ):
        self.post_response = post_response
        self.pre_dns = pre_dns
        self.pre_request = pre_request

    def validate(self):
        if self.post_response:
            for v1 in self.post_response:
                 if v1:
                    v1.validate()
        if self.pre_dns:
            for v1 in self.pre_dns:
                 if v1:
                    v1.validate()
        if self.pre_request:
            for v1 in self.pre_request:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PostResponse'] = []
        if self.post_response is not None:
            for k1 in self.post_response:
                result['PostResponse'].append(k1.to_map() if k1 else None)

        result['PreDns'] = []
        if self.pre_dns is not None:
            for k1 in self.pre_dns:
                result['PreDns'].append(k1.to_map() if k1 else None)

        result['PreRequest'] = []
        if self.pre_request is not None:
            for k1 in self.pre_request:
                result['PreRequest'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.post_response = []
        if m.get('PostResponse') is not None:
            for k1 in m.get('PostResponse'):
                temp_model = main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPostResponse()
                self.post_response.append(temp_model.from_map(k1))

        self.pre_dns = []
        if m.get('PreDns') is not None:
            for k1 in m.get('PreDns'):
                temp_model = main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreDns()
                self.pre_dns.append(temp_model.from_map(k1))

        self.pre_request = []
        if m.get('PreRequest') is not None:
            for k1 in m.get('PreRequest'):
                temp_model = main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreRequest()
                self.pre_request.append(temp_model.from_map(k1))

        return self

class GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreRequest(DaraModel):
    def __init__(
        self,
        action: str = None,
        conditions: List[main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreRequestConditions] = None,
        create_time: str = None,
        description: str = None,
        egress_proxy_rule_id: str = None,
        egress_proxy_rule_name: str = None,
        priority: int = None,
    ):
        self.action = action
        self.conditions = conditions
        self.create_time = create_time
        self.description = description
        self.egress_proxy_rule_id = egress_proxy_rule_id
        self.egress_proxy_rule_name = egress_proxy_rule_name
        self.priority = priority

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_rule_id is not None:
            result['EgressProxyRuleId'] = self.egress_proxy_rule_id

        if self.egress_proxy_rule_name is not None:
            result['EgressProxyRuleName'] = self.egress_proxy_rule_name

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreRequestConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyRuleId') is not None:
            self.egress_proxy_rule_id = m.get('EgressProxyRuleId')

        if m.get('EgressProxyRuleName') is not None:
            self.egress_proxy_rule_name = m.get('EgressProxyRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreRequestConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_operator: str = None,
        condition_values: List[str] = None,
    ):
        self.condition_key = condition_key
        self.condition_operator = condition_operator
        self.condition_values = condition_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_key is not None:
            result['ConditionKey'] = self.condition_key

        if self.condition_operator is not None:
            result['ConditionOperator'] = self.condition_operator

        if self.condition_values is not None:
            result['ConditionValues'] = self.condition_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionKey') is not None:
            self.condition_key = m.get('ConditionKey')

        if m.get('ConditionOperator') is not None:
            self.condition_operator = m.get('ConditionOperator')

        if m.get('ConditionValues') is not None:
            self.condition_values = m.get('ConditionValues')

        return self

class GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreDns(DaraModel):
    def __init__(
        self,
        action: str = None,
        conditions: List[main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreDnsConditions] = None,
        create_time: str = None,
        description: str = None,
        egress_proxy_rule_id: str = None,
        egress_proxy_rule_name: str = None,
        priority: int = None,
    ):
        self.action = action
        self.conditions = conditions
        self.create_time = create_time
        self.description = description
        self.egress_proxy_rule_id = egress_proxy_rule_id
        self.egress_proxy_rule_name = egress_proxy_rule_name
        self.priority = priority

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_rule_id is not None:
            result['EgressProxyRuleId'] = self.egress_proxy_rule_id

        if self.egress_proxy_rule_name is not None:
            result['EgressProxyRuleName'] = self.egress_proxy_rule_name

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreDnsConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyRuleId') is not None:
            self.egress_proxy_rule_id = m.get('EgressProxyRuleId')

        if m.get('EgressProxyRuleName') is not None:
            self.egress_proxy_rule_name = m.get('EgressProxyRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPreDnsConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_operator: str = None,
        condition_values: List[str] = None,
    ):
        self.condition_key = condition_key
        self.condition_operator = condition_operator
        self.condition_values = condition_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_key is not None:
            result['ConditionKey'] = self.condition_key

        if self.condition_operator is not None:
            result['ConditionOperator'] = self.condition_operator

        if self.condition_values is not None:
            result['ConditionValues'] = self.condition_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionKey') is not None:
            self.condition_key = m.get('ConditionKey')

        if m.get('ConditionOperator') is not None:
            self.condition_operator = m.get('ConditionOperator')

        if m.get('ConditionValues') is not None:
            self.condition_values = m.get('ConditionValues')

        return self

class GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPostResponse(DaraModel):
    def __init__(
        self,
        action: str = None,
        conditions: List[main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPostResponseConditions] = None,
        create_time: str = None,
        description: str = None,
        egress_proxy_rule_id: str = None,
        egress_proxy_rule_name: str = None,
        priority: int = None,
    ):
        self.action = action
        self.conditions = conditions
        self.create_time = create_time
        self.description = description
        self.egress_proxy_rule_id = egress_proxy_rule_id
        self.egress_proxy_rule_name = egress_proxy_rule_name
        self.priority = priority

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_rule_id is not None:
            result['EgressProxyRuleId'] = self.egress_proxy_rule_id

        if self.egress_proxy_rule_name is not None:
            result['EgressProxyRuleName'] = self.egress_proxy_rule_name

        if self.priority is not None:
            result['Priority'] = self.priority

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPostResponseConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyRuleId') is not None:
            self.egress_proxy_rule_id = m.get('EgressProxyRuleId')

        if m.get('EgressProxyRuleName') is not None:
            self.egress_proxy_rule_name = m.get('EgressProxyRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        return self

class GetEgressProxyRuleGroupAttributeResponseBodyEgressProxyRulesPostResponseConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_operator: str = None,
        condition_values: List[str] = None,
    ):
        self.condition_key = condition_key
        self.condition_operator = condition_operator
        self.condition_values = condition_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition_key is not None:
            result['ConditionKey'] = self.condition_key

        if self.condition_operator is not None:
            result['ConditionOperator'] = self.condition_operator

        if self.condition_values is not None:
            result['ConditionValues'] = self.condition_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionKey') is not None:
            self.condition_key = m.get('ConditionKey')

        if m.get('ConditionOperator') is not None:
            self.condition_operator = m.get('ConditionOperator')

        if m.get('ConditionValues') is not None:
            self.condition_values = m.get('ConditionValues')

        return self

