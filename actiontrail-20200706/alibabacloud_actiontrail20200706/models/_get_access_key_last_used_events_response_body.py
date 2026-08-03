# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class GetAccessKeyLastUsedEventsResponseBody(DaraModel):
    def __init__(
        self,
        events: List[main_models.GetAccessKeyLastUsedEventsResponseBodyEvents] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The list of returned events.
        # 
        # This parameter is required.
        self.events = events
        # The token that is used to retrieve the next page of results. If the value of this parameter is not empty, the next page exists. You must set the value to the NextToken value returned from the last call.
        # 
        # colspan="1" rowspan="1">
        # 
        # eyJhY2NvdW50IjoiMTQyNDM3OTU4NjM4NzE2MSIsImV2ZW50SWQiOiI3MkJDRTExRi02OTU3LTQ0NUItQjY0MC1CNEUyMkM4NUEwQzgiLCJsb2dJZCI6IjgyLTE0MjQzNzk1ODYzODcxNjEiLCJ0aW1lIjoxNjAyMzExNTQwMD\\*\\*\\*\\*
        self.next_token = next_token
        # The request ID.
        # 
        # This parameter is required.
        self.request_id = request_id

    def validate(self):
        if self.events:
            for v1 in self.events:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Events'] = []
        if self.events is not None:
            for k1 in self.events:
                result['Events'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('Events') is not None:
            for k1 in m.get('Events'):
                temp_model = main_models.GetAccessKeyLastUsedEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAccessKeyLastUsedEventsResponseBodyEvents(DaraModel):
    def __init__(
        self,
        detail: str = None,
        event_name: str = None,
        source: str = None,
        used_timestamp: int = None,
    ):
        # The event details.
        self.detail = detail
        # The event name.
        self.event_name = event_name
        # The source of the last usage record.
        self.source = source
        # The timestamp when the event was generated. Unit: milliseconds.
        self.used_timestamp = used_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.event_name is not None:
            result['EventName'] = self.event_name

        if self.source is not None:
            result['Source'] = self.source

        if self.used_timestamp is not None:
            result['UsedTimestamp'] = self.used_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('UsedTimestamp') is not None:
            self.used_timestamp = m.get('UsedTimestamp')

        return self

