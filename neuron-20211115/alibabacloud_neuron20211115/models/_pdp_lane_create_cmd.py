# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class PdpLaneCreateCmd(DaraModel):
    def __init__(
        self,
        alias: str = None,
        company_id: int = None,
        creator_uid: str = None,
        custome_marking_rules: str = None,
        description: str = None,
        env: str = None,
        init_group_flag: bool = None,
        inlet_service_ids: str = None,
        marking_rule_type: str = None,
        name: str = None,
        product_id: int = None,
        rule_conditions: List[main_models.RuleCondition] = None,
        rule_connect_type: str = None,
        service_group_ids: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.alias = alias
        # This parameter is required.
        self.company_id = company_id
        # This parameter is required.
        self.creator_uid = creator_uid
        self.custome_marking_rules = custome_marking_rules
        self.description = description
        # This parameter is required.
        self.env = env
        self.init_group_flag = init_group_flag
        self.inlet_service_ids = inlet_service_ids
        # This parameter is required.
        self.marking_rule_type = marking_rule_type
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.product_id = product_id
        self.rule_conditions = rule_conditions
        self.rule_connect_type = rule_connect_type
        self.service_group_ids = service_group_ids
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.rule_conditions:
            for v1 in self.rule_conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.creator_uid is not None:
            result['creatorUid'] = self.creator_uid

        if self.custome_marking_rules is not None:
            result['customeMarkingRules'] = self.custome_marking_rules

        if self.description is not None:
            result['description'] = self.description

        if self.env is not None:
            result['env'] = self.env

        if self.init_group_flag is not None:
            result['initGroupFlag'] = self.init_group_flag

        if self.inlet_service_ids is not None:
            result['inletServiceIds'] = self.inlet_service_ids

        if self.marking_rule_type is not None:
            result['markingRuleType'] = self.marking_rule_type

        if self.name is not None:
            result['name'] = self.name

        if self.product_id is not None:
            result['productId'] = self.product_id

        result['ruleConditions'] = []
        if self.rule_conditions is not None:
            for k1 in self.rule_conditions:
                result['ruleConditions'].append(k1.to_map() if k1 else None)

        if self.rule_connect_type is not None:
            result['ruleConnectType'] = self.rule_connect_type

        if self.service_group_ids is not None:
            result['serviceGroupIds'] = self.service_group_ids

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('creatorUid') is not None:
            self.creator_uid = m.get('creatorUid')

        if m.get('customeMarkingRules') is not None:
            self.custome_marking_rules = m.get('customeMarkingRules')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('initGroupFlag') is not None:
            self.init_group_flag = m.get('initGroupFlag')

        if m.get('inletServiceIds') is not None:
            self.inlet_service_ids = m.get('inletServiceIds')

        if m.get('markingRuleType') is not None:
            self.marking_rule_type = m.get('markingRuleType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        self.rule_conditions = []
        if m.get('ruleConditions') is not None:
            for k1 in m.get('ruleConditions'):
                temp_model = main_models.RuleCondition()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('ruleConnectType') is not None:
            self.rule_connect_type = m.get('ruleConnectType')

        if m.get('serviceGroupIds') is not None:
            self.service_group_ids = m.get('serviceGroupIds')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

