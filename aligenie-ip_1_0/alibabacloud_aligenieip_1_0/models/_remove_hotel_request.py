# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveHotelRequest(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        hotel_id: str = None,
        tb_open_id: str = None,
    ):
        # appkey
        # 
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.tb_open_id = tb_open_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')

        return self

