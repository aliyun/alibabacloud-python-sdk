# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class ListAiAppRiskEventByPageResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.ListAiAppRiskEventByPageResponseBodyItems] = None,
        max_results: int = None,
        next_token: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The returned data.
        self.items = items
        # The maximum number of results returned per page.
        self.max_results = max_results
        # The token for the next page. An empty value indicates that no more pages exist.
        self.next_token = next_token
        # The number of entries per page.
        self.page_size = page_size
        # The ID assigned by the backend to uniquely identify a request. You can use this ID to troubleshoot issues.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.ListAiAppRiskEventByPageResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListAiAppRiskEventByPageResponseBodyItems(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        channel: str = None,
        end_time: str = None,
        event_code: str = None,
        event_desc: str = None,
        event_desc_en: str = None,
        event_id: str = None,
        event_name: str = None,
        handle_time: str = None,
        label: str = None,
        label_desc: str = None,
        level: str = None,
        start_time: str = None,
        status: str = None,
        type: str = None,
    ):
        # The unique ID of the AI application.
        self.app_id = app_id
        # The name of the AI application.
        self.app_name = app_name
        # The channel source.
        self.channel = channel
        # The time when the event was resolved. Format: YYYY-MM-DD HH:mm:ss.
        self.end_time = end_time
        # The event code that identifies the type or category of the event.
        self.event_code = event_code
        # The detailed description of the risk event.
        self.event_desc = event_desc
        # The detailed description of the risk event in English.
        self.event_desc_en = event_desc_en
        # The event ID that uniquely identifies a risk event.
        self.event_id = event_id
        # The name that briefly describes the risk event.
        self.event_name = event_name
        # The time when the event was handled. Format: YYYY-MM-DD HH:mm:ss.
        self.handle_time = handle_time
        # The label used to tag or categorize the event.
        self.label = label
        # The detailed description of the label.
        self.label_desc = label_desc
        # The risk level that indicates the severity of the event, such as high, medium, or low.
        self.level = level
        # The time when the event occurred. Format: YYYY-MM-DD HH:mm:ss.
        self.start_time = start_time
        # The event status that indicates the current processing state, such as pending or resolved.
        self.status = status
        # The event type that indicates the category of the risk event, such as security or performance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.channel is not None:
            result['Channel'] = self.channel

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_desc is not None:
            result['EventDesc'] = self.event_desc

        if self.event_desc_en is not None:
            result['EventDescEn'] = self.event_desc_en

        if self.event_id is not None:
            result['EventId'] = self.event_id

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.handle_time is not None:
            result['HandleTime'] = self.handle_time

        if self.label is not None:
            result['Label'] = self.label

        if self.label_desc is not None:
            result['LabelDesc'] = self.label_desc

        if self.level is not None:
            result['Level'] = self.level

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('Channel') is not None:
            self.channel = m.get('Channel')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventDesc') is not None:
            self.event_desc = m.get('EventDesc')

        if m.get('EventDescEn') is not None:
            self.event_desc_en = m.get('EventDescEn')

        if m.get('EventId') is not None:
            self.event_id = m.get('EventId')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('HandleTime') is not None:
            self.handle_time = m.get('HandleTime')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelDesc') is not None:
            self.label_desc = m.get('LabelDesc')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

