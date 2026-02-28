# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ccc20200701 import models as main_models
from darabonba.model import DaraModel

class ListCallDetailRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCallDetailRecordsResponseBodyData = None,
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
            temp_model = main_models.ListCallDetailRecordsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCallDetailRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListCallDetailRecordsResponseBodyDataList] = None,
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
                temp_model = main_models.ListCallDetailRecordsResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCallDetailRecordsResponseBodyDataList(DaraModel):
    def __init__(
        self,
        additional_broker: str = None,
        agent_ids: str = None,
        agent_names: str = None,
        broker: str = None,
        call_duration: str = None,
        call_ids: str = None,
        called_number: str = None,
        callee_location: str = None,
        caller_location: str = None,
        calling_number: str = None,
        contact_disposition: str = None,
        contact_id: str = None,
        contact_type: str = None,
        dialing_time: int = None,
        early_media_state: str = None,
        established_time: int = None,
        held_time: int = None,
        instance_id: str = None,
        ivr_time: int = None,
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
        talk_time: int = None,
        wait_time: int = None,
    ):
        self.additional_broker = additional_broker
        self.agent_ids = agent_ids
        self.agent_names = agent_names
        self.broker = broker
        self.call_duration = call_duration
        self.call_ids = call_ids
        self.called_number = called_number
        self.callee_location = callee_location
        self.caller_location = caller_location
        self.calling_number = calling_number
        self.contact_disposition = contact_disposition
        self.contact_id = contact_id
        self.contact_type = contact_type
        self.dialing_time = dialing_time
        self.early_media_state = early_media_state
        self.established_time = established_time
        self.held_time = held_time
        self.instance_id = instance_id
        self.ivr_time = ivr_time
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
        self.talk_time = talk_time
        self.wait_time = wait_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.additional_broker is not None:
            result['AdditionalBroker'] = self.additional_broker

        if self.agent_ids is not None:
            result['AgentIds'] = self.agent_ids

        if self.agent_names is not None:
            result['AgentNames'] = self.agent_names

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

        if self.established_time is not None:
            result['EstablishedTime'] = self.established_time

        if self.held_time is not None:
            result['HeldTime'] = self.held_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ivr_time is not None:
            result['IvrTime'] = self.ivr_time

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

        if self.talk_time is not None:
            result['TalkTime'] = self.talk_time

        if self.wait_time is not None:
            result['WaitTime'] = self.wait_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdditionalBroker') is not None:
            self.additional_broker = m.get('AdditionalBroker')

        if m.get('AgentIds') is not None:
            self.agent_ids = m.get('AgentIds')

        if m.get('AgentNames') is not None:
            self.agent_names = m.get('AgentNames')

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

        if m.get('EstablishedTime') is not None:
            self.established_time = m.get('EstablishedTime')

        if m.get('HeldTime') is not None:
            self.held_time = m.get('HeldTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IvrTime') is not None:
            self.ivr_time = m.get('IvrTime')

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

        if m.get('TalkTime') is not None:
            self.talk_time = m.get('TalkTime')

        if m.get('WaitTime') is not None:
            self.wait_time = m.get('WaitTime')

        return self

