# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateForwardingRulesRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        forwarding_rules: List[main_models.CreateForwardingRulesRequestForwardingRules] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The ID of the GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # This parameter is required.
        self.forwarding_rules = forwarding_rules
        # The ID of the listener.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.forwarding_rules:
            for v1 in self.forwarding_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['ForwardingRules'] = []
        if self.forwarding_rules is not None:
            for k1 in self.forwarding_rules:
                result['ForwardingRules'].append(k1.to_map() if k1 else None)

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.forwarding_rules = []
        if m.get('ForwardingRules') is not None:
            for k1 in m.get('ForwardingRules'):
                temp_model = main_models.CreateForwardingRulesRequestForwardingRules()
                self.forwarding_rules.append(temp_model.from_map(k1))

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateForwardingRulesRequestForwardingRules(DaraModel):
    def __init__(
        self,
        forwarding_rule_name: str = None,
        priority: int = None,
        rule_actions: List[main_models.CreateForwardingRulesRequestForwardingRulesRuleActions] = None,
        rule_conditions: List[main_models.CreateForwardingRulesRequestForwardingRulesRuleConditions] = None,
        rule_direction: str = None,
    ):
        self.forwarding_rule_name = forwarding_rule_name
        self.priority = priority
        # This parameter is required.
        self.rule_actions = rule_actions
        # This parameter is required.
        self.rule_conditions = rule_conditions
        self.rule_direction = rule_direction

    def validate(self):
        if self.rule_actions:
            for v1 in self.rule_actions:
                 if v1:
                    v1.validate()
        if self.rule_conditions:
            for v1 in self.rule_conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forwarding_rule_name is not None:
            result['ForwardingRuleName'] = self.forwarding_rule_name

        if self.priority is not None:
            result['Priority'] = self.priority

        result['RuleActions'] = []
        if self.rule_actions is not None:
            for k1 in self.rule_actions:
                result['RuleActions'].append(k1.to_map() if k1 else None)

        result['RuleConditions'] = []
        if self.rule_conditions is not None:
            for k1 in self.rule_conditions:
                result['RuleConditions'].append(k1.to_map() if k1 else None)

        if self.rule_direction is not None:
            result['RuleDirection'] = self.rule_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardingRuleName') is not None:
            self.forwarding_rule_name = m.get('ForwardingRuleName')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.rule_actions = []
        if m.get('RuleActions') is not None:
            for k1 in m.get('RuleActions'):
                temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleActions()
                self.rule_actions.append(temp_model.from_map(k1))

        self.rule_conditions = []
        if m.get('RuleConditions') is not None:
            for k1 in m.get('RuleConditions'):
                temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleConditions()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('RuleDirection') is not None:
            self.rule_direction = m.get('RuleDirection')

        return self

class CreateForwardingRulesRequestForwardingRulesRuleConditions(DaraModel):
    def __init__(
        self,
        host_config: main_models.CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig = None,
        path_config: main_models.CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig = None,
        rule_condition_type: str = None,
        rule_condition_value: str = None,
    ):
        self.host_config = host_config
        self.path_config = path_config
        self.rule_condition_type = rule_condition_type
        self.rule_condition_value = rule_condition_value

    def validate(self):
        if self.host_config:
            self.host_config.validate()
        if self.path_config:
            self.path_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_config is not None:
            result['HostConfig'] = self.host_config.to_map()

        if self.path_config is not None:
            result['PathConfig'] = self.path_config.to_map()

        if self.rule_condition_type is not None:
            result['RuleConditionType'] = self.rule_condition_type

        if self.rule_condition_value is not None:
            result['RuleConditionValue'] = self.rule_condition_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostConfig') is not None:
            temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig()
            self.host_config = temp_model.from_map(m.get('HostConfig'))

        if m.get('PathConfig') is not None:
            temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig()
            self.path_config = temp_model.from_map(m.get('PathConfig'))

        if m.get('RuleConditionType') is not None:
            self.rule_condition_type = m.get('RuleConditionType')

        if m.get('RuleConditionValue') is not None:
            self.rule_condition_value = m.get('RuleConditionValue')

        return self

class CreateForwardingRulesRequestForwardingRulesRuleConditionsPathConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class CreateForwardingRulesRequestForwardingRulesRuleConditionsHostConfig(DaraModel):
    def __init__(
        self,
        values: List[str] = None,
    ):
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class CreateForwardingRulesRequestForwardingRulesRuleActions(DaraModel):
    def __init__(
        self,
        forward_group_config: main_models.CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig = None,
        order: int = None,
        rule_action_type: str = None,
        rule_action_value: str = None,
    ):
        self.forward_group_config = forward_group_config
        # This parameter is required.
        self.order = order
        # This parameter is required.
        self.rule_action_type = rule_action_type
        self.rule_action_value = rule_action_value

    def validate(self):
        if self.forward_group_config:
            self.forward_group_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.forward_group_config is not None:
            result['ForwardGroupConfig'] = self.forward_group_config.to_map()

        if self.order is not None:
            result['Order'] = self.order

        if self.rule_action_type is not None:
            result['RuleActionType'] = self.rule_action_type

        if self.rule_action_value is not None:
            result['RuleActionValue'] = self.rule_action_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ForwardGroupConfig') is not None:
            temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig()
            self.forward_group_config = temp_model.from_map(m.get('ForwardGroupConfig'))

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('RuleActionType') is not None:
            self.rule_action_type = m.get('RuleActionType')

        if m.get('RuleActionValue') is not None:
            self.rule_action_value = m.get('RuleActionValue')

        return self

class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfig(DaraModel):
    def __init__(
        self,
        server_group_tuples: List[main_models.CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples] = None,
    ):
        # This parameter is required.
        self.server_group_tuples = server_group_tuples

    def validate(self):
        if self.server_group_tuples:
            for v1 in self.server_group_tuples:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ServerGroupTuples'] = []
        if self.server_group_tuples is not None:
            for k1 in self.server_group_tuples:
                result['ServerGroupTuples'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.server_group_tuples = []
        if m.get('ServerGroupTuples') is not None:
            for k1 in m.get('ServerGroupTuples'):
                temp_model = main_models.CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples()
                self.server_group_tuples.append(temp_model.from_map(k1))

        return self

class CreateForwardingRulesRequestForwardingRulesRuleActionsForwardGroupConfigServerGroupTuples(DaraModel):
    def __init__(
        self,
        endpoint_group_id: str = None,
    ):
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        return self

