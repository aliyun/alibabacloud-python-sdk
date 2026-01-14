# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateSwimmingLaneShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        enable: bool = None,
        enable_rules: bool = None,
        entry_rule: str = None,
        entry_rules: List[main_models.CreateOrUpdateSwimmingLaneShrinkRequestEntryRules] = None,
        gateway_swimming_lane_route_json_shrink: str = None,
        group_id: int = None,
        id: int = None,
        name: str = None,
        namespace: str = None,
        path_independent_percentage_enable: bool = None,
        region_id: str = None,
        tag: str = None,
    ):
        # The language of the response. Valid values: zh and en. Default value: zh. The value zh indicates Chinese, and the value en indicates English.
        self.accept_language = accept_language
        # Specifies whether to enable the lane.
        self.enable = enable
        # Specifies whether to configure a routing rule for the lane. If an Ingress gateway is used, this parameter is not required.
        self.enable_rules = enable_rules
        # The JSON string.
        self.entry_rule = entry_rule
        self.entry_rules = entry_rules
        # The information about the routing rule for the gateway. This parameter is required when a cloud-native gateway is used as the ingress.
        self.gateway_swimming_lane_route_json_shrink = gateway_swimming_lane_route_json_shrink
        # The language of the response. Valid values:****
        # 
        # *   **zh-CN**: Chinese
        # *   **en-US**: English
        # 
        # > Default value: **zh-CN**.
        self.group_id = group_id
        # The ID of the primary key. The value -1 indicates a request that is used to create a lane. A value greater than 0 indicates a request that is used to modify a lane.
        self.id = id
        # The name of the lane.
        # 
        # This parameter is required.
        self.name = name
        self.namespace = namespace
        self.path_independent_percentage_enable = path_independent_percentage_enable
        # The ID of the region.
        self.region_id = region_id
        # The tag.
        self.tag = tag

    def validate(self):
        if self.entry_rules:
            for v1 in self.entry_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.enable_rules is not None:
            result['EnableRules'] = self.enable_rules

        if self.entry_rule is not None:
            result['EntryRule'] = self.entry_rule

        result['EntryRules'] = []
        if self.entry_rules is not None:
            for k1 in self.entry_rules:
                result['EntryRules'].append(k1.to_map() if k1 else None)

        if self.gateway_swimming_lane_route_json_shrink is not None:
            result['GatewaySwimmingLaneRouteJson'] = self.gateway_swimming_lane_route_json_shrink

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.path_independent_percentage_enable is not None:
            result['PathIndependentPercentageEnable'] = self.path_independent_percentage_enable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tag is not None:
            result['Tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EnableRules') is not None:
            self.enable_rules = m.get('EnableRules')

        if m.get('EntryRule') is not None:
            self.entry_rule = m.get('EntryRule')

        self.entry_rules = []
        if m.get('EntryRules') is not None:
            for k1 in m.get('EntryRules'):
                temp_model = main_models.CreateOrUpdateSwimmingLaneShrinkRequestEntryRules()
                self.entry_rules.append(temp_model.from_map(k1))

        if m.get('GatewaySwimmingLaneRouteJson') is not None:
            self.gateway_swimming_lane_route_json_shrink = m.get('GatewaySwimmingLaneRouteJson')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PathIndependentPercentageEnable') is not None:
            self.path_independent_percentage_enable = m.get('PathIndependentPercentageEnable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        return self

class CreateOrUpdateSwimmingLaneShrinkRequestEntryRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        paths: List[str] = None,
        priority: int = None,
        rest_items: List[main_models.CreateOrUpdateSwimmingLaneShrinkRequestEntryRulesRestItems] = None,
    ):
        self.condition = condition
        self.paths = paths
        self.priority = priority
        self.rest_items = rest_items

    def validate(self):
        if self.rest_items:
            for v1 in self.rest_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.priority is not None:
            result['Priority'] = self.priority

        result['RestItems'] = []
        if self.rest_items is not None:
            for k1 in self.rest_items:
                result['RestItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.rest_items = []
        if m.get('RestItems') is not None:
            for k1 in m.get('RestItems'):
                temp_model = main_models.CreateOrUpdateSwimmingLaneShrinkRequestEntryRulesRestItems()
                self.rest_items.append(temp_model.from_map(k1))

        return self

class CreateOrUpdateSwimmingLaneShrinkRequestEntryRulesRestItems(DaraModel):
    def __init__(
        self,
        cond: str = None,
        datum: str = None,
        divisor: int = None,
        name: str = None,
        name_list: List[str] = None,
        operator: str = None,
        rate: int = None,
        remainder: int = None,
        type: str = None,
        value: str = None,
    ):
        self.cond = cond
        self.datum = datum
        self.divisor = divisor
        self.name = name
        self.name_list = name_list
        self.operator = operator
        self.rate = rate
        self.remainder = remainder
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cond is not None:
            result['Cond'] = self.cond

        if self.datum is not None:
            result['Datum'] = self.datum

        if self.divisor is not None:
            result['Divisor'] = self.divisor

        if self.name is not None:
            result['Name'] = self.name

        if self.name_list is not None:
            result['NameList'] = self.name_list

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.rate is not None:
            result['Rate'] = self.rate

        if self.remainder is not None:
            result['Remainder'] = self.remainder

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cond') is not None:
            self.cond = m.get('Cond')

        if m.get('Datum') is not None:
            self.datum = m.get('Datum')

        if m.get('Divisor') is not None:
            self.divisor = m.get('Divisor')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Rate') is not None:
            self.rate = m.get('Rate')

        if m.get('Remainder') is not None:
            self.remainder = m.get('Remainder')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

