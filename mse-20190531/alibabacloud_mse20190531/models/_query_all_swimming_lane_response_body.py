# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QueryAllSwimmingLaneResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryAllSwimmingLaneResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details of the data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The returned message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryAllSwimmingLaneResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAllSwimmingLaneResponseBodyData(DaraModel):
    def __init__(
        self,
        enable: str = None,
        entry_rules: List[main_models.QueryAllSwimmingLaneResponseBodyDataEntryRules] = None,
        gateway_swimming_lane_route: main_models.QueryAllSwimmingLaneResponseBodyDataGatewaySwimmingLaneRoute = None,
        gateway_swimming_lane_route_json: str = None,
        group_id: str = None,
        id: int = None,
        message_queue_filter_side: str = None,
        message_queue_gray_enable: bool = None,
        name: str = None,
        namespace: str = None,
        path_independent_percentage_enable: bool = None,
        record_canary_detail: bool = None,
        region_id: str = None,
        tag: str = None,
        user_id: str = None,
        enable_rules: bool = None,
        gmt_create: str = None,
        gmt_modified: str = None,
    ):
        # 是否开启。
        self.enable = enable
        # The ingress application rules.
        self.entry_rules = entry_rules
        # 网关路由信息（使用云原生网关为入口时使用）
        self.gateway_swimming_lane_route = gateway_swimming_lane_route
        self.gateway_swimming_lane_route_json = gateway_swimming_lane_route_json
        # The ID of the lane group.
        self.group_id = group_id
        # The ID of the lane group.
        self.id = id
        # The side on which canary release for messaging is implemented.
        self.message_queue_filter_side = message_queue_filter_side
        # Indicates whether canary release for messaging is enabled.
        self.message_queue_gray_enable = message_queue_gray_enable
        # The name of the lane group.
        self.name = name
        # The Microservices Engine (MSE) namespace to which the lane belongs.
        self.namespace = namespace
        self.path_independent_percentage_enable = path_independent_percentage_enable
        # Indicates whether request details were recorded (metrics of end-to-end canary release).
        self.record_canary_detail = record_canary_detail
        # The region ID.
        self.region_id = region_id
        # The tag of the lane.
        self.tag = tag
        # The user ID of the lane group.
        self.user_id = user_id
        # Indicates whether the rule is enabled.
        self.enable_rules = enable_rules
        # The time when the lane was created.
        self.gmt_create = gmt_create
        # The time when the lane was updated.
        self.gmt_modified = gmt_modified

    def validate(self):
        if self.entry_rules:
            for v1 in self.entry_rules:
                 if v1:
                    v1.validate()
        if self.gateway_swimming_lane_route:
            self.gateway_swimming_lane_route.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['Enable'] = self.enable

        result['EntryRules'] = []
        if self.entry_rules is not None:
            for k1 in self.entry_rules:
                result['EntryRules'].append(k1.to_map() if k1 else None)

        if self.gateway_swimming_lane_route is not None:
            result['GatewaySwimmingLaneRoute'] = self.gateway_swimming_lane_route.to_map()

        if self.gateway_swimming_lane_route_json is not None:
            result['GatewaySwimmingLaneRouteJson'] = self.gateway_swimming_lane_route_json

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.id is not None:
            result['Id'] = self.id

        if self.message_queue_filter_side is not None:
            result['MessageQueueFilterSide'] = self.message_queue_filter_side

        if self.message_queue_gray_enable is not None:
            result['MessageQueueGrayEnable'] = self.message_queue_gray_enable

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.path_independent_percentage_enable is not None:
            result['PathIndependentPercentageEnable'] = self.path_independent_percentage_enable

        if self.record_canary_detail is not None:
            result['RecordCanaryDetail'] = self.record_canary_detail

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.tag is not None:
            result['Tag'] = self.tag

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.enable_rules is not None:
            result['enableRules'] = self.enable_rules

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        self.entry_rules = []
        if m.get('EntryRules') is not None:
            for k1 in m.get('EntryRules'):
                temp_model = main_models.QueryAllSwimmingLaneResponseBodyDataEntryRules()
                self.entry_rules.append(temp_model.from_map(k1))

        if m.get('GatewaySwimmingLaneRoute') is not None:
            temp_model = main_models.QueryAllSwimmingLaneResponseBodyDataGatewaySwimmingLaneRoute()
            self.gateway_swimming_lane_route = temp_model.from_map(m.get('GatewaySwimmingLaneRoute'))

        if m.get('GatewaySwimmingLaneRouteJson') is not None:
            self.gateway_swimming_lane_route_json = m.get('GatewaySwimmingLaneRouteJson')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MessageQueueFilterSide') is not None:
            self.message_queue_filter_side = m.get('MessageQueueFilterSide')

        if m.get('MessageQueueGrayEnable') is not None:
            self.message_queue_gray_enable = m.get('MessageQueueGrayEnable')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PathIndependentPercentageEnable') is not None:
            self.path_independent_percentage_enable = m.get('PathIndependentPercentageEnable')

        if m.get('RecordCanaryDetail') is not None:
            self.record_canary_detail = m.get('RecordCanaryDetail')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Tag') is not None:
            self.tag = m.get('Tag')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('enableRules') is not None:
            self.enable_rules = m.get('enableRules')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        return self

class QueryAllSwimmingLaneResponseBodyDataGatewaySwimmingLaneRoute(DaraModel):
    def __init__(
        self,
        canary_model: int = None,
        condition: str = None,
        conditions: List[main_models.QueryAllSwimmingLaneResponseBodyDataGatewaySwimmingLaneRouteConditions] = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        percentage: int = None,
        route_id_list: List[int] = None,
        route_independent_percentage_enable: str = None,
        route_independent_percentage_list: List[main_models.QueryAllSwimmingLaneResponseBodyDataGatewaySwimmingLaneRouteRouteIndependentPercentageList] = None,
    ):
        # 全链路灰度模式：
        # 
        # - 0: 按请求内容路由
        # 
        # - 1: 按比例路由
        self.canary_model = canary_model
        self.condition = condition
        # 匹配条件列表（按内容路由使用）
        self.conditions = conditions
        # 网关ID
        self.gateway_id = gateway_id
        # 网关唯一ID
        self.gateway_unique_id = gateway_unique_id
        # 流量比例（按比例路由使用，取值0-100）
        self.percentage = percentage
        # 路由ID列表
        self.route_id_list = route_id_list
        self.route_independent_percentage_enable = route_independent_percentage_enable
        self.route_independent_percentage_list = route_independent_percentage_list

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()
        if self.route_independent_percentage_list:
            for v1 in self.route_independent_percentage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.canary_model is not None:
            result['CanaryModel'] = self.canary_model

        if self.condition is not None:
            result['Condition'] = self.condition

        result['Conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['Conditions'].append(k1.to_map() if k1 else None)

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.route_id_list is not None:
            result['RouteIdList'] = self.route_id_list

        if self.route_independent_percentage_enable is not None:
            result['RouteIndependentPercentageEnable'] = self.route_independent_percentage_enable

        result['RouteIndependentPercentageList'] = []
        if self.route_independent_percentage_list is not None:
            for k1 in self.route_independent_percentage_list:
                result['RouteIndependentPercentageList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanaryModel') is not None:
            self.canary_model = m.get('CanaryModel')

        if m.get('Condition') is not None:
            self.condition = m.get('Condition')

        self.conditions = []
        if m.get('Conditions') is not None:
            for k1 in m.get('Conditions'):
                temp_model = main_models.QueryAllSwimmingLaneResponseBodyDataGatewaySwimmingLaneRouteConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('RouteIdList') is not None:
            self.route_id_list = m.get('RouteIdList')

        if m.get('RouteIndependentPercentageEnable') is not None:
            self.route_independent_percentage_enable = m.get('RouteIndependentPercentageEnable')

        self.route_independent_percentage_list = []
        if m.get('RouteIndependentPercentageList') is not None:
            for k1 in m.get('RouteIndependentPercentageList'):
                temp_model = main_models.QueryAllSwimmingLaneResponseBodyDataGatewaySwimmingLaneRouteRouteIndependentPercentageList()
                self.route_independent_percentage_list.append(temp_model.from_map(k1))

        return self

class QueryAllSwimmingLaneResponseBodyDataGatewaySwimmingLaneRouteRouteIndependentPercentageList(DaraModel):
    def __init__(
        self,
        percentage: str = None,
        route_id: str = None,
    ):
        self.percentage = percentage
        self.route_id = route_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.percentage is not None:
            result['Percentage'] = self.percentage

        if self.route_id is not None:
            result['RouteId'] = self.route_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')

        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        return self

class QueryAllSwimmingLaneResponseBodyDataGatewaySwimmingLaneRouteConditions(DaraModel):
    def __init__(
        self,
        cond: str = None,
        name: str = None,
        name_list: List[str] = None,
        type: str = None,
        value: str = None,
    ):
        # 条件：
        # - PRE：前缀匹配
        # - EQUAL：精确匹配
        # - ERGULAR：正则匹配
        self.cond = cond
        # 参数名称
        self.name = name
        # NameList
        self.name_list = name_list
        # 参数类型：
        # - header：Header
        # - param：Parameter
        self.type = type
        # 参数值
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

        if self.name is not None:
            result['Name'] = self.name

        if self.name_list is not None:
            result['NameList'] = self.name_list

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cond') is not None:
            self.cond = m.get('Cond')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NameList') is not None:
            self.name_list = m.get('NameList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class QueryAllSwimmingLaneResponseBodyDataEntryRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        path: str = None,
        paths: List[str] = None,
        rest_items: List[main_models.QueryAllSwimmingLaneResponseBodyDataEntryRulesRestItems] = None,
    ):
        # The condition.
        self.condition = condition
        # The path.
        self.path = path
        # The paths.
        self.paths = paths
        # The RESTful matching rules.
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
            result['condition'] = self.condition

        if self.path is not None:
            result['path'] = self.path

        if self.paths is not None:
            result['paths'] = self.paths

        result['restItems'] = []
        if self.rest_items is not None:
            for k1 in self.rest_items:
                result['restItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('condition') is not None:
            self.condition = m.get('condition')

        if m.get('path') is not None:
            self.path = m.get('path')

        if m.get('paths') is not None:
            self.paths = m.get('paths')

        self.rest_items = []
        if m.get('restItems') is not None:
            for k1 in m.get('restItems'):
                temp_model = main_models.QueryAllSwimmingLaneResponseBodyDataEntryRulesRestItems()
                self.rest_items.append(temp_model.from_map(k1))

        return self

class QueryAllSwimmingLaneResponseBodyDataEntryRulesRestItems(DaraModel):
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
        # The matching character.
        self.cond = cond
        # The value.
        self.datum = datum
        # The divisor.
        self.divisor = divisor
        # The name of the matching rule.
        self.name = name
        # The matching list.
        self.name_list = name_list
        # The operator.
        self.operator = operator
        # The percentage.
        self.rate = rate
        # The remainder.
        self.remainder = remainder
        # The matching type.
        self.type = type
        # The value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cond is not None:
            result['cond'] = self.cond

        if self.datum is not None:
            result['datum'] = self.datum

        if self.divisor is not None:
            result['divisor'] = self.divisor

        if self.name is not None:
            result['name'] = self.name

        if self.name_list is not None:
            result['nameList'] = self.name_list

        if self.operator is not None:
            result['operator'] = self.operator

        if self.rate is not None:
            result['rate'] = self.rate

        if self.remainder is not None:
            result['remainder'] = self.remainder

        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cond') is not None:
            self.cond = m.get('cond')

        if m.get('datum') is not None:
            self.datum = m.get('datum')

        if m.get('divisor') is not None:
            self.divisor = m.get('divisor')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameList') is not None:
            self.name_list = m.get('nameList')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('rate') is not None:
            self.rate = m.get('rate')

        if m.get('remainder') is not None:
            self.remainder = m.get('remainder')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

