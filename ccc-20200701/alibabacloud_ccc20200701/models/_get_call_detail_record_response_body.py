# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class GetCallDetailRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCallDetailRecordResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetCallDetailRecordResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCallDetailRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        agent_events: List[main_models.GetCallDetailRecordResponseBodyDataAgentEvents] = None,
        agent_ids: str = None,
        agent_names: str = None,
        analytics_report: main_models.GetCallDetailRecordResponseBodyDataAnalyticsReport = None,
        analytics_report_ready: bool = None,
        call_duration: int = None,
        called_number: str = None,
        callee_location: str = None,
        caller_location: str = None,
        calling_number: str = None,
        contact_disposition: str = None,
        contact_id: str = None,
        contact_type: str = None,
        customer_events: List[main_models.GetCallDetailRecordResponseBodyDataCustomerEvents] = None,
        early_media_state: str = None,
        established_time: int = None,
        instance_id: str = None,
        ivr_events: List[main_models.GetCallDetailRecordResponseBodyDataIvrEvents] = None,
        outside_number_release_reason: str = None,
        queue_events: List[main_models.GetCallDetailRecordResponseBodyDataQueueEvents] = None,
        recording_ready: bool = None,
        release_initiator: str = None,
        release_reason: str = None,
        release_time: int = None,
        satisfaction: int = None,
        satisfaction_survey_channel: str = None,
        satisfaction_survey_offered: bool = None,
        skill_group_ids: str = None,
        skill_group_names: str = None,
        start_time: int = None,
    ):
        self.agent_events = agent_events
        self.agent_ids = agent_ids
        self.agent_names = agent_names
        self.analytics_report = analytics_report
        self.analytics_report_ready = analytics_report_ready
        self.call_duration = call_duration
        self.called_number = called_number
        self.callee_location = callee_location
        self.caller_location = caller_location
        self.calling_number = calling_number
        self.contact_disposition = contact_disposition
        self.contact_id = contact_id
        self.contact_type = contact_type
        self.customer_events = customer_events
        self.early_media_state = early_media_state
        self.established_time = established_time
        self.instance_id = instance_id
        self.ivr_events = ivr_events
        self.outside_number_release_reason = outside_number_release_reason
        self.queue_events = queue_events
        self.recording_ready = recording_ready
        self.release_initiator = release_initiator
        self.release_reason = release_reason
        self.release_time = release_time
        self.satisfaction = satisfaction
        self.satisfaction_survey_channel = satisfaction_survey_channel
        self.satisfaction_survey_offered = satisfaction_survey_offered
        self.skill_group_ids = skill_group_ids
        self.skill_group_names = skill_group_names
        self.start_time = start_time

    def validate(self):
        if self.agent_events:
            for v1 in self.agent_events:
                 if v1:
                    v1.validate()
        if self.analytics_report:
            self.analytics_report.validate()
        if self.customer_events:
            for v1 in self.customer_events:
                 if v1:
                    v1.validate()
        if self.ivr_events:
            for v1 in self.ivr_events:
                 if v1:
                    v1.validate()
        if self.queue_events:
            for v1 in self.queue_events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AgentEvents'] = []
        if self.agent_events is not None:
            for k1 in self.agent_events:
                result['AgentEvents'].append(k1.to_map() if k1 else None)

        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids

        if self.agent_names is not None:
            result['AgentNames'] = self.agent_names

        if self.analytics_report is not None:
            result['AnalyticsReport'] = self.analytics_report.to_map()

        if self.analytics_report_ready is not None:
            result['AnalyticsReportReady'] = self.analytics_report_ready

        if self.call_duration is not None:
            result['CallDuration'] = self.call_duration

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.callee_location is not None:
            result['CalleeLocation'] = self.callee_location

        if self.caller_location is not None:
            result['CallerLocation'] = self.caller_location

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.contact_disposition is not None:
            result['ContactDisposition'] = self.contact_disposition

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_type is not None:
            result['ContactType'] = self.contact_type

        result['CustomerEvents'] = []
        if self.customer_events is not None:
            for k1 in self.customer_events:
                result['CustomerEvents'].append(k1.to_map() if k1 else None)

        if self.early_media_state is not None:
            result['EarlyMediaState'] = self.early_media_state

        if self.established_time is not None:
            result['EstablishedTime'] = self.established_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['IvrEvents'] = []
        if self.ivr_events is not None:
            for k1 in self.ivr_events:
                result['IvrEvents'].append(k1.to_map() if k1 else None)

        if self.outside_number_release_reason is not None:
            result['OutsideNumberReleaseReason'] = self.outside_number_release_reason

        result['QueueEvents'] = []
        if self.queue_events is not None:
            for k1 in self.queue_events:
                result['QueueEvents'].append(k1.to_map() if k1 else None)

        if self.recording_ready is not None:
            result['RecordingReady'] = self.recording_ready

        if self.release_initiator is not None:
            result['ReleaseInitiator'] = self.release_initiator

        if self.release_reason is not None:
            result['ReleaseReason'] = self.release_reason

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.satisfaction is not None:
            result['Satisfaction'] = self.satisfaction

        if self.satisfaction_survey_channel is not None:
            result['SatisfactionSurveyChannel'] = self.satisfaction_survey_channel

        if self.satisfaction_survey_offered is not None:
            result['SatisfactionSurveyOffered'] = self.satisfaction_survey_offered

        if self.skill_group_ids is not None:
            result['SkillGroupIds'] = self.skill_group_ids

        if self.skill_group_names is not None:
            result['SkillGroupNames'] = self.skill_group_names

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.agent_events = []
        if m.get('AgentEvents') is not None:
            for k1 in m.get('AgentEvents'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataAgentEvents()
                self.agent_events.append(temp_model.from_map(k1))

        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')

        if m.get('AgentNames') is not None:
            self.agent_names = m.get('AgentNames')

        if m.get('AnalyticsReport') is not None:
            temp_model = main_models.GetCallDetailRecordResponseBodyDataAnalyticsReport()
            self.analytics_report = temp_model.from_map(m.get('AnalyticsReport'))

        if m.get('AnalyticsReportReady') is not None:
            self.analytics_report_ready = m.get('AnalyticsReportReady')

        if m.get('CallDuration') is not None:
            self.call_duration = m.get('CallDuration')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CalleeLocation') is not None:
            self.callee_location = m.get('CalleeLocation')

        if m.get('CallerLocation') is not None:
            self.caller_location = m.get('CallerLocation')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ContactDisposition') is not None:
            self.contact_disposition = m.get('ContactDisposition')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')

        self.customer_events = []
        if m.get('CustomerEvents') is not None:
            for k1 in m.get('CustomerEvents'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataCustomerEvents()
                self.customer_events.append(temp_model.from_map(k1))

        if m.get('EarlyMediaState') is not None:
            self.early_media_state = m.get('EarlyMediaState')

        if m.get('EstablishedTime') is not None:
            self.established_time = m.get('EstablishedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.ivr_events = []
        if m.get('IvrEvents') is not None:
            for k1 in m.get('IvrEvents'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataIvrEvents()
                self.ivr_events.append(temp_model.from_map(k1))

        if m.get('OutsideNumberReleaseReason') is not None:
            self.outside_number_release_reason = m.get('OutsideNumberReleaseReason')

        self.queue_events = []
        if m.get('QueueEvents') is not None:
            for k1 in m.get('QueueEvents'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataQueueEvents()
                self.queue_events.append(temp_model.from_map(k1))

        if m.get('RecordingReady') is not None:
            self.recording_ready = m.get('RecordingReady')

        if m.get('ReleaseInitiator') is not None:
            self.release_initiator = m.get('ReleaseInitiator')

        if m.get('ReleaseReason') is not None:
            self.release_reason = m.get('ReleaseReason')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('Satisfaction') is not None:
            self.satisfaction = m.get('Satisfaction')

        if m.get('SatisfactionSurveyChannel') is not None:
            self.satisfaction_survey_channel = m.get('SatisfactionSurveyChannel')

        if m.get('SatisfactionSurveyOffered') is not None:
            self.satisfaction_survey_offered = m.get('SatisfactionSurveyOffered')

        if m.get('SkillGroupIds') is not None:
            self.skill_group_ids = m.get('SkillGroupIds')

        if m.get('SkillGroupNames') is not None:
            self.skill_group_names = m.get('SkillGroupNames')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetCallDetailRecordResponseBodyDataQueueEvents(DaraModel):
    def __init__(
        self,
        event_sequence: List[main_models.GetCallDetailRecordResponseBodyDataQueueEventsEventSequence] = None,
        flow_id: str = None,
        queue_id: str = None,
        queue_name: str = None,
        queue_type: int = None,
    ):
        self.event_sequence = event_sequence
        self.flow_id = flow_id
        self.queue_id = queue_id
        self.queue_name = queue_name
        self.queue_type = queue_type

    def validate(self):
        if self.event_sequence:
            for v1 in self.event_sequence:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventSequence'] = []
        if self.event_sequence is not None:
            for k1 in self.event_sequence:
                result['EventSequence'].append(k1.to_map() if k1 else None)

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.queue_id is not None:
            result['QueueId'] = self.queue_id

        if self.queue_name is not None:
            result['QueueName'] = self.queue_name

        if self.queue_type is not None:
            result['QueueType'] = self.queue_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_sequence = []
        if m.get('EventSequence') is not None:
            for k1 in m.get('EventSequence'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataQueueEventsEventSequence()
                self.event_sequence.append(temp_model.from_map(k1))

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('QueueId') is not None:
            self.queue_id = m.get('QueueId')

        if m.get('QueueName') is not None:
            self.queue_name = m.get('QueueName')

        if m.get('QueueType') is not None:
            self.queue_type = m.get('QueueType')

        return self

class GetCallDetailRecordResponseBodyDataQueueEventsEventSequence(DaraModel):
    def __init__(
        self,
        event: str = None,
        event_time: int = None,
    ):
        self.event = event
        self.event_time = event_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['Event'] = self.event

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        return self

class GetCallDetailRecordResponseBodyDataIvrEvents(DaraModel):
    def __init__(
        self,
        event_sequence: List[main_models.GetCallDetailRecordResponseBodyDataIvrEventsEventSequence] = None,
        flow_id: str = None,
        flow_type: str = None,
    ):
        self.event_sequence = event_sequence
        self.flow_id = flow_id
        self.flow_type = flow_type

    def validate(self):
        if self.event_sequence:
            for v1 in self.event_sequence:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EventSequence'] = []
        if self.event_sequence is not None:
            for k1 in self.event_sequence:
                result['EventSequence'].append(k1.to_map() if k1 else None)

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_type is not None:
            result['FlowType'] = self.flow_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.event_sequence = []
        if m.get('EventSequence') is not None:
            for k1 in m.get('EventSequence'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataIvrEventsEventSequence()
                self.event_sequence.append(temp_model.from_map(k1))

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowType') is not None:
            self.flow_type = m.get('FlowType')

        return self

class GetCallDetailRecordResponseBodyDataIvrEventsEventSequence(DaraModel):
    def __init__(
        self,
        event: str = None,
        event_time: int = None,
    ):
        self.event = event
        self.event_time = event_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['Event'] = self.event

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        return self

class GetCallDetailRecordResponseBodyDataCustomerEvents(DaraModel):
    def __init__(
        self,
        customer_id: str = None,
        event_sequence: List[main_models.GetCallDetailRecordResponseBodyDataCustomerEventsEventSequence] = None,
    ):
        self.customer_id = customer_id
        self.event_sequence = event_sequence

    def validate(self):
        if self.event_sequence:
            for v1 in self.event_sequence:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_id is not None:
            result['CustomerId'] = self.customer_id

        result['EventSequence'] = []
        if self.event_sequence is not None:
            for k1 in self.event_sequence:
                result['EventSequence'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerId') is not None:
            self.customer_id = m.get('CustomerId')

        self.event_sequence = []
        if m.get('EventSequence') is not None:
            for k1 in m.get('EventSequence'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataCustomerEventsEventSequence()
                self.event_sequence.append(temp_model.from_map(k1))

        return self

class GetCallDetailRecordResponseBodyDataCustomerEventsEventSequence(DaraModel):
    def __init__(
        self,
        event: str = None,
        event_time: int = None,
    ):
        self.event = event
        self.event_time = event_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['Event'] = self.event

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        return self

class GetCallDetailRecordResponseBodyDataAnalyticsReport(DaraModel):
    def __init__(
        self,
        emotion: main_models.GetCallDetailRecordResponseBodyDataAnalyticsReportEmotion = None,
        problem_solving: main_models.GetCallDetailRecordResponseBodyDataAnalyticsReportProblemSolving = None,
        satisfaction: main_models.GetCallDetailRecordResponseBodyDataAnalyticsReportSatisfaction = None,
        todo_list: main_models.GetCallDetailRecordResponseBodyDataAnalyticsReportTodoList = None,
    ):
        self.emotion = emotion
        self.problem_solving = problem_solving
        self.satisfaction = satisfaction
        self.todo_list = todo_list

    def validate(self):
        if self.emotion:
            self.emotion.validate()
        if self.problem_solving:
            self.problem_solving.validate()
        if self.satisfaction:
            self.satisfaction.validate()
        if self.todo_list:
            self.todo_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.emotion is not None:
            result['Emotion'] = self.emotion.to_map()

        if self.problem_solving is not None:
            result['ProblemSolving'] = self.problem_solving.to_map()

        if self.satisfaction is not None:
            result['Satisfaction'] = self.satisfaction.to_map()

        if self.todo_list is not None:
            result['TodoList'] = self.todo_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Emotion') is not None:
            temp_model = main_models.GetCallDetailRecordResponseBodyDataAnalyticsReportEmotion()
            self.emotion = temp_model.from_map(m.get('Emotion'))

        if m.get('ProblemSolving') is not None:
            temp_model = main_models.GetCallDetailRecordResponseBodyDataAnalyticsReportProblemSolving()
            self.problem_solving = temp_model.from_map(m.get('ProblemSolving'))

        if m.get('Satisfaction') is not None:
            temp_model = main_models.GetCallDetailRecordResponseBodyDataAnalyticsReportSatisfaction()
            self.satisfaction = temp_model.from_map(m.get('Satisfaction'))

        if m.get('TodoList') is not None:
            temp_model = main_models.GetCallDetailRecordResponseBodyDataAnalyticsReportTodoList()
            self.todo_list = temp_model.from_map(m.get('TodoList'))

        return self

class GetCallDetailRecordResponseBodyDataAnalyticsReportTodoList(DaraModel):
    def __init__(
        self,
        success: bool = None,
        task_id: str = None,
        tasks: List[str] = None,
    ):
        self.success = success
        self.task_id = task_id
        self.tasks = tasks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.tasks is not None:
            result['Tasks'] = self.tasks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Tasks') is not None:
            self.tasks = m.get('Tasks')

        return self

class GetCallDetailRecordResponseBodyDataAnalyticsReportSatisfaction(DaraModel):
    def __init__(
        self,
        remark: str = None,
        satisfaction_description: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.remark = remark
        self.satisfaction_description = satisfaction_description
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.remark is not None:
            result['Remark'] = self.remark

        if self.satisfaction_description is not None:
            result['SatisfactionDescription'] = self.satisfaction_description

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SatisfactionDescription') is not None:
            self.satisfaction_description = m.get('SatisfactionDescription')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetCallDetailRecordResponseBodyDataAnalyticsReportProblemSolving(DaraModel):
    def __init__(
        self,
        problem: str = None,
        solution: str = None,
        solved: bool = None,
        success: bool = None,
        task_id: str = None,
    ):
        self.problem = problem
        self.solution = solution
        self.solved = solved
        self.success = success
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.problem is not None:
            result['Problem'] = self.problem

        if self.solution is not None:
            result['Solution'] = self.solution

        if self.solved is not None:
            result['Solved'] = self.solved

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Problem') is not None:
            self.problem = m.get('Problem')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        if m.get('Solved') is not None:
            self.solved = m.get('Solved')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class GetCallDetailRecordResponseBodyDataAnalyticsReportEmotion(DaraModel):
    def __init__(
        self,
        confidence: int = None,
        remark: str = None,
        success: bool = None,
        task_id: str = None,
        type: str = None,
    ):
        self.confidence = confidence
        self.remark = remark
        self.success = success
        self.task_id = task_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidence is not None:
            result['Confidence'] = self.confidence

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.success is not None:
            result['Success'] = self.success

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Confidence') is not None:
            self.confidence = m.get('Confidence')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetCallDetailRecordResponseBodyDataAgentEvents(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        event_sequence: List[main_models.GetCallDetailRecordResponseBodyDataAgentEventsEventSequence] = None,
        skill_group_id: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.event_sequence = event_sequence
        self.skill_group_id = skill_group_id

    def validate(self):
        if self.event_sequence:
            for v1 in self.event_sequence:
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

        result['EventSequence'] = []
        if self.event_sequence is not None:
            for k1 in self.event_sequence:
                result['EventSequence'].append(k1.to_map() if k1 else None)

        if self.skill_group_id is not None:
            result['SkillGroupId'] = self.skill_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')

        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        self.event_sequence = []
        if m.get('EventSequence') is not None:
            for k1 in m.get('EventSequence'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataAgentEventsEventSequence()
                self.event_sequence.append(temp_model.from_map(k1))

        if m.get('SkillGroupId') is not None:
            self.skill_group_id = m.get('SkillGroupId')

        return self

class GetCallDetailRecordResponseBodyDataAgentEventsEventSequence(DaraModel):
    def __init__(
        self,
        duration: int = None,
        event: str = None,
        event_time: int = None,
    ):
        self.duration = duration
        self.event = event
        self.event_time = event_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.event is not None:
            result['Event'] = self.event

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        return self

