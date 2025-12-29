# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddOrUpdateHotelSettingShrinkRequest(DaraModel):
    def __init__(
        self,
        hotel_device_mode_list_shrink: str = None,
        hotel_id: str = None,
        hotel_screen_saver_shrink: str = None,
        night_mode_shrink: str = None,
        setting_type: str = None,
        value: str = None,
    ):
        self.hotel_device_mode_list_shrink = hotel_device_mode_list_shrink
        self.hotel_id = hotel_id
        self.hotel_screen_saver_shrink = hotel_screen_saver_shrink
        self.night_mode_shrink = night_mode_shrink
        self.setting_type = setting_type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_device_mode_list_shrink is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list_shrink

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.hotel_screen_saver_shrink is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver_shrink

        if self.night_mode_shrink is not None:
            result['NightMode'] = self.night_mode_shrink

        if self.setting_type is not None:
            result['SettingType'] = self.setting_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list_shrink = m.get('HotelDeviceModeList')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('HotelScreenSaver') is not None:
            self.hotel_screen_saver_shrink = m.get('HotelScreenSaver')

        if m.get('NightMode') is not None:
            self.night_mode_shrink = m.get('NightMode')

        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

