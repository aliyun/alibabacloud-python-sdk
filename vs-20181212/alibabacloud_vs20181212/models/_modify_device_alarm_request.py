# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDeviceAlarmRequest(DaraModel):
    def __init__(
        self,
        alarm_id: str = None,
        channel_id: int = None,
        id: str = None,
        owner_id: int = None,
        status: int = None,
    ):
        # This parameter is required.
        self.alarm_id = alarm_id
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.id = id
        self.owner_id = owner_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.id is not None:
            result['Id'] = self.id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

