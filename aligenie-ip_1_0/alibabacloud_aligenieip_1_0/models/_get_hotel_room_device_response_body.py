# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class GetHotelRoomDeviceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.GetHotelRoomDeviceResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetHotelRoomDeviceResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class GetHotelRoomDeviceResponseBodyResult(DaraModel):
    def __init__(
        self,
        firmware_version: str = None,
        hotel_id: str = None,
        mac: str = None,
        online_status: int = None,
        room_no: str = None,
        sn: str = None,
    ):
        self.firmware_version = firmware_version
        self.hotel_id = hotel_id
        self.mac = mac
        self.online_status = online_status
        self.room_no = room_no
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.sn is not None:
            result['Sn'] = self.sn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        return self

