# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class DeleteHotelAlarmRequest(DaraModel):
    def __init__(
        self,
        alarms: List[main_models.DeleteHotelAlarmRequestAlarms] = None,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.alarms = alarms
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        if self.alarms:
            for v1 in self.alarms:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Alarms'] = []
        if self.alarms is not None:
            for k1 in self.alarms:
                result['Alarms'].append(k1.to_map() if k1 else None)

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alarms = []
        if m.get('Alarms') is not None:
            for k1 in m.get('Alarms'):
                temp_model = main_models.DeleteHotelAlarmRequestAlarms()
                self.alarms.append(temp_model.from_map(k1))

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        return self

class DeleteHotelAlarmRequestAlarms(DaraModel):
    def __init__(
        self,
        alarm_id: int = None,
        device_open_id: str = None,
        room_no: str = None,
        user_open_id: str = None,
    ):
        # This parameter is required.
        self.alarm_id = alarm_id
        # This parameter is required.
        self.device_open_id = device_open_id
        self.room_no = room_no
        # This parameter is required.
        self.user_open_id = user_open_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id

        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')

        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')

        return self

