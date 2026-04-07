# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class ListCallDetailRecordsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListCallDetailRecordsResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        # Id of the request
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
            temp_model = main_models.ListCallDetailRecordsResponseBodyData()
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

class ListCallDetailRecordsResponseBodyData(DaraModel):
    def __init__(
        self,
        call_detail_records: List[main_models.ListCallDetailRecordsResponseBodyDataCallDetailRecords] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.call_detail_records = call_detail_records
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.call_detail_records:
            for v1 in self.call_detail_records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallDetailRecords'] = []
        if self.call_detail_records is not None:
            for k1 in self.call_detail_records:
                result['CallDetailRecords'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_detail_records = []
        if m.get('CallDetailRecords') is not None:
            for k1 in m.get('CallDetailRecords'):
                temp_model = main_models.ListCallDetailRecordsResponseBodyDataCallDetailRecords()
                self.call_detail_records.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCallDetailRecordsResponseBodyDataCallDetailRecords(DaraModel):
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
        transfer_target: str = None,
        transfer_type: str = None,
    ):
        self.callee = callee
        self.caller = caller
        self.disposition_code = disposition_code
        self.disposition_reason = disposition_reason
        self.duration = duration
        self.end_time = end_time
        self.issue_resolved = issue_resolved
        self.release_initiator = release_initiator
        self.resolution_evidence = resolution_evidence
        self.session_id = session_id
        self.start_time = start_time
        self.talk_time = talk_time
        self.talk_turns = talk_turns
        self.transfer_target = transfer_target
        self.transfer_type = transfer_type

    def validate(self):
        pass

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

        if m.get('TransferTarget') is not None:
            self.transfer_target = m.get('TransferTarget')

        if m.get('TransferType') is not None:
            self.transfer_type = m.get('TransferType')

        return self

