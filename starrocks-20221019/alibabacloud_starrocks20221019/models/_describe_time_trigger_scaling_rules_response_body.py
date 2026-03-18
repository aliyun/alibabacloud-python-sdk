# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_starrocks20221019 import models as main_models
from darabonba.model import DaraModel

class DescribeTimeTriggerScalingRulesResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        data: List[main_models.DescribeTimeTriggerScalingRulesResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        self.request_id = request_id
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeTimeTriggerScalingRulesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeTimeTriggerScalingRulesResponseBodyData(DaraModel):
    def __init__(
        self,
        node_number: str = None,
        scaling_in_rule: main_models.DescribeTimeTriggerScalingRulesResponseBodyDataScalingInRule = None,
        scaling_out_rule: main_models.DescribeTimeTriggerScalingRulesResponseBodyDataScalingOutRule = None,
        scaling_rule_id: str = None,
        scaling_rule_name: str = None,
        status: str = None,
    ):
        self.node_number = node_number
        self.scaling_in_rule = scaling_in_rule
        self.scaling_out_rule = scaling_out_rule
        self.scaling_rule_id = scaling_rule_id
        self.scaling_rule_name = scaling_rule_name
        self.status = status

    def validate(self):
        if self.scaling_in_rule:
            self.scaling_in_rule.validate()
        if self.scaling_out_rule:
            self.scaling_out_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_number is not None:
            result['NodeNumber'] = self.node_number

        if self.scaling_in_rule is not None:
            result['ScalingInRule'] = self.scaling_in_rule.to_map()

        if self.scaling_out_rule is not None:
            result['ScalingOutRule'] = self.scaling_out_rule.to_map()

        if self.scaling_rule_id is not None:
            result['ScalingRuleId'] = self.scaling_rule_id

        if self.scaling_rule_name is not None:
            result['ScalingRuleName'] = self.scaling_rule_name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeNumber') is not None:
            self.node_number = m.get('NodeNumber')

        if m.get('ScalingInRule') is not None:
            temp_model = main_models.DescribeTimeTriggerScalingRulesResponseBodyDataScalingInRule()
            self.scaling_in_rule = temp_model.from_map(m.get('ScalingInRule'))

        if m.get('ScalingOutRule') is not None:
            temp_model = main_models.DescribeTimeTriggerScalingRulesResponseBodyDataScalingOutRule()
            self.scaling_out_rule = temp_model.from_map(m.get('ScalingOutRule'))

        if m.get('ScalingRuleId') is not None:
            self.scaling_rule_id = m.get('ScalingRuleId')

        if m.get('ScalingRuleName') is not None:
            self.scaling_rule_name = m.get('ScalingRuleName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeTimeTriggerScalingRulesResponseBodyDataScalingOutRule(DaraModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        recurrence_interval: int = None,
        recurrence_type: str = None,
        recurrence_values: List[str] = None,
        second: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.recurrence_interval = recurrence_interval
        self.recurrence_type = recurrence_type
        self.recurrence_values = recurrence_values
        self.second = second
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day is not None:
            result['Day'] = self.day

        if self.hour is not None:
            result['Hour'] = self.hour

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.month is not None:
            result['Month'] = self.month

        if self.recurrence_interval is not None:
            result['RecurrenceInterval'] = self.recurrence_interval

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values

        if self.second is not None:
            result['Second'] = self.second

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')

        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('Month') is not None:
            self.month = m.get('Month')

        if m.get('RecurrenceInterval') is not None:
            self.recurrence_interval = m.get('RecurrenceInterval')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')

        if m.get('Second') is not None:
            self.second = m.get('Second')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

class DescribeTimeTriggerScalingRulesResponseBodyDataScalingInRule(DaraModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        recurrence_interval: int = None,
        recurrence_type: str = None,
        recurrence_values: List[str] = None,
        second: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.recurrence_interval = recurrence_interval
        self.recurrence_type = recurrence_type
        self.recurrence_values = recurrence_values
        self.second = second
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day is not None:
            result['Day'] = self.day

        if self.hour is not None:
            result['Hour'] = self.hour

        if self.minute is not None:
            result['Minute'] = self.minute

        if self.month is not None:
            result['Month'] = self.month

        if self.recurrence_interval is not None:
            result['RecurrenceInterval'] = self.recurrence_interval

        if self.recurrence_type is not None:
            result['RecurrenceType'] = self.recurrence_type

        if self.recurrence_values is not None:
            result['RecurrenceValues'] = self.recurrence_values

        if self.second is not None:
            result['Second'] = self.second

        if self.year is not None:
            result['Year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')

        if m.get('Hour') is not None:
            self.hour = m.get('Hour')

        if m.get('Minute') is not None:
            self.minute = m.get('Minute')

        if m.get('Month') is not None:
            self.month = m.get('Month')

        if m.get('RecurrenceInterval') is not None:
            self.recurrence_interval = m.get('RecurrenceInterval')

        if m.get('RecurrenceType') is not None:
            self.recurrence_type = m.get('RecurrenceType')

        if m.get('RecurrenceValues') is not None:
            self.recurrence_values = m.get('RecurrenceValues')

        if m.get('Second') is not None:
            self.second = m.get('Second')

        if m.get('Year') is not None:
            self.year = m.get('Year')

        return self

