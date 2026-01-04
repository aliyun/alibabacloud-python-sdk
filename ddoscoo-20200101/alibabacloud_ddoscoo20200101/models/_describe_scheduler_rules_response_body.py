# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSchedulerRulesResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        scheduler_rules: List[main_models.DescribeSchedulerRulesResponseBodySchedulerRules] = None,
        total_count: str = None,
    ):
        self.request_id = request_id
        self.scheduler_rules = scheduler_rules
        self.total_count = total_count

    def validate(self):
        if self.scheduler_rules:
            for v1 in self.scheduler_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SchedulerRules'] = []
        if self.scheduler_rules is not None:
            for k1 in self.scheduler_rules:
                result['SchedulerRules'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scheduler_rules = []
        if m.get('SchedulerRules') is not None:
            for k1 in m.get('SchedulerRules'):
                temp_model = main_models.DescribeSchedulerRulesResponseBodySchedulerRules()
                self.scheduler_rules.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSchedulerRulesResponseBodySchedulerRules(DaraModel):
    def __init__(
        self,
        cname: str = None,
        param: main_models.DescribeSchedulerRulesResponseBodySchedulerRulesParam = None,
        rule_name: str = None,
        rule_type: str = None,
        rules: List[main_models.DescribeSchedulerRulesResponseBodySchedulerRulesRules] = None,
    ):
        self.cname = cname
        self.param = param
        self.rule_name = rule_name
        self.rule_type = rule_type
        self.rules = rules

    def validate(self):
        if self.param:
            self.param.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cname is not None:
            result['Cname'] = self.cname

        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')

        if m.get('Param') is not None:
            temp_model = main_models.DescribeSchedulerRulesResponseBodySchedulerRulesParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.DescribeSchedulerRulesResponseBodySchedulerRulesRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class DescribeSchedulerRulesResponseBodySchedulerRulesRules(DaraModel):
    def __init__(
        self,
        line: str = None,
        priority: int = None,
        region_id: str = None,
        restore_delay: int = None,
        status: int = None,
        type: str = None,
        value: str = None,
        value_type: int = None,
    ):
        self.line = line
        self.priority = priority
        self.region_id = region_id
        self.restore_delay = restore_delay
        self.status = status
        self.type = type
        self.value = value
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.line is not None:
            result['Line'] = self.line

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.restore_delay is not None:
            result['RestoreDelay'] = self.restore_delay

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RestoreDelay') is not None:
            self.restore_delay = m.get('RestoreDelay')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class DescribeSchedulerRulesResponseBodySchedulerRulesParam(DaraModel):
    def __init__(
        self,
        param_data: main_models.DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData = None,
        param_type: str = None,
    ):
        self.param_data = param_data
        self.param_type = param_type

    def validate(self):
        if self.param_data:
            self.param_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.param_data is not None:
            result['ParamData'] = self.param_data.to_map()

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamData') is not None:
            temp_model = main_models.DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData()
            self.param_data = temp_model.from_map(m.get('ParamData'))

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        return self

class DescribeSchedulerRulesResponseBodySchedulerRulesParamParamData(DaraModel):
    def __init__(
        self,
        cloud_instance_id: str = None,
    ):
        self.cloud_instance_id = cloud_instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_instance_id is not None:
            result['CloudInstanceId'] = self.cloud_instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudInstanceId') is not None:
            self.cloud_instance_id = m.get('CloudInstanceId')

        return self

