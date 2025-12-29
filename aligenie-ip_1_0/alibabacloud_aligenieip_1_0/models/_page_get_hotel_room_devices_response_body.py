# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any, List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class PageGetHotelRoomDevicesResponseBody(DaraModel):
    def __init__(
        self,
        extentions: Dict[str, Any] = None,
        message: str = None,
        page: main_models.PageGetHotelRoomDevicesResponseBodyPage = None,
        request_id: str = None,
        result: List[main_models.PageGetHotelRoomDevicesResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.extentions = extentions
        self.message = message
        self.page = page
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.page:
            self.page.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extentions is not None:
            result['Extentions'] = self.extentions

        if self.message is not None:
            result['Message'] = self.message

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extentions') is not None:
            self.extentions = m.get('Extentions')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Page') is not None:
            temp_model = main_models.PageGetHotelRoomDevicesResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.PageGetHotelRoomDevicesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class PageGetHotelRoomDevicesResponseBodyResult(DaraModel):
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

class PageGetHotelRoomDevicesResponseBodyPage(DaraModel):
    def __init__(
        self,
        end: int = None,
        has_next: bool = None,
        page_number: int = None,
        page_size: int = None,
        start: int = None,
        total: int = None,
        total_page: int = None,
    ):
        self.end = end
        self.has_next = has_next
        self.page_number = page_number
        self.page_size = page_size
        self.start = start
        self.total = total
        self.total_page = total_page

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        if self.has_next is not None:
            result['HasNext'] = self.has_next

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start is not None:
            result['Start'] = self.start

        if self.total is not None:
            result['Total'] = self.total

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

