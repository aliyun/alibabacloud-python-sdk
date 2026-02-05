# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeJobGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        job_group: main_models.DescribeJobGroupResponseBodyJobGroup = None,
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
            temp_model = main_models.DescribeJobGroupResponseBodyJobGroup()
            self.job_group = temp_model.from_map(m.get('JobGroup'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeJobGroupResponseBodyJobGroup(DaraModel):
    def __init__(
        self,
        calling_numbers: List[str] = None,
        creation_time: int = None,
        export_progress: main_models.DescribeJobGroupResponseBodyJobGroupExportProgress = None,
        flash_sms_extras: main_models.DescribeJobGroupResponseBodyJobGroupFlashSmsExtras = None,
        job_data_parsing_task_id: str = None,
        job_file_path: str = None,
        job_group_description: str = None,
        job_group_id: str = None,
        job_group_name: str = None,
        min_concurrency: int = None,
        modify_time: str = None,
        priority: str = None,
        progress: main_models.DescribeJobGroupResponseBodyJobGroupProgress = None,
        recall_calling_numbers: List[str] = None,
        recall_strategy: main_models.DescribeJobGroupResponseBodyJobGroupRecallStrategy = None,
        result: main_models.DescribeJobGroupResponseBodyJobGroupResult = None,
        ringing_duration: int = None,
        scenario_id: str = None,
        script_id: str = None,
        script_name: str = None,
        script_nlu_engine: str = None,
        script_version: str = None,
        status: str = None,
        strategy: main_models.DescribeJobGroupResponseBodyJobGroupStrategy = None,
    ):
        self.calling_numbers = calling_numbers
        self.creation_time = creation_time
        self.export_progress = export_progress
        self.flash_sms_extras = flash_sms_extras
        self.job_data_parsing_task_id = job_data_parsing_task_id
        self.job_file_path = job_file_path
        self.job_group_description = job_group_description
        self.job_group_id = job_group_id
        self.job_group_name = job_group_name
        self.min_concurrency = min_concurrency
        self.modify_time = modify_time
        self.priority = priority
        self.progress = progress
        self.recall_calling_numbers = recall_calling_numbers
        self.recall_strategy = recall_strategy
        self.result = result
        self.ringing_duration = ringing_duration
        self.scenario_id = scenario_id
        self.script_id = script_id
        self.script_name = script_name
        self.script_nlu_engine = script_nlu_engine
        self.script_version = script_version
        self.status = status
        self.strategy = strategy

    def validate(self):
        if self.export_progress:
            self.export_progress.validate()
        if self.flash_sms_extras:
            self.flash_sms_extras.validate()
        if self.progress:
            self.progress.validate()
        if self.recall_strategy:
            self.recall_strategy.validate()
        if self.result:
            self.result.validate()
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

        if self.flash_sms_extras is not None:
            result['FlashSmsExtras'] = self.flash_sms_extras.to_map()

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

        if self.progress is not None:
            result['Progress'] = self.progress.to_map()

        if self.recall_calling_numbers is not None:
            result['RecallCallingNumbers'] = self.recall_calling_numbers

        if self.recall_strategy is not None:
            result['RecallStrategy'] = self.recall_strategy.to_map()

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.ringing_duration is not None:
            result['RingingDuration'] = self.ringing_duration

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.script_nlu_engine is not None:
            result['ScriptNluEngine'] = self.script_nlu_engine

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
            temp_model = main_models.DescribeJobGroupResponseBodyJobGroupExportProgress()
            self.export_progress = temp_model.from_map(m.get('ExportProgress'))

        if m.get('FlashSmsExtras') is not None:
            temp_model = main_models.DescribeJobGroupResponseBodyJobGroupFlashSmsExtras()
            self.flash_sms_extras = temp_model.from_map(m.get('FlashSmsExtras'))

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

        if m.get('Progress') is not None:
            temp_model = main_models.DescribeJobGroupResponseBodyJobGroupProgress()
            self.progress = temp_model.from_map(m.get('Progress'))

        if m.get('RecallCallingNumbers') is not None:
            self.recall_calling_numbers = m.get('RecallCallingNumbers')

        if m.get('RecallStrategy') is not None:
            temp_model = main_models.DescribeJobGroupResponseBodyJobGroupRecallStrategy()
            self.recall_strategy = temp_model.from_map(m.get('RecallStrategy'))

        if m.get('Result') is not None:
            temp_model = main_models.DescribeJobGroupResponseBodyJobGroupResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('RingingDuration') is not None:
            self.ringing_duration = m.get('RingingDuration')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('ScriptNluEngine') is not None:
            self.script_nlu_engine = m.get('ScriptNluEngine')

        if m.get('ScriptVersion') is not None:
            self.script_version = m.get('ScriptVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Strategy') is not None:
            temp_model = main_models.DescribeJobGroupResponseBodyJobGroupStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class DescribeJobGroupResponseBodyJobGroupStrategy(DaraModel):
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
        repeatable: bool = None,
        routing_strategy: str = None,
        start_time: int = None,
        strategy_description: str = None,
        strategy_id: str = None,
        strategy_name: str = None,
        type: str = None,
        working_time: List[main_models.DescribeJobGroupResponseBodyJobGroupStrategyWorkingTime] = None,
    ):
        self.customized = customized
        self.end_time = end_time
        self.follow_up_strategy = follow_up_strategy
        self.is_template = is_template
        self.max_attempts_per_day = max_attempts_per_day
        self.min_attempt_interval = min_attempt_interval
        self.repeat_by = repeat_by
        self.repeat_days = repeat_days
        self.repeatable = repeatable
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

        if self.repeatable is not None:
            result['Repeatable'] = self.repeatable

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

        if m.get('Repeatable') is not None:
            self.repeatable = m.get('Repeatable')

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
                temp_model = main_models.DescribeJobGroupResponseBodyJobGroupStrategyWorkingTime()
                self.working_time.append(temp_model.from_map(k1))

        return self

class DescribeJobGroupResponseBodyJobGroupStrategyWorkingTime(DaraModel):
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

class DescribeJobGroupResponseBodyJobGroupResult(DaraModel):
    def __init__(
        self,
        client_hangup_num: int = None,
        finished_num: int = None,
        no_interact_num: int = None,
        timeout_hangup_num: int = None,
        unrecognized_num: int = None,
    ):
        self.client_hangup_num = client_hangup_num
        self.finished_num = finished_num
        self.no_interact_num = no_interact_num
        self.timeout_hangup_num = timeout_hangup_num
        self.unrecognized_num = unrecognized_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_hangup_num is not None:
            result['ClientHangupNum'] = self.client_hangup_num

        if self.finished_num is not None:
            result['FinishedNum'] = self.finished_num

        if self.no_interact_num is not None:
            result['NoInteractNum'] = self.no_interact_num

        if self.timeout_hangup_num is not None:
            result['TimeoutHangupNum'] = self.timeout_hangup_num

        if self.unrecognized_num is not None:
            result['UnrecognizedNum'] = self.unrecognized_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientHangupNum') is not None:
            self.client_hangup_num = m.get('ClientHangupNum')

        if m.get('FinishedNum') is not None:
            self.finished_num = m.get('FinishedNum')

        if m.get('NoInteractNum') is not None:
            self.no_interact_num = m.get('NoInteractNum')

        if m.get('TimeoutHangupNum') is not None:
            self.timeout_hangup_num = m.get('TimeoutHangupNum')

        if m.get('UnrecognizedNum') is not None:
            self.unrecognized_num = m.get('UnrecognizedNum')

        return self

class DescribeJobGroupResponseBodyJobGroupRecallStrategy(DaraModel):
    def __init__(
        self,
        empty_number_ignore: bool = None,
        in_arrears_ignore: bool = None,
        out_of_service_ignore: bool = None,
    ):
        self.empty_number_ignore = empty_number_ignore
        self.in_arrears_ignore = in_arrears_ignore
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

class DescribeJobGroupResponseBodyJobGroupProgress(DaraModel):
    def __init__(
        self,
        briefs: List[main_models.DescribeJobGroupResponseBodyJobGroupProgressBriefs] = None,
        cancelled: int = None,
        categories: List[main_models.DescribeJobGroupResponseBodyJobGroupProgressCategories] = None,
        duration: int = None,
        executing: int = None,
        failed: int = None,
        paused: int = None,
        scheduling: int = None,
        start_time: int = None,
        status: str = None,
        total_completed: int = None,
        total_jobs: int = None,
        total_not_answered: int = None,
    ):
        self.briefs = briefs
        self.cancelled = cancelled
        self.categories = categories
        self.duration = duration
        self.executing = executing
        self.failed = failed
        self.paused = paused
        self.scheduling = scheduling
        self.start_time = start_time
        self.status = status
        self.total_completed = total_completed
        self.total_jobs = total_jobs
        self.total_not_answered = total_not_answered

    def validate(self):
        if self.briefs:
            for v1 in self.briefs:
                 if v1:
                    v1.validate()
        if self.categories:
            for v1 in self.categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Briefs'] = []
        if self.briefs is not None:
            for k1 in self.briefs:
                result['Briefs'].append(k1.to_map() if k1 else None)

        if self.cancelled is not None:
            result['Cancelled'] = self.cancelled

        result['Categories'] = []
        if self.categories is not None:
            for k1 in self.categories:
                result['Categories'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.executing is not None:
            result['Executing'] = self.executing

        if self.failed is not None:
            result['Failed'] = self.failed

        if self.paused is not None:
            result['Paused'] = self.paused

        if self.scheduling is not None:
            result['Scheduling'] = self.scheduling

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.total_completed is not None:
            result['TotalCompleted'] = self.total_completed

        if self.total_jobs is not None:
            result['TotalJobs'] = self.total_jobs

        if self.total_not_answered is not None:
            result['TotalNotAnswered'] = self.total_not_answered

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.briefs = []
        if m.get('Briefs') is not None:
            for k1 in m.get('Briefs'):
                temp_model = main_models.DescribeJobGroupResponseBodyJobGroupProgressBriefs()
                self.briefs.append(temp_model.from_map(k1))

        if m.get('Cancelled') is not None:
            self.cancelled = m.get('Cancelled')

        self.categories = []
        if m.get('Categories') is not None:
            for k1 in m.get('Categories'):
                temp_model = main_models.DescribeJobGroupResponseBodyJobGroupProgressCategories()
                self.categories.append(temp_model.from_map(k1))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Executing') is not None:
            self.executing = m.get('Executing')

        if m.get('Failed') is not None:
            self.failed = m.get('Failed')

        if m.get('Paused') is not None:
            self.paused = m.get('Paused')

        if m.get('Scheduling') is not None:
            self.scheduling = m.get('Scheduling')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalCompleted') is not None:
            self.total_completed = m.get('TotalCompleted')

        if m.get('TotalJobs') is not None:
            self.total_jobs = m.get('TotalJobs')

        if m.get('TotalNotAnswered') is not None:
            self.total_not_answered = m.get('TotalNotAnswered')

        return self

class DescribeJobGroupResponseBodyJobGroupProgressCategories(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeJobGroupResponseBodyJobGroupProgressBriefs(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeJobGroupResponseBodyJobGroupFlashSmsExtras(DaraModel):
    def __init__(
        self,
        config_id: str = None,
        template_id: str = None,
    ):
        self.config_id = config_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_id is not None:
            result['ConfigId'] = self.config_id

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigId') is not None:
            self.config_id = m.get('ConfigId')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        return self

class DescribeJobGroupResponseBodyJobGroupExportProgress(DaraModel):
    def __init__(
        self,
        file_http_url: str = None,
        progress: str = None,
        status: str = None,
    ):
        self.file_http_url = file_http_url
        self.progress = progress
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

