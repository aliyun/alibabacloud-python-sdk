# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class CreateAiOutboundTaskRequest(DaraModel):
    def __init__(
        self,
        concurrent_rate: int = None,
        description: str = None,
        execution_time: str = None,
        forecast_call_rate: float = None,
        handler_id: int = None,
        instance_id: str = None,
        name: str = None,
        num_repeated: int = None,
        outbound_nums: List[str] = None,
        recall_rule: main_models.CreateAiOutboundTaskRequestRecallRule = None,
        type: int = None,
    ):
        self.concurrent_rate = concurrent_rate
        self.description = description
        # This parameter is required.
        self.execution_time = execution_time
        self.forecast_call_rate = forecast_call_rate
        # This parameter is required.
        self.handler_id = handler_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.num_repeated = num_repeated
        # This parameter is required.
        self.outbound_nums = outbound_nums
        self.recall_rule = recall_rule
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.recall_rule:
            self.recall_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.concurrent_rate is not None:
            result['ConcurrentRate'] = self.concurrent_rate

        if self.description is not None:
            result['Description'] = self.description

        if self.execution_time is not None:
            result['ExecutionTime'] = self.execution_time

        if self.forecast_call_rate is not None:
            result['ForecastCallRate'] = self.forecast_call_rate

        if self.handler_id is not None:
            result['HandlerId'] = self.handler_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.num_repeated is not None:
            result['NumRepeated'] = self.num_repeated

        if self.outbound_nums is not None:
            result['OutboundNums'] = self.outbound_nums

        if self.recall_rule is not None:
            result['RecallRule'] = self.recall_rule.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrentRate') is not None:
            self.concurrent_rate = m.get('ConcurrentRate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExecutionTime') is not None:
            self.execution_time = m.get('ExecutionTime')

        if m.get('ForecastCallRate') is not None:
            self.forecast_call_rate = m.get('ForecastCallRate')

        if m.get('HandlerId') is not None:
            self.handler_id = m.get('HandlerId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NumRepeated') is not None:
            self.num_repeated = m.get('NumRepeated')

        if m.get('OutboundNums') is not None:
            self.outbound_nums = m.get('OutboundNums')

        if m.get('RecallRule') is not None:
            temp_model = main_models.CreateAiOutboundTaskRequestRecallRule()
            self.recall_rule = temp_model.from_map(m.get('RecallRule'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateAiOutboundTaskRequestRecallRule(DaraModel):
    def __init__(
        self,
        count: int = None,
        interval: int = None,
    ):
        self.count = count
        self.interval = interval

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.interval is not None:
            result['Interval'] = self.interval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        return self

