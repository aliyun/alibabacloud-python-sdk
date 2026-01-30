# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDeviceAlarmRequest(DaraModel):
    def __init__(
        self,
        alarm: int = None,
        channel_id: int = None,
        end_time: int = None,
        expire: int = None,
        id: str = None,
        object_type: int = None,
        owner_id: int = None,
        start_time: int = None,
        sub_alarm: int = None,
    ):
        # This parameter is required.
        self.alarm = alarm
        # This parameter is required.
        self.channel_id = channel_id
        # This parameter is required.
        self.end_time = end_time
        self.expire = expire
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.object_type = object_type
        self.owner_id = owner_id
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.sub_alarm = sub_alarm

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm is not None:
            result['Alarm'] = self.alarm

        if self.channel_id is not None:
            result['ChannelId'] = self.channel_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.expire is not None:
            result['Expire'] = self.expire

        if self.id is not None:
            result['Id'] = self.id

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.sub_alarm is not None:
            result['SubAlarm'] = self.sub_alarm

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alarm') is not None:
            self.alarm = m.get('Alarm')

        if m.get('ChannelId') is not None:
            self.channel_id = m.get('ChannelId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Expire') is not None:
            self.expire = m.get('Expire')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SubAlarm') is not None:
            self.sub_alarm = m.get('SubAlarm')

        return self

