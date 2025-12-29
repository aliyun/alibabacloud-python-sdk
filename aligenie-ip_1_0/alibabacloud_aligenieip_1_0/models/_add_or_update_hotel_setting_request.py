# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class AddOrUpdateHotelSettingRequest(DaraModel):
    def __init__(
        self,
        hotel_device_mode_list: List[str] = None,
        hotel_id: str = None,
        hotel_screen_saver: main_models.AddOrUpdateHotelSettingRequestHotelScreenSaver = None,
        night_mode: main_models.AddOrUpdateHotelSettingRequestNightMode = None,
        setting_type: str = None,
        value: str = None,
    ):
        self.hotel_device_mode_list = hotel_device_mode_list
        self.hotel_id = hotel_id
        self.hotel_screen_saver = hotel_screen_saver
        self.night_mode = night_mode
        self.setting_type = setting_type
        self.value = value

    def validate(self):
        if self.hotel_screen_saver:
            self.hotel_screen_saver.validate()
        if self.night_mode:
            self.night_mode.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_device_mode_list is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.hotel_screen_saver is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver.to_map()

        if self.night_mode is not None:
            result['NightMode'] = self.night_mode.to_map()

        if self.setting_type is not None:
            result['SettingType'] = self.setting_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list = m.get('HotelDeviceModeList')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('HotelScreenSaver') is not None:
            temp_model = main_models.AddOrUpdateHotelSettingRequestHotelScreenSaver()
            self.hotel_screen_saver = temp_model.from_map(m.get('HotelScreenSaver'))

        if m.get('NightMode') is not None:
            temp_model = main_models.AddOrUpdateHotelSettingRequestNightMode()
            self.night_mode = temp_model.from_map(m.get('NightMode'))

        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class AddOrUpdateHotelSettingRequestNightMode(DaraModel):
    def __init__(
        self,
        default_bright: str = None,
        default_volume: str = None,
        enable: bool = None,
        end: str = None,
        standby_action: str = None,
        start: str = None,
    ):
        self.default_bright = default_bright
        self.default_volume = default_volume
        self.enable = enable
        self.end = end
        self.standby_action = standby_action
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_bright is not None:
            result['DefaultBright'] = self.default_bright

        if self.default_volume is not None:
            result['DefaultVolume'] = self.default_volume

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.end is not None:
            result['End'] = self.end

        if self.standby_action is not None:
            result['StandbyAction'] = self.standby_action

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultBright') is not None:
            self.default_bright = m.get('DefaultBright')

        if m.get('DefaultVolume') is not None:
            self.default_volume = m.get('DefaultVolume')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('StandbyAction') is not None:
            self.standby_action = m.get('StandbyAction')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class AddOrUpdateHotelSettingRequestHotelScreenSaver(DaraModel):
    def __init__(
        self,
        screen_saver_pic_url: str = None,
        screen_saver_style: str = None,
    ):
        self.screen_saver_pic_url = screen_saver_pic_url
        self.screen_saver_style = screen_saver_style

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.screen_saver_pic_url is not None:
            result['ScreenSaverPicUrl'] = self.screen_saver_pic_url

        if self.screen_saver_style is not None:
            result['ScreenSaverStyle'] = self.screen_saver_style

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScreenSaverPicUrl') is not None:
            self.screen_saver_pic_url = m.get('ScreenSaverPicUrl')

        if m.get('ScreenSaverStyle') is not None:
            self.screen_saver_style = m.get('ScreenSaverStyle')

        return self

