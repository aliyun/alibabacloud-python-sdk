# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class ListCasesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCasesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code.
        self.code = code
        # The paged data.
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
            temp_model = main_models.ListCasesResponseBodyData()
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

class ListCasesResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.ListCasesResponseBodyDataList] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of cases.
        self.list = list
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of records.
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
                temp_model = main_models.ListCasesResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCasesResponseBodyDataList(DaraModel):
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
        labels: List[main_models.ListCasesResponseBodyDataListLabels] = None,
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
        # The number of dial attempts.
        self.attempted_count = attempted_count
        # The caller number.
        self.caller_number = caller_number
        # The outbound campaign ID.
        self.campaign_id = campaign_id
        # The name of the outbound campaign.
        self.campaign_name = campaign_name
        # The case ID.
        self.case_id = case_id
        # The time when the case was created.
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
        # The time of the last dial attempt.
        self.last_attempted_time = last_attempted_time
        # The called number.
        self.phone_number = phone_number
        # The priority of the case.
        self.priority = priority
        # The reference ID.
        self.reference_id = reference_id
        # The ringing duration.
        self.ringing_duration = ringing_duration
        # The ringing time.
        self.ringing_time = ringing_time
        # The script ID.
        self.script_id = script_id
        # The name of the script.
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
                temp_model = main_models.ListCasesResponseBodyDataListLabels()
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

class ListCasesResponseBodyDataListLabels(DaraModel):
    def __init__(
        self,
        candidate_values: List[str] = None,
        collected: bool = None,
        description: str = None,
        matched_value: str = None,
        name: str = None,
        system: bool = None,
    ):
        # The candidate values of the label.
        self.candidate_values = candidate_values
        # Indicates whether the item is collected.
        self.collected = collected
        # The description of the label.
        self.description = description
        # The matched value of the label.
        self.matched_value = matched_value
        # The name of the label.
        self.name = name
        # The system label.
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

