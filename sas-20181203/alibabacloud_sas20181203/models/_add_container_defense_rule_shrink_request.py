# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AddContainerDefenseRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        rule_action: int = None,
        rule_id: int = None,
        rule_name: str = None,
        rule_switch: int = None,
        rule_type: int = None,
        scope: List[main_models.AddContainerDefenseRuleShrinkRequestScope] = None,
        whitelist_shrink: str = None,
    ):
        # The description.
        self.description = description
        # The action to take when the rule is matched. Valid values:
        # 
        # - **1**: Alert.
        # 
        # - **2**: Block.
        self.rule_action = rule_action
        # The rule ID. You do not need to specify this parameter when creating a rule.
        self.rule_id = rule_id
        # The rule name.
        self.rule_name = rule_name
        # The rule switch. Valid values:
        # 
        # - **0**: Disabled.
        # 
        # - **1**: Enabled.
        self.rule_switch = rule_switch
        # The rule type. Valid values:
        # - 2: user rule
        # 
        # >Notice: Only the value 2 is supported.
        self.rule_type = rule_type
        # The scope. This parameter is required. Specify at least one Scope entry, such as Scope.1.AllNamespace=1, which indicates that the rule applies to all namespaces. If this parameter is not specified, the API returns a 400 error.
        self.scope = scope
        # The whitelist.
        self.whitelist_shrink = whitelist_shrink

    def validate(self):
        if self.scope:
            for v1 in self.scope:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.rule_action is not None:
            result['RuleAction'] = self.rule_action

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_switch is not None:
            result['RuleSwitch'] = self.rule_switch

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        result['Scope'] = []
        if self.scope is not None:
            for k1 in self.scope:
                result['Scope'].append(k1.to_map() if k1 else None)

        if self.whitelist_shrink is not None:
            result['Whitelist'] = self.whitelist_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RuleAction') is not None:
            self.rule_action = m.get('RuleAction')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleSwitch') is not None:
            self.rule_switch = m.get('RuleSwitch')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        self.scope = []
        if m.get('Scope') is not None:
            for k1 in m.get('Scope'):
                temp_model = main_models.AddContainerDefenseRuleShrinkRequestScope()
                self.scope.append(temp_model.from_map(k1))

        if m.get('Whitelist') is not None:
            self.whitelist_shrink = m.get('Whitelist')

        return self

class AddContainerDefenseRuleShrinkRequestScope(DaraModel):
    def __init__(
        self,
        all_namespace: int = None,
        cluster_id: str = None,
        namespaces: List[str] = None,
    ):
        # Specifies whether to include all namespaces. Valid values:
        # 
        # - **0**: Specifies the namespaces to include by using the Namespaces parameter.
        # 
        # - **1**: Includes all namespaces.
        self.all_namespace = all_namespace
        # The cluster ID.
        # > You can call the [DescribeGroupedContainerInstances](https://help.aliyun.com/document_detail/182997.html) operation to obtain this parameter.
        self.cluster_id = cluster_id
        # The list of included namespaces.
        self.namespaces = namespaces

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_namespace is not None:
            result['AllNamespace'] = self.all_namespace

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllNamespace') is not None:
            self.all_namespace = m.get('AllNamespace')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')

        return self

