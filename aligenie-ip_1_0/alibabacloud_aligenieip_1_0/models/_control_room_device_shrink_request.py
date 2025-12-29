# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ControlRoomDeviceShrinkRequest(DaraModel):
    def __init__(
        self,
        cmd: str = None,
        device_index: int = None,
        device_number: str = None,
        hotel_id: str = None,
        properties_shrink: str = None,
        room_no: str = None,
    ):
        # This parameter is required.
        self.cmd = cmd
        self.device_index = device_index
        # This parameter is required.
        self.device_number = device_number
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.properties_shrink = properties_shrink
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cmd is not None:
            result['Cmd'] = self.cmd

        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index

        if self.device_number is not None:
            result['DeviceNumber'] = self.device_number

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.properties_shrink is not None:
            result['Properties'] = self.properties_shrink

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')

        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')

        if m.get('DeviceNumber') is not None:
            self.device_number = m.get('DeviceNumber')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Properties') is not None:
            self.properties_shrink = m.get('Properties')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

