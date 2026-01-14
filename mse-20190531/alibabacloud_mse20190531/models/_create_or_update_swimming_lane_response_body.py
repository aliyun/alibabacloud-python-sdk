# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class CreateOrUpdateSwimmingLaneResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.CreateOrUpdateSwimmingLaneResponseBodyData = None,
        error_code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. The value 200 is returned if the request is successful.
        self.code = code
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The message returned.
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
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateOrUpdateSwimmingLaneResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateOrUpdateSwimmingLaneResponseBodyData(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        enable_rules: bool = None,
        entry_rule: str = None,
        entry_rules: List[main_models.CreateOrUpdateSwimmingLaneResponseBodyDataEntryRules] = None,
        gateway_swimming_lane_route_json: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_id: int = None,
        id: int = None,
        name: str = None,
        path_independent_percentage_enable: bool = None,
        region_id: str = None,
        status: int = None,
        tag: str = None,
    ):
        self.enable = enable
        self.enable_rules = enable_rules
        self.entry_rule = entry_rule
        self.entry_rules = entry_rules
        self.gateway_swimming_lane_route_json = gateway_swimming_lane_route_json
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.group_id = group_id
        self.id = id
        self.name = name
        self.path_independent_percentage_enable = path_independent_percentage_enable
        self.region_id = region_id
        self.status = status
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

        if self.path_independent_percentage_enable is not None:
            result['pathIndependentPercentageEnable'] = self.path_independent_percentage_enable

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.status is not None:
            result['status'] = self.status

        if self.tag is not None:
            result['tag'] = self.tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('enableRules') is not None:
            self.enable_rules = m.get('enableRules')

        if m.get('entryRule') is not None:
            self.entry_rule = m.get('entryRule')

        self.entry_rules = []
        if m.get('entryRules') is not None:
            for k1 in m.get('entryRules'):
                temp_model = main_models.CreateOrUpdateSwimmingLaneResponseBodyDataEntryRules()
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

        if m.get('pathIndependentPercentageEnable') is not None:
            self.path_independent_percentage_enable = m.get('pathIndependentPercentageEnable')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('tag') is not None:
            self.tag = m.get('tag')

        return self

class CreateOrUpdateSwimmingLaneResponseBodyDataEntryRules(DaraModel):
    def __init__(
        self,
        condition: str = None,
        path: str = None,
        paths: List[str] = None,
        rest_items: List[main_models.CreateOrUpdateSwimmingLaneResponseBodyDataEntryRulesRestItems] = None,
    ):
        self.condition = condition
        self.path = path
        self.paths = paths
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
                temp_model = main_models.CreateOrUpdateSwimmingLaneResponseBodyDataEntryRulesRestItems()
                self.rest_items.append(temp_model.from_map(k1))

        return self

class CreateOrUpdateSwimmingLaneResponseBodyDataEntryRulesRestItems(DaraModel):
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

