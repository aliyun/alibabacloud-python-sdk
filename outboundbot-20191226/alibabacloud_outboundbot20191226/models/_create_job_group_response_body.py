# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class CreateJobGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        job_group: main_models.CreateJobGroupResponseBodyJobGroup = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The job information.
        self.job_group = job_group
        # The message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful.
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
            temp_model = main_models.CreateJobGroupResponseBodyJobGroup()
            self.job_group = temp_model.from_map(m.get('JobGroup'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class CreateJobGroupResponseBodyJobGroup(DaraModel):
    def __init__(
        self,
        calling_numbers: List[str] = None,
        creation_time: int = None,
        export_progress: main_models.CreateJobGroupResponseBodyJobGroupExportProgress = None,
        job_data_parsing_task_id: str = None,
        job_file_path: str = None,
        job_group_description: str = None,
        job_group_id: str = None,
        job_group_name: str = None,
        min_concurrency: int = None,
        modify_time: str = None,
        priority: str = None,
        recall_calling_numbers: List[str] = None,
        recall_strategy: main_models.CreateJobGroupResponseBodyJobGroupRecallStrategy = None,
        ringing_duration: int = None,
        scenario_id: str = None,
        script_name: str = None,
        script_version: str = None,
        status: str = None,
        strategy: main_models.CreateJobGroupResponseBodyJobGroupStrategy = None,
    ):
        # The list of caller numbers.
        self.calling_numbers = calling_numbers
        # The creation time. The value is a UNIX timestamp in milliseconds.
        self.creation_time = creation_time
        # The export progress.
        # >**[Deprecated]** This field is deprecated in the current parameter.
        self.export_progress = export_progress
        # The ID of the background asynchronous parsing operation corresponding to the uploaded job file. If no value exists, this parameter is not returned.
        self.job_data_parsing_task_id = job_data_parsing_task_id
        # The OSS path of the job file. If no value exists, this parameter is not returned.
        self.job_file_path = job_file_path
        # The description of the job.
        self.job_group_description = job_group_description
        # The job ID.
        self.job_group_id = job_group_id
        # The job name.
        self.job_group_name = job_group_name
        # The guaranteed concurrency.
        # - When the job starts, a minimum of N concurrent calls are guaranteed.
        # - The sum of guaranteed concurrency for jobs of the same priority cannot exceed the instance concurrency.
        # - If the guaranteed concurrency is set to 0, the system intelligently allocates idle concurrency.
        self.min_concurrency = min_concurrency
        # The modification time. The value is a UNIX timestamp in milliseconds.
        self.modify_time = modify_time
        # The priority of the job group. Valid values:
        # - **Urgent**: urgent job.
        # - **Daily**: daily job.
        self.priority = priority
        # The list of caller numbers for redialing.
        self.recall_calling_numbers = recall_calling_numbers
        # The redial strategy.
        self.recall_strategy = recall_strategy
        # The ringing duration.
        self.ringing_duration = ringing_duration
        # The scenario ID.
        self.scenario_id = scenario_id
        # The script scenario name.
        self.script_name = script_name
        # The script scenario version.
        self.script_version = script_version
        # The job status.
        self.status = status
        # The job scheduling strategy.
        self.strategy = strategy

    def validate(self):
        if self.export_progress:
            self.export_progress.validate()
        if self.recall_strategy:
            self.recall_strategy.validate()
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

        if self.export_progress is not None:
            result['ExportProgress'] = self.export_progress.to_map()

        if self.job_data_parsing_task_id is not None:
            result['JobDataParsingTaskId'] = self.job_data_parsing_task_id

        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path

        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name

        if self.min_concurrency is not None:
            result['MinConcurrency'] = self.min_concurrency

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.recall_calling_numbers is not None:
            result['RecallCallingNumbers'] = self.recall_calling_numbers

        if self.recall_strategy is not None:
            result['RecallStrategy'] = self.recall_strategy.to_map()

        if self.ringing_duration is not None:
            result['RingingDuration'] = self.ringing_duration

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.script_version is not None:
            result['ScriptVersion'] = self.script_version

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ExportProgress') is not None:
            temp_model = main_models.CreateJobGroupResponseBodyJobGroupExportProgress()
            self.export_progress = temp_model.from_map(m.get('ExportProgress'))

        if m.get('JobDataParsingTaskId') is not None:
            self.job_data_parsing_task_id = m.get('JobDataParsingTaskId')

        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')

        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')

        if m.get('MinConcurrency') is not None:
            self.min_concurrency = m.get('MinConcurrency')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RecallCallingNumbers') is not None:
            self.recall_calling_numbers = m.get('RecallCallingNumbers')

        if m.get('RecallStrategy') is not None:
            temp_model = main_models.CreateJobGroupResponseBodyJobGroupRecallStrategy()
            self.recall_strategy = temp_model.from_map(m.get('RecallStrategy'))

        if m.get('RingingDuration') is not None:
            self.ringing_duration = m.get('RingingDuration')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptVersion') is not None:
            self.script_version = m.get('ScriptVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strategy') is not None:
            temp_model = main_models.CreateJobGroupResponseBodyJobGroupStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class CreateJobGroupResponseBodyJobGroupStrategy(DaraModel):
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
        working_time: List[main_models.CreateJobGroupResponseBodyJobGroupStrategyWorkingTime] = None,
    ):
        # The custom data of the strategy.
        self.customized = customized
        # The end time. The value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The follow-up processing method after the execution cycle ends. This field is no longer used.
        self.follow_up_strategy = follow_up_strategy
        # Indicates whether the strategy is a template.
        self.is_template = is_template
        # The maximum number of call attempts per day when the call is not answered in the job.
        self.max_attempts_per_day = max_attempts_per_day
        # The call interval.
        self.min_attempt_interval = min_attempt_interval
        # The repetition method. Valid values: once (no repetition), day (daily repetition), week (weekly repetition), and month (monthly repetition).
        self.repeat_by = repeat_by
        # The execution days for repetition.
        # - If the repetition cycle **RepeatBy** is **Week**, 0 represents Sunday, and 1 to 6 represent Monday to Saturday.
        # - If the repetition cycle **RepeatBy** is **Month**, 1 to 31 represent the 1st to the 31st day. Months without the specified date are not executed. For example, if the 30th is selected, the job is not executed in February.
        self.repeat_days = repeat_days
        # The number strategy. Valid values:
        # - None: no special rules.
        # - LocalFirst: local numbers first.
        # - LocalProvinceFirst: local province numbers first.
        self.routing_strategy = routing_strategy
        # The start time. The value is a UNIX timestamp in milliseconds.
        self.start_time = start_time
        # The strategy description.
        self.strategy_description = strategy_description
        # The strategy ID.
        self.strategy_id = strategy_id
        # The strategy name.
        self.strategy_name = strategy_name
        # The strategy type.
        self.type = type
        # The execution time window of the strategy.
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
                temp_model = main_models.CreateJobGroupResponseBodyJobGroupStrategyWorkingTime()
                self.working_time.append(temp_model.from_map(k1))

        return self

class CreateJobGroupResponseBodyJobGroupStrategyWorkingTime(DaraModel):
    def __init__(
        self,
        begin_time: str = None,
        end_time: str = None,
    ):
        # The start time of the window. Format: HH:mm:ss.
        self.begin_time = begin_time
        # The end time of the window. Format: HH:mm:ss.
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

class CreateJobGroupResponseBodyJobGroupRecallStrategy(DaraModel):
    def __init__(
        self,
        empty_number_ignore: bool = None,
        in_arrears_ignore: bool = None,
        out_of_service_ignore: bool = None,
    ):
        # Indicates whether nonexistent numbers are skipped.
        self.empty_number_ignore = empty_number_ignore
        # Indicates whether numbers with overdue payments are skipped.
        self.in_arrears_ignore = in_arrears_ignore
        # Indicates whether suspended numbers are skipped.
        self.out_of_service_ignore = out_of_service_ignore

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.empty_number_ignore is not None:
            result['EmptyNumberIgnore'] = self.empty_number_ignore

        if self.in_arrears_ignore is not None:
            result['InArrearsIgnore'] = self.in_arrears_ignore

        if self.out_of_service_ignore is not None:
            result['OutOfServiceIgnore'] = self.out_of_service_ignore

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmptyNumberIgnore') is not None:
            self.empty_number_ignore = m.get('EmptyNumberIgnore')

        if m.get('InArrearsIgnore') is not None:
            self.in_arrears_ignore = m.get('InArrearsIgnore')

        if m.get('OutOfServiceIgnore') is not None:
            self.out_of_service_ignore = m.get('OutOfServiceIgnore')

        return self

class CreateJobGroupResponseBodyJobGroupExportProgress(DaraModel):
    def __init__(
        self,
        file_http_url: str = None,
        progress: str = None,
        status: str = None,
    ):
        # **[Deprecated]** The file URL.
        self.file_http_url = file_http_url
        # **[Deprecated]** The progress.
        self.progress = progress
        # **[Deprecated]** The job export status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_http_url is not None:
            result['FileHttpUrl'] = self.file_http_url

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileHttpUrl') is not None:
            self.file_http_url = m.get('FileHttpUrl')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

