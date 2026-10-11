# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_epg20260715 import models as main_models
from darabonba.model import DaraModel

class UpdateEgressProxyRulesAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_proxy_rule_group_id: str = None,
        egress_proxy_rules: List[main_models.UpdateEgressProxyRulesAttributeRequestEgressProxyRules] = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        # This parameter is required.
        self.egress_proxy_rule_group_id = egress_proxy_rule_group_id
        # This parameter is required.
        self.egress_proxy_rules = egress_proxy_rules

    def validate(self):
        if self.egress_proxy_rules:
            for v1 in self.egress_proxy_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_rule_group_id is not None:
            result['EgressProxyRuleGroupId'] = self.egress_proxy_rule_group_id

        result['EgressProxyRules'] = []
        if self.egress_proxy_rules is not None:
            for k1 in self.egress_proxy_rules:
                result['EgressProxyRules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyRuleGroupId') is not None:
            self.egress_proxy_rule_group_id = m.get('EgressProxyRuleGroupId')

        self.egress_proxy_rules = []
        if m.get('EgressProxyRules') is not None:
            for k1 in m.get('EgressProxyRules'):
                temp_model = main_models.UpdateEgressProxyRulesAttributeRequestEgressProxyRules()
                self.egress_proxy_rules.append(temp_model.from_map(k1))

        return self

class UpdateEgressProxyRulesAttributeRequestEgressProxyRules(DaraModel):
    def __init__(
        self,
        action: str = None,
        add_conditions: List[main_models.UpdateEgressProxyRulesAttributeRequestEgressProxyRulesAddConditions] = None,
        description: str = None,
        egress_proxy_rule_id: str = None,
        egress_proxy_rule_name: str = None,
        priority: int = None,
        remove_conditions: List[main_models.UpdateEgressProxyRulesAttributeRequestEgressProxyRulesRemoveConditions] = None,
    ):
        self.action = action
        self.add_conditions = add_conditions
        self.description = description
        # This parameter is required.
        self.egress_proxy_rule_id = egress_proxy_rule_id
        self.egress_proxy_rule_name = egress_proxy_rule_name
        self.priority = priority
        self.remove_conditions = remove_conditions

    def validate(self):
        if self.add_conditions:
            for v1 in self.add_conditions:
                 if v1:
                    v1.validate()
        if self.remove_conditions:
            for v1 in self.remove_conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        result['AddConditions'] = []
        if self.add_conditions is not None:
            for k1 in self.add_conditions:
                result['AddConditions'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.egress_proxy_rule_id is not None:
            result['EgressProxyRuleId'] = self.egress_proxy_rule_id

        if self.egress_proxy_rule_name is not None:
            result['EgressProxyRuleName'] = self.egress_proxy_rule_name

        if self.priority is not None:
            result['Priority'] = self.priority

        result['RemoveConditions'] = []
        if self.remove_conditions is not None:
            for k1 in self.remove_conditions:
                result['RemoveConditions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        self.add_conditions = []
        if m.get('AddConditions') is not None:
            for k1 in m.get('AddConditions'):
                temp_model = main_models.UpdateEgressProxyRulesAttributeRequestEgressProxyRulesAddConditions()
                self.add_conditions.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EgressProxyRuleId') is not None:
            self.egress_proxy_rule_id = m.get('EgressProxyRuleId')

        if m.get('EgressProxyRuleName') is not None:
            self.egress_proxy_rule_name = m.get('EgressProxyRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.remove_conditions = []
        if m.get('RemoveConditions') is not None:
            for k1 in m.get('RemoveConditions'):
                temp_model = main_models.UpdateEgressProxyRulesAttributeRequestEgressProxyRulesRemoveConditions()
                self.remove_conditions.append(temp_model.from_map(k1))

        return self

class UpdateEgressProxyRulesAttributeRequestEgressProxyRulesRemoveConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_operator: str = None,
        condition_values: List[str] = None,
    ):
        # This parameter is required.
        self.condition_key = condition_key
        # This parameter is required.
        self.condition_operator = condition_operator
        # This parameter is required.
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

class UpdateEgressProxyRulesAttributeRequestEgressProxyRulesAddConditions(DaraModel):
    def __init__(
        self,
        condition_key: str = None,
        condition_operator: str = None,
        condition_values: List[str] = None,
    ):
        # This parameter is required.
        self.condition_key = condition_key
        # This parameter is required.
        self.condition_operator = condition_operator
        # This parameter is required.
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

