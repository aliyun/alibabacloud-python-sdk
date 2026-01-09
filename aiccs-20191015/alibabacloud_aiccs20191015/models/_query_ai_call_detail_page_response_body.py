# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryAiCallDetailPageResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QueryAiCallDetailPageResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryAiCallDetailPageResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryAiCallDetailPageResponseBodyData(DaraModel):
    def __init__(
        self,
        list: List[main_models.QueryAiCallDetailPageResponseBodyDataList] = None,
        page_no: int = None,
        page_size: int = None,
        total: int = None,
    ):
        self.list = list
        self.page_no = page_no
        self.page_size = page_size
        self.total = total

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

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('List') is not None:
            for k1 in m.get('List'):
                temp_model = main_models.QueryAiCallDetailPageResponseBodyDataList()
                self.list.append(temp_model.from_map(k1))

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryAiCallDetailPageResponseBodyDataList(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        call_result: str = None,
        called_number: str = None,
        calling_time: int = None,
        conversation_duration: int = None,
        conversation_record: str = None,
        conversation_turn_count: int = None,
        detail_id: str = None,
        failed_reason: str = None,
        imported_time: int = None,
        major_intent: str = None,
        options: str = None,
        out_id: str = None,
        recording_file_path: str = None,
        status: int = None,
        task_id: str = None,
    ):
        self.batch_id = batch_id
        self.call_result = call_result
        self.called_number = called_number
        self.calling_time = calling_time
        self.conversation_duration = conversation_duration
        self.conversation_record = conversation_record
        self.conversation_turn_count = conversation_turn_count
        self.detail_id = detail_id
        self.failed_reason = failed_reason
        self.imported_time = imported_time
        self.major_intent = major_intent
        self.options = options
        self.out_id = out_id
        self.recording_file_path = recording_file_path
        self.status = status
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['BatchId'] = self.batch_id

        if self.call_result is not None:
            result['CallResult'] = self.call_result

        if self.called_number is not None:
            result['CalledNumber'] = self.called_number

        if self.calling_time is not None:
            result['CallingTime'] = self.calling_time

        if self.conversation_duration is not None:
            result['ConversationDuration'] = self.conversation_duration

        if self.conversation_record is not None:
            result['ConversationRecord'] = self.conversation_record

        if self.conversation_turn_count is not None:
            result['ConversationTurnCount'] = self.conversation_turn_count

        if self.detail_id is not None:
            result['DetailId'] = self.detail_id

        if self.failed_reason is not None:
            result['FailedReason'] = self.failed_reason

        if self.imported_time is not None:
            result['ImportedTime'] = self.imported_time

        if self.major_intent is not None:
            result['MajorIntent'] = self.major_intent

        if self.options is not None:
            result['Options'] = self.options

        if self.out_id is not None:
            result['OutId'] = self.out_id

        if self.recording_file_path is not None:
            result['RecordingFilePath'] = self.recording_file_path

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchId') is not None:
            self.batch_id = m.get('BatchId')

        if m.get('CallResult') is not None:
            self.call_result = m.get('CallResult')

        if m.get('CalledNumber') is not None:
            self.called_number = m.get('CalledNumber')

        if m.get('CallingTime') is not None:
            self.calling_time = m.get('CallingTime')

        if m.get('ConversationDuration') is not None:
            self.conversation_duration = m.get('ConversationDuration')

        if m.get('ConversationRecord') is not None:
            self.conversation_record = m.get('ConversationRecord')

        if m.get('ConversationTurnCount') is not None:
            self.conversation_turn_count = m.get('ConversationTurnCount')

        if m.get('DetailId') is not None:
            self.detail_id = m.get('DetailId')

        if m.get('FailedReason') is not None:
            self.failed_reason = m.get('FailedReason')

        if m.get('ImportedTime') is not None:
            self.imported_time = m.get('ImportedTime')

        if m.get('MajorIntent') is not None:
            self.major_intent = m.get('MajorIntent')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('OutId') is not None:
            self.out_id = m.get('OutId')

        if m.get('RecordingFilePath') is not None:
            self.recording_file_path = m.get('RecordingFilePath')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

