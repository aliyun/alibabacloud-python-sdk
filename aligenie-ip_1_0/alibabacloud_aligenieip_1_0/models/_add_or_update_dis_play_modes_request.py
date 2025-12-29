# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddOrUpdateDisPlayModesRequest(DaraModel):
    def __init__(
        self,
        hotel_device_mode_list: List[str] = None,
        hotel_id: str = None,
    ):
        # This parameter is required.
        self.hotel_device_mode_list = hotel_device_mode_list
        # This parameter is required.
        self.hotel_id = hotel_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_device_mode_list is not None:
            result['HotelDeviceModeList'] = self.hotel_device_mode_list

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelDeviceModeList') is not None:
            self.hotel_device_mode_list = m.get('HotelDeviceModeList')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        return self

