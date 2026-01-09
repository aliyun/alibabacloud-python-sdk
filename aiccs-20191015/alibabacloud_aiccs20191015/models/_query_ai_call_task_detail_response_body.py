# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryAiCallTaskDetailResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QueryAiCallTaskDetailResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
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
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryAiCallTaskDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAiCallTaskDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        call_days: List[str] = None,
        call_times: List[main_models.QueryAiCallTaskDetailResponseBodyDataCallTimes] = None,
        caller_number: str = None,
        concurrent_count: int = None,
        real_start_time: int = None,
        retry_count: int = None,
        retry_enable: bool = None,
        retry_interval: int = None,
        retry_reasons: List[str] = None,
        start_time: int = None,
        start_type: str = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.call_days = call_days
        self.call_times = call_times
        self.caller_number = caller_number
        self.concurrent_count = concurrent_count
        self.real_start_time = real_start_time
        self.retry_count = retry_count
        self.retry_enable = retry_enable
        self.retry_interval = retry_interval
        self.retry_reasons = retry_reasons
        self.start_time = start_time
        self.start_type = start_type
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        if self.call_times:
            for v1 in self.call_times:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id

        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.call_days is not None:
            result['CallDays'] = self.call_days

        result['CallTimes'] = []
        if self.call_times is not None:
            for k1 in self.call_times:
                result['CallTimes'].append(k1.to_map() if k1 else None)

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.concurrent_count is not None:
            result['ConcurrentCount'] = self.concurrent_count

        if self.real_start_time is not None:
            result['RealStartTime'] = self.real_start_time

        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count

        if self.retry_enable is not None:
            result['RetryEnable'] = self.retry_enable

        if self.retry_interval is not None:
            result['RetryInterval'] = self.retry_interval

        if self.retry_reasons is not None:
            result['RetryReasons'] = self.retry_reasons

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.start_type is not None:
            result['StartType'] = self.start_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('CallDays') is not None:
            self.call_days = m.get('CallDays')

        self.call_times = []
        if m.get('CallTimes') is not None:
            for k1 in m.get('CallTimes'):
                temp_model = main_models.QueryAiCallTaskDetailResponseBodyDataCallTimes()
                self.call_times.append(temp_model.from_map(k1))

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('ConcurrentCount') is not None:
            self.concurrent_count = m.get('ConcurrentCount')

        if m.get('RealStartTime') is not None:
            self.real_start_time = m.get('RealStartTime')

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        if m.get('RetryEnable') is not None:
            self.retry_enable = m.get('RetryEnable')

        if m.get('RetryInterval') is not None:
            self.retry_interval = m.get('RetryInterval')

        if m.get('RetryReasons') is not None:
            self.retry_reasons = m.get('RetryReasons')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StartType') is not None:
            self.start_type = m.get('StartType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

class QueryAiCallTaskDetailResponseBodyDataCallTimes(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

