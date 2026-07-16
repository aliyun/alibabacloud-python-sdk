# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class UpdateAiOutboundTaskRequest(DaraModel):
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
        recall_rule: main_models.UpdateAiOutboundTaskRequestRecallRule = None,
        task_id: int = None,
    ):
        # The concurrent rate for automated outbound calls.
        self.concurrent_rate = concurrent_rate
        # The job description. It can contain 0 to 100 characters.
        self.description = description
        # The job execution time.
        # 
        # > The end time must be later than the start time.
        # 
        # This parameter is required.
        self.execution_time = execution_time
        # Fixed dialing ratio for predictive outbound calls. Valid values: **≥1**.
        self.forecast_call_rate = forecast_call_rate
        # The skill group ID (for predictive outbound calls) or IVR ID (for automated outbound calls).
        # 
        # This parameter is required.
        self.handler_id = handler_id
        # AICCS instance ID.  
        # You can obtain it from **Instance Management** in the left-side navigation pane of the [Artificial Intelligence Cloud Call Service console](https://aiccs.console.aliyun.com/overview).
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Job name. Length: 1 to 15 characters.
        # 
        # This parameter is required.
        self.name = name
        # The policy for handling duplicate callee numbers.
        # - **0**: Remove duplicates within the job.
        # - **1**: Do not remove duplicates within the job.
        # 
        # This parameter is required.
        self.num_repeated = num_repeated
        # Outbound caller numbers.
        # 
        # This parameter is required.
        self.outbound_nums = outbound_nums
        # Failed-call retry policy.
        # 
        # > If empty, no retry is performed when an outbound call fails.
        self.recall_rule = recall_rule
        # The job ID.
        # 
        # You can invoke the [CreateAiOutboundTask](https://help.aliyun.com/document_detail/312260.html) API and check the **Data** field in the response, or invoke the [GetAiOutboundTaskList](https://help.aliyun.com/document_detail/2718026.html) API and check the **TaskId** field in the response.
        # 
        # This parameter is required.
        self.task_id = task_id

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
            self.outbound_nums = m.get('OutboundNums')

        if m.get('RecallRule') is not None:
            temp_model = main_models.UpdateAiOutboundTaskRequestRecallRule()
            self.recall_rule = temp_model.from_map(m.get('RecallRule'))

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class UpdateAiOutboundTaskRequestRecallRule(DaraModel):
    def __init__(
        self,
        count: int = None,
        interval: int = None,
    ):
        # Number of retries after a failed call. Valid values: **1 to 3**.
        self.count = count
        # Time interval between retries after a failed call. Valid values: **1 to 60**, unit: minutes.
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

