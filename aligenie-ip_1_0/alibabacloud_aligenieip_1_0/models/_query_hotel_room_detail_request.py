# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryHotelRoomDetailRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        mac: str = None,
        room_no: str = None,
        sn: str = None,
        uuid: str = None,
    ):
        self.hotel_id = hotel_id
        self.mac = mac
        self.room_no = room_no
        # 设备sn信息
        # 注：若在mac uuid sn全都输入的情况下 按照输入正确的内容查询 若全输入都是正确的 则 按照 uuid > mac > sn 优先级查询
        # 传入mac uuid sn其中一个 则酒店id和房间号可不传
        self.sn = sn
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

