# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateScheduleConferenceResponseBody(DaraModel):
    def __init__(
        self,
        phones: List[str] = None,
        request_id: str = None,
        room_code: str = None,
        schedule_conference_id: str = None,
        url: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.phones = phones
        self.request_id = request_id
        self.room_code = room_code
        self.schedule_conference_id = schedule_conference_id
        self.url = url
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phones is not None:
            result['phones'] = self.phones

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.room_code is not None:
            result['roomCode'] = self.room_code

        if self.schedule_conference_id is not None:
            result['scheduleConferenceId'] = self.schedule_conference_id

        if self.url is not None:
            result['url'] = self.url

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phones') is not None:
            self.phones = m.get('phones')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('roomCode') is not None:
            self.room_code = m.get('roomCode')

        if m.get('scheduleConferenceId') is not None:
            self.schedule_conference_id = m.get('scheduleConferenceId')

        if m.get('url') is not None:
            self.url = m.get('url')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

