# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AssignJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
        strategy_json: str = None,
        calling_number: List[str] = None,
        jobs_json: List[str] = None,
    ):
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.strategy_json = strategy_json
        self.calling_number = calling_number
        self.jobs_json = jobs_json

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.strategy_json is not None:
            result['StrategyJson'] = self.strategy_json
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.jobs_json is not None:
            result['JobsJson'] = self.jobs_json
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('StrategyJson') is not None:
            self.strategy_json = m.get('StrategyJson')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('JobsJson') is not None:
            self.jobs_json = m.get('JobsJson')
        return self


class AssignJobsResponseBody(TeaModel):
    def __init__(
        self,
        job_group_id: str = None,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.job_group_id = job_group_id
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AssignJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AssignJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AssignJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        all: bool = None,
        scenario_id: str = None,
        job_group_id: str = None,
        job_id: List[str] = None,
        job_reference_id: List[str] = None,
    ):
        self.instance_id = instance_id
        self.all = all
        self.scenario_id = scenario_id
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.job_reference_id = job_reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.all is not None:
            result['All'] = self.all
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_reference_id is not None:
            result['JobReferenceId'] = self.job_reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobReferenceId') is not None:
            self.job_reference_id = m.get('JobReferenceId')
        return self


class CancelJobsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CancelJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBatchJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        batch_job_name: str = None,
        batch_job_description: str = None,
        scenario_id: str = None,
        script_id: str = None,
        strategy_json: str = None,
        job_file_path: str = None,
        submitted: bool = None,
        calling_number: List[str] = None,
    ):
        self.instance_id = instance_id
        self.batch_job_name = batch_job_name
        self.batch_job_description = batch_job_description
        self.scenario_id = scenario_id
        self.script_id = script_id
        self.strategy_json = strategy_json
        self.job_file_path = job_file_path
        self.submitted = submitted
        self.calling_number = calling_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.batch_job_name is not None:
            result['BatchJobName'] = self.batch_job_name
        if self.batch_job_description is not None:
            result['BatchJobDescription'] = self.batch_job_description
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.strategy_json is not None:
            result['StrategyJson'] = self.strategy_json
        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path
        if self.submitted is not None:
            result['Submitted'] = self.submitted
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BatchJobName') is not None:
            self.batch_job_name = m.get('BatchJobName')
        if m.get('BatchJobDescription') is not None:
            self.batch_job_description = m.get('BatchJobDescription')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('StrategyJson') is not None:
            self.strategy_json = m.get('StrategyJson')
        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')
        if m.get('Submitted') is not None:
            self.submitted = m.get('Submitted')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        return self


class CreateBatchJobsResponseBodyBatchJobStrategyWorkingTime(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        begin_time: str = None,
    ):
        self.end_time = end_time
        self.begin_time = begin_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        return self


class CreateBatchJobsResponseBodyBatchJobStrategy(TeaModel):
    def __init__(
        self,
        type: str = None,
        strategy_name: str = None,
        max_attempts_per_day: int = None,
        working_time: List[CreateBatchJobsResponseBodyBatchJobStrategyWorkingTime] = None,
        follow_up_strategy: str = None,
        end_time: int = None,
        start_time: int = None,
        is_template: bool = None,
        customized: str = None,
        strategy_id: str = None,
        repeat_days: List[str] = None,
        routing_strategy: str = None,
        min_attempt_interval: int = None,
        strategy_description: str = None,
        repeat_by: str = None,
    ):
        self.type = type
        self.strategy_name = strategy_name
        self.max_attempts_per_day = max_attempts_per_day
        self.working_time = working_time
        self.follow_up_strategy = follow_up_strategy
        self.end_time = end_time
        self.start_time = start_time
        self.is_template = is_template
        self.customized = customized
        self.strategy_id = strategy_id
        self.repeat_days = repeat_days
        self.routing_strategy = routing_strategy
        self.min_attempt_interval = min_attempt_interval
        self.strategy_description = strategy_description
        self.repeat_by = repeat_by

    def validate(self):
        if self.working_time:
            for k in self.working_time:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.max_attempts_per_day is not None:
            result['MaxAttemptsPerDay'] = self.max_attempts_per_day
        result['WorkingTime'] = []
        if self.working_time is not None:
            for k in self.working_time:
                result['WorkingTime'].append(k.to_map() if k else None)
        if self.follow_up_strategy is not None:
            result['FollowUpStrategy'] = self.follow_up_strategy
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.customized is not None:
            result['Customized'] = self.customized
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.routing_strategy is not None:
            result['RoutingStrategy'] = self.routing_strategy
        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval
        if self.strategy_description is not None:
            result['StrategyDescription'] = self.strategy_description
        if self.repeat_by is not None:
            result['RepeatBy'] = self.repeat_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('MaxAttemptsPerDay') is not None:
            self.max_attempts_per_day = m.get('MaxAttemptsPerDay')
        self.working_time = []
        if m.get('WorkingTime') is not None:
            for k in m.get('WorkingTime'):
                temp_model = CreateBatchJobsResponseBodyBatchJobStrategyWorkingTime()
                self.working_time.append(temp_model.from_map(k))
        if m.get('FollowUpStrategy') is not None:
            self.follow_up_strategy = m.get('FollowUpStrategy')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('Customized') is not None:
            self.customized = m.get('Customized')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RoutingStrategy') is not None:
            self.routing_strategy = m.get('RoutingStrategy')
        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')
        if m.get('StrategyDescription') is not None:
            self.strategy_description = m.get('StrategyDescription')
        if m.get('RepeatBy') is not None:
            self.repeat_by = m.get('RepeatBy')
        return self


class CreateBatchJobsResponseBodyBatchJob(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        scenario_id: str = None,
        strategy: CreateBatchJobsResponseBodyBatchJobStrategy = None,
        calling_numbers: List[str] = None,
        job_group_name: str = None,
        batch_job_id: str = None,
        job_file_path: str = None,
        job_group_description: str = None,
    ):
        self.creation_time = creation_time
        self.scenario_id = scenario_id
        self.strategy = strategy
        self.calling_numbers = calling_numbers
        self.job_group_name = job_group_name
        self.batch_job_id = batch_job_id
        self.job_file_path = job_file_path
        self.job_group_description = job_group_description

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.batch_job_id is not None:
            result['BatchJobId'] = self.batch_job_id
        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path
        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Strategy') is not None:
            temp_model = CreateBatchJobsResponseBodyBatchJobStrategy()
            self.strategy = temp_model.from_map(m['Strategy'])
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('BatchJobId') is not None:
            self.batch_job_id = m.get('BatchJobId')
        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')
        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')
        return self


class CreateBatchJobsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        batch_job: CreateBatchJobsResponseBodyBatchJob = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.batch_job = batch_job
        self.code = code
        self.success = success

    def validate(self):
        if self.batch_job:
            self.batch_job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.batch_job is not None:
            result['BatchJob'] = self.batch_job.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('BatchJob') is not None:
            temp_model = CreateBatchJobsResponseBodyBatchJob()
            self.batch_job = temp_model.from_map(m['BatchJob'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateBatchJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBatchJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBatchJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDialogueFlowRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        dialogue_name: str = None,
        script_id: str = None,
        dialogue_flow_type: str = None,
    ):
        self.instance_id = instance_id
        self.dialogue_name = dialogue_name
        self.script_id = script_id
        self.dialogue_flow_type = dialogue_flow_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.dialogue_name is not None:
            result['DialogueName'] = self.dialogue_name
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.dialogue_flow_type is not None:
            result['DialogueFlowType'] = self.dialogue_flow_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('DialogueName') is not None:
            self.dialogue_name = m.get('DialogueName')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('DialogueFlowType') is not None:
            self.dialogue_flow_type = m.get('DialogueFlowType')
        return self


class CreateDialogueFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        dialogue_flow_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.dialogue_flow_id = dialogue_flow_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.dialogue_flow_id is not None:
            result['DialogueFlowId'] = self.dialogue_flow_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('DialogueFlowId') is not None:
            self.dialogue_flow_id = m.get('DialogueFlowId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateDialogueFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDialogueFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDialogueFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGlobalQuestionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        global_question_name: str = None,
        global_question_type: str = None,
        questions: str = None,
        answers: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.global_question_name = global_question_name
        self.global_question_type = global_question_type
        self.questions = questions
        self.answers = answers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.global_question_name is not None:
            result['GlobalQuestionName'] = self.global_question_name
        if self.global_question_type is not None:
            result['GlobalQuestionType'] = self.global_question_type
        if self.questions is not None:
            result['Questions'] = self.questions
        if self.answers is not None:
            result['Answers'] = self.answers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('GlobalQuestionName') is not None:
            self.global_question_name = m.get('GlobalQuestionName')
        if m.get('GlobalQuestionType') is not None:
            self.global_question_type = m.get('GlobalQuestionType')
        if m.get('Questions') is not None:
            self.questions = m.get('Questions')
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        return self


class CreateGlobalQuestionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        global_question_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.global_question_id = global_question_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.global_question_id is not None:
            result['GlobalQuestionId'] = self.global_question_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('GlobalQuestionId') is not None:
            self.global_question_id = m.get('GlobalQuestionId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateGlobalQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGlobalQuestionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateGlobalQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_description: str = None,
        max_concurrent_conversation: int = None,
    ):
        self.instance_name = instance_name
        self.instance_description = instance_description
        self.max_concurrent_conversation = max_concurrent_conversation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')
        return self


class CreateInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        instance_name: str = None,
        max_concurrent_conversation: int = None,
        instance_id: str = None,
        instance_description: str = None,
    ):
        self.creation_time = creation_time
        self.instance_name = instance_name
        self.max_concurrent_conversation = max_concurrent_conversation
        self.instance_id = instance_id
        self.instance_description = instance_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        return self


class CreateInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        instance: CreateInstanceResponseBodyInstance = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.instance = instance
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Instance') is not None:
            temp_model = CreateInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIntentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        intent_name: str = None,
        intent_description: str = None,
        utterances: str = None,
        keywords: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.intent_name = intent_name
        self.intent_description = intent_description
        self.utterances = utterances
        self.keywords = keywords

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description
        if self.utterances is not None:
            result['Utterances'] = self.utterances
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')
        if m.get('Utterances') is not None:
            self.utterances = m.get('Utterances')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class CreateIntentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        intent_id: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class CreateIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateIntentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_name: str = None,
        job_group_description: str = None,
        scenario_id: str = None,
        script_id: str = None,
        strategy_json: str = None,
        calling_number: List[str] = None,
    ):
        self.instance_id = instance_id
        self.job_group_name = job_group_name
        self.job_group_description = job_group_description
        self.scenario_id = scenario_id
        self.script_id = script_id
        self.strategy_json = strategy_json
        self.calling_number = calling_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.strategy_json is not None:
            result['StrategyJson'] = self.strategy_json
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('StrategyJson') is not None:
            self.strategy_json = m.get('StrategyJson')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        return self


class CreateJobGroupResponseBodyJobGroupStrategyWorkingTime(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        begin_time: str = None,
    ):
        self.end_time = end_time
        self.begin_time = begin_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        return self


class CreateJobGroupResponseBodyJobGroupStrategy(TeaModel):
    def __init__(
        self,
        type: str = None,
        strategy_name: str = None,
        max_attempts_per_day: int = None,
        working_time: List[CreateJobGroupResponseBodyJobGroupStrategyWorkingTime] = None,
        follow_up_strategy: str = None,
        end_time: int = None,
        start_time: int = None,
        is_template: bool = None,
        customized: str = None,
        strategy_id: str = None,
        repeat_days: List[str] = None,
        routing_strategy: str = None,
        min_attempt_interval: int = None,
        strategy_description: str = None,
        repeat_by: str = None,
    ):
        self.type = type
        self.strategy_name = strategy_name
        self.max_attempts_per_day = max_attempts_per_day
        self.working_time = working_time
        self.follow_up_strategy = follow_up_strategy
        self.end_time = end_time
        self.start_time = start_time
        self.is_template = is_template
        self.customized = customized
        self.strategy_id = strategy_id
        self.repeat_days = repeat_days
        self.routing_strategy = routing_strategy
        self.min_attempt_interval = min_attempt_interval
        self.strategy_description = strategy_description
        self.repeat_by = repeat_by

    def validate(self):
        if self.working_time:
            for k in self.working_time:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.max_attempts_per_day is not None:
            result['MaxAttemptsPerDay'] = self.max_attempts_per_day
        result['WorkingTime'] = []
        if self.working_time is not None:
            for k in self.working_time:
                result['WorkingTime'].append(k.to_map() if k else None)
        if self.follow_up_strategy is not None:
            result['FollowUpStrategy'] = self.follow_up_strategy
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.customized is not None:
            result['Customized'] = self.customized
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.routing_strategy is not None:
            result['RoutingStrategy'] = self.routing_strategy
        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval
        if self.strategy_description is not None:
            result['StrategyDescription'] = self.strategy_description
        if self.repeat_by is not None:
            result['RepeatBy'] = self.repeat_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('MaxAttemptsPerDay') is not None:
            self.max_attempts_per_day = m.get('MaxAttemptsPerDay')
        self.working_time = []
        if m.get('WorkingTime') is not None:
            for k in m.get('WorkingTime'):
                temp_model = CreateJobGroupResponseBodyJobGroupStrategyWorkingTime()
                self.working_time.append(temp_model.from_map(k))
        if m.get('FollowUpStrategy') is not None:
            self.follow_up_strategy = m.get('FollowUpStrategy')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('Customized') is not None:
            self.customized = m.get('Customized')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RoutingStrategy') is not None:
            self.routing_strategy = m.get('RoutingStrategy')
        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')
        if m.get('StrategyDescription') is not None:
            self.strategy_description = m.get('StrategyDescription')
        if m.get('RepeatBy') is not None:
            self.repeat_by = m.get('RepeatBy')
        return self


class CreateJobGroupResponseBodyJobGroup(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        job_group_id: str = None,
        scenario_id: str = None,
        strategy: CreateJobGroupResponseBodyJobGroupStrategy = None,
        calling_numbers: List[str] = None,
        job_group_name: str = None,
        job_file_path: str = None,
        job_group_description: str = None,
    ):
        self.creation_time = creation_time
        self.job_group_id = job_group_id
        self.scenario_id = scenario_id
        self.strategy = strategy
        self.calling_numbers = calling_numbers
        self.job_group_name = job_group_name
        self.job_file_path = job_file_path
        self.job_group_description = job_group_description

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path
        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Strategy') is not None:
            temp_model = CreateJobGroupResponseBodyJobGroupStrategy()
            self.strategy = temp_model.from_map(m['Strategy'])
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')
        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')
        return self


class CreateJobGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_group: CreateJobGroupResponseBodyJobGroup = None,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.job_group = job_group
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.job_group:
            self.job_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_group is not None:
            result['JobGroup'] = self.job_group.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroup') is not None:
            temp_model = CreateJobGroupResponseBodyJobGroup()
            self.job_group = temp_model.from_map(m['JobGroup'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateJobGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateJobGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateJobGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOutboundCallNumberRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        number: str = None,
        rate_limit_period: int = None,
        rate_limit_count: int = None,
    ):
        self.instance_id = instance_id
        self.number = number
        self.rate_limit_period = rate_limit_period
        self.rate_limit_count = rate_limit_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.number is not None:
            result['Number'] = self.number
        if self.rate_limit_period is not None:
            result['RateLimitPeriod'] = self.rate_limit_period
        if self.rate_limit_count is not None:
            result['RateLimitCount'] = self.rate_limit_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('RateLimitPeriod') is not None:
            self.rate_limit_period = m.get('RateLimitPeriod')
        if m.get('RateLimitCount') is not None:
            self.rate_limit_count = m.get('RateLimitCount')
        return self


class CreateOutboundCallNumberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        outbound_call_number_id: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.outbound_call_number_id = outbound_call_number_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.outbound_call_number_id is not None:
            result['OutboundCallNumberId'] = self.outbound_call_number_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('OutboundCallNumberId') is not None:
            self.outbound_call_number_id = m.get('OutboundCallNumberId')
        return self


class CreateOutboundCallNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateOutboundCallNumberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateOutboundCallNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScriptRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_name: str = None,
        script_description: str = None,
        industry: str = None,
        scene: str = None,
    ):
        self.instance_id = instance_id
        self.script_name = script_name
        self.script_description = script_description
        self.industry = industry
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class CreateScriptResponseBodyScript(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: int = None,
        industry: str = None,
        script_description: str = None,
        is_drafted: bool = None,
        debug_status: str = None,
        script_id: str = None,
        is_debug_drafted: bool = None,
        script_name: str = None,
        scene: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.industry = industry
        self.script_description = script_description
        self.is_drafted = is_drafted
        self.debug_status = debug_status
        self.script_id = script_id
        self.is_debug_drafted = is_debug_drafted
        self.script_name = script_name
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description
        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted
        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.is_debug_drafted is not None:
            result['IsDebugDrafted'] = self.is_debug_drafted
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')
        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')
        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IsDebugDrafted') is not None:
            self.is_debug_drafted = m.get('IsDebugDrafted')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class CreateScriptResponseBody(TeaModel):
    def __init__(
        self,
        script: CreateScriptResponseBodyScript = None,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.script = script
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.script:
            self.script.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script is not None:
            result['Script'] = self.script.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Script') is not None:
            temp_model = CreateScriptResponseBodyScript()
            self.script = temp_model.from_map(m['Script'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScriptWaveformRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        script_content: str = None,
        file_id: str = None,
        file_name: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_content = script_content
        self.file_id = file_id
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_content is not None:
            result['ScriptContent'] = self.script_content
        if self.file_id is not None:
            result['FileId'] = self.file_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class CreateScriptWaveformResponseBody(TeaModel):
    def __init__(
        self,
        script_waveform_id: str = None,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.script_waveform_id = script_waveform_id
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script_waveform_id is not None:
            result['ScriptWaveformId'] = self.script_waveform_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScriptWaveformId') is not None:
            self.script_waveform_id = m.get('ScriptWaveformId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateScriptWaveformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateScriptWaveformResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateScriptWaveformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTagRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        tag_name: str = None,
        tag_group: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.tag_name = tag_name
        self.tag_group = tag_group

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')
        return self


class CreateTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        tag_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.tag_id = tag_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTagResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDialogueFlowRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        dialogue_flow_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.dialogue_flow_id = dialogue_flow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.dialogue_flow_id is not None:
            result['DialogueFlowId'] = self.dialogue_flow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('DialogueFlowId') is not None:
            self.dialogue_flow_id = m.get('DialogueFlowId')
        return self


class DeleteDialogueFlowResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteDialogueFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDialogueFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDialogueFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGlobalQuestionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        global_question_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.global_question_id = global_question_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.global_question_id is not None:
            result['GlobalQuestionId'] = self.global_question_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('GlobalQuestionId') is not None:
            self.global_question_id = m.get('GlobalQuestionId')
        return self


class DeleteGlobalQuestionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGlobalQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteGlobalQuestionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteGlobalQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteIntentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        intent_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DeleteIntentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteIntentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteJobGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.job_group_id = job_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        return self


class DeleteJobGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteJobGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteJobGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteJobGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteOutboundCallNumberRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        outbound_call_number_id: str = None,
    ):
        self.instance_id = instance_id
        self.outbound_call_number_id = outbound_call_number_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.outbound_call_number_id is not None:
            result['OutboundCallNumberId'] = self.outbound_call_number_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OutboundCallNumberId') is not None:
            self.outbound_call_number_id = m.get('OutboundCallNumberId')
        return self


class DeleteOutboundCallNumberResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteOutboundCallNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteOutboundCallNumberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteOutboundCallNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScriptRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class DeleteScriptResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScriptWaveformRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        script_waveform_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_waveform_id = script_waveform_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_waveform_id is not None:
            result['ScriptWaveformId'] = self.script_waveform_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptWaveformId') is not None:
            self.script_waveform_id = m.get('ScriptWaveformId')
        return self


class DeleteScriptWaveformResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteScriptWaveformResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteScriptWaveformResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteScriptWaveformResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeGlobalQuestionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        global_question_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.global_question_id = global_question_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.global_question_id is not None:
            result['GlobalQuestionId'] = self.global_question_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('GlobalQuestionId') is not None:
            self.global_question_id = m.get('GlobalQuestionId')
        return self


class DescribeGlobalQuestionResponseBodyGlobalQuestion(TeaModel):
    def __init__(
        self,
        global_question_id: str = None,
        answers: str = None,
        global_question_type: str = None,
        global_question_name: str = None,
        questions: str = None,
        script_id: str = None,
    ):
        self.global_question_id = global_question_id
        self.answers = answers
        self.global_question_type = global_question_type
        self.global_question_name = global_question_name
        self.questions = questions
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_question_id is not None:
            result['GlobalQuestionId'] = self.global_question_id
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.global_question_type is not None:
            result['GlobalQuestionType'] = self.global_question_type
        if self.global_question_name is not None:
            result['GlobalQuestionName'] = self.global_question_name
        if self.questions is not None:
            result['Questions'] = self.questions
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalQuestionId') is not None:
            self.global_question_id = m.get('GlobalQuestionId')
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('GlobalQuestionType') is not None:
            self.global_question_type = m.get('GlobalQuestionType')
        if m.get('GlobalQuestionName') is not None:
            self.global_question_name = m.get('GlobalQuestionName')
        if m.get('Questions') is not None:
            self.questions = m.get('Questions')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class DescribeGlobalQuestionResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        global_question: DescribeGlobalQuestionResponseBodyGlobalQuestion = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.global_question = global_question
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.global_question:
            self.global_question.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.global_question is not None:
            result['GlobalQuestion'] = self.global_question.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GlobalQuestion') is not None:
            temp_model = DescribeGlobalQuestionResponseBodyGlobalQuestion()
            self.global_question = temp_model.from_map(m['GlobalQuestion'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeGlobalQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeGlobalQuestionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeGlobalQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DescribeInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        instance_name: str = None,
        max_concurrent_conversation: int = None,
        instance_id: str = None,
        instance_description: str = None,
    ):
        self.creation_time = creation_time
        self.instance_name = instance_name
        self.max_concurrent_conversation = max_concurrent_conversation
        self.instance_id = instance_id
        self.instance_description = instance_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        return self


class DescribeInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        instance: DescribeInstanceResponseBodyInstance = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.instance = instance
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Instance') is not None:
            temp_model = DescribeInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeIntentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        intent_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class DescribeIntentResponseBodyIntent(TeaModel):
    def __init__(
        self,
        utterances: str = None,
        intent_description: str = None,
        update_time: int = None,
        create_time: int = None,
        keywords: str = None,
        script_id: str = None,
        intent_id: str = None,
        intent_name: str = None,
    ):
        self.utterances = utterances
        self.intent_description = intent_description
        self.update_time = update_time
        self.create_time = create_time
        self.keywords = keywords
        self.script_id = script_id
        self.intent_id = intent_id
        self.intent_name = intent_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.utterances is not None:
            result['Utterances'] = self.utterances
        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Utterances') is not None:
            self.utterances = m.get('Utterances')
        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        return self


class DescribeIntentResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        intent: DescribeIntentResponseBodyIntent = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.intent = intent
        self.code = code
        self.success = success

    def validate(self):
        if self.intent:
            self.intent.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.intent is not None:
            result['Intent'] = self.intent.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Intent') is not None:
            temp_model = DescribeIntentResponseBodyIntent()
            self.intent = temp_model.from_map(m['Intent'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeIntentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_id: str = None,
    ):
        self.instance_id = instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeJobResponseBodyJobSummary(TeaModel):
    def __init__(
        self,
        summary_name: str = None,
        category: str = None,
        content: str = None,
    ):
        self.summary_name = summary_name
        self.category = category
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary_name is not None:
            result['SummaryName'] = self.summary_name
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeJobResponseBodyJobContacts(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        state: str = None,
        contact_id: str = None,
        honorific: str = None,
        job_id: str = None,
        contact_name: str = None,
        role: str = None,
        reference_id: str = None,
    ):
        self.phone_number = phone_number
        self.state = state
        self.contact_id = contact_id
        self.honorific = honorific
        self.job_id = job_id
        self.contact_name = contact_name
        self.role = role
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.state is not None:
            result['State'] = self.state
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.honorific is not None:
            result['Honorific'] = self.honorific
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.role is not None:
            result['Role'] = self.role
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        return self


class DescribeJobResponseBodyJobExtras(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeJobResponseBodyJobTasksContact(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        state: str = None,
        contact_id: str = None,
        honorific: str = None,
        job_id: str = None,
        contact_name: str = None,
        role: str = None,
        reference_id: str = None,
    ):
        self.phone_number = phone_number
        self.state = state
        self.contact_id = contact_id
        self.honorific = honorific
        self.job_id = job_id
        self.contact_name = contact_name
        self.role = role
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.state is not None:
            result['State'] = self.state
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.honorific is not None:
            result['Honorific'] = self.honorific
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.role is not None:
            result['Role'] = self.role
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        return self


class DescribeJobResponseBodyJobTasksConversationSummary(TeaModel):
    def __init__(
        self,
        summary_name: str = None,
        category: str = None,
        content: str = None,
    ):
        self.summary_name = summary_name
        self.category = category
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary_name is not None:
            result['SummaryName'] = self.summary_name
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DescribeJobResponseBodyJobTasksConversation(TeaModel):
    def __init__(
        self,
        summary: List[DescribeJobResponseBodyJobTasksConversationSummary] = None,
        speaker: str = None,
        timestamp: int = None,
        script: str = None,
    ):
        self.summary = summary
        self.speaker = speaker
        self.timestamp = timestamp
        self.script = script

    def validate(self):
        if self.summary:
            for k in self.summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Summary'] = []
        if self.summary is not None:
            for k in self.summary:
                result['Summary'].append(k.to_map() if k else None)
        if self.speaker is not None:
            result['Speaker'] = self.speaker
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.script is not None:
            result['Script'] = self.script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summary = []
        if m.get('Summary') is not None:
            for k in m.get('Summary'):
                temp_model = DescribeJobResponseBodyJobTasksConversationSummary()
                self.summary.append(temp_model.from_map(k))
        if m.get('Speaker') is not None:
            self.speaker = m.get('Speaker')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        return self


class DescribeJobResponseBodyJobTasks(TeaModel):
    def __init__(
        self,
        status: str = None,
        planed_time: int = None,
        chatbot_id: str = None,
        actual_time: int = None,
        called_number: str = None,
        scenario_id: str = None,
        contact: DescribeJobResponseBodyJobTasksContact = None,
        job_id: str = None,
        call_id: str = None,
        calling_number: str = None,
        brief: str = None,
        duration: int = None,
        task_id: str = None,
        conversation: List[DescribeJobResponseBodyJobTasksConversation] = None,
    ):
        self.status = status
        self.planed_time = planed_time
        self.chatbot_id = chatbot_id
        self.actual_time = actual_time
        self.called_number = called_number
        self.scenario_id = scenario_id
        self.contact = contact
        self.job_id = job_id
        self.call_id = call_id
        self.calling_number = calling_number
        self.brief = brief
        self.duration = duration
        self.task_id = task_id
        self.conversation = conversation

    def validate(self):
        if self.contact:
            self.contact.validate()
        if self.conversation:
            for k in self.conversation:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.planed_time is not None:
            result['PlanedTime'] = self.planed_time
        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.contact is not None:
            result['Contact'] = self.contact.to_map()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.brief is not None:
            result['Brief'] = self.brief
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        result['Conversation'] = []
        if self.conversation is not None:
            for k in self.conversation:
                result['Conversation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PlanedTime') is not None:
            self.planed_time = m.get('PlanedTime')
        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Contact') is not None:
            temp_model = DescribeJobResponseBodyJobTasksContact()
            self.contact = temp_model.from_map(m['Contact'])
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('Brief') is not None:
            self.brief = m.get('Brief')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        self.conversation = []
        if m.get('Conversation') is not None:
            for k in m.get('Conversation'):
                temp_model = DescribeJobResponseBodyJobTasksConversation()
                self.conversation.append(temp_model.from_map(k))
        return self


class DescribeJobResponseBodyJob(TeaModel):
    def __init__(
        self,
        status: str = None,
        calling_numbers: List[str] = None,
        summary: List[DescribeJobResponseBodyJobSummary] = None,
        contacts: List[DescribeJobResponseBodyJobContacts] = None,
        priority: int = None,
        system_priority: int = None,
        failure_reason: str = None,
        extras: List[DescribeJobResponseBodyJobExtras] = None,
        reference_id: str = None,
        scenario_id: str = None,
        job_group_id: str = None,
        tasks: List[DescribeJobResponseBodyJobTasks] = None,
        strategy_id: str = None,
        job_id: str = None,
    ):
        self.status = status
        self.calling_numbers = calling_numbers
        self.summary = summary
        self.contacts = contacts
        self.priority = priority
        self.system_priority = system_priority
        self.failure_reason = failure_reason
        self.extras = extras
        self.reference_id = reference_id
        self.scenario_id = scenario_id
        self.job_group_id = job_group_id
        self.tasks = tasks
        self.strategy_id = strategy_id
        self.job_id = job_id

    def validate(self):
        if self.summary:
            for k in self.summary:
                if k:
                    k.validate()
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()
        if self.extras:
            for k in self.extras:
                if k:
                    k.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers
        result['Summary'] = []
        if self.summary is not None:
            for k in self.summary:
                result['Summary'].append(k.to_map() if k else None)
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.system_priority is not None:
            result['SystemPriority'] = self.system_priority
        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason
        result['Extras'] = []
        if self.extras is not None:
            for k in self.extras:
                result['Extras'].append(k.to_map() if k else None)
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')
        self.summary = []
        if m.get('Summary') is not None:
            for k in m.get('Summary'):
                temp_model = DescribeJobResponseBodyJobSummary()
                self.summary.append(temp_model.from_map(k))
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = DescribeJobResponseBodyJobContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SystemPriority') is not None:
            self.system_priority = m.get('SystemPriority')
        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')
        self.extras = []
        if m.get('Extras') is not None:
            for k in m.get('Extras'):
                temp_model = DescribeJobResponseBodyJobExtras()
                self.extras.append(temp_model.from_map(k))
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = DescribeJobResponseBodyJobTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class DescribeJobResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        job: DescribeJobResponseBodyJob = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.job = job
        self.code = code
        self.success = success

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.job is not None:
            result['Job'] = self.job.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Job') is not None:
            temp_model = DescribeJobResponseBodyJob()
            self.job = temp_model.from_map(m['Job'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeJobGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
        brief_types: List[str] = None,
    ):
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.brief_types = brief_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.brief_types is not None:
            result['BriefTypes'] = self.brief_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('BriefTypes') is not None:
            self.brief_types = m.get('BriefTypes')
        return self


class DescribeJobGroupResponseBodyJobGroupStrategyWorkingTime(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        begin_time: str = None,
    ):
        self.end_time = end_time
        self.begin_time = begin_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        return self


class DescribeJobGroupResponseBodyJobGroupStrategy(TeaModel):
    def __init__(
        self,
        type: str = None,
        strategy_name: str = None,
        max_attempts_per_day: int = None,
        working_time: List[DescribeJobGroupResponseBodyJobGroupStrategyWorkingTime] = None,
        follow_up_strategy: str = None,
        end_time: int = None,
        start_time: int = None,
        is_template: bool = None,
        customized: str = None,
        strategy_id: str = None,
        repeat_days: List[str] = None,
        routing_strategy: str = None,
        min_attempt_interval: int = None,
        strategy_description: str = None,
        repeat_by: str = None,
    ):
        self.type = type
        self.strategy_name = strategy_name
        self.max_attempts_per_day = max_attempts_per_day
        self.working_time = working_time
        self.follow_up_strategy = follow_up_strategy
        self.end_time = end_time
        self.start_time = start_time
        self.is_template = is_template
        self.customized = customized
        self.strategy_id = strategy_id
        self.repeat_days = repeat_days
        self.routing_strategy = routing_strategy
        self.min_attempt_interval = min_attempt_interval
        self.strategy_description = strategy_description
        self.repeat_by = repeat_by

    def validate(self):
        if self.working_time:
            for k in self.working_time:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.max_attempts_per_day is not None:
            result['MaxAttemptsPerDay'] = self.max_attempts_per_day
        result['WorkingTime'] = []
        if self.working_time is not None:
            for k in self.working_time:
                result['WorkingTime'].append(k.to_map() if k else None)
        if self.follow_up_strategy is not None:
            result['FollowUpStrategy'] = self.follow_up_strategy
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.customized is not None:
            result['Customized'] = self.customized
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.routing_strategy is not None:
            result['RoutingStrategy'] = self.routing_strategy
        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval
        if self.strategy_description is not None:
            result['StrategyDescription'] = self.strategy_description
        if self.repeat_by is not None:
            result['RepeatBy'] = self.repeat_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('MaxAttemptsPerDay') is not None:
            self.max_attempts_per_day = m.get('MaxAttemptsPerDay')
        self.working_time = []
        if m.get('WorkingTime') is not None:
            for k in m.get('WorkingTime'):
                temp_model = DescribeJobGroupResponseBodyJobGroupStrategyWorkingTime()
                self.working_time.append(temp_model.from_map(k))
        if m.get('FollowUpStrategy') is not None:
            self.follow_up_strategy = m.get('FollowUpStrategy')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('Customized') is not None:
            self.customized = m.get('Customized')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RoutingStrategy') is not None:
            self.routing_strategy = m.get('RoutingStrategy')
        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')
        if m.get('StrategyDescription') is not None:
            self.strategy_description = m.get('StrategyDescription')
        if m.get('RepeatBy') is not None:
            self.repeat_by = m.get('RepeatBy')
        return self


class DescribeJobGroupResponseBodyJobGroupProgressBriefs(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeJobGroupResponseBodyJobGroupProgressCategories(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeJobGroupResponseBodyJobGroupProgress(TeaModel):
    def __init__(
        self,
        status: str = None,
        failed: int = None,
        total_completed: int = None,
        briefs: List[DescribeJobGroupResponseBodyJobGroupProgressBriefs] = None,
        paused: int = None,
        cancelled: int = None,
        total_not_answered: int = None,
        start_time: int = None,
        executing: int = None,
        categories: List[DescribeJobGroupResponseBodyJobGroupProgressCategories] = None,
        total_jobs: int = None,
        duration: int = None,
        scheduling: int = None,
    ):
        self.status = status
        self.failed = failed
        self.total_completed = total_completed
        self.briefs = briefs
        self.paused = paused
        self.cancelled = cancelled
        self.total_not_answered = total_not_answered
        self.start_time = start_time
        self.executing = executing
        self.categories = categories
        self.total_jobs = total_jobs
        self.duration = duration
        self.scheduling = scheduling

    def validate(self):
        if self.briefs:
            for k in self.briefs:
                if k:
                    k.validate()
        if self.categories:
            for k in self.categories:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.failed is not None:
            result['Failed'] = self.failed
        if self.total_completed is not None:
            result['TotalCompleted'] = self.total_completed
        result['Briefs'] = []
        if self.briefs is not None:
            for k in self.briefs:
                result['Briefs'].append(k.to_map() if k else None)
        if self.paused is not None:
            result['Paused'] = self.paused
        if self.cancelled is not None:
            result['Cancelled'] = self.cancelled
        if self.total_not_answered is not None:
            result['TotalNotAnswered'] = self.total_not_answered
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.executing is not None:
            result['Executing'] = self.executing
        result['Categories'] = []
        if self.categories is not None:
            for k in self.categories:
                result['Categories'].append(k.to_map() if k else None)
        if self.total_jobs is not None:
            result['TotalJobs'] = self.total_jobs
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.scheduling is not None:
            result['Scheduling'] = self.scheduling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Failed') is not None:
            self.failed = m.get('Failed')
        if m.get('TotalCompleted') is not None:
            self.total_completed = m.get('TotalCompleted')
        self.briefs = []
        if m.get('Briefs') is not None:
            for k in m.get('Briefs'):
                temp_model = DescribeJobGroupResponseBodyJobGroupProgressBriefs()
                self.briefs.append(temp_model.from_map(k))
        if m.get('Paused') is not None:
            self.paused = m.get('Paused')
        if m.get('Cancelled') is not None:
            self.cancelled = m.get('Cancelled')
        if m.get('TotalNotAnswered') is not None:
            self.total_not_answered = m.get('TotalNotAnswered')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Executing') is not None:
            self.executing = m.get('Executing')
        self.categories = []
        if m.get('Categories') is not None:
            for k in m.get('Categories'):
                temp_model = DescribeJobGroupResponseBodyJobGroupProgressCategories()
                self.categories.append(temp_model.from_map(k))
        if m.get('TotalJobs') is not None:
            self.total_jobs = m.get('TotalJobs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Scheduling') is not None:
            self.scheduling = m.get('Scheduling')
        return self


class DescribeJobGroupResponseBodyJobGroup(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        job_group_id: str = None,
        scenario_id: str = None,
        strategy: DescribeJobGroupResponseBodyJobGroupStrategy = None,
        calling_numbers: List[str] = None,
        progress: DescribeJobGroupResponseBodyJobGroupProgress = None,
        job_group_name: str = None,
        job_file_path: str = None,
        script_id: str = None,
        job_group_description: str = None,
        script_name: str = None,
    ):
        self.creation_time = creation_time
        self.job_group_id = job_group_id
        self.scenario_id = scenario_id
        self.strategy = strategy
        self.calling_numbers = calling_numbers
        self.progress = progress
        self.job_group_name = job_group_name
        self.job_file_path = job_file_path
        self.script_id = script_id
        self.job_group_description = job_group_description
        self.script_name = script_name

    def validate(self):
        if self.strategy:
            self.strategy.validate()
        if self.progress:
            self.progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers
        if self.progress is not None:
            result['Progress'] = self.progress.to_map()
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Strategy') is not None:
            temp_model = DescribeJobGroupResponseBodyJobGroupStrategy()
            self.strategy = temp_model.from_map(m['Strategy'])
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')
        if m.get('Progress') is not None:
            temp_model = DescribeJobGroupResponseBodyJobGroupProgress()
            self.progress = temp_model.from_map(m['Progress'])
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        return self


class DescribeJobGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_group: DescribeJobGroupResponseBodyJobGroup = None,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.job_group = job_group
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.job_group:
            self.job_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_group is not None:
            result['JobGroup'] = self.job_group.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroup') is not None:
            temp_model = DescribeJobGroupResponseBodyJobGroup()
            self.job_group = temp_model.from_map(m['JobGroup'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeJobGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeJobGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeJobGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScriptRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class DescribeScriptResponseBodyScript(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: int = None,
        industry: str = None,
        script_description: str = None,
        is_drafted: bool = None,
        debug_status: str = None,
        script_id: str = None,
        is_debug_drafted: bool = None,
        script_name: str = None,
        scene: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.industry = industry
        self.script_description = script_description
        self.is_drafted = is_drafted
        self.debug_status = debug_status
        self.script_id = script_id
        self.is_debug_drafted = is_debug_drafted
        self.script_name = script_name
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description
        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted
        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.is_debug_drafted is not None:
            result['IsDebugDrafted'] = self.is_debug_drafted
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')
        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')
        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IsDebugDrafted') is not None:
            self.is_debug_drafted = m.get('IsDebugDrafted')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class DescribeScriptResponseBody(TeaModel):
    def __init__(
        self,
        script: DescribeScriptResponseBodyScript = None,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.script = script
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.script:
            self.script.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script is not None:
            result['Script'] = self.script.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Script') is not None:
            temp_model = DescribeScriptResponseBodyScript()
            self.script = temp_model.from_map(m['Script'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeScriptVoiceConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        script_voice_config_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_voice_config_id = script_voice_config_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_voice_config_id is not None:
            result['ScriptVoiceConfigId'] = self.script_voice_config_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptVoiceConfigId') is not None:
            self.script_voice_config_id = m.get('ScriptVoiceConfigId')
        return self


class DescribeScriptVoiceConfigResponseBodyScriptVoiceConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        script_voice_config_id: str = None,
        script_content: str = None,
        instance_id: str = None,
        script_id: str = None,
        script_waveform_relation: str = None,
        source: str = None,
    ):
        self.type = type
        self.script_voice_config_id = script_voice_config_id
        self.script_content = script_content
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_waveform_relation = script_waveform_relation
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.script_voice_config_id is not None:
            result['ScriptVoiceConfigId'] = self.script_voice_config_id
        if self.script_content is not None:
            result['ScriptContent'] = self.script_content
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_waveform_relation is not None:
            result['ScriptWaveformRelation'] = self.script_waveform_relation
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ScriptVoiceConfigId') is not None:
            self.script_voice_config_id = m.get('ScriptVoiceConfigId')
        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptWaveformRelation') is not None:
            self.script_waveform_relation = m.get('ScriptWaveformRelation')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class DescribeScriptVoiceConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        script_voice_config: DescribeScriptVoiceConfigResponseBodyScriptVoiceConfig = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.script_voice_config = script_voice_config

    def validate(self):
        if self.script_voice_config:
            self.script_voice_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.script_voice_config is not None:
            result['ScriptVoiceConfig'] = self.script_voice_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ScriptVoiceConfig') is not None:
            temp_model = DescribeScriptVoiceConfigResponseBodyScriptVoiceConfig()
            self.script_voice_config = temp_model.from_map(m['ScriptVoiceConfig'])
        return self


class DescribeScriptVoiceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeScriptVoiceConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeScriptVoiceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTagHitsSummaryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.job_group_id = job_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        return self


class DescribeTagHitsSummaryResponseBodyTagGroups(TeaModel):
    def __init__(
        self,
        tag_group: str = None,
        tag_group_index: int = None,
        script_id: str = None,
        id: str = None,
    ):
        self.tag_group = tag_group
        self.tag_group_index = tag_group_index
        self.script_id = script_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group
        if self.tag_group_index is not None:
            result['TagGroupIndex'] = self.tag_group_index
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')
        if m.get('TagGroupIndex') is not None:
            self.tag_group_index = m.get('TagGroupIndex')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeTagHitsSummaryResponseBodyTagHitsList(TeaModel):
    def __init__(
        self,
        hit_count: int = None,
        tag_group: str = None,
        tag_name: str = None,
    ):
        self.hit_count = hit_count
        self.tag_group = tag_group
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hit_count is not None:
            result['HitCount'] = self.hit_count
        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HitCount') is not None:
            self.hit_count = m.get('HitCount')
        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        return self


class DescribeTagHitsSummaryResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        tag_groups: List[DescribeTagHitsSummaryResponseBodyTagGroups] = None,
        http_status_code: int = None,
        tag_hits_list: List[DescribeTagHitsSummaryResponseBodyTagHitsList] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.tag_groups = tag_groups
        self.http_status_code = http_status_code
        self.tag_hits_list = tag_hits_list
        self.code = code
        self.success = success

    def validate(self):
        if self.tag_groups:
            for k in self.tag_groups:
                if k:
                    k.validate()
        if self.tag_hits_list:
            for k in self.tag_hits_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagGroups'] = []
        if self.tag_groups is not None:
            for k in self.tag_groups:
                result['TagGroups'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['TagHitsList'] = []
        if self.tag_hits_list is not None:
            for k in self.tag_hits_list:
                result['TagHitsList'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_groups = []
        if m.get('TagGroups') is not None:
            for k in m.get('TagGroups'):
                temp_model = DescribeTagHitsSummaryResponseBodyTagGroups()
                self.tag_groups.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.tag_hits_list = []
        if m.get('TagHitsList') is not None:
            for k in m.get('TagHitsList'):
                temp_model = DescribeTagHitsSummaryResponseBodyTagHitsList()
                self.tag_hits_list.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTagHitsSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTagHitsSummaryResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTagHitsSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTTSConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class DescribeTTSConfigResponseBodyTTSConfig(TeaModel):
    def __init__(
        self,
        voice: str = None,
        speech_rate: str = None,
        volume: str = None,
        instance_id: str = None,
        script_id: str = None,
        id: str = None,
    ):
        self.voice = voice
        self.speech_rate = speech_rate
        self.volume = volume
        self.instance_id = instance_id
        self.script_id = script_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeTTSConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        ttsconfig: DescribeTTSConfigResponseBodyTTSConfig = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.ttsconfig = ttsconfig
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.ttsconfig:
            self.ttsconfig.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ttsconfig is not None:
            result['TTSConfig'] = self.ttsconfig.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TTSConfig') is not None:
            temp_model = DescribeTTSConfigResponseBodyTTSConfig()
            self.ttsconfig = temp_model.from_map(m['TTSConfig'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTTSConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTTSConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTTSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTTSDemoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        voice: str = None,
        text: str = None,
        speech_rate: int = None,
        volume: int = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.voice = voice
        self.text = text
        self.speech_rate = speech_rate
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.text is not None:
            result['Text'] = self.text
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class DescribeTTSDemoResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        audition_url: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.audition_url = audition_url
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.audition_url is not None:
            result['AuditionUrl'] = self.audition_url
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('AuditionUrl') is not None:
            self.audition_url = m.get('AuditionUrl')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DescribeTTSDemoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeTTSDemoResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeTTSDemoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DialogueRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        call_id: str = None,
        call_type: str = None,
        scenario_id: str = None,
        task_id: str = None,
        utterance: str = None,
        action_key: str = None,
        action_params: str = None,
        calling_number: str = None,
        called_number: str = None,
    ):
        self.instance_id = instance_id
        self.call_id = call_id
        self.call_type = call_type
        self.scenario_id = scenario_id
        self.task_id = task_id
        self.utterance = utterance
        self.action_key = action_key
        self.action_params = action_params
        self.calling_number = calling_number
        self.called_number = called_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.call_type is not None:
            result['CallType'] = self.call_type
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.utterance is not None:
            result['Utterance'] = self.utterance
        if self.action_key is not None:
            result['ActionKey'] = self.action_key
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallType') is not None:
            self.call_type = m.get('CallType')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')
        if m.get('ActionKey') is not None:
            self.action_key = m.get('ActionKey')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        return self


class DialogueResponseBodyFeedback(TeaModel):
    def __init__(
        self,
        action: str = None,
        interruptible: bool = None,
        action_params: str = None,
        content: str = None,
    ):
        self.action = action
        self.interruptible = interruptible
        self.action_params = action_params
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.interruptible is not None:
            result['Interruptible'] = self.interruptible
        if self.action_params is not None:
            result['ActionParams'] = self.action_params
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('Interruptible') is not None:
            self.interruptible = m.get('Interruptible')
        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class DialogueResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        feedback: DialogueResponseBodyFeedback = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.feedback = feedback
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.feedback:
            self.feedback.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.feedback is not None:
            result['Feedback'] = self.feedback.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Feedback') is not None:
            temp_model = DialogueResponseBodyFeedback()
            self.feedback = temp_model.from_map(m['Feedback'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DialogueResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadRecordingRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: str = None,
    ):
        self.instance_id = instance_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DownloadRecordingResponseBodyDownloadParams(TeaModel):
    def __init__(
        self,
        signature_url: str = None,
        file_name: str = None,
    ):
        self.signature_url = signature_url
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class DownloadRecordingResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        download_params: DownloadRecordingResponseBodyDownloadParams = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.download_params = download_params
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.download_params:
            self.download_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.download_params is not None:
            result['DownloadParams'] = self.download_params.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DownloadParams') is not None:
            temp_model = DownloadRecordingResponseBodyDownloadParams()
            self.download_params = temp_model.from_map(m['DownloadParams'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DownloadRecordingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DownloadRecordingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DownloadRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DuplicateScriptRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        source_script_id: str = None,
        name: str = None,
    ):
        self.instance_id = instance_id
        self.source_script_id = source_script_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.source_script_id is not None:
            result['SourceScriptId'] = self.source_script_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SourceScriptId') is not None:
            self.source_script_id = m.get('SourceScriptId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DuplicateScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        script_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.script_id = script_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DuplicateScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DuplicateScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DuplicateScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportScriptRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class ExportScriptResponseBodyDownloadParams(TeaModel):
    def __init__(
        self,
        signature_url: str = None,
    ):
        self.signature_url = signature_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')
        return self


class ExportScriptResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        download_params: ExportScriptResponseBodyDownloadParams = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.download_params = download_params
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.download_params:
            self.download_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.download_params is not None:
            result['DownloadParams'] = self.download_params.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DownloadParams') is not None:
            temp_model = ExportScriptResponseBodyDownloadParams()
            self.download_params = temp_model.from_map(m['DownloadParams'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ExportScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ExportScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportScriptRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        signature_url: str = None,
    ):
        self.instance_id = instance_id
        self.signature_url = signature_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.signature_url is not None:
            result['SignatureUrl'] = self.signature_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SignatureUrl') is not None:
            self.signature_url = m.get('SignatureUrl')
        return self


class ImportScriptResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        script_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.script_id = script_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ImportScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InflightTaskTimeoutRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: str = None,
        instance_owner_id: int = None,
    ):
        self.instance_id = instance_id
        self.task_id = task_id
        self.instance_owner_id = instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        return self


class InflightTaskTimeoutResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InflightTaskTimeoutResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InflightTaskTimeoutResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = InflightTaskTimeoutResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDialogueFlowsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class ListDialogueFlowsResponseBodyDialogueFlows(TeaModel):
    def __init__(
        self,
        dialogue_flow_definition: str = None,
        dialogue_flow_type: str = None,
        dialogue_flow_id: str = None,
        dialogue_flow_name: str = None,
        script_id: str = None,
        script_version: str = None,
    ):
        self.dialogue_flow_definition = dialogue_flow_definition
        self.dialogue_flow_type = dialogue_flow_type
        self.dialogue_flow_id = dialogue_flow_id
        self.dialogue_flow_name = dialogue_flow_name
        self.script_id = script_id
        self.script_version = script_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialogue_flow_definition is not None:
            result['DialogueFlowDefinition'] = self.dialogue_flow_definition
        if self.dialogue_flow_type is not None:
            result['DialogueFlowType'] = self.dialogue_flow_type
        if self.dialogue_flow_id is not None:
            result['DialogueFlowId'] = self.dialogue_flow_id
        if self.dialogue_flow_name is not None:
            result['DialogueFlowName'] = self.dialogue_flow_name
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_version is not None:
            result['ScriptVersion'] = self.script_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogueFlowDefinition') is not None:
            self.dialogue_flow_definition = m.get('DialogueFlowDefinition')
        if m.get('DialogueFlowType') is not None:
            self.dialogue_flow_type = m.get('DialogueFlowType')
        if m.get('DialogueFlowId') is not None:
            self.dialogue_flow_id = m.get('DialogueFlowId')
        if m.get('DialogueFlowName') is not None:
            self.dialogue_flow_name = m.get('DialogueFlowName')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptVersion') is not None:
            self.script_version = m.get('ScriptVersion')
        return self


class ListDialogueFlowsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        dialogue_flows: List[ListDialogueFlowsResponseBodyDialogueFlows] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.dialogue_flows = dialogue_flows

    def validate(self):
        if self.dialogue_flows:
            for k in self.dialogue_flows:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['DialogueFlows'] = []
        if self.dialogue_flows is not None:
            for k in self.dialogue_flows:
                result['DialogueFlows'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.dialogue_flows = []
        if m.get('DialogueFlows') is not None:
            for k in m.get('DialogueFlows'):
                temp_model = ListDialogueFlowsResponseBodyDialogueFlows()
                self.dialogue_flows.append(temp_model.from_map(k))
        return self


class ListDialogueFlowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDialogueFlowsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDialogueFlowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGlobalQuestionsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListGlobalQuestionsResponseBodyGlobalQuestionsList(TeaModel):
    def __init__(
        self,
        global_question_id: str = None,
        answers: str = None,
        global_question_type: str = None,
        global_question_name: str = None,
        questions: str = None,
        script_id: str = None,
    ):
        self.global_question_id = global_question_id
        self.answers = answers
        self.global_question_type = global_question_type
        self.global_question_name = global_question_name
        self.questions = questions
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.global_question_id is not None:
            result['GlobalQuestionId'] = self.global_question_id
        if self.answers is not None:
            result['Answers'] = self.answers
        if self.global_question_type is not None:
            result['GlobalQuestionType'] = self.global_question_type
        if self.global_question_name is not None:
            result['GlobalQuestionName'] = self.global_question_name
        if self.questions is not None:
            result['Questions'] = self.questions
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GlobalQuestionId') is not None:
            self.global_question_id = m.get('GlobalQuestionId')
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        if m.get('GlobalQuestionType') is not None:
            self.global_question_type = m.get('GlobalQuestionType')
        if m.get('GlobalQuestionName') is not None:
            self.global_question_name = m.get('GlobalQuestionName')
        if m.get('Questions') is not None:
            self.questions = m.get('Questions')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class ListGlobalQuestionsResponseBodyGlobalQuestions(TeaModel):
    def __init__(
        self,
        list: List[ListGlobalQuestionsResponseBodyGlobalQuestionsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListGlobalQuestionsResponseBodyGlobalQuestionsList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListGlobalQuestionsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        global_questions: ListGlobalQuestionsResponseBodyGlobalQuestions = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.global_questions = global_questions
        self.success = success

    def validate(self):
        if self.global_questions:
            self.global_questions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.global_questions is not None:
            result['GlobalQuestions'] = self.global_questions.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GlobalQuestions') is not None:
            temp_model = ListGlobalQuestionsResponseBodyGlobalQuestions()
            self.global_questions = temp_model.from_map(m['GlobalQuestions'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListGlobalQuestionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGlobalQuestionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListGlobalQuestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesResponseBodyInstances(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        instance_name: str = None,
        max_concurrent_conversation: int = None,
        instance_id: str = None,
        instance_description: str = None,
    ):
        self.creation_time = creation_time
        self.instance_name = instance_name
        self.max_concurrent_conversation = max_concurrent_conversation
        self.instance_id = instance_id
        self.instance_description = instance_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[ListInstancesResponseBodyInstances] = None,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.instances = instances
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntentsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListIntentsResponseBodyIntentsList(TeaModel):
    def __init__(
        self,
        utterances: str = None,
        intent_description: str = None,
        update_time: int = None,
        create_time: int = None,
        keywords: str = None,
        script_id: str = None,
        intent_id: str = None,
        intent_name: str = None,
    ):
        self.utterances = utterances
        self.intent_description = intent_description
        self.update_time = update_time
        self.create_time = create_time
        self.keywords = keywords
        self.script_id = script_id
        self.intent_id = intent_id
        self.intent_name = intent_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.utterances is not None:
            result['Utterances'] = self.utterances
        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Utterances') is not None:
            self.utterances = m.get('Utterances')
        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        return self


class ListIntentsResponseBodyIntents(TeaModel):
    def __init__(
        self,
        list: List[ListIntentsResponseBodyIntentsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListIntentsResponseBodyIntentsList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListIntentsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        intents: ListIntentsResponseBodyIntents = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.intents = intents
        self.code = code
        self.success = success

    def validate(self):
        if self.intents:
            self.intents.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.intents is not None:
            result['Intents'] = self.intents.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Intents') is not None:
            temp_model = ListIntentsResponseBodyIntents()
            self.intents = temp_model.from_map(m['Intents'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListIntentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListIntentsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListIntentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        start_time: int = None,
        end_time: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListJobGroupsResponseBodyJobGroupsListStrategy(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListJobGroupsResponseBodyJobGroupsListProgress(TeaModel):
    def __init__(
        self,
        status: str = None,
        total_not_answered: int = None,
        start_time: int = None,
        total_completed: int = None,
        total_jobs: int = None,
        duration: int = None,
    ):
        self.status = status
        self.total_not_answered = total_not_answered
        self.start_time = start_time
        self.total_completed = total_completed
        self.total_jobs = total_jobs
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.total_not_answered is not None:
            result['TotalNotAnswered'] = self.total_not_answered
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.total_completed is not None:
            result['TotalCompleted'] = self.total_completed
        if self.total_jobs is not None:
            result['TotalJobs'] = self.total_jobs
        if self.duration is not None:
            result['Duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TotalNotAnswered') is not None:
            self.total_not_answered = m.get('TotalNotAnswered')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TotalCompleted') is not None:
            self.total_completed = m.get('TotalCompleted')
        if m.get('TotalJobs') is not None:
            self.total_jobs = m.get('TotalJobs')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        return self


class ListJobGroupsResponseBodyJobGroupsList(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        job_group_id: str = None,
        strategy: ListJobGroupsResponseBodyJobGroupsListStrategy = None,
        progress: ListJobGroupsResponseBodyJobGroupsListProgress = None,
        job_group_name: str = None,
        job_group_description: str = None,
        script_id: str = None,
        script_name: str = None,
    ):
        self.creation_time = creation_time
        self.job_group_id = job_group_id
        self.strategy = strategy
        self.progress = progress
        self.job_group_name = job_group_name
        self.job_group_description = job_group_description
        self.script_id = script_id
        self.script_name = script_name

    def validate(self):
        if self.strategy:
            self.strategy.validate()
        if self.progress:
            self.progress.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()
        if self.progress is not None:
            result['Progress'] = self.progress.to_map()
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('Strategy') is not None:
            temp_model = ListJobGroupsResponseBodyJobGroupsListStrategy()
            self.strategy = temp_model.from_map(m['Strategy'])
        if m.get('Progress') is not None:
            temp_model = ListJobGroupsResponseBodyJobGroupsListProgress()
            self.progress = temp_model.from_map(m['Progress'])
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        return self


class ListJobGroupsResponseBodyJobGroups(TeaModel):
    def __init__(
        self,
        list: List[ListJobGroupsResponseBodyJobGroupsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListJobGroupsResponseBodyJobGroupsList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobGroupsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        job_groups: ListJobGroupsResponseBodyJobGroups = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.job_groups = job_groups

    def validate(self):
        if self.job_groups:
            self.job_groups.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.job_groups is not None:
            result['JobGroups'] = self.job_groups.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('JobGroups') is not None:
            temp_model = ListJobGroupsResponseBodyJobGroups()
            self.job_groups = temp_model.from_map(m['JobGroups'])
        return self


class ListJobGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListJobGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListJobGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_id: List[str] = None,
    ):
        self.instance_id = instance_id
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class ListJobsResponseBodyJobsSummary(TeaModel):
    def __init__(
        self,
        summary_name: str = None,
        category: str = None,
        content: str = None,
    ):
        self.summary_name = summary_name
        self.category = category
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary_name is not None:
            result['SummaryName'] = self.summary_name
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ListJobsResponseBodyJobsContacts(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        state: str = None,
        contact_id: str = None,
        honorific: str = None,
        job_id: str = None,
        contact_name: str = None,
        role: str = None,
        reference_id: str = None,
    ):
        self.phone_number = phone_number
        self.state = state
        self.contact_id = contact_id
        self.honorific = honorific
        self.job_id = job_id
        self.contact_name = contact_name
        self.role = role
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.state is not None:
            result['State'] = self.state
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.honorific is not None:
            result['Honorific'] = self.honorific
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.role is not None:
            result['Role'] = self.role
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        return self


class ListJobsResponseBodyJobsExtras(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListJobsResponseBodyJobsTasksContact(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        state: str = None,
        contact_id: str = None,
        honorific: str = None,
        job_id: str = None,
        contact_name: str = None,
        role: str = None,
        reference_id: str = None,
    ):
        self.phone_number = phone_number
        self.state = state
        self.contact_id = contact_id
        self.honorific = honorific
        self.job_id = job_id
        self.contact_name = contact_name
        self.role = role
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.state is not None:
            result['State'] = self.state
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.honorific is not None:
            result['Honorific'] = self.honorific
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.role is not None:
            result['Role'] = self.role
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        return self


class ListJobsResponseBodyJobsTasksConversationSummary(TeaModel):
    def __init__(
        self,
        summary_name: str = None,
        category: str = None,
        content: str = None,
    ):
        self.summary_name = summary_name
        self.category = category
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary_name is not None:
            result['SummaryName'] = self.summary_name
        if self.category is not None:
            result['Category'] = self.category
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class ListJobsResponseBodyJobsTasksConversation(TeaModel):
    def __init__(
        self,
        summary: List[ListJobsResponseBodyJobsTasksConversationSummary] = None,
        speaker: str = None,
        timestamp: int = None,
        script: str = None,
    ):
        self.summary = summary
        self.speaker = speaker
        self.timestamp = timestamp
        self.script = script

    def validate(self):
        if self.summary:
            for k in self.summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Summary'] = []
        if self.summary is not None:
            for k in self.summary:
                result['Summary'].append(k.to_map() if k else None)
        if self.speaker is not None:
            result['Speaker'] = self.speaker
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        if self.script is not None:
            result['Script'] = self.script
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summary = []
        if m.get('Summary') is not None:
            for k in m.get('Summary'):
                temp_model = ListJobsResponseBodyJobsTasksConversationSummary()
                self.summary.append(temp_model.from_map(k))
        if m.get('Speaker') is not None:
            self.speaker = m.get('Speaker')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        if m.get('Script') is not None:
            self.script = m.get('Script')
        return self


class ListJobsResponseBodyJobsTasks(TeaModel):
    def __init__(
        self,
        status: str = None,
        planed_time: int = None,
        chatbot_id: str = None,
        actual_time: int = None,
        called_number: str = None,
        scenario_id: str = None,
        contact: ListJobsResponseBodyJobsTasksContact = None,
        job_id: str = None,
        call_id: str = None,
        calling_number: str = None,
        brief: str = None,
        duration: int = None,
        task_id: str = None,
        conversation: List[ListJobsResponseBodyJobsTasksConversation] = None,
    ):
        self.status = status
        self.planed_time = planed_time
        self.chatbot_id = chatbot_id
        self.actual_time = actual_time
        self.called_number = called_number
        self.scenario_id = scenario_id
        self.contact = contact
        self.job_id = job_id
        self.call_id = call_id
        self.calling_number = calling_number
        self.brief = brief
        self.duration = duration
        self.task_id = task_id
        self.conversation = conversation

    def validate(self):
        if self.contact:
            self.contact.validate()
        if self.conversation:
            for k in self.conversation:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.planed_time is not None:
            result['PlanedTime'] = self.planed_time
        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.contact is not None:
            result['Contact'] = self.contact.to_map()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.brief is not None:
            result['Brief'] = self.brief
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        result['Conversation'] = []
        if self.conversation is not None:
            for k in self.conversation:
                result['Conversation'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PlanedTime') is not None:
            self.planed_time = m.get('PlanedTime')
        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Contact') is not None:
            temp_model = ListJobsResponseBodyJobsTasksContact()
            self.contact = temp_model.from_map(m['Contact'])
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('Brief') is not None:
            self.brief = m.get('Brief')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        self.conversation = []
        if m.get('Conversation') is not None:
            for k in m.get('Conversation'):
                temp_model = ListJobsResponseBodyJobsTasksConversation()
                self.conversation.append(temp_model.from_map(k))
        return self


class ListJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        status: str = None,
        calling_numbers: List[str] = None,
        summary: List[ListJobsResponseBodyJobsSummary] = None,
        contacts: List[ListJobsResponseBodyJobsContacts] = None,
        priority: int = None,
        system_priority: int = None,
        failure_reason: str = None,
        extras: List[ListJobsResponseBodyJobsExtras] = None,
        reference_id: str = None,
        scenario_id: str = None,
        job_group_id: str = None,
        tasks: List[ListJobsResponseBodyJobsTasks] = None,
        strategy_id: str = None,
        job_id: str = None,
    ):
        self.status = status
        self.calling_numbers = calling_numbers
        self.summary = summary
        self.contacts = contacts
        self.priority = priority
        self.system_priority = system_priority
        self.failure_reason = failure_reason
        self.extras = extras
        self.reference_id = reference_id
        self.scenario_id = scenario_id
        self.job_group_id = job_group_id
        self.tasks = tasks
        self.strategy_id = strategy_id
        self.job_id = job_id

    def validate(self):
        if self.summary:
            for k in self.summary:
                if k:
                    k.validate()
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()
        if self.extras:
            for k in self.extras:
                if k:
                    k.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers
        result['Summary'] = []
        if self.summary is not None:
            for k in self.summary:
                result['Summary'].append(k.to_map() if k else None)
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.system_priority is not None:
            result['SystemPriority'] = self.system_priority
        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason
        result['Extras'] = []
        if self.extras is not None:
            for k in self.extras:
                result['Extras'].append(k.to_map() if k else None)
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')
        self.summary = []
        if m.get('Summary') is not None:
            for k in m.get('Summary'):
                temp_model = ListJobsResponseBodyJobsSummary()
                self.summary.append(temp_model.from_map(k))
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = ListJobsResponseBodyJobsContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SystemPriority') is not None:
            self.system_priority = m.get('SystemPriority')
        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')
        self.extras = []
        if m.get('Extras') is not None:
            for k in m.get('Extras'):
                temp_model = ListJobsResponseBodyJobsExtras()
                self.extras.append(temp_model.from_map(k))
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListJobsResponseBodyJobsTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        jobs: List[ListJobsResponseBodyJobs] = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.jobs = jobs
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['Jobs'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.jobs = []
        if m.get('Jobs') is not None:
            for k in m.get('Jobs'):
                temp_model = ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsByGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
        job_status: str = None,
        job_failure_reason: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.job_status = job_status
        self.job_failure_reason = job_failure_reason
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.job_status is not None:
            result['JobStatus'] = self.job_status
        if self.job_failure_reason is not None:
            result['JobFailureReason'] = self.job_failure_reason
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('JobStatus') is not None:
            self.job_status = m.get('JobStatus')
        if m.get('JobFailureReason') is not None:
            self.job_failure_reason = m.get('JobFailureReason')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListJobsByGroupResponseBodyJobsListSummary(TeaModel):
    def __init__(
        self,
        summary_name: str = None,
        job_group_id: str = None,
        job_id: str = None,
        category: str = None,
        task_id: str = None,
        content: str = None,
        conversation_detail_id: str = None,
        summary_id: str = None,
    ):
        self.summary_name = summary_name
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.category = category
        self.task_id = task_id
        self.content = content
        self.conversation_detail_id = conversation_detail_id
        self.summary_id = summary_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary_name is not None:
            result['SummaryName'] = self.summary_name
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.category is not None:
            result['Category'] = self.category
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.content is not None:
            result['Content'] = self.content
        if self.conversation_detail_id is not None:
            result['ConversationDetailId'] = self.conversation_detail_id
        if self.summary_id is not None:
            result['SummaryId'] = self.summary_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ConversationDetailId') is not None:
            self.conversation_detail_id = m.get('ConversationDetailId')
        if m.get('SummaryId') is not None:
            self.summary_id = m.get('SummaryId')
        return self


class ListJobsByGroupResponseBodyJobsListContacts(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        state: str = None,
        contact_id: str = None,
        honorific: str = None,
        job_id: str = None,
        contact_name: str = None,
        role: str = None,
        reference_id: str = None,
    ):
        self.phone_number = phone_number
        self.state = state
        self.contact_id = contact_id
        self.honorific = honorific
        self.job_id = job_id
        self.contact_name = contact_name
        self.role = role
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.state is not None:
            result['State'] = self.state
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.honorific is not None:
            result['Honorific'] = self.honorific
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.role is not None:
            result['Role'] = self.role
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        return self


class ListJobsByGroupResponseBodyJobsListExtras(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ListJobsByGroupResponseBodyJobsList(TeaModel):
    def __init__(
        self,
        status: str = None,
        calling_numbers: List[str] = None,
        summary: List[ListJobsByGroupResponseBodyJobsListSummary] = None,
        contacts: List[ListJobsByGroupResponseBodyJobsListContacts] = None,
        priority: int = None,
        system_priority: int = None,
        failure_reason: str = None,
        extras: List[ListJobsByGroupResponseBodyJobsListExtras] = None,
        reference_id: str = None,
        scenario_id: str = None,
        job_group_id: str = None,
        strategy_id: str = None,
        job_id: str = None,
    ):
        self.status = status
        self.calling_numbers = calling_numbers
        self.summary = summary
        self.contacts = contacts
        self.priority = priority
        self.system_priority = system_priority
        self.failure_reason = failure_reason
        self.extras = extras
        self.reference_id = reference_id
        self.scenario_id = scenario_id
        self.job_group_id = job_group_id
        self.strategy_id = strategy_id
        self.job_id = job_id

    def validate(self):
        if self.summary:
            for k in self.summary:
                if k:
                    k.validate()
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()
        if self.extras:
            for k in self.extras:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers
        result['Summary'] = []
        if self.summary is not None:
            for k in self.summary:
                result['Summary'].append(k.to_map() if k else None)
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.system_priority is not None:
            result['SystemPriority'] = self.system_priority
        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason
        result['Extras'] = []
        if self.extras is not None:
            for k in self.extras:
                result['Extras'].append(k.to_map() if k else None)
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')
        self.summary = []
        if m.get('Summary') is not None:
            for k in m.get('Summary'):
                temp_model = ListJobsByGroupResponseBodyJobsListSummary()
                self.summary.append(temp_model.from_map(k))
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = ListJobsByGroupResponseBodyJobsListContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('SystemPriority') is not None:
            self.system_priority = m.get('SystemPriority')
        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')
        self.extras = []
        if m.get('Extras') is not None:
            for k in m.get('Extras'):
                temp_model = ListJobsByGroupResponseBodyJobsListExtras()
                self.extras.append(temp_model.from_map(k))
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class ListJobsByGroupResponseBodyJobs(TeaModel):
    def __init__(
        self,
        list: List[ListJobsByGroupResponseBodyJobsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListJobsByGroupResponseBodyJobsList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListJobsByGroupResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        jobs: ListJobsByGroupResponseBodyJobs = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.jobs = jobs
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.jobs:
            self.jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.jobs is not None:
            result['Jobs'] = self.jobs.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Jobs') is not None:
            temp_model = ListJobsByGroupResponseBodyJobs()
            self.jobs = temp_model.from_map(m['Jobs'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListJobsByGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListJobsByGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListJobsByGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMediaRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        name_prefix: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.name_prefix = name_prefix
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name_prefix is not None:
            result['NamePrefix'] = self.name_prefix
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamePrefix') is not None:
            self.name_prefix = m.get('NamePrefix')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListMediaResponseBodyMediaList(TeaModel):
    def __init__(
        self,
        name: str = None,
        media_id: str = None,
    ):
        self.name = name
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class ListMediaResponseBody(TeaModel):
    def __init__(
        self,
        media_list: List[ListMediaResponseBodyMediaList] = None,
        total_count: int = None,
        request_id: str = None,
        message: str = None,
        page_size: int = None,
        page_number: int = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.media_list = media_list
        self.total_count = total_count
        self.request_id = request_id
        self.message = message
        self.page_size = page_size
        self.page_number = page_number
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.media_list:
            for k in self.media_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['MediaList'] = []
        if self.media_list is not None:
            for k in self.media_list:
                result['MediaList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.media_list = []
        if m.get('MediaList') is not None:
            for k in m.get('MediaList'):
                temp_model = ListMediaResponseBodyMediaList()
                self.media_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListMediaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListMediaResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListMediaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOutboundCallNumbersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListOutboundCallNumbersResponseBodyOutboundCallNumbersList(TeaModel):
    def __init__(
        self,
        rate_limit_count: str = None,
        number: str = None,
        outbound_call_number_id: str = None,
        rate_limit_period: str = None,
    ):
        self.rate_limit_count = rate_limit_count
        self.number = number
        self.outbound_call_number_id = outbound_call_number_id
        self.rate_limit_period = rate_limit_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate_limit_count is not None:
            result['RateLimitCount'] = self.rate_limit_count
        if self.number is not None:
            result['Number'] = self.number
        if self.outbound_call_number_id is not None:
            result['OutboundCallNumberId'] = self.outbound_call_number_id
        if self.rate_limit_period is not None:
            result['RateLimitPeriod'] = self.rate_limit_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RateLimitCount') is not None:
            self.rate_limit_count = m.get('RateLimitCount')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OutboundCallNumberId') is not None:
            self.outbound_call_number_id = m.get('OutboundCallNumberId')
        if m.get('RateLimitPeriod') is not None:
            self.rate_limit_period = m.get('RateLimitPeriod')
        return self


class ListOutboundCallNumbersResponseBodyOutboundCallNumbers(TeaModel):
    def __init__(
        self,
        list: List[ListOutboundCallNumbersResponseBodyOutboundCallNumbersList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListOutboundCallNumbersResponseBodyOutboundCallNumbersList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOutboundCallNumbersResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        outbound_call_numbers: ListOutboundCallNumbersResponseBodyOutboundCallNumbers = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.outbound_call_numbers = outbound_call_numbers
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.outbound_call_numbers:
            self.outbound_call_numbers.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.outbound_call_numbers is not None:
            result['OutboundCallNumbers'] = self.outbound_call_numbers.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('OutboundCallNumbers') is not None:
            temp_model = ListOutboundCallNumbersResponseBodyOutboundCallNumbers()
            self.outbound_call_numbers = temp_model.from_map(m['OutboundCallNumbers'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListOutboundCallNumbersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOutboundCallNumbersResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOutboundCallNumbersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSchedulerInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_owner_id: int = None,
    ):
        self.instance_owner_id = instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        return self


class ListSchedulerInstancesResponseBodySchedulerInstances(TeaModel):
    def __init__(
        self,
        business: str = None,
        max_concurrency: int = None,
        instance_id: str = None,
        owner_id: str = None,
    ):
        self.business = business
        self.max_concurrency = max_concurrency
        self.instance_id = instance_id
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business is not None:
            result['Business'] = self.business
        if self.max_concurrency is not None:
            result['MaxConcurrency'] = self.max_concurrency
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')
        if m.get('MaxConcurrency') is not None:
            self.max_concurrency = m.get('MaxConcurrency')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')
        return self


class ListSchedulerInstancesResponseBody(TeaModel):
    def __init__(
        self,
        scheduler_instances: List[ListSchedulerInstancesResponseBodySchedulerInstances] = None,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.scheduler_instances = scheduler_instances
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.scheduler_instances:
            for k in self.scheduler_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['SchedulerInstances'] = []
        if self.scheduler_instances is not None:
            for k in self.scheduler_instances:
                result['SchedulerInstances'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scheduler_instances = []
        if m.get('SchedulerInstances') is not None:
            for k in m.get('SchedulerInstances'):
                temp_model = ListSchedulerInstancesResponseBodySchedulerInstances()
                self.scheduler_instances.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListSchedulerInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSchedulerInstancesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSchedulerInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScriptPublishHistoriesRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListScriptPublishHistoriesResponseBodyScriptPublishHistoriesList(TeaModel):
    def __init__(
        self,
        publish_time: int = None,
        description: str = None,
        instance_id: str = None,
        script_id: str = None,
        script_version: str = None,
    ):
        self.publish_time = publish_time
        self.description = description
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_version = script_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_version is not None:
            result['ScriptVersion'] = self.script_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptVersion') is not None:
            self.script_version = m.get('ScriptVersion')
        return self


class ListScriptPublishHistoriesResponseBodyScriptPublishHistories(TeaModel):
    def __init__(
        self,
        list: List[ListScriptPublishHistoriesResponseBodyScriptPublishHistoriesList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListScriptPublishHistoriesResponseBodyScriptPublishHistoriesList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScriptPublishHistoriesResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        script_publish_histories: ListScriptPublishHistoriesResponseBodyScriptPublishHistories = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.script_publish_histories = script_publish_histories
        self.code = code
        self.success = success

    def validate(self):
        if self.script_publish_histories:
            self.script_publish_histories.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.script_publish_histories is not None:
            result['ScriptPublishHistories'] = self.script_publish_histories.to_map()
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('ScriptPublishHistories') is not None:
            temp_model = ListScriptPublishHistoriesResponseBodyScriptPublishHistories()
            self.script_publish_histories = temp_model.from_map(m['ScriptPublishHistories'])
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListScriptPublishHistoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListScriptPublishHistoriesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListScriptPublishHistoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScriptsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListScriptsResponseBodyScriptsList(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: int = None,
        script_id: str = None,
        is_debug_drafted: bool = None,
        industry: str = None,
        script_description: str = None,
        is_drafted: bool = None,
        debug_status: str = None,
        reject_reason: str = None,
        script_name: str = None,
        scene: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.script_id = script_id
        self.is_debug_drafted = is_debug_drafted
        self.industry = industry
        self.script_description = script_description
        self.is_drafted = is_drafted
        self.debug_status = debug_status
        self.reject_reason = reject_reason
        self.script_name = script_name
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.is_debug_drafted is not None:
            result['IsDebugDrafted'] = self.is_debug_drafted
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description
        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted
        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status
        if self.reject_reason is not None:
            result['RejectReason'] = self.reject_reason
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IsDebugDrafted') is not None:
            self.is_debug_drafted = m.get('IsDebugDrafted')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')
        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')
        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')
        if m.get('RejectReason') is not None:
            self.reject_reason = m.get('RejectReason')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class ListScriptsResponseBodyScripts(TeaModel):
    def __init__(
        self,
        list: List[ListScriptsResponseBodyScriptsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListScriptsResponseBodyScriptsList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScriptsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        scripts: ListScriptsResponseBodyScripts = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.scripts = scripts
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.scripts:
            self.scripts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scripts is not None:
            result['Scripts'] = self.scripts.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scripts') is not None:
            temp_model = ListScriptsResponseBodyScripts()
            self.scripts = temp_model.from_map(m['Scripts'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListScriptsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListScriptsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListScriptsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScriptVoiceConfigsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListScriptVoiceConfigsResponseBodyScriptVoiceConfigsList(TeaModel):
    def __init__(
        self,
        type: str = None,
        script_voice_config_id: str = None,
        script_content: str = None,
        instance_id: str = None,
        script_id: str = None,
        script_waveform_relation: str = None,
        source: str = None,
    ):
        self.type = type
        self.script_voice_config_id = script_voice_config_id
        self.script_content = script_content
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_waveform_relation = script_waveform_relation
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.script_voice_config_id is not None:
            result['ScriptVoiceConfigId'] = self.script_voice_config_id
        if self.script_content is not None:
            result['ScriptContent'] = self.script_content
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_waveform_relation is not None:
            result['ScriptWaveformRelation'] = self.script_waveform_relation
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ScriptVoiceConfigId') is not None:
            self.script_voice_config_id = m.get('ScriptVoiceConfigId')
        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptWaveformRelation') is not None:
            self.script_waveform_relation = m.get('ScriptWaveformRelation')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListScriptVoiceConfigsResponseBodyScriptVoiceConfigs(TeaModel):
    def __init__(
        self,
        list: List[ListScriptVoiceConfigsResponseBodyScriptVoiceConfigsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListScriptVoiceConfigsResponseBodyScriptVoiceConfigsList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScriptVoiceConfigsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        script_voice_configs: ListScriptVoiceConfigsResponseBodyScriptVoiceConfigs = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.script_voice_configs = script_voice_configs

    def validate(self):
        if self.script_voice_configs:
            self.script_voice_configs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.script_voice_configs is not None:
            result['ScriptVoiceConfigs'] = self.script_voice_configs.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ScriptVoiceConfigs') is not None:
            temp_model = ListScriptVoiceConfigsResponseBodyScriptVoiceConfigs()
            self.script_voice_configs = temp_model.from_map(m['ScriptVoiceConfigs'])
        return self


class ListScriptVoiceConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListScriptVoiceConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListScriptVoiceConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class ListTagsResponseBodyTagGroups(TeaModel):
    def __init__(
        self,
        tag_group: str = None,
        tag_group_id: str = None,
        tag_group_index: int = None,
        script_id: str = None,
    ):
        self.tag_group = tag_group
        self.tag_group_id = tag_group_id
        self.tag_group_index = tag_group_index
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group
        if self.tag_group_id is not None:
            result['TagGroupId'] = self.tag_group_id
        if self.tag_group_index is not None:
            result['TagGroupIndex'] = self.tag_group_index
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')
        if m.get('TagGroupId') is not None:
            self.tag_group_id = m.get('TagGroupId')
        if m.get('TagGroupIndex') is not None:
            self.tag_group_index = m.get('TagGroupIndex')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class ListTagsResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_group: str = None,
        tag_name: str = None,
        tag_index: int = None,
        script_id: str = None,
        tag_id: str = None,
    ):
        self.tag_group = tag_group
        self.tag_name = tag_name
        self.tag_index = tag_index
        self.script_id = script_id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_index is not None:
            result['TagIndex'] = self.tag_index
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagIndex') is not None:
            self.tag_index = m.get('TagIndex')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        tag_groups: List[ListTagsResponseBodyTagGroups] = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        tags: List[ListTagsResponseBodyTags] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.tag_groups = tag_groups
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.tags = tags

    def validate(self):
        if self.tag_groups:
            for k in self.tag_groups:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagGroups'] = []
        if self.tag_groups is not None:
            for k in self.tag_groups:
                result['TagGroups'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_groups = []
        if m.get('TagGroups') is not None:
            for k in m.get('TagGroups'):
                temp_model = ListTagsResponseBodyTagGroups()
                self.tag_groups.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListTagsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTagsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyBatchJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
        batch_job_name: str = None,
        description: str = None,
        scenario_id: str = None,
        strategy_json: str = None,
        job_file_path: str = None,
        submitted: bool = None,
        script_id: str = None,
        calling_number: List[str] = None,
    ):
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.batch_job_name = batch_job_name
        self.description = description
        self.scenario_id = scenario_id
        self.strategy_json = strategy_json
        self.job_file_path = job_file_path
        self.submitted = submitted
        self.script_id = script_id
        self.calling_number = calling_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.batch_job_name is not None:
            result['BatchJobName'] = self.batch_job_name
        if self.description is not None:
            result['Description'] = self.description
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.strategy_json is not None:
            result['StrategyJson'] = self.strategy_json
        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path
        if self.submitted is not None:
            result['Submitted'] = self.submitted
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('BatchJobName') is not None:
            self.batch_job_name = m.get('BatchJobName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('StrategyJson') is not None:
            self.strategy_json = m.get('StrategyJson')
        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')
        if m.get('Submitted') is not None:
            self.submitted = m.get('Submitted')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        return self


class ModifyBatchJobsResponseBodyJobGroupStrategyWorkingTime(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        begin_time: str = None,
    ):
        self.end_time = end_time
        self.begin_time = begin_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        return self


class ModifyBatchJobsResponseBodyJobGroupStrategy(TeaModel):
    def __init__(
        self,
        type: str = None,
        strategy_name: str = None,
        max_attempts_per_day: int = None,
        working_time: List[ModifyBatchJobsResponseBodyJobGroupStrategyWorkingTime] = None,
        follow_up_strategy: str = None,
        end_time: int = None,
        start_time: int = None,
        is_template: bool = None,
        customized: str = None,
        strategy_id: str = None,
        repeat_days: List[str] = None,
        routing_strategy: str = None,
        min_attempt_interval: int = None,
        strategy_description: str = None,
        repeat_by: str = None,
    ):
        self.type = type
        self.strategy_name = strategy_name
        self.max_attempts_per_day = max_attempts_per_day
        self.working_time = working_time
        self.follow_up_strategy = follow_up_strategy
        self.end_time = end_time
        self.start_time = start_time
        self.is_template = is_template
        self.customized = customized
        self.strategy_id = strategy_id
        self.repeat_days = repeat_days
        self.routing_strategy = routing_strategy
        self.min_attempt_interval = min_attempt_interval
        self.strategy_description = strategy_description
        self.repeat_by = repeat_by

    def validate(self):
        if self.working_time:
            for k in self.working_time:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.max_attempts_per_day is not None:
            result['MaxAttemptsPerDay'] = self.max_attempts_per_day
        result['WorkingTime'] = []
        if self.working_time is not None:
            for k in self.working_time:
                result['WorkingTime'].append(k.to_map() if k else None)
        if self.follow_up_strategy is not None:
            result['FollowUpStrategy'] = self.follow_up_strategy
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.customized is not None:
            result['Customized'] = self.customized
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.routing_strategy is not None:
            result['RoutingStrategy'] = self.routing_strategy
        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval
        if self.strategy_description is not None:
            result['StrategyDescription'] = self.strategy_description
        if self.repeat_by is not None:
            result['RepeatBy'] = self.repeat_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('MaxAttemptsPerDay') is not None:
            self.max_attempts_per_day = m.get('MaxAttemptsPerDay')
        self.working_time = []
        if m.get('WorkingTime') is not None:
            for k in m.get('WorkingTime'):
                temp_model = ModifyBatchJobsResponseBodyJobGroupStrategyWorkingTime()
                self.working_time.append(temp_model.from_map(k))
        if m.get('FollowUpStrategy') is not None:
            self.follow_up_strategy = m.get('FollowUpStrategy')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('Customized') is not None:
            self.customized = m.get('Customized')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RoutingStrategy') is not None:
            self.routing_strategy = m.get('RoutingStrategy')
        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')
        if m.get('StrategyDescription') is not None:
            self.strategy_description = m.get('StrategyDescription')
        if m.get('RepeatBy') is not None:
            self.repeat_by = m.get('RepeatBy')
        return self


class ModifyBatchJobsResponseBodyJobGroup(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        job_group_id: str = None,
        scenario_id: str = None,
        strategy: ModifyBatchJobsResponseBodyJobGroupStrategy = None,
        calling_numbers: List[str] = None,
        job_group_name: str = None,
        job_file_path: str = None,
        job_group_description: str = None,
    ):
        self.creation_time = creation_time
        self.job_group_id = job_group_id
        self.scenario_id = scenario_id
        self.strategy = strategy
        self.calling_numbers = calling_numbers
        self.job_group_name = job_group_name
        self.job_file_path = job_file_path
        self.job_group_description = job_group_description

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path
        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Strategy') is not None:
            temp_model = ModifyBatchJobsResponseBodyJobGroupStrategy()
            self.strategy = temp_model.from_map(m['Strategy'])
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')
        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')
        return self


class ModifyBatchJobsResponseBody(TeaModel):
    def __init__(
        self,
        job_group: ModifyBatchJobsResponseBodyJobGroup = None,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.job_group = job_group
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.job_group:
            self.job_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_group is not None:
            result['JobGroup'] = self.job_group.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroup') is not None:
            temp_model = ModifyBatchJobsResponseBodyJobGroup()
            self.job_group = temp_model.from_map(m['JobGroup'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyBatchJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyBatchJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyBatchJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyDialogueFlowRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        dialogue_flow_id: str = None,
        dialogue_flow_definition: str = None,
        is_drafted: bool = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.dialogue_flow_id = dialogue_flow_id
        self.dialogue_flow_definition = dialogue_flow_definition
        self.is_drafted = is_drafted

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.dialogue_flow_id is not None:
            result['DialogueFlowId'] = self.dialogue_flow_id
        if self.dialogue_flow_definition is not None:
            result['DialogueFlowDefinition'] = self.dialogue_flow_definition
        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('DialogueFlowId') is not None:
            self.dialogue_flow_id = m.get('DialogueFlowId')
        if m.get('DialogueFlowDefinition') is not None:
            self.dialogue_flow_definition = m.get('DialogueFlowDefinition')
        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')
        return self


class ModifyDialogueFlowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        dialogue_flow_id: str = None,
        code: str = None,
        dialogue_flow_definition: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.dialogue_flow_id = dialogue_flow_id
        self.code = code
        self.dialogue_flow_definition = dialogue_flow_definition
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.dialogue_flow_id is not None:
            result['DialogueFlowId'] = self.dialogue_flow_id
        if self.code is not None:
            result['Code'] = self.code
        if self.dialogue_flow_definition is not None:
            result['DialogueFlowDefinition'] = self.dialogue_flow_definition
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('DialogueFlowId') is not None:
            self.dialogue_flow_id = m.get('DialogueFlowId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DialogueFlowDefinition') is not None:
            self.dialogue_flow_definition = m.get('DialogueFlowDefinition')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyDialogueFlowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyDialogueFlowResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyDialogueFlowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyGlobalQuestionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        global_question_id: str = None,
        global_question_name: str = None,
        global_question_type: str = None,
        questions: str = None,
        answers: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.global_question_id = global_question_id
        self.global_question_name = global_question_name
        self.global_question_type = global_question_type
        self.questions = questions
        self.answers = answers

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.global_question_id is not None:
            result['GlobalQuestionId'] = self.global_question_id
        if self.global_question_name is not None:
            result['GlobalQuestionName'] = self.global_question_name
        if self.global_question_type is not None:
            result['GlobalQuestionType'] = self.global_question_type
        if self.questions is not None:
            result['Questions'] = self.questions
        if self.answers is not None:
            result['Answers'] = self.answers
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('GlobalQuestionId') is not None:
            self.global_question_id = m.get('GlobalQuestionId')
        if m.get('GlobalQuestionName') is not None:
            self.global_question_name = m.get('GlobalQuestionName')
        if m.get('GlobalQuestionType') is not None:
            self.global_question_type = m.get('GlobalQuestionType')
        if m.get('Questions') is not None:
            self.questions = m.get('Questions')
        if m.get('Answers') is not None:
            self.answers = m.get('Answers')
        return self


class ModifyGlobalQuestionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        dialogue_question_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.dialogue_question_id = dialogue_question_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.dialogue_question_id is not None:
            result['DialogueQuestionId'] = self.dialogue_question_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('DialogueQuestionId') is not None:
            self.dialogue_question_id = m.get('DialogueQuestionId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyGlobalQuestionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyGlobalQuestionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyGlobalQuestionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_description: str = None,
        max_concurrent_conversation: int = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_description = instance_description
        self.max_concurrent_conversation = max_concurrent_conversation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')
        return self


class ModifyInstanceResponseBodyInstance(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        instance_name: str = None,
        max_concurrent_conversation: int = None,
        instance_id: str = None,
        instance_description: str = None,
    ):
        self.creation_time = creation_time
        self.instance_name = instance_name
        self.max_concurrent_conversation = max_concurrent_conversation
        self.instance_id = instance_id
        self.instance_description = instance_description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.max_concurrent_conversation is not None:
            result['MaxConcurrentConversation'] = self.max_concurrent_conversation
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('MaxConcurrentConversation') is not None:
            self.max_concurrent_conversation = m.get('MaxConcurrentConversation')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')
        return self


class ModifyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        instance: ModifyInstanceResponseBodyInstance = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.instance = instance
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.instance is not None:
            result['Instance'] = self.instance.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Instance') is not None:
            temp_model = ModifyInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m['Instance'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyInstanceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyIntentRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        intent_id: str = None,
        intent_name: str = None,
        intent_description: str = None,
        utterances: str = None,
        keywords: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.intent_id = intent_id
        self.intent_name = intent_name
        self.intent_description = intent_description
        self.utterances = utterances
        self.keywords = keywords

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        if self.intent_name is not None:
            result['IntentName'] = self.intent_name
        if self.intent_description is not None:
            result['IntentDescription'] = self.intent_description
        if self.utterances is not None:
            result['Utterances'] = self.utterances
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        if m.get('IntentName') is not None:
            self.intent_name = m.get('IntentName')
        if m.get('IntentDescription') is not None:
            self.intent_description = m.get('IntentDescription')
        if m.get('Utterances') is not None:
            self.utterances = m.get('Utterances')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        return self


class ModifyIntentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        intent_id: str = None,
    ):
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.intent_id = intent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.intent_id is not None:
            result['IntentId'] = self.intent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('IntentId') is not None:
            self.intent_id = m.get('IntentId')
        return self


class ModifyIntentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyIntentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyIntentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyJobGroupRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
        name: str = None,
        scenario_id: str = None,
        description: str = None,
        strategy_json: str = None,
        script_id: str = None,
        calling_number: List[str] = None,
    ):
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.name = name
        self.scenario_id = scenario_id
        self.description = description
        self.strategy_json = strategy_json
        self.script_id = script_id
        self.calling_number = calling_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.description is not None:
            result['Description'] = self.description
        if self.strategy_json is not None:
            result['StrategyJson'] = self.strategy_json
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('StrategyJson') is not None:
            self.strategy_json = m.get('StrategyJson')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        return self


class ModifyJobGroupResponseBodyJobGroupStrategyWorkingTime(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        begin_time: str = None,
    ):
        self.end_time = end_time
        self.begin_time = begin_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')
        return self


class ModifyJobGroupResponseBodyJobGroupStrategy(TeaModel):
    def __init__(
        self,
        type: str = None,
        strategy_name: str = None,
        max_attempts_per_day: int = None,
        working_time: List[ModifyJobGroupResponseBodyJobGroupStrategyWorkingTime] = None,
        follow_up_strategy: str = None,
        end_time: int = None,
        start_time: int = None,
        is_template: bool = None,
        customized: str = None,
        strategy_id: str = None,
        repeat_days: List[str] = None,
        routing_strategy: str = None,
        min_attempt_interval: int = None,
        strategy_description: str = None,
        repeat_by: str = None,
    ):
        self.type = type
        self.strategy_name = strategy_name
        self.max_attempts_per_day = max_attempts_per_day
        self.working_time = working_time
        self.follow_up_strategy = follow_up_strategy
        self.end_time = end_time
        self.start_time = start_time
        self.is_template = is_template
        self.customized = customized
        self.strategy_id = strategy_id
        self.repeat_days = repeat_days
        self.routing_strategy = routing_strategy
        self.min_attempt_interval = min_attempt_interval
        self.strategy_description = strategy_description
        self.repeat_by = repeat_by

    def validate(self):
        if self.working_time:
            for k in self.working_time:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.strategy_name is not None:
            result['StrategyName'] = self.strategy_name
        if self.max_attempts_per_day is not None:
            result['MaxAttemptsPerDay'] = self.max_attempts_per_day
        result['WorkingTime'] = []
        if self.working_time is not None:
            for k in self.working_time:
                result['WorkingTime'].append(k.to_map() if k else None)
        if self.follow_up_strategy is not None:
            result['FollowUpStrategy'] = self.follow_up_strategy
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.is_template is not None:
            result['IsTemplate'] = self.is_template
        if self.customized is not None:
            result['Customized'] = self.customized
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.repeat_days is not None:
            result['RepeatDays'] = self.repeat_days
        if self.routing_strategy is not None:
            result['RoutingStrategy'] = self.routing_strategy
        if self.min_attempt_interval is not None:
            result['MinAttemptInterval'] = self.min_attempt_interval
        if self.strategy_description is not None:
            result['StrategyDescription'] = self.strategy_description
        if self.repeat_by is not None:
            result['RepeatBy'] = self.repeat_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('StrategyName') is not None:
            self.strategy_name = m.get('StrategyName')
        if m.get('MaxAttemptsPerDay') is not None:
            self.max_attempts_per_day = m.get('MaxAttemptsPerDay')
        self.working_time = []
        if m.get('WorkingTime') is not None:
            for k in m.get('WorkingTime'):
                temp_model = ModifyJobGroupResponseBodyJobGroupStrategyWorkingTime()
                self.working_time.append(temp_model.from_map(k))
        if m.get('FollowUpStrategy') is not None:
            self.follow_up_strategy = m.get('FollowUpStrategy')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('IsTemplate') is not None:
            self.is_template = m.get('IsTemplate')
        if m.get('Customized') is not None:
            self.customized = m.get('Customized')
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('RepeatDays') is not None:
            self.repeat_days = m.get('RepeatDays')
        if m.get('RoutingStrategy') is not None:
            self.routing_strategy = m.get('RoutingStrategy')
        if m.get('MinAttemptInterval') is not None:
            self.min_attempt_interval = m.get('MinAttemptInterval')
        if m.get('StrategyDescription') is not None:
            self.strategy_description = m.get('StrategyDescription')
        if m.get('RepeatBy') is not None:
            self.repeat_by = m.get('RepeatBy')
        return self


class ModifyJobGroupResponseBodyJobGroup(TeaModel):
    def __init__(
        self,
        creation_time: int = None,
        job_group_id: str = None,
        scenario_id: str = None,
        strategy: ModifyJobGroupResponseBodyJobGroupStrategy = None,
        calling_numbers: List[str] = None,
        job_group_name: str = None,
        job_file_path: str = None,
        job_group_description: str = None,
    ):
        self.creation_time = creation_time
        self.job_group_id = job_group_id
        self.scenario_id = scenario_id
        self.strategy = strategy
        self.calling_numbers = calling_numbers
        self.job_group_name = job_group_name
        self.job_file_path = job_file_path
        self.job_group_description = job_group_description

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers
        if self.job_group_name is not None:
            result['JobGroupName'] = self.job_group_name
        if self.job_file_path is not None:
            result['JobFilePath'] = self.job_file_path
        if self.job_group_description is not None:
            result['JobGroupDescription'] = self.job_group_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Strategy') is not None:
            temp_model = ModifyJobGroupResponseBodyJobGroupStrategy()
            self.strategy = temp_model.from_map(m['Strategy'])
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')
        if m.get('JobGroupName') is not None:
            self.job_group_name = m.get('JobGroupName')
        if m.get('JobFilePath') is not None:
            self.job_file_path = m.get('JobFilePath')
        if m.get('JobGroupDescription') is not None:
            self.job_group_description = m.get('JobGroupDescription')
        return self


class ModifyJobGroupResponseBody(TeaModel):
    def __init__(
        self,
        job_group: ModifyJobGroupResponseBodyJobGroup = None,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.job_group = job_group
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.job_group:
            self.job_group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_group is not None:
            result['JobGroup'] = self.job_group.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobGroup') is not None:
            temp_model = ModifyJobGroupResponseBodyJobGroup()
            self.job_group = temp_model.from_map(m['JobGroup'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyJobGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyJobGroupResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyJobGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyOutboundCallNumberRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        number: str = None,
        rate_limit_period: int = None,
        rate_limit_count: int = None,
        outbound_call_number_id: str = None,
    ):
        self.instance_id = instance_id
        self.number = number
        self.rate_limit_period = rate_limit_period
        self.rate_limit_count = rate_limit_count
        self.outbound_call_number_id = outbound_call_number_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.number is not None:
            result['Number'] = self.number
        if self.rate_limit_period is not None:
            result['RateLimitPeriod'] = self.rate_limit_period
        if self.rate_limit_count is not None:
            result['RateLimitCount'] = self.rate_limit_count
        if self.outbound_call_number_id is not None:
            result['OutboundCallNumberId'] = self.outbound_call_number_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('RateLimitPeriod') is not None:
            self.rate_limit_period = m.get('RateLimitPeriod')
        if m.get('RateLimitCount') is not None:
            self.rate_limit_count = m.get('RateLimitCount')
        if m.get('OutboundCallNumberId') is not None:
            self.outbound_call_number_id = m.get('OutboundCallNumberId')
        return self


class ModifyOutboundCallNumberResponseBodyOutboundCallNumber(TeaModel):
    def __init__(
        self,
        rate_limit_count: str = None,
        number: str = None,
        outbound_call_number_id: str = None,
        rate_limit_period: str = None,
    ):
        self.rate_limit_count = rate_limit_count
        self.number = number
        self.outbound_call_number_id = outbound_call_number_id
        self.rate_limit_period = rate_limit_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rate_limit_count is not None:
            result['RateLimitCount'] = self.rate_limit_count
        if self.number is not None:
            result['Number'] = self.number
        if self.outbound_call_number_id is not None:
            result['OutboundCallNumberId'] = self.outbound_call_number_id
        if self.rate_limit_period is not None:
            result['RateLimitPeriod'] = self.rate_limit_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RateLimitCount') is not None:
            self.rate_limit_count = m.get('RateLimitCount')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('OutboundCallNumberId') is not None:
            self.outbound_call_number_id = m.get('OutboundCallNumberId')
        if m.get('RateLimitPeriod') is not None:
            self.rate_limit_period = m.get('RateLimitPeriod')
        return self


class ModifyOutboundCallNumberResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        outbound_call_number: ModifyOutboundCallNumberResponseBodyOutboundCallNumber = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.outbound_call_number = outbound_call_number
        self.success = success

    def validate(self):
        if self.outbound_call_number:
            self.outbound_call_number.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.outbound_call_number is not None:
            result['OutboundCallNumber'] = self.outbound_call_number.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('OutboundCallNumber') is not None:
            temp_model = ModifyOutboundCallNumberResponseBodyOutboundCallNumber()
            self.outbound_call_number = temp_model.from_map(m['OutboundCallNumber'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyOutboundCallNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyOutboundCallNumberResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyOutboundCallNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScriptRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        script_name: str = None,
        script_description: str = None,
        industry: str = None,
        scene: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_name = script_name
        self.script_description = script_description
        self.industry = industry
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class ModifyScriptResponseBodyScript(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: int = None,
        industry: str = None,
        script_description: str = None,
        is_drafted: bool = None,
        debug_status: str = None,
        script_id: str = None,
        is_debug_drafted: bool = None,
        script_name: str = None,
        scene: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.industry = industry
        self.script_description = script_description
        self.is_drafted = is_drafted
        self.debug_status = debug_status
        self.script_id = script_id
        self.is_debug_drafted = is_debug_drafted
        self.script_name = script_name
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description
        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted
        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.is_debug_drafted is not None:
            result['IsDebugDrafted'] = self.is_debug_drafted
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')
        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')
        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IsDebugDrafted') is not None:
            self.is_debug_drafted = m.get('IsDebugDrafted')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class ModifyScriptResponseBody(TeaModel):
    def __init__(
        self,
        script: ModifyScriptResponseBodyScript = None,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.script = script
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.script:
            self.script.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script is not None:
            result['Script'] = self.script.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Script') is not None:
            temp_model = ModifyScriptResponseBodyScript()
            self.script = temp_model.from_map(m['Script'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyScriptVoiceConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        script_voice_config_id: str = None,
        type: str = None,
        script_waveform_relation: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_voice_config_id = script_voice_config_id
        self.type = type
        self.script_waveform_relation = script_waveform_relation

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_voice_config_id is not None:
            result['ScriptVoiceConfigId'] = self.script_voice_config_id
        if self.type is not None:
            result['Type'] = self.type
        if self.script_waveform_relation is not None:
            result['ScriptWaveformRelation'] = self.script_waveform_relation
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptVoiceConfigId') is not None:
            self.script_voice_config_id = m.get('ScriptVoiceConfigId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ScriptWaveformRelation') is not None:
            self.script_waveform_relation = m.get('ScriptWaveformRelation')
        return self


class ModifyScriptVoiceConfigResponseBodyScriptVoiceConfig(TeaModel):
    def __init__(
        self,
        type: str = None,
        script_voice_config_id: str = None,
        script_content: str = None,
        instance_id: str = None,
        script_id: str = None,
        script_waveform_relation: str = None,
        source: str = None,
    ):
        self.type = type
        self.script_voice_config_id = script_voice_config_id
        self.script_content = script_content
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_waveform_relation = script_waveform_relation
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.script_voice_config_id is not None:
            result['ScriptVoiceConfigId'] = self.script_voice_config_id
        if self.script_content is not None:
            result['ScriptContent'] = self.script_content
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_waveform_relation is not None:
            result['ScriptWaveformRelation'] = self.script_waveform_relation
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('ScriptVoiceConfigId') is not None:
            self.script_voice_config_id = m.get('ScriptVoiceConfigId')
        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptWaveformRelation') is not None:
            self.script_waveform_relation = m.get('ScriptWaveformRelation')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ModifyScriptVoiceConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        script_voice_config: ModifyScriptVoiceConfigResponseBodyScriptVoiceConfig = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.script_voice_config = script_voice_config

    def validate(self):
        if self.script_voice_config:
            self.script_voice_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        if self.script_voice_config is not None:
            result['ScriptVoiceConfig'] = self.script_voice_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('ScriptVoiceConfig') is not None:
            temp_model = ModifyScriptVoiceConfigResponseBodyScriptVoiceConfig()
            self.script_voice_config = temp_model.from_map(m['ScriptVoiceConfig'])
        return self


class ModifyScriptVoiceConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyScriptVoiceConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyScriptVoiceConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTagGroupsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        tags: str = None,
        tag_groups: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.tags = tags
        self.tag_groups = tag_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.tag_groups is not None:
            result['TagGroups'] = self.tag_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('TagGroups') is not None:
            self.tag_groups = m.get('TagGroups')
        return self


class ModifyTagGroupsResponseBodyTagGroups(TeaModel):
    def __init__(
        self,
        tag_group: str = None,
        tag_group_id: str = None,
        tag_group_index: int = None,
        script_id: str = None,
    ):
        self.tag_group = tag_group
        self.tag_group_id = tag_group_id
        self.tag_group_index = tag_group_index
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group
        if self.tag_group_id is not None:
            result['TagGroupId'] = self.tag_group_id
        if self.tag_group_index is not None:
            result['TagGroupIndex'] = self.tag_group_index
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')
        if m.get('TagGroupId') is not None:
            self.tag_group_id = m.get('TagGroupId')
        if m.get('TagGroupIndex') is not None:
            self.tag_group_index = m.get('TagGroupIndex')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class ModifyTagGroupsResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_group: str = None,
        tag_name: str = None,
        tag_index: int = None,
        script_id: str = None,
        tag_id: str = None,
    ):
        self.tag_group = tag_group
        self.tag_name = tag_name
        self.tag_index = tag_index
        self.script_id = script_id
        self.tag_id = tag_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_group is not None:
            result['TagGroup'] = self.tag_group
        if self.tag_name is not None:
            result['TagName'] = self.tag_name
        if self.tag_index is not None:
            result['TagIndex'] = self.tag_index
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.tag_id is not None:
            result['TagId'] = self.tag_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagGroup') is not None:
            self.tag_group = m.get('TagGroup')
        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')
        if m.get('TagIndex') is not None:
            self.tag_index = m.get('TagIndex')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')
        return self


class ModifyTagGroupsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        tag_groups: List[ModifyTagGroupsResponseBodyTagGroups] = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
        tags: List[ModifyTagGroupsResponseBodyTags] = None,
    ):
        self.message = message
        self.request_id = request_id
        self.tag_groups = tag_groups
        self.http_status_code = http_status_code
        self.code = code
        self.success = success
        self.tags = tags

    def validate(self):
        if self.tag_groups:
            for k in self.tag_groups:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagGroups'] = []
        if self.tag_groups is not None:
            for k in self.tag_groups:
                result['TagGroups'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_groups = []
        if m.get('TagGroups') is not None:
            for k in m.get('TagGroups'):
                temp_model = ModifyTagGroupsResponseBodyTagGroups()
                self.tag_groups.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ModifyTagGroupsResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ModifyTagGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyTagGroupsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyTagGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyTTSConfigRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        voice: str = None,
        speech_rate: str = None,
        volume: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.voice = voice
        self.speech_rate = speech_rate
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class ModifyTTSConfigResponseBodyTTSConfig(TeaModel):
    def __init__(
        self,
        voice: str = None,
        ttsconfig_id: str = None,
        speech_rate: str = None,
        volume: str = None,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.voice = voice
        self.ttsconfig_id = ttsconfig_id
        self.speech_rate = speech_rate
        self.volume = volume
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.voice is not None:
            result['Voice'] = self.voice
        if self.ttsconfig_id is not None:
            result['TTSConfigId'] = self.ttsconfig_id
        if self.speech_rate is not None:
            result['SpeechRate'] = self.speech_rate
        if self.volume is not None:
            result['Volume'] = self.volume
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Voice') is not None:
            self.voice = m.get('Voice')
        if m.get('TTSConfigId') is not None:
            self.ttsconfig_id = m.get('TTSConfigId')
        if m.get('SpeechRate') is not None:
            self.speech_rate = m.get('SpeechRate')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class ModifyTTSConfigResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        ttsconfig: ModifyTTSConfigResponseBodyTTSConfig = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.ttsconfig = ttsconfig
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.ttsconfig:
            self.ttsconfig.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.ttsconfig is not None:
            result['TTSConfig'] = self.ttsconfig.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TTSConfig') is not None:
            temp_model = ModifyTTSConfigResponseBodyTTSConfig()
            self.ttsconfig = temp_model.from_map(m['TTSConfig'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ModifyTTSConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyTTSConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyTTSConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishScriptRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        description: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class PublishScriptResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PublishScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PublishScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishScriptForDebugRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class PublishScriptForDebugResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PublishScriptForDebugResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishScriptForDebugResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = PublishScriptForDebugResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        scenario_id: str = None,
        job_group_id: str = None,
        start_time: int = None,
        end_time: int = None,
        time_alignment: str = None,
        contact_name: str = None,
        phone_number: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.scenario_id = scenario_id
        self.job_group_id = job_group_id
        self.start_time = start_time
        self.end_time = end_time
        self.time_alignment = time_alignment
        self.contact_name = contact_name
        self.phone_number = phone_number
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.time_alignment is not None:
            result['TimeAlignment'] = self.time_alignment
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('TimeAlignment') is not None:
            self.time_alignment = m.get('TimeAlignment')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class QueryJobsResponseBodyJobsListSummary(TeaModel):
    def __init__(
        self,
        summary_name: str = None,
        group_id: str = None,
        job_id: str = None,
        category: str = None,
        task_id: str = None,
        content: str = None,
        conversation_detail_id: str = None,
        summary_id: str = None,
    ):
        self.summary_name = summary_name
        self.group_id = group_id
        self.job_id = job_id
        self.category = category
        self.task_id = task_id
        self.content = content
        self.conversation_detail_id = conversation_detail_id
        self.summary_id = summary_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary_name is not None:
            result['SummaryName'] = self.summary_name
        if self.group_id is not None:
            result['GroupId'] = self.group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.category is not None:
            result['Category'] = self.category
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.content is not None:
            result['Content'] = self.content
        if self.conversation_detail_id is not None:
            result['ConversationDetailId'] = self.conversation_detail_id
        if self.summary_id is not None:
            result['SummaryId'] = self.summary_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ConversationDetailId') is not None:
            self.conversation_detail_id = m.get('ConversationDetailId')
        if m.get('SummaryId') is not None:
            self.summary_id = m.get('SummaryId')
        return self


class QueryJobsResponseBodyJobsListContacts(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        state: str = None,
        contact_id: str = None,
        honorific: str = None,
        job_id: str = None,
        contact_name: str = None,
        role: str = None,
        reference_id: str = None,
    ):
        self.phone_number = phone_number
        self.state = state
        self.contact_id = contact_id
        self.honorific = honorific
        self.job_id = job_id
        self.contact_name = contact_name
        self.role = role
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.state is not None:
            result['State'] = self.state
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.honorific is not None:
            result['Honorific'] = self.honorific
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.role is not None:
            result['Role'] = self.role
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        return self


class QueryJobsResponseBodyJobsListExtras(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class QueryJobsResponseBodyJobsListTasksContact(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        state: str = None,
        contact_id: str = None,
        honorific: str = None,
        job_id: str = None,
        contact_name: str = None,
        role: str = None,
        reference_id: str = None,
    ):
        self.phone_number = phone_number
        self.state = state
        self.contact_id = contact_id
        self.honorific = honorific
        self.job_id = job_id
        self.contact_name = contact_name
        self.role = role
        self.reference_id = reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.state is not None:
            result['State'] = self.state
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id
        if self.honorific is not None:
            result['Honorific'] = self.honorific
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.contact_name is not None:
            result['ContactName'] = self.contact_name
        if self.role is not None:
            result['Role'] = self.role
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('State') is not None:
            self.state = m.get('State')
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')
        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        return self


class QueryJobsResponseBodyJobsListTasks(TeaModel):
    def __init__(
        self,
        status: str = None,
        planed_time: int = None,
        chatbot_id: str = None,
        actual_time: int = None,
        called_number: str = None,
        scenario_id: str = None,
        contact: QueryJobsResponseBodyJobsListTasksContact = None,
        job_id: str = None,
        call_id: str = None,
        calling_number: str = None,
        brief: str = None,
        duration: int = None,
        task_id: str = None,
    ):
        self.status = status
        self.planed_time = planed_time
        self.chatbot_id = chatbot_id
        self.actual_time = actual_time
        self.called_number = called_number
        self.scenario_id = scenario_id
        self.contact = contact
        self.job_id = job_id
        self.call_id = call_id
        self.calling_number = calling_number
        self.brief = brief
        self.duration = duration
        self.task_id = task_id

    def validate(self):
        if self.contact:
            self.contact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.planed_time is not None:
            result['PlanedTime'] = self.planed_time
        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.contact is not None:
            result['Contact'] = self.contact.to_map()
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.brief is not None:
            result['Brief'] = self.brief
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PlanedTime') is not None:
            self.planed_time = m.get('PlanedTime')
        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('Contact') is not None:
            temp_model = QueryJobsResponseBodyJobsListTasksContact()
            self.contact = temp_model.from_map(m['Contact'])
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('Brief') is not None:
            self.brief = m.get('Brief')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryJobsResponseBodyJobsList(TeaModel):
    def __init__(
        self,
        status: str = None,
        calling_numbers: List[str] = None,
        summary: List[QueryJobsResponseBodyJobsListSummary] = None,
        contacts: List[QueryJobsResponseBodyJobsListContacts] = None,
        priority: int = None,
        failure_reason: str = None,
        extras: List[QueryJobsResponseBodyJobsListExtras] = None,
        reference_id: str = None,
        job_group_id: str = None,
        scenario_id: str = None,
        tasks: List[QueryJobsResponseBodyJobsListTasks] = None,
        strategy_id: str = None,
        job_id: str = None,
    ):
        self.status = status
        self.calling_numbers = calling_numbers
        self.summary = summary
        self.contacts = contacts
        self.priority = priority
        self.failure_reason = failure_reason
        self.extras = extras
        self.reference_id = reference_id
        self.job_group_id = job_group_id
        self.scenario_id = scenario_id
        self.tasks = tasks
        self.strategy_id = strategy_id
        self.job_id = job_id

    def validate(self):
        if self.summary:
            for k in self.summary:
                if k:
                    k.validate()
        if self.contacts:
            for k in self.contacts:
                if k:
                    k.validate()
        if self.extras:
            for k in self.extras:
                if k:
                    k.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers
        result['Summary'] = []
        if self.summary is not None:
            for k in self.summary:
                result['Summary'].append(k.to_map() if k else None)
        result['Contacts'] = []
        if self.contacts is not None:
            for k in self.contacts:
                result['Contacts'].append(k.to_map() if k else None)
        if self.priority is not None:
            result['Priority'] = self.priority
        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason
        result['Extras'] = []
        if self.extras is not None:
            for k in self.extras:
                result['Extras'].append(k.to_map() if k else None)
        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')
        self.summary = []
        if m.get('Summary') is not None:
            for k in m.get('Summary'):
                temp_model = QueryJobsResponseBodyJobsListSummary()
                self.summary.append(temp_model.from_map(k))
        self.contacts = []
        if m.get('Contacts') is not None:
            for k in m.get('Contacts'):
                temp_model = QueryJobsResponseBodyJobsListContacts()
                self.contacts.append(temp_model.from_map(k))
        if m.get('Priority') is not None:
            self.priority = m.get('Priority')
        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')
        self.extras = []
        if m.get('Extras') is not None:
            for k in m.get('Extras'):
                temp_model = QueryJobsResponseBodyJobsListExtras()
                self.extras.append(temp_model.from_map(k))
        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = QueryJobsResponseBodyJobsListTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        return self


class QueryJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        list: List[QueryJobsResponseBodyJobsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryJobsResponseBodyJobsList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryJobsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        jobs: QueryJobsResponseBodyJobs = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.jobs = jobs
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.jobs:
            self.jobs.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.jobs is not None:
            result['Jobs'] = self.jobs.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Jobs') is not None:
            temp_model = QueryJobsResponseBodyJobs()
            self.jobs = temp_model.from_map(m['Jobs'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryScriptsByStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        status_list: List[str] = None,
    ):
        self.instance_id = instance_id
        self.page_number = page_number
        self.page_size = page_size
        self.status_list = status_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.status_list is not None:
            result['StatusList'] = self.status_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('StatusList') is not None:
            self.status_list = m.get('StatusList')
        return self


class QueryScriptsByStatusResponseBodyScriptsList(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: int = None,
        script_id: str = None,
        is_debug_drafted: bool = None,
        applied_version: str = None,
        industry: str = None,
        script_description: str = None,
        is_drafted: bool = None,
        debug_status: str = None,
        debug_version: str = None,
        script_name: str = None,
        scene: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.script_id = script_id
        self.is_debug_drafted = is_debug_drafted
        self.applied_version = applied_version
        self.industry = industry
        self.script_description = script_description
        self.is_drafted = is_drafted
        self.debug_status = debug_status
        self.debug_version = debug_version
        self.script_name = script_name
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.is_debug_drafted is not None:
            result['IsDebugDrafted'] = self.is_debug_drafted
        if self.applied_version is not None:
            result['AppliedVersion'] = self.applied_version
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description
        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted
        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status
        if self.debug_version is not None:
            result['DebugVersion'] = self.debug_version
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IsDebugDrafted') is not None:
            self.is_debug_drafted = m.get('IsDebugDrafted')
        if m.get('AppliedVersion') is not None:
            self.applied_version = m.get('AppliedVersion')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')
        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')
        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')
        if m.get('DebugVersion') is not None:
            self.debug_version = m.get('DebugVersion')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class QueryScriptsByStatusResponseBodyScripts(TeaModel):
    def __init__(
        self,
        list: List[QueryScriptsByStatusResponseBodyScriptsList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.list = list
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = QueryScriptsByStatusResponseBodyScriptsList()
                self.list.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class QueryScriptsByStatusResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        scripts: QueryScriptsByStatusResponseBodyScripts = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.scripts = scripts
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.scripts:
            self.scripts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scripts is not None:
            result['Scripts'] = self.scripts.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scripts') is not None:
            temp_model = QueryScriptsByStatusResponseBodyScripts()
            self.scripts = temp_model.from_map(m['Scripts'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryScriptsByStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryScriptsByStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryScriptsByStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryScriptWaveformsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        script_content: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.script_content = script_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.script_content is not None:
            result['ScriptContent'] = self.script_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')
        return self


class QueryScriptWaveformsResponseBodyScriptWaveforms(TeaModel):
    def __init__(
        self,
        script_content: str = None,
        script_waveform_id: str = None,
        file_name: str = None,
        script_id: str = None,
        file_id: str = None,
    ):
        self.script_content = script_content
        self.script_waveform_id = script_waveform_id
        self.file_name = file_name
        self.script_id = script_id
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script_content is not None:
            result['ScriptContent'] = self.script_content
        if self.script_waveform_id is not None:
            result['ScriptWaveformId'] = self.script_waveform_id
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.file_id is not None:
            result['FileId'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScriptContent') is not None:
            self.script_content = m.get('ScriptContent')
        if m.get('ScriptWaveformId') is not None:
            self.script_waveform_id = m.get('ScriptWaveformId')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')
        return self


class QueryScriptWaveformsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        script_waveforms: List[QueryScriptWaveformsResponseBodyScriptWaveforms] = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.script_waveforms = script_waveforms
        self.code = code
        self.success = success

    def validate(self):
        if self.script_waveforms:
            for k in self.script_waveforms:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        result['ScriptWaveforms'] = []
        if self.script_waveforms is not None:
            for k in self.script_waveforms:
                result['ScriptWaveforms'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        self.script_waveforms = []
        if m.get('ScriptWaveforms') is not None:
            for k in m.get('ScriptWaveforms'):
                temp_model = QueryScriptWaveformsResponseBodyScriptWaveforms()
                self.script_waveforms.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryScriptWaveformsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryScriptWaveformsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryScriptWaveformsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecordFailureRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        call_id: str = None,
        task_id: str = None,
        actual_time: int = None,
        calling_number: str = None,
        called_number: str = None,
        disposition_code: str = None,
    ):
        self.instance_id = instance_id
        self.call_id = call_id
        self.task_id = task_id
        self.actual_time = actual_time
        self.calling_number = calling_number
        self.called_number = called_number
        self.disposition_code = disposition_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.call_id is not None:
            result['CallId'] = self.call_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        if self.called_number is not None:
            result['CalledNumber'] = self.called_number
        if self.disposition_code is not None:
            result['DispositionCode'] = self.disposition_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')
        if m.get('DispositionCode') is not None:
            self.disposition_code = m.get('DispositionCode')
        return self


class RecordFailureResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecordFailureResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecordFailureResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RecordFailureResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        all: bool = None,
        scenario_id: str = None,
        job_group_id: str = None,
        job_id: List[str] = None,
        job_reference_id: List[str] = None,
    ):
        self.instance_id = instance_id
        self.all = all
        self.scenario_id = scenario_id
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.job_reference_id = job_reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.all is not None:
            result['All'] = self.all
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_reference_id is not None:
            result['JobReferenceId'] = self.job_reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobReferenceId') is not None:
            self.job_reference_id = m.get('JobReferenceId')
        return self


class ResumeJobsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ResumeJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResumeJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResumeJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackScriptRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
        rollback_version: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id
        self.rollback_version = rollback_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.rollback_version is not None:
            result['RollbackVersion'] = self.rollback_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('RollbackVersion') is not None:
            self.rollback_version = m.get('RollbackVersion')
        return self


class RollbackScriptResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RollbackScriptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollbackScriptResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RollbackScriptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
        scenario_id: str = None,
        job_json: str = None,
        calling_number: List[str] = None,
    ):
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.scenario_id = scenario_id
        self.job_json = job_json
        self.calling_number = calling_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.job_json is not None:
            result['JobJson'] = self.job_json
        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('JobJson') is not None:
            self.job_json = m.get('JobJson')
        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')
        return self


class StartJobResponseBodyTaskIds(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class StartJobResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        task_ids: List[StartJobResponseBodyTaskIds] = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.task_ids = task_ids
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.task_ids:
            for k in self.task_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskIds'] = []
        if self.task_ids is not None:
            for k in self.task_ids:
                result['TaskIds'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_ids = []
        if m.get('TaskIds') is not None:
            for k in m.get('TaskIds'):
                temp_model = StartJobResponseBodyTaskIds()
                self.task_ids.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class StartJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StartJobResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitBatchJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_group_id: str = None,
    ):
        self.instance_id = instance_id
        self.job_group_id = job_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        return self


class SubmitBatchJobsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitBatchJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitBatchJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitBatchJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitRecordingRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: str = None,
        resource_recording: str = None,
        merged_recording: str = None,
    ):
        self.instance_id = instance_id
        self.task_id = task_id
        self.resource_recording = resource_recording
        self.merged_recording = merged_recording

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.resource_recording is not None:
            result['ResourceRecording'] = self.resource_recording
        if self.merged_recording is not None:
            result['MergedRecording'] = self.merged_recording
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('ResourceRecording') is not None:
            self.resource_recording = m.get('ResourceRecording')
        if m.get('MergedRecording') is not None:
            self.merged_recording = m.get('MergedRecording')
        return self


class SubmitRecordingResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitRecordingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitRecordingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitRecordingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitScriptReviewRequest(TeaModel):
    def __init__(
        self,
        script_id: str = None,
        instance_id: str = None,
        description: str = None,
    ):
        self.script_id = script_id
        self.instance_id = instance_id
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class SubmitScriptReviewResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitScriptReviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SubmitScriptReviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SubmitScriptReviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SuspendJobsRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        all: bool = None,
        scenario_id: str = None,
        job_group_id: str = None,
        job_id: List[str] = None,
        job_reference_id: List[str] = None,
    ):
        self.instance_id = instance_id
        self.all = all
        self.scenario_id = scenario_id
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.job_reference_id = job_reference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.all is not None:
            result['All'] = self.all
        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id
        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.job_reference_id is not None:
            result['JobReferenceId'] = self.job_reference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')
        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('JobReferenceId') is not None:
            self.job_reference_id = m.get('JobReferenceId')
        return self


class SuspendJobsResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SuspendJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SuspendJobsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SuspendJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TaskPreparingRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        job_id: str = None,
        instance_owner_id: int = None,
    ):
        self.instance_id = instance_id
        self.job_id = job_id
        self.instance_owner_id = instance_owner_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.job_id is not None:
            result['JobId'] = self.job_id
        if self.instance_owner_id is not None:
            result['InstanceOwnerId'] = self.instance_owner_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')
        if m.get('InstanceOwnerId') is not None:
            self.instance_owner_id = m.get('InstanceOwnerId')
        return self


class TaskPreparingResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        request_id: str = None,
        message: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.task_id = task_id
        self.request_id = request_id
        self.message = message
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TaskPreparingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TaskPreparingResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TaskPreparingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class WithdrawScriptReviewRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        script_id: str = None,
    ):
        self.instance_id = instance_id
        self.script_id = script_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        return self


class WithdrawScriptReviewResponseBodyScript(TeaModel):
    def __init__(
        self,
        status: str = None,
        update_time: int = None,
        industry: str = None,
        script_description: str = None,
        is_drafted: bool = None,
        debug_status: str = None,
        script_id: str = None,
        is_debug_drafted: bool = None,
        script_name: str = None,
        scene: str = None,
    ):
        self.status = status
        self.update_time = update_time
        self.industry = industry
        self.script_description = script_description
        self.is_drafted = is_drafted
        self.debug_status = debug_status
        self.script_id = script_id
        self.is_debug_drafted = is_debug_drafted
        self.script_name = script_name
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.industry is not None:
            result['Industry'] = self.industry
        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description
        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted
        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status
        if self.script_id is not None:
            result['ScriptId'] = self.script_id
        if self.is_debug_drafted is not None:
            result['IsDebugDrafted'] = self.is_debug_drafted
        if self.script_name is not None:
            result['ScriptName'] = self.script_name
        if self.scene is not None:
            result['Scene'] = self.scene
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Industry') is not None:
            self.industry = m.get('Industry')
        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')
        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')
        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')
        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')
        if m.get('IsDebugDrafted') is not None:
            self.is_debug_drafted = m.get('IsDebugDrafted')
        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        return self


class WithdrawScriptReviewResponseBody(TeaModel):
    def __init__(
        self,
        script: WithdrawScriptReviewResponseBodyScript = None,
        message: str = None,
        request_id: str = None,
        http_status_code: int = None,
        code: str = None,
        success: bool = None,
    ):
        self.script = script
        self.message = message
        self.request_id = request_id
        self.http_status_code = http_status_code
        self.code = code
        self.success = success

    def validate(self):
        if self.script:
            self.script.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.script is not None:
            result['Script'] = self.script.to_map()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Script') is not None:
            temp_model = WithdrawScriptReviewResponseBodyScript()
            self.script = temp_model.from_map(m['Script'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class WithdrawScriptReviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: WithdrawScriptReviewResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = WithdrawScriptReviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


