# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeSimilarSecurityEventsResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribeSimilarSecurityEventsResponseBodyPageInfo = None,
        request_id: str = None,
        security_events_response: List[main_models.DescribeSimilarSecurityEventsResponseBodySecurityEventsResponse] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The information about the alert events that are triggered by the same rule or of the same alert type.
        self.security_events_response = security_events_response

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.security_events_response:
            for v1 in self.security_events_response:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SecurityEventsResponse'] = []
        if self.security_events_response is not None:
            for k1 in self.security_events_response:
                result['SecurityEventsResponse'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribeSimilarSecurityEventsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.security_events_response = []
        if m.get('SecurityEventsResponse') is not None:
            for k1 in m.get('SecurityEventsResponse'):
                temp_model = main_models.DescribeSimilarSecurityEventsResponseBodySecurityEventsResponse()
                self.security_events_response.append(temp_model.from_map(k1))

        return self

class DescribeSimilarSecurityEventsResponseBodySecurityEventsResponse(DaraModel):
    def __init__(
        self,
        event_name: str = None,
        event_type: str = None,
        last_time: int = None,
        occurrence_time: int = None,
        security_event_id: int = None,
        uuid: str = None,
    ):
        # The name of the alert event.
        self.event_name = event_name
        # The type of the alert event. Valid values:
        # 
        # *   Suspicious Process
        # *   Webshell
        # *   Unusual Logon
        # *   Malicious Software
        # *   Sensitive File Tampering
        # *   Unusual Network Connection
        # *   Other
        # *   Suspicious Account
        # *   Cloud threat detection
        # *   Precision defense
        # *   Application Whitelist
        # *   Persistence
        # *   Web Application Threat Detection
        # *   Malicious scripts
        # *   Malicious Network Activity
        # *   K8s Abnormal Behavior
        # *   Website backdoor (local engine)
        # *   Exploit
        # *   Image Scan
        # *   Trusted exception
        # 
        # For more information about alert types, see [Overview](https://help.aliyun.com/document_detail/68388.html).
        self.event_type = event_type
        # The timestamp generated when the alert event was last detected. Unit: milliseconds.
        self.last_time = last_time
        # The timestamp generated when the alert event was first detected. Unit: milliseconds.
        self.occurrence_time = occurrence_time
        # The ID of the alert event.
        self.security_event_id = security_event_id
        # The UUID of the server that was affected by the alert event.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.occurrence_time is not None:
            result['OccurrenceTime'] = self.occurrence_time

        if self.security_event_id is not None:
            result['SecurityEventId'] = self.security_event_id

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('OccurrenceTime') is not None:
            self.occurrence_time = m.get('OccurrenceTime')

        if m.get('SecurityEventId') is not None:
            self.security_event_id = m.get('SecurityEventId')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class DescribeSimilarSecurityEventsResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries returned per page. Default value: **20**.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

