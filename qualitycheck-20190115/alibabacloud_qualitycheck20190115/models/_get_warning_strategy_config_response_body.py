# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class GetWarningStrategyConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetWarningStrategyConfigResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.GetWarningStrategyConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetWarningStrategyConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        id: int = None,
        interval_time: int = None,
        lambda_: str = None,
        level: int = None,
        max_number: int = None,
        name: str = None,
        warning_strategy_list: main_models.GetWarningStrategyConfigResponseBodyDataWarningStrategyList = None,
    ):
        self.id = id
        self.interval_time = interval_time
        self.lambda_ = lambda_
        self.level = level
        self.max_number = max_number
        self.name = name
        self.warning_strategy_list = warning_strategy_list

    def validate(self):
        if self.warning_strategy_list:
            self.warning_strategy_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.interval_time is not None:
            result['IntervalTime'] = self.interval_time

        if self.lambda_ is not None:
            result['Lambda'] = self.lambda_

        if self.level is not None:
            result['Level'] = self.level

        if self.max_number is not None:
            result['MaxNumber'] = self.max_number

        if self.name is not None:
            result['Name'] = self.name

        if self.warning_strategy_list is not None:
            result['WarningStrategyList'] = self.warning_strategy_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IntervalTime') is not None:
            self.interval_time = m.get('IntervalTime')

        if m.get('Lambda') is not None:
            self.lambda_ = m.get('Lambda')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('MaxNumber') is not None:
            self.max_number = m.get('MaxNumber')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WarningStrategyList') is not None:
            temp_model = main_models.GetWarningStrategyConfigResponseBodyDataWarningStrategyList()
            self.warning_strategy_list = temp_model.from_map(m.get('WarningStrategyList'))

        return self

class GetWarningStrategyConfigResponseBodyDataWarningStrategyList(DaraModel):
    def __init__(
        self,
        warning_strategy_list: List[main_models.GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyList] = None,
    ):
        self.warning_strategy_list = warning_strategy_list

    def validate(self):
        if self.warning_strategy_list:
            for v1 in self.warning_strategy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['warningStrategyList'] = []
        if self.warning_strategy_list is not None:
            for k1 in self.warning_strategy_list:
                result['warningStrategyList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.warning_strategy_list = []
        if m.get('warningStrategyList') is not None:
            for k1 in m.get('warningStrategyList'):
                temp_model = main_models.GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyList()
                self.warning_strategy_list.append(temp_model.from_map(k1))

        return self

class GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyList(DaraModel):
    def __init__(
        self,
        code: str = None,
        duration: int = None,
        duration_expression: int = None,
        hit_number: int = None,
        hit_number_expression: int = None,
        hit_rule_list: str = None,
        hit_type: int = None,
        id: int = None,
        range: main_models.GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyListRange = None,
        status: int = None,
    ):
        self.code = code
        self.duration = duration
        self.duration_expression = duration_expression
        self.hit_number = hit_number
        self.hit_number_expression = hit_number_expression
        self.hit_rule_list = hit_rule_list
        self.hit_type = hit_type
        self.id = id
        self.range = range
        self.status = status

    def validate(self):
        if self.range:
            self.range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.duration_expression is not None:
            result['DurationExpression'] = self.duration_expression

        if self.hit_number is not None:
            result['HitNumber'] = self.hit_number

        if self.hit_number_expression is not None:
            result['HitNumberExpression'] = self.hit_number_expression

        if self.hit_rule_list is not None:
            result['HitRuleList'] = self.hit_rule_list

        if self.hit_type is not None:
            result['HitType'] = self.hit_type

        if self.id is not None:
            result['Id'] = self.id

        if self.range is not None:
            result['Range'] = self.range.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('DurationExpression') is not None:
            self.duration_expression = m.get('DurationExpression')

        if m.get('HitNumber') is not None:
            self.hit_number = m.get('HitNumber')

        if m.get('HitNumberExpression') is not None:
            self.hit_number_expression = m.get('HitNumberExpression')

        if m.get('HitRuleList') is not None:
            self.hit_rule_list = m.get('HitRuleList')

        if m.get('HitType') is not None:
            self.hit_type = m.get('HitType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Range') is not None:
            temp_model = main_models.GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyListRange()
            self.range = temp_model.from_map(m.get('Range'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class GetWarningStrategyConfigResponseBodyDataWarningStrategyListWarningStrategyListRange(DaraModel):
    def __init__(
        self,
        range_num: int = None,
        type: int = None,
    ):
        self.range_num = range_num
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.range_num is not None:
            result['RangeNum'] = self.range_num

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RangeNum') is not None:
            self.range_num = m.get('RangeNum')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

