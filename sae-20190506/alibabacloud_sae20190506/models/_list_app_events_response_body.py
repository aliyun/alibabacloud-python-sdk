# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListAppEventsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListAppEventsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The call was successful.
        # *   **3xx**: The call was redirected.
        # *   **4xx**: The call failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # The events.
        self.data = data
        # The error code returned if the call failed. Take note of the following rules:
        # 
        # *   If the call is successful, the **ErrorCode** parameter is not returned.
        # *   If the call fails, the **ErrorCode** parameter is returned. For more information, see the "**Error codes**" section in this topic.
        self.error_code = error_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the events that occurred in the application were queried. Valid values:
        # 
        # *   **true**: The events were queried.
        # *   **false**: The events failed to be queried.
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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

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
            temp_model = main_models.ListAppEventsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListAppEventsResponseBodyData(DaraModel):
    def __init__(
        self,
        app_event_entity: List[main_models.ListAppEventsResponseBodyDataAppEventEntity] = None,
        current_page: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        # The events.
        self.app_event_entity = app_event_entity
        # The number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of events that occurred in an application.
        self.total_size = total_size

    def validate(self):
        if self.app_event_entity:
            for v1 in self.app_event_entity:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppEventEntity'] = []
        if self.app_event_entity is not None:
            for k1 in self.app_event_entity:
                result['AppEventEntity'].append(k1.to_map() if k1 else None)

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_event_entity = []
        if m.get('AppEventEntity') is not None:
            for k1 in m.get('AppEventEntity'):
                temp_model = main_models.ListAppEventsResponseBodyDataAppEventEntity()
                self.app_event_entity.append(temp_model.from_map(k1))

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListAppEventsResponseBodyDataAppEventEntity(DaraModel):
    def __init__(
        self,
        cause_analysis: str = None,
        event_type: str = None,
        first_timestamp: str = None,
        last_timestamp: str = None,
        message: str = None,
        object_kind: str = None,
        object_name: str = None,
        reason: str = None,
    ):
        self.cause_analysis = cause_analysis
        # The type of the event. Valid values:
        self.event_type = event_type
        # The timestamp of the first occurrence of the event.
        self.first_timestamp = first_timestamp
        # The timestamp of the last occurrence of the event.
        self.last_timestamp = last_timestamp
        # The information about the event.
        self.message = message
        # The type of the object.
        self.object_kind = object_kind
        # The name of the object.
        self.object_name = object_name
        # The cause of the event.
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cause_analysis is not None:
            result['CauseAnalysis'] = self.cause_analysis

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.first_timestamp is not None:
            result['FirstTimestamp'] = self.first_timestamp

        if self.last_timestamp is not None:
            result['LastTimestamp'] = self.last_timestamp

        if self.message is not None:
            result['Message'] = self.message

        if self.object_kind is not None:
            result['ObjectKind'] = self.object_kind

        if self.object_name is not None:
            result['ObjectName'] = self.object_name

        if self.reason is not None:
            result['Reason'] = self.reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CauseAnalysis') is not None:
            self.cause_analysis = m.get('CauseAnalysis')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('FirstTimestamp') is not None:
            self.first_timestamp = m.get('FirstTimestamp')

        if m.get('LastTimestamp') is not None:
            self.last_timestamp = m.get('LastTimestamp')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ObjectKind') is not None:
            self.object_kind = m.get('ObjectKind')

        if m.get('ObjectName') is not None:
            self.object_name = m.get('ObjectName')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        return self

