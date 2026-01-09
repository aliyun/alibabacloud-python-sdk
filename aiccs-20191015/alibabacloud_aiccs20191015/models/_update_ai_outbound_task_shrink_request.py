# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAiOutboundTaskShrinkRequest(DaraModel):
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
        outbound_nums_shrink: str = None,
        recall_rule_shrink: str = None,
        task_id: int = None,
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
        self.outbound_nums_shrink = outbound_nums_shrink
        self.recall_rule_shrink = recall_rule_shrink
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

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

        if self.outbound_nums_shrink is not None:
            result['OutboundNums'] = self.outbound_nums_shrink

        if self.recall_rule_shrink is not None:
            result['RecallRule'] = self.recall_rule_shrink

        if self.task_id is not None:
            result['TaskId'] = self.task_id

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
            self.outbound_nums_shrink = m.get('OutboundNums')

        if m.get('RecallRule') is not None:
            self.recall_rule_shrink = m.get('RecallRule')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

