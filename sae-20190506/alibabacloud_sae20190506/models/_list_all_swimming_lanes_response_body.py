# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListAllSwimmingLanesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListAllSwimmingLanesResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The interface status or POP error code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: Redirection.
        # *   **4xx**: Request error.
        # *   **5xx**: Server error.
        self.code = code
        # The output parameters of the node.
        self.data = data
        # Error code. Valid values:
        # 
        # *   If the request is successful, no **ErrorCode** fields are returned.
        # *   Request failed: **ErrorCode** fields are returned. For more information, see **Error codes**.
        self.error_code = error_code
        # Additional information. Valid values:
        # 
        # *   The error message returned because the request is normal and **success** is returned.
        # *   If the request is abnormal, the specific exception error code is returned.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Whether the data is successful. Valid values:
        # 
        # *   **true**: The application instances were restarted.
        # *   **false**: Restart failed.
        self.success = success
        # The ID of the trace. This parameter is used to query the exact call information.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAllSwimmingLanesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class ListAllSwimmingLanesResponseBodyData(DaraModel):
    def __init__(
        self,
        app_entry_rule: main_models.ListAllSwimmingLanesResponseBodyDataAppEntryRule = None,
        apps: List[main_models.ListAllSwimmingLanesResponseBodyDataApps] = None,
        canary_model: int = None,
        enable: bool = None,
        enable_rules: bool = None,
        lane_id: int = None,
        lane_name: str = None,
        lane_tag: str = None,
        mse_gateway_entry_rule: main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRule = None,
    ):
        # Apply ingress rules.
        self.app_entry_rule = app_entry_rule
        # The associated application.
        self.apps = apps
        # Full-link Grayscale Mode:
        # 
        # *   0: The request is routed based on the content of the request.
        # *   1: Proportional routing
        self.canary_model = canary_model
        # Lane status:
        # 
        # *   true: enabled
        # *   false: disabled
        self.enable = enable
        # Whether the traffic rule is enabled.
        self.enable_rules = enable_rules
        # The ID of the lane.
        self.lane_id = lane_id
        # The name of the lane group.
        self.lane_name = lane_name
        # The tag of the lane.
        self.lane_tag = lane_tag
        # MSE gateway routing
        self.mse_gateway_entry_rule = mse_gateway_entry_rule

    def validate(self):
        if self.app_entry_rule:
            self.app_entry_rule.validate()
        if self.apps:
            for v1 in self.apps:
                 if v1:
                    v1.validate()
        if self.mse_gateway_entry_rule:
            self.mse_gateway_entry_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_entry_rule is not None:
            result['AppEntryRule'] = self.app_entry_rule.to_map()

        result['Apps'] = []
        if self.apps is not None:
            for k1 in self.apps:
                result['Apps'].append(k1.to_map() if k1 else None)

        if self.canary_model is not None:
            result['CanaryModel'] = self.canary_model

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.enable_rules is not None:
            result['EnableRules'] = self.enable_rules

        if self.lane_id is not None:
            result['LaneId'] = self.lane_id

        if self.lane_name is not None:
            result['LaneName'] = self.lane_name

        if self.lane_tag is not None:
            result['LaneTag'] = self.lane_tag

        if self.mse_gateway_entry_rule is not None:
            result['MseGatewayEntryRule'] = self.mse_gateway_entry_rule.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppEntryRule') is not None:
            temp_model = main_models.ListAllSwimmingLanesResponseBodyDataAppEntryRule()
            self.app_entry_rule = temp_model.from_map(m.get('AppEntryRule'))

        self.apps = []
        if m.get('Apps') is not None:
            for k1 in m.get('Apps'):
                temp_model = main_models.ListAllSwimmingLanesResponseBodyDataApps()
                self.apps.append(temp_model.from_map(k1))

        if m.get('CanaryModel') is not None:
            self.canary_model = m.get('CanaryModel')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('EnableRules') is not None:
            self.enable_rules = m.get('EnableRules')

        if m.get('LaneId') is not None:
            self.lane_id = m.get('LaneId')

        if m.get('LaneName') is not None:
            self.lane_name = m.get('LaneName')

        if m.get('LaneTag') is not None:
            self.lane_tag = m.get('LaneTag')

        if m.get('MseGatewayEntryRule') is not None:
            temp_model = main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRule()
            self.mse_gateway_entry_rule = temp_model.from_map(m.get('MseGatewayEntryRule'))

        return self

class ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRule(DaraModel):
    def __init__(
        self,
        condition_joiner: str = None,
        conditions: List[main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleConditions] = None,
        independent_percentage_enable: bool = None,
        percentage: int = None,
        percentage_by_route: Dict[str, int] = None,
        route_ids: List[int] = None,
        routes: List[main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleRoutes] = None,
    ):
        # The logical connector between conditions.
        self.condition_joiner = condition_joiner
        # The matching condition.
        self.conditions = conditions
        # Whether to enable proportional grayscale.
        self.independent_percentage_enable = independent_percentage_enable
        # The proportion of path traffic.
        self.percentage = percentage
        # The traffic configuration.
        self.percentage_by_route = percentage_by_route
        # The IDs of the route tables.
        self.route_ids = route_ids
        # The detailed configuration of the routing rule.
        self.routes = routes

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.routes:
            for v1 in self.routes:
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

        result['Routes'] = []
        if self.routes is not None:
            for k1 in self.routes:
                result['Routes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConditionJoiner') is not None:
            self.condition_joiner = m.get('ConditionJoiner')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('IndependentPercentageEnable') is not None:
            self.independent_percentage_enable = m.get('IndependentPercentageEnable')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('PercentageByRoute') is not None:
            self.percentage_by_route = m.get('PercentageByRoute')

        if m.get('RouteIds') is not None:
            self.route_ids = m.get('RouteIds')

        self.routes = []
        if m.get('Routes') is not None:
            for k1 in m.get('Routes'):
                temp_model = main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleRoutes()
                self.routes.append(temp_model.from_map(k1))

        return self

class ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleRoutes(DaraModel):
    def __init__(
        self,
        route_id: int = None,
        route_name: str = None,
        route_predicate: main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleRoutesRoutePredicate = None,
    ):
        # The route ID.
        self.route_id = route_id
        # The name of the route.
        self.route_name = route_name
        # The routing rule.
        self.route_predicate = route_predicate

    def validate(self):
        if self.route_predicate:
            self.route_predicate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_id is not None:
            result['RouteId'] = self.route_id

        if self.route_name is not None:
            result['RouteName'] = self.route_name

        if self.route_predicate is not None:
            result['RoutePredicate'] = self.route_predicate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')

        if m.get('RoutePredicate') is not None:
            temp_model = main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleRoutesRoutePredicate()
            self.route_predicate = temp_model.from_map(m.get('RoutePredicate'))

        return self

class ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleRoutesRoutePredicate(DaraModel):
    def __init__(
        self,
        path_predicate: main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleRoutesRoutePredicatePathPredicate = None,
    ):
        # The path matching rule.
        self.path_predicate = path_predicate

    def validate(self):
        if self.path_predicate:
            self.path_predicate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path_predicate is not None:
            result['PathPredicate'] = self.path_predicate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PathPredicate') is not None:
            temp_model = main_models.ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleRoutesRoutePredicatePathPredicate()
            self.path_predicate = temp_model.from_map(m.get('PathPredicate'))

        return self

class ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleRoutesRoutePredicatePathPredicate(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The path.
        self.path = path
        # The matching rule.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['path'] = self.path

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListAllSwimmingLanesResponseBodyDataMseGatewayEntryRuleConditions(DaraModel):
    def __init__(
        self,
        condition: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
    ):
        # The matching rule.
        self.condition = condition
        # The parameter name.
        self.name = name
        # The type of the parameter.
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

class ListAllSwimmingLanesResponseBodyDataApps(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        mse_app_id: str = None,
        mse_app_name: str = None,
        mse_namespace_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The name of the application.
        self.app_name = app_name
        # The ID of the MSE instance.
        self.mse_app_id = mse_app_id
        # The name of the MSE instance.
        self.mse_app_name = mse_app_name
        # The ID of the namespace to which the MSE instance belongs.
        self.mse_namespace_id = mse_namespace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.mse_app_id is not None:
            result['MseAppId'] = self.mse_app_id

        if self.mse_app_name is not None:
            result['MseAppName'] = self.mse_app_name

        if self.mse_namespace_id is not None:
            result['MseNamespaceId'] = self.mse_namespace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('MseAppId') is not None:
            self.mse_app_id = m.get('MseAppId')

        if m.get('MseAppName') is not None:
            self.mse_app_name = m.get('MseAppName')

        if m.get('MseNamespaceId') is not None:
            self.mse_namespace_id = m.get('MseNamespaceId')

        return self

class ListAllSwimmingLanesResponseBodyDataAppEntryRule(DaraModel):
    def __init__(
        self,
        condition_joiner: str = None,
        conditions: List[main_models.ListAllSwimmingLanesResponseBodyDataAppEntryRuleConditions] = None,
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
        # The matching condition.
        self.conditions = conditions
        # Whether to enable proportional grayscale.
        self.independent_percentage_enable = independent_percentage_enable
        # The request path.
        self.paths = paths
        # The traffic ratio. Valid values: 0 to 100.
        self.percentage = percentage
        # Traffic matching.
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
                temp_model = main_models.ListAllSwimmingLanesResponseBodyDataAppEntryRuleConditions()
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

class ListAllSwimmingLanesResponseBodyDataAppEntryRuleConditions(DaraModel):
    def __init__(
        self,
        condition: str = None,
        name: str = None,
        type: str = None,
        value: str = None,
        values: List[str] = None,
    ):
        # The matching rule.
        self.condition = condition
        # The parameter name.
        self.name = name
        # The type of the parameter.
        self.type = type
        # The match value.
        self.value = value
        # The match value of the condition.
        self.values = values

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

        if self.values is not None:
            result['Values'] = self.values

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

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

