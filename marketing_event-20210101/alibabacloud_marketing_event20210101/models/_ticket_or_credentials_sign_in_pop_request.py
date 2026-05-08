# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class TicketOrCredentialsSignInPopRequest(DaraModel):
    def __init__(
        self,
        activity_id: str = None,
        code: str = None,
        conference_name: str = None,
        device_id: str = None,
        entry_name: str = None,
        idcard: str = None,
        sign_time: str = None,
        type: int = None,
    ):
        # This parameter is required.
        self.activity_id = activity_id
        self.code = code
        # This parameter is required.
        self.conference_name = conference_name
        # This parameter is required.
        self.device_id = device_id
        # This parameter is required.
        self.entry_name = entry_name
        self.idcard = idcard
        # This parameter is required.
        self.sign_time = sign_time
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_id is not None:
            result['ActivityId'] = self.activity_id

        if self.code is not None:
            result['Code'] = self.code

        if self.conference_name is not None:
            result['ConferenceName'] = self.conference_name

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.entry_name is not None:
            result['EntryName'] = self.entry_name

        if self.idcard is not None:
            result['Idcard'] = self.idcard

        if self.sign_time is not None:
            result['SignTime'] = self.sign_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityId') is not None:
            self.activity_id = m.get('ActivityId')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ConferenceName') is not None:
            self.conference_name = m.get('ConferenceName')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('EntryName') is not None:
            self.entry_name = m.get('EntryName')

        if m.get('Idcard') is not None:
            self.idcard = m.get('Idcard')

        if m.get('SignTime') is not None:
            self.sign_time = m.get('SignTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

