# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class PdpLane(DaraModel):
    def __init__(
        self,
        alias: str = None,
        company_id: int = None,
        creator_name: str = None,
        creator_uid: str = None,
        custome_marking_rules: str = None,
        description: str = None,
        env: str = None,
        id: int = None,
        init_group_flag: bool = None,
        inlet_services: List[main_models.PdpServiceInfo] = None,
        marking_rule_type: str = None,
        name: str = None,
        product_id: int = None,
        product_name: str = None,
        request_id: str = None,
        rule_conditions: List[main_models.RuleCondition] = None,
        rule_connect_type: str = None,
        service_groups: List[main_models.ServiceGroupInfo] = None,
        type: str = None,
    ):
        self.alias = alias
        self.company_id = company_id
        self.creator_name = creator_name
        self.creator_uid = creator_uid
        # This parameter is required.
        self.custome_marking_rules = custome_marking_rules
        self.description = description
        self.env = env
        self.id = id
        self.init_group_flag = init_group_flag
        self.inlet_services = inlet_services
        # This parameter is required.
        self.marking_rule_type = marking_rule_type
        self.name = name
        self.product_id = product_id
        self.product_name = product_name
        self.request_id = request_id
        self.rule_conditions = rule_conditions
        self.rule_connect_type = rule_connect_type
        self.service_groups = service_groups
        self.type = type

    def validate(self):
        if self.inlet_services:
            for v1 in self.inlet_services:
                 if v1:
                    v1.validate()
        if self.rule_conditions:
            for v1 in self.rule_conditions:
                 if v1:
                    v1.validate()
        if self.service_groups:
            for v1 in self.service_groups:
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

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.creator_uid is not None:
            result['creatorUid'] = self.creator_uid

        if self.custome_marking_rules is not None:
            result['customeMarkingRules'] = self.custome_marking_rules

        if self.description is not None:
            result['description'] = self.description

        if self.env is not None:
            result['env'] = self.env

        if self.id is not None:
            result['id'] = self.id

        if self.init_group_flag is not None:
            result['initGroupFlag'] = self.init_group_flag

        result['inletServices'] = []
        if self.inlet_services is not None:
            for k1 in self.inlet_services:
                result['inletServices'].append(k1.to_map() if k1 else None)

        if self.marking_rule_type is not None:
            result['markingRuleType'] = self.marking_rule_type

        if self.name is not None:
            result['name'] = self.name

        if self.product_id is not None:
            result['productId'] = self.product_id

        if self.product_name is not None:
            result['productName'] = self.product_name

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['ruleConditions'] = []
        if self.rule_conditions is not None:
            for k1 in self.rule_conditions:
                result['ruleConditions'].append(k1.to_map() if k1 else None)

        if self.rule_connect_type is not None:
            result['ruleConnectType'] = self.rule_connect_type

        result['serviceGroups'] = []
        if self.service_groups is not None:
            for k1 in self.service_groups:
                result['serviceGroups'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('creatorUid') is not None:
            self.creator_uid = m.get('creatorUid')

        if m.get('customeMarkingRules') is not None:
            self.custome_marking_rules = m.get('customeMarkingRules')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('env') is not None:
            self.env = m.get('env')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('initGroupFlag') is not None:
            self.init_group_flag = m.get('initGroupFlag')

        self.inlet_services = []
        if m.get('inletServices') is not None:
            for k1 in m.get('inletServices'):
                temp_model = main_models.PdpServiceInfo()
                self.inlet_services.append(temp_model.from_map(k1))

        if m.get('markingRuleType') is not None:
            self.marking_rule_type = m.get('markingRuleType')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('productId') is not None:
            self.product_id = m.get('productId')

        if m.get('productName') is not None:
            self.product_name = m.get('productName')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.rule_conditions = []
        if m.get('ruleConditions') is not None:
            for k1 in m.get('ruleConditions'):
                temp_model = main_models.RuleCondition()
                self.rule_conditions.append(temp_model.from_map(k1))

        if m.get('ruleConnectType') is not None:
            self.rule_connect_type = m.get('ruleConnectType')

        self.service_groups = []
        if m.get('serviceGroups') is not None:
            for k1 in m.get('serviceGroups'):
                temp_model = main_models.ServiceGroupInfo()
                self.service_groups.append(temp_model.from_map(k1))

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

