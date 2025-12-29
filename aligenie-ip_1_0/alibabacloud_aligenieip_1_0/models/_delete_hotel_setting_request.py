# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteHotelSettingRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        setting_type: str = None,
    ):
        self.hotel_id = hotel_id
        self.setting_type = setting_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.setting_type is not None:
            result['SettingType'] = self.setting_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('SettingType') is not None:
            self.setting_type = m.get('SettingType')

        return self

