# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListCallDetailRecordsV2ResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCallDetailRecordsV2ResponseBodyData = None,
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
            temp_model = main_models.ListCallDetailRecordsV2ResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCallDetailRecordsV2ResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListCallDetailRecordsV2ResponseBodyDataList] = None,
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
            for v1 in self.list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['List'] = []
        if self.list is not None:
            for k1 in self.list:
                result['List'].append(k1.to_map() if k1 else None)

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
            for k1 in m.get('List'):
                temp_model = main_models.ListCallDetailRecordsV2ResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCallDetailRecordsV2ResponseBodyDataList(DaraModel):
    def __init__(
        self,
        access_channel_name: str = None,
        access_channel_type: str = None,
        access_channel_user_id: str = None,
        access_channel_user_name: str = None,
        additional_broker: str = None,
        agent_ids: str = None,
        agent_names: str = None,
        analytics_report: main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReport = None,
        analytics_report_ready: bool = None,
        broker: str = None,
        call_duration: str = None,
        call_ids: str = None,
        called_number: str = None,
        callee_location: str = None,
        caller_location: str = None,
        calling_number: str = None,
        client_app_name: str = None,
        client_ip_address: str = None,
        client_location: str = None,
        client_user_agent: str = None,
        contact_disposition: str = None,
        contact_id: str = None,
        contact_type: str = None,
        dialing_time: int = None,
        early_media_state: str = None,
        early_media_text: str = None,
        established_time: int = None,
        first_response_time: int = None,
        held_time: int = None,
        instance_id: str = None,
        ivr_time: int = None,
        media_type: str = None,
        messages_sent: int = None,
        messages_sent_by_agent: int = None,
        messages_sent_by_customer: int = None,
        off_site_agent_ids: str = None,
        offsite_agent_destination_numbers: str = None,
        offsite_agent_originator_numbers: str = None,
        offsite_agent_release_reason: str = None,
        outside_number_release_reason: str = None,
        queue_time: int = None,
        recording_duration: int = None,
        recording_ready: bool = None,
        release_initiator: str = None,
        release_reason: str = None,
        release_time: int = None,
        ring_time: int = None,
        satisfaction_description: str = None,
        satisfaction_index: int = None,
        satisfaction_survey_channel: str = None,
        satisfaction_survey_offered: bool = None,
        skill_group_ids: str = None,
        skill_group_names: str = None,
        start_time: int = None,
        summary_index: main_models.ListCallDetailRecordsV2ResponseBodyDataListSummaryIndex = None,
        talk_time: int = None,
        transfer_count: int = None,
        voicebot_destination_number: str = None,
        voicebot_originator_number: str = None,
        wait_time: int = None,
    ):
        self.access_channel_name = access_channel_name
        self.access_channel_type = access_channel_type
        self.access_channel_user_id = access_channel_user_id
        self.access_channel_user_name = access_channel_user_name
        self.additional_broker = additional_broker
        self.agent_ids = agent_ids
        self.agent_names = agent_names
        self.analytics_report = analytics_report
        self.analytics_report_ready = analytics_report_ready
        self.broker = broker
        self.call_duration = call_duration
        self.call_ids = call_ids
        self.called_number = called_number
        self.callee_location = callee_location
        self.caller_location = caller_location
        self.calling_number = calling_number
        self.client_app_name = client_app_name
        self.client_ip_address = client_ip_address
        self.client_location = client_location
        self.client_user_agent = client_user_agent
        self.contact_disposition = contact_disposition
        self.contact_id = contact_id
        self.contact_type = contact_type
        self.dialing_time = dialing_time
        self.early_media_state = early_media_state
        self.early_media_text = early_media_text
        self.established_time = established_time
        self.first_response_time = first_response_time
        self.held_time = held_time
        self.instance_id = instance_id
        self.ivr_time = ivr_time
        self.media_type = media_type
        self.messages_sent = messages_sent
        self.messages_sent_by_agent = messages_sent_by_agent
        self.messages_sent_by_customer = messages_sent_by_customer
        self.off_site_agent_ids = off_site_agent_ids
        self.offsite_agent_destination_numbers = offsite_agent_destination_numbers
        self.offsite_agent_originator_numbers = offsite_agent_originator_numbers
        self.offsite_agent_release_reason = offsite_agent_release_reason
        self.outside_number_release_reason = outside_number_release_reason
        self.queue_time = queue_time
        self.recording_duration = recording_duration
        self.recording_ready = recording_ready
        self.release_initiator = release_initiator
        self.release_reason = release_reason
        self.release_time = release_time
        self.ring_time = ring_time
        self.satisfaction_description = satisfaction_description
        self.satisfaction_index = satisfaction_index
        self.satisfaction_survey_channel = satisfaction_survey_channel
        self.satisfaction_survey_offered = satisfaction_survey_offered
        self.skill_group_ids = skill_group_ids
        self.skill_group_names = skill_group_names
        self.start_time = start_time
        self.summary_index = summary_index
        self.talk_time = talk_time
        self.transfer_count = transfer_count
        self.voicebot_destination_number = voicebot_destination_number
        self.voicebot_originator_number = voicebot_originator_number
        self.wait_time = wait_time

    def validate(self):
        if self.analytics_report:
            self.analytics_report.validate()
        if self.summary_index:
            self.summary_index.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_name is not None:
            result['AccessChannelName'] = self.access_channel_name

        if self.access_channel_type is not None:
            result['AccessChannelType'] = self.access_channel_type

        if self.access_channel_user_id is not None:
            result['AccessChannelUserId'] = self.access_channel_user_id

        if self.access_channel_user_name is not None:
            result['AccessChannelUserName'] = self.access_channel_user_name

        if self.additional_broker is not None:
            result['AdditionalBroker'] = self.additional_broker

        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids

        if self.agent_names is not None:
            result['AgentNames'] = self.agent_names

        if self.analytics_report is not None:
            result['AnalyticsReport'] = self.analytics_report.to_map()

        if self.analytics_report_ready is not None:
            result['AnalyticsReportReady'] = self.analytics_report_ready

        if self.broker is not None:
            result['Broker'] = self.broker

        if self.call_duration is not None:
            result['CallDuration'] = self.call_duration

        if self.call_ids is not None:
            result['CallIds'] = self.call_ids

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.callee_location is not None:
            result['CalleeLocation'] = self.callee_location

        if self.caller_location is not None:
            result['CallerLocation'] = self.caller_location

        if self.calling_number is not None:
            result['CallingNumber'] = self.calling_number

        if self.client_app_name is not None:
            result['ClientAppName'] = self.client_app_name

        if self.client_ip_address is not None:
            result['ClientIpAddress'] = self.client_ip_address

        if self.client_location is not None:
            result['ClientLocation'] = self.client_location

        if self.client_user_agent is not None:
            result['ClientUserAgent'] = self.client_user_agent

        if self.contact_disposition is not None:
            result['ContactDisposition'] = self.contact_disposition

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_type is not None:
            result['ContactType'] = self.contact_type

        if self.dialing_time is not None:
            result['DialingTime'] = self.dialing_time

        if self.early_media_state is not None:
            result['EarlyMediaState'] = self.early_media_state

        if self.early_media_text is not None:
            result['EarlyMediaText'] = self.early_media_text

        if self.established_time is not None:
            result['EstablishedTime'] = self.established_time

        if self.first_response_time is not None:
            result['FirstResponseTime'] = self.first_response_time

        if self.held_time is not None:
            result['HeldTime'] = self.held_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ivr_time is not None:
            result['IvrTime'] = self.ivr_time

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.messages_sent is not None:
            result['MessagesSent'] = self.messages_sent

        if self.messages_sent_by_agent is not None:
            result['MessagesSentByAgent'] = self.messages_sent_by_agent

        if self.messages_sent_by_customer is not None:
            result['MessagesSentByCustomer'] = self.messages_sent_by_customer

        if self.off_site_agent_ids is not None:
            result['OffSiteAgentIds'] = self.off_site_agent_ids

        if self.offsite_agent_destination_numbers is not None:
            result['OffsiteAgentDestinationNumbers'] = self.offsite_agent_destination_numbers

        if self.offsite_agent_originator_numbers is not None:
            result['OffsiteAgentOriginatorNumbers'] = self.offsite_agent_originator_numbers

        if self.offsite_agent_release_reason is not None:
            result['OffsiteAgentReleaseReason'] = self.offsite_agent_release_reason

        if self.outside_number_release_reason is not None:
            result['OutsideNumberReleaseReason'] = self.outside_number_release_reason

        if self.queue_time is not None:
            result['QueueTime'] = self.queue_time

        if self.recording_duration is not None:
            result['RecordingDuration'] = self.recording_duration

        if self.recording_ready is not None:
            result['RecordingReady'] = self.recording_ready

        if self.release_initiator is not None:
            result['ReleaseInitiator'] = self.release_initiator

        if self.release_reason is not None:
            result['ReleaseReason'] = self.release_reason

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.ring_time is not None:
            result['RingTime'] = self.ring_time

        if self.satisfaction_description is not None:
            result['SatisfactionDescription'] = self.satisfaction_description

        if self.satisfaction_index is not None:
            result['SatisfactionIndex'] = self.satisfaction_index

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

        if self.summary_index is not None:
            result['SummaryIndex'] = self.summary_index.to_map()

        if self.talk_time is not None:
            result['TalkTime'] = self.talk_time

        if self.transfer_count is not None:
            result['TransferCount'] = self.transfer_count

        if self.voicebot_destination_number is not None:
            result['VoicebotDestinationNumber'] = self.voicebot_destination_number

        if self.voicebot_originator_number is not None:
            result['VoicebotOriginatorNumber'] = self.voicebot_originator_number

        if self.wait_time is not None:
            result['WaitTime'] = self.wait_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelName') is not None:
            self.access_channel_name = m.get('AccessChannelName')

        if m.get('AccessChannelType') is not None:
            self.access_channel_type = m.get('AccessChannelType')

        if m.get('AccessChannelUserId') is not None:
            self.access_channel_user_id = m.get('AccessChannelUserId')

        if m.get('AccessChannelUserName') is not None:
            self.access_channel_user_name = m.get('AccessChannelUserName')

        if m.get('AdditionalBroker') is not None:
            self.additional_broker = m.get('AdditionalBroker')

        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')

        if m.get('AgentNames') is not None:
            self.agent_names = m.get('AgentNames')

        if m.get('AnalyticsReport') is not None:
            temp_model = main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReport()
            self.analytics_report = temp_model.from_map(m.get('AnalyticsReport'))

        if m.get('AnalyticsReportReady') is not None:
            self.analytics_report_ready = m.get('AnalyticsReportReady')

        if m.get('Broker') is not None:
            self.broker = m.get('Broker')

        if m.get('CallDuration') is not None:
            self.call_duration = m.get('CallDuration')

        if m.get('CallIds') is not None:
            self.call_ids = m.get('CallIds')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CalleeLocation') is not None:
            self.callee_location = m.get('CalleeLocation')

        if m.get('CallerLocation') is not None:
            self.caller_location = m.get('CallerLocation')

        if m.get('CallingNumber') is not None:
            self.calling_number = m.get('CallingNumber')

        if m.get('ClientAppName') is not None:
            self.client_app_name = m.get('ClientAppName')

        if m.get('ClientIpAddress') is not None:
            self.client_ip_address = m.get('ClientIpAddress')

        if m.get('ClientLocation') is not None:
            self.client_location = m.get('ClientLocation')

        if m.get('ClientUserAgent') is not None:
            self.client_user_agent = m.get('ClientUserAgent')

        if m.get('ContactDisposition') is not None:
            self.contact_disposition = m.get('ContactDisposition')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactType') is not None:
            self.contact_type = m.get('ContactType')

        if m.get('DialingTime') is not None:
            self.dialing_time = m.get('DialingTime')

        if m.get('EarlyMediaState') is not None:
            self.early_media_state = m.get('EarlyMediaState')

        if m.get('EarlyMediaText') is not None:
            self.early_media_text = m.get('EarlyMediaText')

        if m.get('EstablishedTime') is not None:
            self.established_time = m.get('EstablishedTime')

        if m.get('FirstResponseTime') is not None:
            self.first_response_time = m.get('FirstResponseTime')

        if m.get('HeldTime') is not None:
            self.held_time = m.get('HeldTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IvrTime') is not None:
            self.ivr_time = m.get('IvrTime')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('MessagesSent') is not None:
            self.messages_sent = m.get('MessagesSent')

        if m.get('MessagesSentByAgent') is not None:
            self.messages_sent_by_agent = m.get('MessagesSentByAgent')

        if m.get('MessagesSentByCustomer') is not None:
            self.messages_sent_by_customer = m.get('MessagesSentByCustomer')

        if m.get('OffSiteAgentIds') is not None:
            self.off_site_agent_ids = m.get('OffSiteAgentIds')

        if m.get('OffsiteAgentDestinationNumbers') is not None:
            self.offsite_agent_destination_numbers = m.get('OffsiteAgentDestinationNumbers')

        if m.get('OffsiteAgentOriginatorNumbers') is not None:
            self.offsite_agent_originator_numbers = m.get('OffsiteAgentOriginatorNumbers')

        if m.get('OffsiteAgentReleaseReason') is not None:
            self.offsite_agent_release_reason = m.get('OffsiteAgentReleaseReason')

        if m.get('OutsideNumberReleaseReason') is not None:
            self.outside_number_release_reason = m.get('OutsideNumberReleaseReason')

        if m.get('QueueTime') is not None:
            self.queue_time = m.get('QueueTime')

        if m.get('RecordingDuration') is not None:
            self.recording_duration = m.get('RecordingDuration')

        if m.get('RecordingReady') is not None:
            self.recording_ready = m.get('RecordingReady')

        if m.get('ReleaseInitiator') is not None:
            self.release_initiator = m.get('ReleaseInitiator')

        if m.get('ReleaseReason') is not None:
            self.release_reason = m.get('ReleaseReason')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('RingTime') is not None:
            self.ring_time = m.get('RingTime')

        if m.get('SatisfactionDescription') is not None:
            self.satisfaction_description = m.get('SatisfactionDescription')

        if m.get('SatisfactionIndex') is not None:
            self.satisfaction_index = m.get('SatisfactionIndex')

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

        if m.get('SummaryIndex') is not None:
            temp_model = main_models.ListCallDetailRecordsV2ResponseBodyDataListSummaryIndex()
            self.summary_index = temp_model.from_map(m.get('SummaryIndex'))

        if m.get('TalkTime') is not None:
            self.talk_time = m.get('TalkTime')

        if m.get('TransferCount') is not None:
            self.transfer_count = m.get('TransferCount')

        if m.get('VoicebotDestinationNumber') is not None:
            self.voicebot_destination_number = m.get('VoicebotDestinationNumber')

        if m.get('VoicebotOriginatorNumber') is not None:
            self.voicebot_originator_number = m.get('VoicebotOriginatorNumber')

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

class ListCallDetailRecordsV2ResponseBodyDataListSummaryIndex(DaraModel):
    def __init__(
        self,
        keywords: str = None,
    ):
        self.keywords = keywords

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keywords is not None:
            result['Keywords'] = self.keywords

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')

        return self

class ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReport(DaraModel):
    def __init__(
        self,
        emotion: main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportEmotion = None,
        problem_solving: main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportProblemSolving = None,
        satisfaction: main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportSatisfaction = None,
        todo_list: main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportTodoList = None,
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
            temp_model = main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportEmotion()
            self.emotion = temp_model.from_map(m.get('Emotion'))

        if m.get('ProblemSolving') is not None:
            temp_model = main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportProblemSolving()
            self.problem_solving = temp_model.from_map(m.get('ProblemSolving'))

        if m.get('Satisfaction') is not None:
            temp_model = main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportSatisfaction()
            self.satisfaction = temp_model.from_map(m.get('Satisfaction'))

        if m.get('TodoList') is not None:
            temp_model = main_models.ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportTodoList()
            self.todo_list = temp_model.from_map(m.get('TodoList'))

        return self

class ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportTodoList(DaraModel):
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

class ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportSatisfaction(DaraModel):
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

class ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportProblemSolving(DaraModel):
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

class ListCallDetailRecordsV2ResponseBodyDataListAnalyticsReportEmotion(DaraModel):
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

