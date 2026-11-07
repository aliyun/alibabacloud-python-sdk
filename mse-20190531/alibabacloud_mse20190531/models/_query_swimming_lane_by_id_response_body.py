# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class QuerySwimmingLaneByIdResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.QuerySwimmingLaneByIdResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # 
        # - `true`: The request was successful.
        # 
        # - `false`: The request failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

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
        if m.get('Data') is not None:
            temp_model = main_models.QuerySwimmingLaneByIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QuerySwimmingLaneByIdResponseBodyData(DaraModel):
    def __init__(
        self,
        path_independent_percentage_enable: bool = None,
        enable: bool = None,
        enable_rules: bool = None,
        entry_rule: str = None,
        entry_rules: List[main_models.QuerySwimmingLaneByIdResponseBodyDataEntryRules] = None,
        gateway_swimming_lane_route_json: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_id: int = None,
        id: int = None,
        name: str = None,
        region_id: str = None,
        status: int = None,
        tag: str = None,
    ):
        # This parameter is discontinued. This parameter is used to specify whether to enable grayscale by path when Java gateway is used as the entry for the swimming lane group.
        self.path_independent_percentage_enable = path_independent_percentage_enable
        # The swimming lane switch.
        self.enable = enable
        # Specifies whether to enable the rule. Valid values:
        self.enable_rules = enable_rules
        # The entry application rule.
        self.entry_rule = entry_rule
        # The details of the entry application rules.
        self.entry_rules = entry_rules
        # The MSE gateway routing rule.
        self.gateway_swimming_lane_route_json = gateway_swimming_lane_route_json
        # Rule Created At
        self.gmt_create = gmt_create
        # Rule Modified At
        self.gmt_modified = gmt_modified
        # The swimming lane group ID.
        self.group_id = group_id
        # The swimming lane ID.
        self.id = id
        # The swimming lane name.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The swimming lane status.
        self.status = status
        # The tag corresponding to the swimming lane.
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
        if self.path_independent_percentage_enable is not None:
            result['PathIndependentPercentageEnable'] = self.path_independent_percentage_enable

        if self.enable is not None:
            result['enable'] = self.enable

        if self.enable_rules is not None:
            result['enableRules'] = self.enable_rules

        if self.entry_rule is not None:
            result['entryRule'] = self.entry_rule

        result['entryRules'] = []
        if self.entry_rules is not None:
            for k1 in self.entry_rules:
                result['entryRules'].append(k1.to_map() if k1 else None)

        if self.gateway_swimming_lane_route_json is not None:
            result['gatewaySwimmingLaneRouteJson'] = self.gateway_swimming_lane_route_json

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        if self.tag is not None:
            result['tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PathIndependentPercentageEnable') is not None:
            self.path_independent_percentage_enable = m.get('PathIndependentPercentageEnable')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('enableRules') is not None:
            self.enable_rules = m.get('enableRules')

        if m.get('entryRule') is not None:
            self.entry_rule = m.get('entryRule')

        self.entry_rules = []
        if m.get('entryRules') is not None:
            for k1 in m.get('entryRules'):
                temp_model = main_models.QuerySwimmingLaneByIdResponseBodyDataEntryRules()
                self.entry_rules.append(temp_model.from_map(k1))

        if m.get('gatewaySwimmingLaneRouteJson') is not None:
            self.gateway_swimming_lane_route_json = m.get('gatewaySwimmingLaneRouteJson')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        return self

class QuerySwimmingLaneByIdResponseBodyDataEntryRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        path: str = None,
        paths: List[str] = None,
        rest_items: List[main_models.QuerySwimmingLaneByIdResponseBodyDataEntryRulesRestItems] = None,
    ):
        # The condition.
        self.condition = condition
        # The path.
        self.path = path
        # The list of paths.
        self.paths = paths
        # The Restful matching rules.
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
                temp_model = main_models.QuerySwimmingLaneByIdResponseBodyDataEntryRulesRestItems()
                self.rest_items.append(temp_model.from_map(k1))

        return self

class QuerySwimmingLaneByIdResponseBodyDataEntryRulesRestItems(DaraModel):
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
        # The number.
        self.datum = datum
        # The divisor.
        self.divisor = divisor
        # The name.
        self.name = name
        # The names.
        self.name_list = name_list
        # The filter operator.
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

