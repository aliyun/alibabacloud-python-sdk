# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class GetCallDetailRecordResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCallDetailRecordResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The call detail data.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The pass-through parameters.
        self.params = params
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

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

        if self.params is not None:
            result['Params'] = self.params

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

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

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetCallDetailRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        access_channel_type: str = None,
        callee: str = None,
        caller: str = None,
        case_id: str = None,
        disposition_code: str = None,
        disposition_reason: str = None,
        draft_version: bool = None,
        duration: int = None,
        end_time: int = None,
        labels: List[main_models.GetCallDetailRecordResponseBodyDataLabels] = None,
        release_initiator: str = None,
        session_id: str = None,
        start_time: int = None,
        talk_time: int = None,
        talk_turns: int = None,
        task_completed: bool = None,
        transcripts: List[main_models.GetCallDetailRecordResponseBodyDataTranscripts] = None,
        transfer_target: str = None,
        transfer_type: str = None,
    ):
        # The access channel ID.
        self.access_channel_id = access_channel_id
        # The access channel type.
        self.access_channel_type = access_channel_type
        # The callee number.
        self.callee = callee
        # The caller number.
        self.caller = caller
        # The case ID.
        self.case_id = case_id
        # The disposition code.
        self.disposition_code = disposition_code
        # The disposition reason.
        self.disposition_reason = disposition_reason
        # Indicates whether this is a draft version.
        self.draft_version = draft_version
        # The total duration.
        self.duration = duration
        # The end time of the call.
        self.end_time = end_time
        # The list of labels.
        self.labels = labels
        # The party that initiated the hang-up.
        self.release_initiator = release_initiator
        # The call session ID.
        self.session_id = session_id
        # The start time of the call.
        self.start_time = start_time
        # The talk time.
        self.talk_time = talk_time
        # The number of conversation turns.
        self.talk_turns = talk_turns
        # Indicates whether the task was completed.
        self.task_completed = task_completed
        # The conversation transcripts.
        self.transcripts = transcripts
        # The transfer target.
        self.transfer_target = transfer_target
        # The transfer type.
        self.transfer_type = transfer_type

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.transcripts:
            for v1 in self.transcripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_channel_id is not None:
            result['AccessChannelId'] = self.access_channel_id

        if self.access_channel_type is not None:
            result['AccessChannelType'] = self.access_channel_type

        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.disposition_code is not None:
            result['DispositionCode'] = self.disposition_code

        if self.disposition_reason is not None:
            result['DispositionReason'] = self.disposition_reason

        if self.draft_version is not None:
            result['DraftVersion'] = self.draft_version

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.release_initiator is not None:
            result['ReleaseInitiator'] = self.release_initiator

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.talk_time is not None:
            result['TalkTime'] = self.talk_time

        if self.talk_turns is not None:
            result['TalkTurns'] = self.talk_turns

        if self.task_completed is not None:
            result['TaskCompleted'] = self.task_completed

        result['Transcripts'] = []
        if self.transcripts is not None:
            for k1 in self.transcripts:
                result['Transcripts'].append(k1.to_map() if k1 else None)

        if self.transfer_target is not None:
            result['TransferTarget'] = self.transfer_target

        if self.transfer_type is not None:
            result['TransferType'] = self.transfer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessChannelId') is not None:
            self.access_channel_id = m.get('AccessChannelId')

        if m.get('AccessChannelType') is not None:
            self.access_channel_type = m.get('AccessChannelType')

        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('DispositionCode') is not None:
            self.disposition_code = m.get('DispositionCode')

        if m.get('DispositionReason') is not None:
            self.disposition_reason = m.get('DispositionReason')

        if m.get('DraftVersion') is not None:
            self.draft_version = m.get('DraftVersion')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('ReleaseInitiator') is not None:
            self.release_initiator = m.get('ReleaseInitiator')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TalkTime') is not None:
            self.talk_time = m.get('TalkTime')

        if m.get('TalkTurns') is not None:
            self.talk_turns = m.get('TalkTurns')

        if m.get('TaskCompleted') is not None:
            self.task_completed = m.get('TaskCompleted')

        self.transcripts = []
        if m.get('Transcripts') is not None:
            for k1 in m.get('Transcripts'):
                temp_model = main_models.GetCallDetailRecordResponseBodyDataTranscripts()
                self.transcripts.append(temp_model.from_map(k1))

        if m.get('TransferTarget') is not None:
            self.transfer_target = m.get('TransferTarget')

        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')

        return self

class GetCallDetailRecordResponseBodyDataTranscripts(DaraModel):
    def __init__(
        self,
        answer: str = None,
        backchannels: bool = None,
        begin_time: int = None,
        control_params_list: str = None,
        end_time: int = None,
        event_time: int = None,
        extras: str = None,
        input_tokens: int = None,
        interrupted: bool = None,
        legacy: bool = None,
        model: str = None,
        output_tokens: int = None,
        played_words: str = None,
        role: str = None,
        session_id: str = None,
        stream_id: str = None,
        total_tokens: int = None,
        utterance: str = None,
        vendor_params: str = None,
    ):
        # The assistant answer.
        self.answer = answer
        # Indicates whether the transcript is a backchannel response.
        self.backchannels = backchannels
        # The begin time.
        self.begin_time = begin_time
        # The list of control parameters.
        self.control_params_list = control_params_list
        # The end time of the call.
        self.end_time = end_time
        # The event time.
        self.event_time = event_time
        # The extended information.
        self.extras = extras
        # The number of input tokens.
        self.input_tokens = input_tokens
        # Indicates whether the response was interrupted.
        self.interrupted = interrupted
        # Indicates whether the transcript is from the legacy version.
        self.legacy = legacy
        # The model.
        self.model = model
        # The number of output tokens.
        self.output_tokens = output_tokens
        # The played text.
        self.played_words = played_words
        # The role.
        self.role = role
        # The call session ID.
        self.session_id = session_id
        # The stream ID.
        self.stream_id = stream_id
        # The total number of tokens.
        self.total_tokens = total_tokens
        # The user utterance.
        self.utterance = utterance
        # The vendor parameters.
        self.vendor_params = vendor_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.backchannels is not None:
            result['Backchannels'] = self.backchannels

        if self.begin_time is not None:
            result['BeginTime'] = self.begin_time

        if self.control_params_list is not None:
            result['ControlParamsList'] = self.control_params_list

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_time is not None:
            result['EventTime'] = self.event_time

        if self.extras is not None:
            result['Extras'] = self.extras

        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.interrupted is not None:
            result['Interrupted'] = self.interrupted

        if self.legacy is not None:
            result['Legacy'] = self.legacy

        if self.model is not None:
            result['Model'] = self.model

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.played_words is not None:
            result['PlayedWords'] = self.played_words

        if self.role is not None:
            result['Role'] = self.role

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.stream_id is not None:
            result['StreamId'] = self.stream_id

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        if self.utterance is not None:
            result['Utterance'] = self.utterance

        if self.vendor_params is not None:
            result['VendorParams'] = self.vendor_params

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('Backchannels') is not None:
            self.backchannels = m.get('Backchannels')

        if m.get('BeginTime') is not None:
            self.begin_time = m.get('BeginTime')

        if m.get('ControlParamsList') is not None:
            self.control_params_list = m.get('ControlParamsList')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventTime') is not None:
            self.event_time = m.get('EventTime')

        if m.get('Extras') is not None:
            self.extras = m.get('Extras')

        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('Interrupted') is not None:
            self.interrupted = m.get('Interrupted')

        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('PlayedWords') is not None:
            self.played_words = m.get('PlayedWords')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        if m.get('VendorParams') is not None:
            self.vendor_params = m.get('VendorParams')

        return self

class GetCallDetailRecordResponseBodyDataLabels(DaraModel):
    def __init__(
        self,
        candidate_values: List[str] = None,
        collected: bool = None,
        description: str = None,
        matched_value: str = None,
        name: str = None,
        system: bool = None,
    ):
        # The set of preset values for the label.
        self.candidate_values = candidate_values
        # Indicates whether the label has been collected.
        self.collected = collected
        # The label description.
        self.description = description
        # The matched value.
        self.matched_value = matched_value
        # The label name.
        self.name = name
        # Indicates whether the label is a system label.
        self.system = system

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.candidate_values is not None:
            result['CandidateValues'] = self.candidate_values

        if self.collected is not None:
            result['Collected'] = self.collected

        if self.description is not None:
            result['Description'] = self.description

        if self.matched_value is not None:
            result['MatchedValue'] = self.matched_value

        if self.name is not None:
            result['Name'] = self.name

        if self.system is not None:
            result['System'] = self.system

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CandidateValues') is not None:
            self.candidate_values = m.get('CandidateValues')

        if m.get('Collected') is not None:
            self.collected = m.get('Collected')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MatchedValue') is not None:
            self.matched_value = m.get('MatchedValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('System') is not None:
            self.system = m.get('System')

        return self

