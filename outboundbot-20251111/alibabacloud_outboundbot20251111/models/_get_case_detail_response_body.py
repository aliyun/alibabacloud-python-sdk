# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class GetCaseDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetCaseDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The case details data.
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
            temp_model = main_models.GetCaseDetailResponseBodyData()
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

class GetCaseDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        call_detail_records: List[main_models.GetCaseDetailResponseBodyDataCallDetailRecords] = None,
        case: main_models.GetCaseDetailResponseBodyDataCase = None,
    ):
        # The list of associated call detail records.
        self.call_detail_records = call_detail_records
        # The case information.
        self.case = case

    def validate(self):
        if self.call_detail_records:
            for v1 in self.call_detail_records:
                 if v1:
                    v1.validate()
        if self.case:
            self.case.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallDetailRecords'] = []
        if self.call_detail_records is not None:
            for k1 in self.call_detail_records:
                result['CallDetailRecords'].append(k1.to_map() if k1 else None)

        if self.case is not None:
            result['Case'] = self.case.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_detail_records = []
        if m.get('CallDetailRecords') is not None:
            for k1 in m.get('CallDetailRecords'):
                temp_model = main_models.GetCaseDetailResponseBodyDataCallDetailRecords()
                self.call_detail_records.append(temp_model.from_map(k1))

        if m.get('Case') is not None:
            temp_model = main_models.GetCaseDetailResponseBodyDataCase()
            self.case = temp_model.from_map(m.get('Case'))

        return self

class GetCaseDetailResponseBodyDataCase(DaraModel):
    def __init__(
        self,
        attempted_count: int = None,
        caller_number: str = None,
        campaign_id: str = None,
        campaign_name: str = None,
        case_id: str = None,
        created_time: int = None,
        custom_variables: str = None,
        dialing_time: int = None,
        disposition_code: str = None,
        disposition_reason: str = None,
        instance_id: str = None,
        labels: List[main_models.GetCaseDetailResponseBodyDataCaseLabels] = None,
        last_attempted_time: int = None,
        phone_number: str = None,
        priority: int = None,
        reference_id: str = None,
        ringing_duration: int = None,
        ringing_time: int = None,
        script_id: str = None,
        script_name: str = None,
        session_id: str = None,
        state: str = None,
        talk_time: int = None,
    ):
        # The number of call attempts.
        self.attempted_count = attempted_count
        # The caller number.
        self.caller_number = caller_number
        # The ID of the outbound campaign.
        self.campaign_id = campaign_id
        # The name of the outbound campaign.
        self.campaign_name = campaign_name
        # The case ID.
        self.case_id = case_id
        # The creation time.
        self.created_time = created_time
        # The custom variables in JSON string format.
        self.custom_variables = custom_variables
        # The dialing time.
        self.dialing_time = dialing_time
        # The disposition code.
        self.disposition_code = disposition_code
        # The disposition reason.
        self.disposition_reason = disposition_reason
        # The instance ID.
        self.instance_id = instance_id
        # The list of labels.
        self.labels = labels
        # The time of the last call attempt.
        self.last_attempted_time = last_attempted_time
        # The called number.
        self.phone_number = phone_number
        # The priority.
        self.priority = priority
        # The reference ID.
        self.reference_id = reference_id
        # The ringing duration.
        self.ringing_duration = ringing_duration
        # The ringing time.
        self.ringing_time = ringing_time
        # The script ID.
        self.script_id = script_id
        # The script name.
        self.script_name = script_name
        # The session ID of the last call.
        self.session_id = session_id
        # The case state.
        self.state = state
        # The talk time.
        self.talk_time = talk_time

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attempted_count is not None:
            result['AttemptedCount'] = self.attempted_count

        if self.caller_number is not None:
            result['CallerNumber'] = self.caller_number

        if self.campaign_id is not None:
            result['CampaignId'] = self.campaign_id

        if self.campaign_name is not None:
            result['CampaignName'] = self.campaign_name

        if self.case_id is not None:
            result['CaseId'] = self.case_id

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.custom_variables is not None:
            result['CustomVariables'] = self.custom_variables

        if self.dialing_time is not None:
            result['DialingTime'] = self.dialing_time

        if self.disposition_code is not None:
            result['DispositionCode'] = self.disposition_code

        if self.disposition_reason is not None:
            result['DispositionReason'] = self.disposition_reason

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.last_attempted_time is not None:
            result['LastAttemptedTime'] = self.last_attempted_time

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reference_id is not None:
            result['ReferenceId'] = self.reference_id

        if self.ringing_duration is not None:
            result['RingingDuration'] = self.ringing_duration

        if self.ringing_time is not None:
            result['RingingTime'] = self.ringing_time

        if self.script_id is not None:
            result['ScriptId'] = self.script_id

        if self.script_name is not None:
            result['ScriptName'] = self.script_name

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.state is not None:
            result['State'] = self.state

        if self.talk_time is not None:
            result['TalkTime'] = self.talk_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttemptedCount') is not None:
            self.attempted_count = m.get('AttemptedCount')

        if m.get('CallerNumber') is not None:
            self.caller_number = m.get('CallerNumber')

        if m.get('CampaignId') is not None:
            self.campaign_id = m.get('CampaignId')

        if m.get('CampaignName') is not None:
            self.campaign_name = m.get('CampaignName')

        if m.get('CaseId') is not None:
            self.case_id = m.get('CaseId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CustomVariables') is not None:
            self.custom_variables = m.get('CustomVariables')

        if m.get('DialingTime') is not None:
            self.dialing_time = m.get('DialingTime')

        if m.get('DispositionCode') is not None:
            self.disposition_code = m.get('DispositionCode')

        if m.get('DispositionReason') is not None:
            self.disposition_reason = m.get('DispositionReason')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.GetCaseDetailResponseBodyDataCaseLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('LastAttemptedTime') is not None:
            self.last_attempted_time = m.get('LastAttemptedTime')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ReferenceId') is not None:
            self.reference_id = m.get('ReferenceId')

        if m.get('RingingDuration') is not None:
            self.ringing_duration = m.get('RingingDuration')

        if m.get('RingingTime') is not None:
            self.ringing_time = m.get('RingingTime')

        if m.get('ScriptId') is not None:
            self.script_id = m.get('ScriptId')

        if m.get('ScriptName') is not None:
            self.script_name = m.get('ScriptName')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TalkTime') is not None:
            self.talk_time = m.get('TalkTime')

        return self

class GetCaseDetailResponseBodyDataCaseLabels(DaraModel):
    def __init__(
        self,
        candidate_values: List[str] = None,
        collected: bool = None,
        description: str = None,
        matched_value: str = None,
        name: str = None,
        system: bool = None,
    ):
        # The set of candidate values for the label.
        self.candidate_values = candidate_values
        # Indicates whether the label was collected.
        self.collected = collected
        # The label description.
        self.description = description
        # The matched value of the label.
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

class GetCaseDetailResponseBodyDataCallDetailRecords(DaraModel):
    def __init__(
        self,
        access_channel_id: str = None,
        access_channel_type: str = None,
        callee: str = None,
        caller: str = None,
        disposition_code: str = None,
        disposition_reason: str = None,
        draft_version: bool = None,
        duration: int = None,
        end_time: int = None,
        release_initiator: str = None,
        session_id: str = None,
        start_time: int = None,
        talk_time: int = None,
        talk_turns: int = None,
        transfer_target: str = None,
        transfer_type: str = None,
    ):
        # The access channel ID.
        self.access_channel_id = access_channel_id
        # The access channel type.
        self.access_channel_type = access_channel_type
        # The called number.
        self.callee = callee
        # The caller number.
        self.caller = caller
        # The disposition code.
        self.disposition_code = disposition_code
        # The disposition reason.
        self.disposition_reason = disposition_reason
        # Indicates whether the version is a draft version.
        self.draft_version = draft_version
        # The total duration.
        self.duration = duration
        # The time when the call ended.
        self.end_time = end_time
        # The party that initiated the hangup.
        self.release_initiator = release_initiator
        # The call session ID.
        self.session_id = session_id
        # The time when the call started.
        self.start_time = start_time
        # The talk time.
        self.talk_time = talk_time
        # The number of conversation turns.
        self.talk_turns = talk_turns
        # The transfer target.
        self.transfer_target = transfer_target
        # The transfer type.
        self.transfer_type = transfer_type

    def validate(self):
        pass

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

        if m.get('TransferTarget') is not None:
            self.transfer_target = m.get('TransferTarget')

        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')

        return self

