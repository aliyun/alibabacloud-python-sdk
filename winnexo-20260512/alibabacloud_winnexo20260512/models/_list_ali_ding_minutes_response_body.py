# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListAliDingMinutesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        has_more: bool = None,
        items: List[main_models.ListAliDingMinutesResponseBodyItems] = None,
        message: str = None,
        next_cursor: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # Indicates whether more pages are available.
        self.has_more = has_more
        # The location clusters.
        self.items = items
        # The description of the status code.
        self.message = message
        # The token for the next retrieval.
        self.next_cursor = next_cursor
        # The request ID.
        self.request_id = request_id

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
        if self.code is not None:
            result['code'] = self.code

        if self.has_more is not None:
            result['hasMore'] = self.has_more

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.next_cursor is not None:
            result['nextCursor'] = self.next_cursor

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('hasMore') is not None:
            self.has_more = m.get('hasMore')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListAliDingMinutesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextCursor') is not None:
            self.next_cursor = m.get('nextCursor')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListAliDingMinutesResponseBodyItems(DaraModel):
    def __init__(
        self,
        creator_name: str = None,
        duration_ms: int = None,
        end_time: str = None,
        minutes_id: str = None,
        start_time: str = None,
        status: str = None,
        title: str = None,
    ):
        # The name of the creator.
        self.creator_name = creator_name
        # The execution duration of the asynchronous task.
        self.duration_ms = duration_ms
        # The end timestamp, in milliseconds.
        self.end_time = end_time
        # The DingTalk meeting minutes ID.
        self.minutes_id = minutes_id
        # The start timestamp, in milliseconds.
        self.start_time = start_time
        # The task status. Running is returned upon submission.
        self.status = status
        # The title of the scheduled meeting.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.duration_ms is not None:
            result['durationMs'] = self.duration_ms

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.minutes_id is not None:
            result['minutesId'] = self.minutes_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.status is not None:
            result['status'] = self.status

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('durationMs') is not None:
            self.duration_ms = m.get('durationMs')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('minutesId') is not None:
            self.minutes_id = m.get('minutesId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

