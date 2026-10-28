# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
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
    ):
        # The status code.
        self.code = code
        # The call detail record.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # A list of parameters related to the error.
        self.params = params
        # The ID of the request.
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

        if self.params is not None:
            result['Params'] = self.params

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

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCallDetailRecordResponseBodyData(DaraModel):
    def __init__(
        self,
        callee: str = None,
        caller: str = None,
        disposition_code: str = None,
        disposition_reason: str = None,
        duration: int = None,
        end_time: int = None,
        issue_resolved: bool = None,
        release_initiator: str = None,
        resolution_evidence: str = None,
        session_id: str = None,
        start_time: int = None,
        talk_time: int = None,
        talk_turns: int = None,
        transcripts: List[main_models.GetCallDetailRecordResponseBodyDataTranscripts] = None,
        transfer_target: str = None,
        transfer_type: str = None,
    ):
        # The phone number of the callee.
        self.callee = callee
        # The phone number of the caller.
        self.caller = caller
        # The disposition code for the call.
        self.disposition_code = disposition_code
        # The reason for the call\\"s disposition.
        self.disposition_reason = disposition_reason
        # The session duration, in seconds.
        self.duration = duration
        # The end time.
        self.end_time = end_time
        # Indicates whether the user\\"s issue was resolved.
        self.issue_resolved = issue_resolved
        # The party that ended the call.
        self.release_initiator = release_initiator
        # The basis for the resolution judgment.
        self.resolution_evidence = resolution_evidence
        # The session ID.
        self.session_id = session_id
        # The start time.
        self.start_time = start_time
        # The talk time, in seconds.
        self.talk_time = talk_time
        # The number of conversation turns.
        self.talk_turns = talk_turns
        # The conversation transcripts.
        self.transcripts = transcripts
        # The transfer target.
        self.transfer_target = transfer_target
        # The transfer type.
        self.transfer_type = transfer_type

    def validate(self):
        if self.transcripts:
            for v1 in self.transcripts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callee is not None:
            result['Callee'] = self.callee

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.disposition_code is not None:
            result['DispositionCode'] = self.disposition_code

        if self.disposition_reason is not None:
            result['DispositionReason'] = self.disposition_reason

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.issue_resolved is not None:
            result['IssueResolved'] = self.issue_resolved

        if self.release_initiator is not None:
            result['ReleaseInitiator'] = self.release_initiator

        if self.resolution_evidence is not None:
            result['ResolutionEvidence'] = self.resolution_evidence

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.talk_time is not None:
            result['TalkTime'] = self.talk_time

        if self.talk_turns is not None:
            result['TalkTurns'] = self.talk_turns

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
        if m.get('Callee') is not None:
            self.callee = m.get('Callee')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('DispositionCode') is not None:
            self.disposition_code = m.get('DispositionCode')

        if m.get('DispositionReason') is not None:
            self.disposition_reason = m.get('DispositionReason')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IssueResolved') is not None:
            self.issue_resolved = m.get('IssueResolved')

        if m.get('ReleaseInitiator') is not None:
            self.release_initiator = m.get('ReleaseInitiator')

        if m.get('ResolutionEvidence') is not None:
            self.resolution_evidence = m.get('ResolutionEvidence')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TalkTime') is not None:
            self.talk_time = m.get('TalkTime')

        if m.get('TalkTurns') is not None:
            self.talk_turns = m.get('TalkTurns')

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
        event_time: str = None,
        extras: str = None,
        interrupted: bool = None,
        legacy: bool = None,
        playback_status: str = None,
        played_answer: str = None,
        played_words: int = None,
        role: str = None,
        stream_end: bool = None,
        stream_id: str = None,
        utterance: str = None,
        vendor_params: str = None,
    ):
        # The bot\\"s response. This parameter is valid when `Role` is `ASSISTANT`.
        self.answer = answer
        # Indicates whether the user\\"s utterance is a backchannel (for example, "uh-huh" or "okay"). This parameter is valid when `Role` is `USER`.
        self.backchannels = backchannels
        # The start timestamp of the turn, in milliseconds since the Unix epoch.
        self.begin_time = begin_time
        # A list of control parameters. This parameter is valid when `Role` is `ASSISTANT`.
        self.control_params_list = control_params_list
        # The end timestamp of the turn, in milliseconds since the Unix epoch.
        self.end_time = end_time
        # The event timestamp, in milliseconds since the Unix epoch.
        self.event_time = event_time
        # Additional input from the user other than speech. This parameter is valid when `Role` is `USER`.
        self.extras = extras
        # Indicates whether the turn was interrupted.
        self.interrupted = interrupted
        # Indicates whether the bot\\"s response is obsolete. This parameter is valid when `Role` is `ASSISTANT`.
        self.legacy = legacy
        self.playback_status = playback_status
        self.played_answer = played_answer
        # The number of words played from the bot\\"s response. This parameter is valid when `Role` is `USER`.
        self.played_words = played_words
        # The role of the speaker.
        self.role = role
        # Indicates if this is the final part of a streamed response.
        self.stream_end = stream_end
        # The ID of the conversation turn.
        self.stream_id = stream_id
        # The user\\"s utterance. This parameter is valid when `Role` is `USER`.
        self.utterance = utterance
        # Vendor-specific data sent from the client. This parameter is valid when `Role` is `USER`.
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

        if self.interrupted is not None:
            result['Interrupted'] = self.interrupted

        if self.legacy is not None:
            result['Legacy'] = self.legacy

        if self.playback_status is not None:
            result['PlaybackStatus'] = self.playback_status

        if self.played_answer is not None:
            result['PlayedAnswer'] = self.played_answer

        if self.played_words is not None:
            result['PlayedWords'] = self.played_words

        if self.role is not None:
            result['Role'] = self.role

        if self.stream_end is not None:
            result['StreamEnd'] = self.stream_end

        if self.stream_id is not None:
            result['StreamId'] = self.stream_id

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

        if m.get('Interrupted') is not None:
            self.interrupted = m.get('Interrupted')

        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')

        if m.get('PlaybackStatus') is not None:
            self.playback_status = m.get('PlaybackStatus')

        if m.get('PlayedAnswer') is not None:
            self.played_answer = m.get('PlayedAnswer')

        if m.get('PlayedWords') is not None:
            self.played_words = m.get('PlayedWords')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('StreamEnd') is not None:
            self.stream_end = m.get('StreamEnd')

        if m.get('StreamId') is not None:
            self.stream_id = m.get('StreamId')

        if m.get('Utterance') is not None:
            self.utterance = m.get('Utterance')

        if m.get('VendorParams') is not None:
            self.vendor_params = m.get('VendorParams')

        return self

