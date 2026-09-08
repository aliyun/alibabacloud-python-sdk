# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class PutEventsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.PutEventsResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The unique identifier that Alibaba Cloud generated for the request.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values: true: The operation was successful. false: The operation failed.
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

        if m.get('Data') is not None:
            temp_model = main_models.PutEventsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PutEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        entry_list: List[main_models.PutEventsResponseBodyDataEntryList] = None,
        failed_entry_count: int = None,
    ):
        # The collection of event sending results.
        self.entry_list = entry_list
        # The number of events that failed to be sent.
        self.failed_entry_count = failed_entry_count

    def validate(self):
        if self.entry_list:
            for v1 in self.entry_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EntryList'] = []
        if self.entry_list is not None:
            for k1 in self.entry_list:
                result['EntryList'].append(k1.to_map() if k1 else None)

        if self.failed_entry_count is not None:
            result['FailedEntryCount'] = self.failed_entry_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entry_list = []
        if m.get('EntryList') is not None:
            for k1 in m.get('EntryList'):
                temp_model = main_models.PutEventsResponseBodyDataEntryList()
                self.entry_list.append(temp_model.from_map(k1))

        if m.get('FailedEntryCount') is not None:
            self.failed_entry_count = m.get('FailedEntryCount')

        return self

class PutEventsResponseBodyDataEntryList(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event_id: str = None,
        trace_id: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The detailed error description.
        self.error_message = error_message
        # The event ID.
        self.event_id = event_id
        # The trace ID, which is used to query the exact call information.
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

