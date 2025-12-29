# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateHotelShrinkRequest(DaraModel):
    def __init__(
        self,
        app_key: str = None,
        est_open_time: str = None,
        hotel_address: str = None,
        hotel_email: str = None,
        hotel_id: str = None,
        hotel_name: str = None,
        phone_number: str = None,
        related_pks_shrink: str = None,
        remark: str = None,
        room_num: int = None,
        tb_open_id: str = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        self.est_open_time = est_open_time
        self.hotel_address = hotel_address
        self.hotel_email = hotel_email
        # This parameter is required.
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.phone_number = phone_number
        self.related_pks_shrink = related_pks_shrink
        self.remark = remark
        self.room_num = room_num
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

        if self.est_open_time is not None:
            result['EstOpenTime'] = self.est_open_time

        if self.hotel_address is not None:
            result['HotelAddress'] = self.hotel_address

        if self.hotel_email is not None:
            result['HotelEmail'] = self.hotel_email

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.related_pks_shrink is not None:
            result['RelatedPks'] = self.related_pks_shrink

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.room_num is not None:
            result['RoomNum'] = self.room_num

        if self.tb_open_id is not None:
            result['TbOpenId'] = self.tb_open_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('EstOpenTime') is not None:
            self.est_open_time = m.get('EstOpenTime')

        if m.get('HotelAddress') is not None:
            self.hotel_address = m.get('HotelAddress')

        if m.get('HotelEmail') is not None:
            self.hotel_email = m.get('HotelEmail')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('RelatedPks') is not None:
            self.related_pks_shrink = m.get('RelatedPks')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('RoomNum') is not None:
            self.room_num = m.get('RoomNum')

        if m.get('TbOpenId') is not None:
            self.tb_open_id = m.get('TbOpenId')

        return self

