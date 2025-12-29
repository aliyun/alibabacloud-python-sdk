# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SyncDeviceStatusWithAkRequest(DaraModel):
    def __init__(
        self,
        category_cn_name: str = None,
        category_en_name: str = None,
        device_name: str = None,
        hotel_id: str = None,
        location: str = None,
        location_cn_name: str = None,
        number: str = None,
        room_no: str = None,
        switch: int = None,
        fan_speed: str = None,
        mode: str = None,
        room_temperature: str = None,
        temperature: str = None,
        value: int = None,
    ):
        self.category_cn_name = category_cn_name
        # This parameter is required.
        self.category_en_name = category_en_name
        self.device_name = device_name
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.location = location
        self.location_cn_name = location_cn_name
        # This parameter is required.
        self.number = number
        # This parameter is required.
        self.room_no = room_no
        # This parameter is required.
        self.switch = switch
        self.fan_speed = fan_speed
        self.mode = mode
        self.room_temperature = room_temperature
        self.temperature = temperature
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_cn_name is not None:
            result['CategoryCnName'] = self.category_cn_name

        if self.category_en_name is not None:
            result['CategoryEnName'] = self.category_en_name

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.location is not None:
            result['Location'] = self.location

        if self.location_cn_name is not None:
            result['LocationCnName'] = self.location_cn_name

        if self.number is not None:
            result['Number'] = self.number

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.switch is not None:
            result['Switch'] = self.switch

        if self.fan_speed is not None:
            result['fanSpeed'] = self.fan_speed

        if self.mode is not None:
            result['mode'] = self.mode

        if self.room_temperature is not None:
            result['roomTemperature'] = self.room_temperature

        if self.temperature is not None:
            result['temperature'] = self.temperature

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCnName') is not None:
            self.category_cn_name = m.get('CategoryCnName')

        if m.get('CategoryEnName') is not None:
            self.category_en_name = m.get('CategoryEnName')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('LocationCnName') is not None:
            self.location_cn_name = m.get('LocationCnName')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('Switch') is not None:
            self.switch = m.get('Switch')

        if m.get('fanSpeed') is not None:
            self.fan_speed = m.get('fanSpeed')

        if m.get('mode') is not None:
            self.mode = m.get('mode')

        if m.get('roomTemperature') is not None:
            self.room_temperature = m.get('roomTemperature')

        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

