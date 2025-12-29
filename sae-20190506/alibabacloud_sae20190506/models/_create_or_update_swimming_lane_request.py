# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateSwimmingLaneRequest(DaraModel):
    def __init__(
        self,
        app_entry_rule: main_models.CreateOrUpdateSwimmingLaneRequestAppEntryRule = None,
        canary_model: int = None,
        enable: bool = None,
        group_id: int = None,
        lane_id: int = None,
        lane_name: str = None,
        lane_tag: str = None,
        mse_gateway_entry_rule: main_models.CreateOrUpdateSwimmingLaneRequestMseGatewayEntryRule = None,
        namespace_id: str = None,
    ):
        # The route configuration of the gateway.
        # 
        # >  This parameter is required if the gateway entry of the lane group is Java.
        self.app_entry_rule = app_entry_rule
        # Full-link Grayscale Mode:
        # 
        # *   0: The request is routed based on the content of the request.
        # *   1: routing based on percentages
        self.canary_model = canary_model
        # Lane Status
        # 
        # *   true: enabled
        # *   false: disabled
        self.enable = enable
        # The ID of the lane group to which the lane belongs.
        self.group_id = group_id
        # The ID of the lane.
        self.lane_id = lane_id
        # The name of the lane.
        self.lane_name = lane_name
        # The tag of the lane.
        self.lane_tag = lane_tag
        # The route configuration of the MSE gateway.
        # 
        # >  If the **EntryAppType** is set to **apig** or **mse-gw**, it is required.
        self.mse_gateway_entry_rule = mse_gateway_entry_rule
        # The namespace ID.
        self.namespace_id = namespace_id

    def validate(self):
        if self.app_entry_rule:
            self.app_entry_rule.validate()
        if self.mse_gateway_entry_rule:
            self.mse_gateway_entry_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_entry_rule is not None:
            result['AppEntryRule'] = self.app_entry_rule.to_map()

        if self.canary_model is not None:
            result['CanaryModel'] = self.canary_model

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.lane_id is not None:
            result['LaneId'] = self.lane_id

        if self.lane_name is not None:
            result['LaneName'] = self.lane_name

        if self.lane_tag is not None:
            result['LaneTag'] = self.lane_tag

        if self.mse_gateway_entry_rule is not None:
            result['MseGatewayEntryRule'] = self.mse_gateway_entry_rule.to_map()

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppEntryRule') is not None:
            temp_model = main_models.CreateOrUpdateSwimmingLaneRequestAppEntryRule()
            self.app_entry_rule = temp_model.from_map(m.get('AppEntryRule'))

        if m.get('CanaryModel') is not None:
            self.canary_model = m.get('CanaryModel')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')

        if m.get('LaneName') is not None:
            self.lane_name = m.get('LaneName')

        if m.get('LaneTag') is not None:
            self.lane_tag = m.get('LaneTag')

        if m.get('MseGatewayEntryRule') is not None:
            temp_model = main_models.CreateOrUpdateSwimmingLaneRequestMseGatewayEntryRule()
            self.mse_gateway_entry_rule = temp_model.from_map(m.get('MseGatewayEntryRule'))

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        return self

class CreateOrUpdateSwimmingLaneRequestMseGatewayEntryRule(DaraModel):
    def __init__(
        self,
        condition_joiner: str = None,
        conditions: List[main_models.CreateOrUpdateSwimmingLaneRequestMseGatewayEntryRuleConditions] = None,
        independent_percentage_enable: bool = None,
        percentage: int = None,
        percentage_by_route: Dict[str, int] = None,
        route_ids: List[int] = None,
    ):
        # Logical connectors between conditions:
        # 
        # *   AND: All conditions are met at the same time.
        # *   OR: Any condition is met.
        self.condition_joiner = condition_joiner
        # Routing Condition
        self.conditions = conditions
        # Whether to enable proportional grayscale.
        # 
        # *   true: Enabled. After you enable this parameter, you must configure the PercentageByPath.
        # *   false: Disabled.
        self.independent_percentage_enable = independent_percentage_enable
        # The percentage of traffic replication. Valid values: 0 to 100.
        self.percentage = percentage
        # The traffic configuration.
        self.percentage_by_route = percentage_by_route
        # The ID of the route.
        self.route_ids = route_ids

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
        if self.condition_joiner is not None:
            result['ConditionJoiner'] = self.condition_joiner

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.independent_percentage_enable is not None:
            result['IndependentPercentageEnable'] = self.independent_percentage_enable

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.percentage_by_route is not None:
            result['PercentageByRoute'] = self.percentage_by_route

        if self.route_ids is not None:
            result['RouteIds'] = self.route_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionJoiner') is not None:
            self.condition_joiner = m.get('ConditionJoiner')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.CreateOrUpdateSwimmingLaneRequestMseGatewayEntryRuleConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('IndependentPercentageEnable') is not None:
            self.independent_percentage_enable = m.get('IndependentPercentageEnable')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('PercentageByRoute') is not None:
            self.percentage_by_route = m.get('PercentageByRoute')

        if m.get('RouteIds') is not None:
            self.route_ids = m.get('RouteIds')

        return self

class CreateOrUpdateSwimmingLaneRequestMseGatewayEntryRuleConditions(DaraModel):
    def __init__(
        self,
        condition: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The matching rule.
        # 
        # *   \\==: exact match.
        # *   ! =: exact match.
        # *   in: contains matches.
        # *   Percentage: Percentage matching.
        # *   Regular matching: specifies whether a regular expression is used to search for the original string.
        self.condition = condition
        # The parameter name.
        self.name = name
        # The parameter type. Valid values:
        # 
        # *   header
        # *   param
        # *   Cookie: forwards requests based on cookies.
        self.type = type
        # The match value of the condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateOrUpdateSwimmingLaneRequestAppEntryRule(DaraModel):
    def __init__(
        self,
        condition_joiner: str = None,
        conditions: List[main_models.CreateOrUpdateSwimmingLaneRequestAppEntryRuleConditions] = None,
        independent_percentage_enable: bool = None,
        paths: List[str] = None,
        percentage: int = None,
        percentage_by_path: Dict[str, int] = None,
    ):
        # Logical connectors between conditions:
        # 
        # *   AND: All conditions are met at the same time.
        # *   OR: Any condition is met.
        self.condition_joiner = condition_joiner
        # The conditions that trigger circuit breaking.
        self.conditions = conditions
        # Whether to enable proportional grayscale.
        # 
        # *   true: enabled. After you enable this parameter, you must configure the PercentageByPath.
        # *   false: disables the service.
        self.independent_percentage_enable = independent_percentage_enable
        # The matched request path.
        self.paths = paths
        # The traffic ratio. Valid values: 0 to 100.
        self.percentage = percentage
        # The traffic configuration.
        self.percentage_by_path = percentage_by_path

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
        if self.condition_joiner is not None:
            result['ConditionJoiner'] = self.condition_joiner

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.independent_percentage_enable is not None:
            result['IndependentPercentageEnable'] = self.independent_percentage_enable

        if self.paths is not None:
            result['Paths'] = self.paths

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.percentage_by_path is not None:
            result['PercentageByPath'] = self.percentage_by_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionJoiner') is not None:
            self.condition_joiner = m.get('ConditionJoiner')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.CreateOrUpdateSwimmingLaneRequestAppEntryRuleConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('IndependentPercentageEnable') is not None:
            self.independent_percentage_enable = m.get('IndependentPercentageEnable')

        if m.get('Paths') is not None:
            self.paths = m.get('Paths')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('PercentageByPath') is not None:
            self.percentage_by_path = m.get('PercentageByPath')

        return self

class CreateOrUpdateSwimmingLaneRequestAppEntryRuleConditions(DaraModel):
    def __init__(
        self,
        condition: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # Matching Rule:
        # 
        # *   The exact match. The condition is met if the traffic value and the condition value are exactly the same.
        # *   The exact match. The condition is met if the traffic value and the condition value are exactly the same.
        # *   The inclusive match. The condition is met if the traffic value is included in the specified list.
        # *   The percentage match. Principle: The condition is met if \\"hash(get(`key`)) % 100 < value\\".
        # *   Regular match: a regular expression match. The condition is met when the match is based on regular expression rules.
        self.condition = condition
        # The parameter name.
        self.name = name
        # The parameter type. Valid values:
        # 
        # *   header
        # *   param
        # *   Cookie: forwards requests based on cookies.
        self.type = type
        # The match value of the condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

