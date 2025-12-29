# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class AddOrUpdateScreenSaverRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        hotel_screen_saver: main_models.AddOrUpdateScreenSaverRequestHotelScreenSaver = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.hotel_screen_saver = hotel_screen_saver

    def validate(self):
        if self.hotel_screen_saver:
            self.hotel_screen_saver.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.hotel_screen_saver is not None:
            result['HotelScreenSaver'] = self.hotel_screen_saver.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('HotelScreenSaver') is not None:
            temp_model = main_models.AddOrUpdateScreenSaverRequestHotelScreenSaver()
            self.hotel_screen_saver = temp_model.from_map(m.get('HotelScreenSaver'))

        return self

class AddOrUpdateScreenSaverRequestHotelScreenSaver(DaraModel):
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

