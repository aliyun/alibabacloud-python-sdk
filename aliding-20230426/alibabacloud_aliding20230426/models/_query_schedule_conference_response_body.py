# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class QueryScheduleConferenceResponseBody(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        phones: List[str] = None,
        request_id: str = None,
        room_code: str = None,
        schedule_conference_id: str = None,
        start_time: int = None,
        title: str = None,
        url: str = None,
    ):
        self.end_time = end_time
        self.phones = phones
        self.request_id = request_id
        self.room_code = room_code
        self.schedule_conference_id = schedule_conference_id
        self.start_time = start_time
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.phones is not None:
            result['phones'] = self.phones

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.room_code is not None:
            result['roomCode'] = self.room_code

        if self.schedule_conference_id is not None:
            result['scheduleConferenceId'] = self.schedule_conference_id

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.title is not None:
            result['title'] = self.title

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('phones') is not None:
            self.phones = m.get('phones')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('roomCode') is not None:
            self.room_code = m.get('roomCode')

        if m.get('scheduleConferenceId') is not None:
            self.schedule_conference_id = m.get('scheduleConferenceId')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

