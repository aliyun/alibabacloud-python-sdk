# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20191226 import models as main_models
from darabonba.model import DaraModel

class DescribeJobResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        job: main_models.DescribeJobResponseBodyJob = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.job = job
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.job is not None:
            result['Job'] = self.job.to_map()

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

        if m.get('Job') is not None:
            temp_model = main_models.DescribeJobResponseBodyJob()
            self.job = temp_model.from_map(m.get('Job'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeJobResponseBodyJob(DaraModel):
    def __init__(
        self,
        actual_time: int = None,
        called_number: str = None,
        calling_numbers: List[str] = None,
        contacts: List[main_models.DescribeJobResponseBodyJobContacts] = None,
        ds_report: str = None,
        end_reason: int = None,
        extras: List[main_models.DescribeJobResponseBodyJobExtras] = None,
        failure_reason: str = None,
        instance_id: str = None,
        job_group_id: str = None,
        job_id: str = None,
        next_execution_time: int = None,
        priority: int = None,
        reference_id: str = None,
        scenario_id: str = None,
        script: main_models.DescribeJobResponseBodyJobScript = None,
        status: str = None,
        strategy_id: str = None,
        summary: List[main_models.DescribeJobResponseBodyJobSummary] = None,
        system_priority: int = None,
        tasks: List[main_models.DescribeJobResponseBodyJobTasks] = None,
    ):
        self.actual_time = actual_time
        self.called_number = called_number
        self.calling_numbers = calling_numbers
        self.contacts = contacts
        self.ds_report = ds_report
        self.end_reason = end_reason
        self.extras = extras
        self.failure_reason = failure_reason
        self.instance_id = instance_id
        self.job_group_id = job_group_id
        self.job_id = job_id
        self.next_execution_time = next_execution_time
        self.priority = priority
        self.reference_id = reference_id
        self.scenario_id = scenario_id
        self.script = script
        self.status = status
        self.strategy_id = strategy_id
        self.summary = summary
        self.system_priority = system_priority
        self.tasks = tasks

    def validate(self):
        if self.contacts:
            for v1 in self.contacts:
                 if v1:
                    v1.validate()
        if self.extras:
            for v1 in self.extras:
                 if v1:
                    v1.validate()
        if self.script:
            self.script.validate()
        if self.summary:
            for v1 in self.summary:
                 if v1:
                    v1.validate()
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_numbers is not None:
            result['CallingNumbers'] = self.calling_numbers

        result['Contacts'] = []
        if self.contacts is not None:
            for k1 in self.contacts:
                result['Contacts'].append(k1.to_map() if k1 else None)

        if self.ds_report is not None:
            result['DsReport'] = self.ds_report

        if self.end_reason is not None:
            result['EndReason'] = self.end_reason

        result['Extras'] = []
        if self.extras is not None:
            for k1 in self.extras:
                result['Extras'].append(k1.to_map() if k1 else None)

        if self.failure_reason is not None:
            result['FailureReason'] = self.failure_reason

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.job_group_id is not None:
            result['JobGroupId'] = self.job_group_id

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.next_execution_time is not None:
            result['NextExecutionTime'] = self.next_execution_time

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.script is not None:
            result['Script'] = self.script.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_id is not None:
            result['StrategyId'] = self.strategy_id

        result['Summary'] = []
        if self.summary is not None:
            for k1 in self.summary:
                result['Summary'].append(k1.to_map() if k1 else None)

        if self.system_priority is not None:
            result['SystemPriority'] = self.system_priority

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumbers') is not None:
            self.calling_numbers = m.get('CallingNumbers')

        self.contacts = []
        if m.get('Contacts') is not None:
            for k1 in m.get('Contacts'):
                temp_model = main_models.DescribeJobResponseBodyJobContacts()
                self.contacts.append(temp_model.from_map(k1))

        if m.get('DsReport') is not None:
            self.ds_report = m.get('DsReport')

        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')

        self.extras = []
        if m.get('Extras') is not None:
            for k1 in m.get('Extras'):
                temp_model = main_models.DescribeJobResponseBodyJobExtras()
                self.extras.append(temp_model.from_map(k1))

        if m.get('FailureReason') is not None:
            self.failure_reason = m.get('FailureReason')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('JobGroupId') is not None:
            self.job_group_id = m.get('JobGroupId')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('NextExecutionTime') is not None:
            self.next_execution_time = m.get('NextExecutionTime')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('Script') is not None:
            temp_model = main_models.DescribeJobResponseBodyJobScript()
            self.script = temp_model.from_map(m.get('Script'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyId') is not None:
            self.strategy_id = m.get('StrategyId')

        self.summary = []
        if m.get('Summary') is not None:
            for k1 in m.get('Summary'):
                temp_model = main_models.DescribeJobResponseBodyJobSummary()
                self.summary.append(temp_model.from_map(k1))

        if m.get('SystemPriority') is not None:
            self.system_priority = m.get('SystemPriority')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.DescribeJobResponseBodyJobTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class DescribeJobResponseBodyJobTasks(DaraModel):
    def __init__(
        self,
        actual_time: int = None,
        brief: str = None,
        call_id: str = None,
        called_number: str = None,
        calling_number: str = None,
        chatbot_id: str = None,
        contact: main_models.DescribeJobResponseBodyJobTasksContact = None,
        conversation: List[main_models.DescribeJobResponseBodyJobTasksConversation] = None,
        duration: int = None,
        end_reason: str = None,
        end_time: int = None,
        hang_up_direction: str = None,
        job_id: str = None,
        planed_time: int = None,
        real_ringing_duration: int = None,
        ringing_duration: int = None,
        scenario_id: str = None,
        sip_code: str = None,
        sip_duration: int = None,
        status: str = None,
        task_id: str = None,
    ):
        self.actual_time = actual_time
        self.brief = brief
        self.call_id = call_id
        self.called_number = called_number
        self.calling_number = calling_number
        self.chatbot_id = chatbot_id
        self.contact = contact
        self.conversation = conversation
        self.duration = duration
        self.end_reason = end_reason
        self.end_time = end_time
        self.hang_up_direction = hang_up_direction
        self.job_id = job_id
        self.planed_time = planed_time
        self.real_ringing_duration = real_ringing_duration
        self.ringing_duration = ringing_duration
        self.scenario_id = scenario_id
        self.sip_code = sip_code
        self.sip_duration = sip_duration
        self.status = status
        self.task_id = task_id

    def validate(self):
        if self.contact:
            self.contact.validate()
        if self.conversation:
            for v1 in self.conversation:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.actual_time is not None:
            result['ActualTime'] = self.actual_time

        if self.brief is not None:
            result['Brief'] = self.brief

        if self.call_id is not None:
            result['CallId'] = self.call_id

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id

        if self.contact is not None:
            result['Contact'] = self.contact.to_map()

        result['Conversation'] = []
        if self.conversation is not None:
            for k1 in self.conversation:
                result['Conversation'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_reason is not None:
            result['EndReason'] = self.end_reason

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.hang_up_direction is not None:
            result['HangUpDirection'] = self.hang_up_direction

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.planed_time is not None:
            result['PlanedTime'] = self.planed_time

        if self.real_ringing_duration is not None:
            result['RealRingingDuration'] = self.real_ringing_duration

        if self.ringing_duration is not None:
            result['RingingDuration'] = self.ringing_duration

        if self.scenario_id is not None:
            result['ScenarioId'] = self.scenario_id

        if self.sip_code is not None:
            result['SipCode'] = self.sip_code

        if self.sip_duration is not None:
            result['SipDuration'] = self.sip_duration

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActualTime') is not None:
            self.actual_time = m.get('ActualTime')

        if m.get('Brief') is not None:
            self.brief = m.get('Brief')

        if m.get('CallId') is not None:
            self.call_id = m.get('CallId')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('Contact') is not None:
            temp_model = main_models.DescribeJobResponseBodyJobTasksContact()
            self.contact = temp_model.from_map(m.get('Contact'))

        self.conversation = []
        if m.get('Conversation') is not None:
            for k1 in m.get('Conversation'):
                temp_model = main_models.DescribeJobResponseBodyJobTasksConversation()
                self.conversation.append(temp_model.from_map(k1))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndReason') is not None:
            self.end_reason = m.get('EndReason')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('HangUpDirection') is not None:
            self.hang_up_direction = m.get('HangUpDirection')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PlanedTime') is not None:
            self.planed_time = m.get('PlanedTime')

        if m.get('RealRingingDuration') is not None:
            self.real_ringing_duration = m.get('RealRingingDuration')

        if m.get('RingingDuration') is not None:
            self.ringing_duration = m.get('RingingDuration')

        if m.get('ScenarioId') is not None:
            self.scenario_id = m.get('ScenarioId')

        if m.get('SipCode') is not None:
            self.sip_code = m.get('SipCode')

        if m.get('SipDuration') is not None:
            self.sip_duration = m.get('SipDuration')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class DescribeJobResponseBodyJobTasksConversation(DaraModel):
    def __init__(
        self,
        action: str = None,
        action_params: str = None,
        script: str = None,
        sequence_id: str = None,
        speaker: str = None,
        summary: List[main_models.DescribeJobResponseBodyJobTasksConversationSummary] = None,
        timestamp: int = None,
    ):
        self.action = action
        self.action_params = action_params
        self.script = script
        self.sequence_id = sequence_id
        self.speaker = speaker
        self.summary = summary
        self.timestamp = timestamp

    def validate(self):
        if self.summary:
            for v1 in self.summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.action_params is not None:
            result['ActionParams'] = self.action_params

        if self.script is not None:
            result['Script'] = self.script

        if self.sequence_id is not None:
            result['SequenceId'] = self.sequence_id

        if self.speaker is not None:
            result['Speaker'] = self.speaker

        result['Summary'] = []
        if self.summary is not None:
            for k1 in self.summary:
                result['Summary'].append(k1.to_map() if k1 else None)

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ActionParams') is not None:
            self.action_params = m.get('ActionParams')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        if m.get('SequenceId') is not None:
            self.sequence_id = m.get('SequenceId')

        if m.get('Speaker') is not None:
            self.speaker = m.get('Speaker')

        self.summary = []
        if m.get('Summary') is not None:
            for k1 in m.get('Summary'):
                temp_model = main_models.DescribeJobResponseBodyJobTasksConversationSummary()
                self.summary.append(temp_model.from_map(k1))

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        return self

class DescribeJobResponseBodyJobTasksConversationSummary(DaraModel):
    def __init__(
        self,
        category: str = None,
        content: str = None,
        summary_name: str = None,
    ):
        self.category = category
        self.content = content
        self.summary_name = summary_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.content is not None:
            result['Content'] = self.content

        if self.summary_name is not None:
            result['SummaryName'] = self.summary_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')

        return self

class DescribeJobResponseBodyJobTasksContact(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        contact_name: str = None,
        honorific: str = None,
        job_id: str = None,
        phone_number: str = None,
        reference_id: str = None,
        role: str = None,
        state: str = None,
    ):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.honorific = honorific
        self.job_id = job_id
        self.phone_number = phone_number
        self.reference_id = reference_id
        self.role = role
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.honorific is not None:
            result['Honorific'] = self.honorific

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.role is not None:
            result['Role'] = self.role

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeJobResponseBodyJobSummary(DaraModel):
    def __init__(
        self,
        category: str = None,
        content: str = None,
        summary_name: str = None,
    ):
        self.category = category
        self.content = content
        self.summary_name = summary_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.content is not None:
            result['Content'] = self.content

        if self.summary_name is not None:
            result['SummaryName'] = self.summary_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('SummaryName') is not None:
            self.summary_name = m.get('SummaryName')

        return self

class DescribeJobResponseBodyJobScript(DaraModel):
    def __init__(
        self,
        asr_config: str = None,
        chatbot_id: str = None,
        debug_status: str = None,
        industry: str = None,
        is_debug_drafted: bool = None,
        is_drafted: bool = None,
        mini_playback_config_enabled: bool = None,
        name: str = None,
        scene: str = None,
        script_description: str = None,
        script_id: str = None,
        status: str = None,
        tts_config: str = None,
        update_time: int = None,
    ):
        self.asr_config = asr_config
        self.chatbot_id = chatbot_id
        self.debug_status = debug_status
        self.industry = industry
        self.is_debug_drafted = is_debug_drafted
        self.is_drafted = is_drafted
        self.mini_playback_config_enabled = mini_playback_config_enabled
        self.name = name
        self.scene = scene
        self.script_description = script_description
        self.script_id = script_id
        self.status = status
        self.tts_config = tts_config
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_config is not None:
            result['AsrConfig'] = self.asr_config

        if self.chatbot_id is not None:
            result['ChatbotId'] = self.chatbot_id

        if self.debug_status is not None:
            result['DebugStatus'] = self.debug_status

        if self.industry is not None:
            result['Industry'] = self.industry

        if self.is_debug_drafted is not None:
            result['IsDebugDrafted'] = self.is_debug_drafted

        if self.is_drafted is not None:
            result['IsDrafted'] = self.is_drafted

        if self.mini_playback_config_enabled is not None:
            result['MiniPlaybackConfigEnabled'] = self.mini_playback_config_enabled

        if self.name is not None:
            result['Name'] = self.name

        if self.scene is not None:
            result['Scene'] = self.scene

        if self.script_description is not None:
            result['ScriptDescription'] = self.script_description

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.status is not None:
            result['Status'] = self.status

        if self.tts_config is not None:
            result['TtsConfig'] = self.tts_config

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrConfig') is not None:
            self.asr_config = m.get('AsrConfig')

        if m.get('ChatbotId') is not None:
            self.chatbot_id = m.get('ChatbotId')

        if m.get('DebugStatus') is not None:
            self.debug_status = m.get('DebugStatus')

        if m.get('Industry') is not None:
            self.industry = m.get('Industry')

        if m.get('IsDebugDrafted') is not None:
            self.is_debug_drafted = m.get('IsDebugDrafted')

        if m.get('IsDrafted') is not None:
            self.is_drafted = m.get('IsDrafted')

        if m.get('MiniPlaybackConfigEnabled') is not None:
            self.mini_playback_config_enabled = m.get('MiniPlaybackConfigEnabled')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        if m.get('ScriptDescription') is not None:
            self.script_description = m.get('ScriptDescription')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TtsConfig') is not None:
            self.tts_config = m.get('TtsConfig')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DescribeJobResponseBodyJobExtras(DaraModel):
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

class DescribeJobResponseBodyJobContacts(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        contact_name: str = None,
        honorific: str = None,
        job_id: str = None,
        phone_number: str = None,
        reference_id: str = None,
        role: str = None,
        state: str = None,
    ):
        self.contact_id = contact_id
        self.contact_name = contact_name
        self.honorific = honorific
        self.job_id = job_id
        self.phone_number = phone_number
        self.reference_id = reference_id
        self.role = role
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.honorific is not None:
            result['Honorific'] = self.honorific

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.role is not None:
            result['Role'] = self.role

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Honorific') is not None:
            self.honorific = m.get('Honorific')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

