# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class ModifyBatchJobsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        job_group: main_models.ModifyBatchJobsResponseBodyJobGroup = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.job_group = job_group
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.job_group:
            self.job_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.job_group is not None:
            result['JobGroup'] = self.job_group.to_map()

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

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('JobGroup') is not None:
            temp_model = main_models.ModifyBatchJobsResponseBodyJobGroup()
            self.job_group = temp_model.from_map(m.get('JobGroup'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ModifyBatchJobsResponseBodyJobGroup(DaraModel):
    def __init__(
        self,
        calling_numbers: List[str] = None,
        creation_time: int = None,
        job_file_path: str = None,
        job_group_description: str = None,
        job_group_id: str = None,
        job_group_name: str = None,
        scenario_id: str = None,
        strategy: main_models.ModifyBatchJobsResponseBodyJobGroupStrategy = None,
    ):
        self.calling_numbers = calling_numbers
        self.creation_time = creation_time
        self.job_file_path = job_file_path
        self.job_group_description = job_group_description
        self.job_group_id = job_group_id
        self.job_group_name = job_group_name
        self.scenario_id = scenario_id
        self.strategy = strategy

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path

        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')

        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('Strategy') is not None:
            temp_model = main_models.ModifyBatchJobsResponseBodyJobGroupStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class ModifyBatchJobsResponseBodyJobGroupStrategy(DaraModel):
    def __init__(
        self,
        customized: str = None,
        end_time: int = None,
        follow_up_strategy: str = None,
        is_template: bool = None,
        max_attempts_per_day: int = None,
        min_attempt_interval: int = None,
        repeat_by: str = None,
        repeat_days: List[str] = None,
        routing_strategy: str = None,
        start_time: int = None,
        strategy_description: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
        type: str = None,
        working_time: List[main_models.ModifyBatchJobsResponseBodyJobGroupStrategyWorkingTime] = None,
    ):
        self.customized = customized
        self.end_time = end_time
        self.follow_up_strategy = follow_up_strategy
        self.is_template = is_template
        self.max_attempts_per_day = max_attempts_per_day
        self.min_attempt_interval = min_attempt_interval
        self.repeat_by = repeat_by
        self.repeat_days = repeat_days
        self.routing_strategy = routing_strategy
        self.start_time = start_time
        self.strategy_description = strategy_description
        self.strategy_id = strategy_id
        self.strategy_name = strategy_name
        self.type = type
        self.working_time = working_time

    def validate(self):
        if self.working_time:
            for v1 in self.working_time:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customized is not None:
            result['Customized'] = self.customized

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.follow_up_strategy is not None:
            result['FollowUpStrategy'] = self.follow_up_strategy

        if self.is_template is not None:
            result['IsTemplate'] = self.is_template

        if self.max_attempts_per_day is not None:
            result['MaxAttemptsPerDay'] = self.max_attempts_per_day

        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval

        if self.repeat_by is not None:
            result['RepeatBy'] = self.repeat_by

        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days

        if self.routing_strategy is not None:
            result['RoutingStrategy'] = self.routing_strategy

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.strategy_description is not None:
            result['StrategyDescription'] = self.strategy_description

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name

        if self.type is not None:
            result['Type'] = self.type

        result['WorkingTime'] = []
        if self.working_time is not None:
            for k1 in self.working_time:
                result['WorkingTime'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Customized') is not None:
            self.customized = m.get('Customized')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FollowUpStrategy') is not None:
            self.follow_up_strategy = m.get('FollowUpStrategy')

        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')

        if m.get('MaxAttemptsPerDay') is not None:
            self.max_attempts_per_day = m.get('MaxAttemptsPerDay')

        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')

        if m.get('RepeatBy') is not None:
            self.repeat_by = m.get('RepeatBy')

        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')

        if m.get('RoutingStrategy') is not None:
            self.routing_strategy = m.get('RoutingStrategy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('StrategyDescription') is not None:
            self.strategy_description = m.get('StrategyDescription')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.working_time = []
        if m.get('WorkingTime') is not None:
            for k1 in m.get('WorkingTime'):
                temp_model = main_models.ModifyBatchJobsResponseBodyJobGroupStrategyWorkingTime()
                self.working_time.append(temp_model.from_map(k1))

        return self

class ModifyBatchJobsResponseBodyJobGroupStrategyWorkingTime(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
    ):
        self.begin_time = begin_time
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        return self

