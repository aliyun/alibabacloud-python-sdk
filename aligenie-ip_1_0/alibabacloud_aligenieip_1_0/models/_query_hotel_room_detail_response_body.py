# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class QueryHotelRoomDetailResponseBody(DaraModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        result: main_models.QueryHotelRoomDetailResponseBodyResult = None,
        status_code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.QueryHotelRoomDetailResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class QueryHotelRoomDetailResponseBodyResult(DaraModel):
    def __init__(
        self,
        auth_accounts: List[main_models.QueryHotelRoomDetailResponseBodyResultAuthAccounts] = None,
        connect_type: str = None,
        creator_account_name: str = None,
        device_infos: List[main_models.QueryHotelRoomDetailResponseBodyResultDeviceInfos] = None,
        hotel_id: str = None,
        hotel_name: str = None,
        other_service: main_models.QueryHotelRoomDetailResponseBodyResultOtherService = None,
        room_control_info: main_models.QueryHotelRoomDetailResponseBodyResultRoomControlInfo = None,
        room_no: str = None,
        room_service_info: main_models.QueryHotelRoomDetailResponseBodyResultRoomServiceInfo = None,
    ):
        self.auth_accounts = auth_accounts
        self.connect_type = connect_type
        self.creator_account_name = creator_account_name
        self.device_infos = device_infos
        self.hotel_id = hotel_id
        self.hotel_name = hotel_name
        self.other_service = other_service
        self.room_control_info = room_control_info
        self.room_no = room_no
        self.room_service_info = room_service_info

    def validate(self):
        if self.auth_accounts:
            for v1 in self.auth_accounts:
                 if v1:
                    v1.validate()
        if self.device_infos:
            for v1 in self.device_infos:
                 if v1:
                    v1.validate()
        if self.other_service:
            self.other_service.validate()
        if self.room_control_info:
            self.room_control_info.validate()
        if self.room_service_info:
            self.room_service_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AuthAccounts'] = []
        if self.auth_accounts is not None:
            for k1 in self.auth_accounts:
                result['AuthAccounts'].append(k1.to_map() if k1 else None)

        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.creator_account_name is not None:
            result['CreatorAccountName'] = self.creator_account_name

        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k1 in self.device_infos:
                result['DeviceInfos'].append(k1.to_map() if k1 else None)

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.hotel_name is not None:
            result['HotelName'] = self.hotel_name

        if self.other_service is not None:
            result['OtherService'] = self.other_service.to_map()

        if self.room_control_info is not None:
            result['RoomControlInfo'] = self.room_control_info.to_map()

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        if self.room_service_info is not None:
            result['RoomServiceInfo'] = self.room_service_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auth_accounts = []
        if m.get('AuthAccounts') is not None:
            for k1 in m.get('AuthAccounts'):
                temp_model = main_models.QueryHotelRoomDetailResponseBodyResultAuthAccounts()
                self.auth_accounts.append(temp_model.from_map(k1))

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('CreatorAccountName') is not None:
            self.creator_account_name = m.get('CreatorAccountName')

        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k1 in m.get('DeviceInfos'):
                temp_model = main_models.QueryHotelRoomDetailResponseBodyResultDeviceInfos()
                self.device_infos.append(temp_model.from_map(k1))

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('HotelName') is not None:
            self.hotel_name = m.get('HotelName')

        if m.get('OtherService') is not None:
            temp_model = main_models.QueryHotelRoomDetailResponseBodyResultOtherService()
            self.other_service = temp_model.from_map(m.get('OtherService'))

        if m.get('RoomControlInfo') is not None:
            temp_model = main_models.QueryHotelRoomDetailResponseBodyResultRoomControlInfo()
            self.room_control_info = temp_model.from_map(m.get('RoomControlInfo'))

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        if m.get('RoomServiceInfo') is not None:
            temp_model = main_models.QueryHotelRoomDetailResponseBodyResultRoomServiceInfo()
            self.room_service_info = temp_model.from_map(m.get('RoomServiceInfo'))

        return self

class QueryHotelRoomDetailResponseBodyResultRoomServiceInfo(DaraModel):
    def __init__(
        self,
        book_service_cnt: int = None,
        goods_service_cnt: int = None,
        repair_service_cnt: int = None,
        room_service_cnt: int = None,
    ):
        self.book_service_cnt = book_service_cnt
        self.goods_service_cnt = goods_service_cnt
        self.repair_service_cnt = repair_service_cnt
        self.room_service_cnt = room_service_cnt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.book_service_cnt is not None:
            result['BookServiceCnt'] = self.book_service_cnt

        if self.goods_service_cnt is not None:
            result['GoodsServiceCnt'] = self.goods_service_cnt

        if self.repair_service_cnt is not None:
            result['RepairServiceCnt'] = self.repair_service_cnt

        if self.room_service_cnt is not None:
            result['RoomServiceCnt'] = self.room_service_cnt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BookServiceCnt') is not None:
            self.book_service_cnt = m.get('BookServiceCnt')

        if m.get('GoodsServiceCnt') is not None:
            self.goods_service_cnt = m.get('GoodsServiceCnt')

        if m.get('RepairServiceCnt') is not None:
            self.repair_service_cnt = m.get('RepairServiceCnt')

        if m.get('RoomServiceCnt') is not None:
            self.room_service_cnt = m.get('RoomServiceCnt')

        return self

class QueryHotelRoomDetailResponseBodyResultRoomControlInfo(DaraModel):
    def __init__(
        self,
        app_id: int = None,
        app_name: str = None,
        device_infos: List[main_models.QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos] = None,
        rcu_url: str = None,
        template_id: int = None,
        template_name: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.device_infos = device_infos
        self.rcu_url = rcu_url
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        if self.device_infos:
            for v1 in self.device_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k1 in self.device_infos:
                result['DeviceInfos'].append(k1.to_map() if k1 else None)

        if self.rcu_url is not None:
            result['RcuUrl'] = self.rcu_url

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k1 in m.get('DeviceInfos'):
                temp_model = main_models.QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos()
                self.device_infos.append(temp_model.from_map(k1))

        if m.get('RcuUrl') is not None:
            self.rcu_url = m.get('RcuUrl')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class QueryHotelRoomDetailResponseBodyResultRoomControlInfoDeviceInfos(DaraModel):
    def __init__(
        self,
        category_en_name: str = None,
        category_id: int = None,
        category_name: str = None,
        device_connect_type: str = None,
        device_count: int = None,
        device_id: str = None,
        device_name: str = None,
        location_en_name: str = None,
        location_id: int = None,
        location_name: str = None,
        product_key: str = None,
    ):
        self.category_en_name = category_en_name
        self.category_id = category_id
        self.category_name = category_name
        self.device_connect_type = device_connect_type
        self.device_count = device_count
        self.device_id = device_id
        self.device_name = device_name
        self.location_en_name = location_en_name
        self.location_id = location_id
        self.location_name = location_name
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_en_name is not None:
            result['CategoryEnName'] = self.category_en_name

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.device_connect_type is not None:
            result['DeviceConnectType'] = self.device_connect_type

        if self.device_count is not None:
            result['DeviceCount'] = self.device_count

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.location_en_name is not None:
            result['LocationEnName'] = self.location_en_name

        if self.location_id is not None:
            result['LocationId'] = self.location_id

        if self.location_name is not None:
            result['LocationName'] = self.location_name

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryEnName') is not None:
            self.category_en_name = m.get('CategoryEnName')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('DeviceConnectType') is not None:
            self.device_connect_type = m.get('DeviceConnectType')

        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('LocationEnName') is not None:
            self.location_en_name = m.get('LocationEnName')

        if m.get('LocationId') is not None:
            self.location_id = m.get('LocationId')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

class QueryHotelRoomDetailResponseBodyResultOtherService(DaraModel):
    def __init__(
        self,
        open_call: bool = None,
        unhandle_tickets: int = None,
    ):
        self.open_call = open_call
        self.unhandle_tickets = unhandle_tickets

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_call is not None:
            result['OpenCall'] = self.open_call

        if self.unhandle_tickets is not None:
            result['UnhandleTickets'] = self.unhandle_tickets

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenCall') is not None:
            self.open_call = m.get('OpenCall')

        if m.get('UnhandleTickets') is not None:
            self.unhandle_tickets = m.get('UnhandleTickets')

        return self

class QueryHotelRoomDetailResponseBodyResultDeviceInfos(DaraModel):
    def __init__(
        self,
        active_time: str = None,
        device_name: str = None,
        firmware_version: str = None,
        mac: str = None,
        online_status: int = None,
        sn: str = None,
        uuid: str = None,
    ):
        self.active_time = active_time
        self.device_name = device_name
        self.firmware_version = firmware_version
        self.mac = mac
        self.online_status = online_status
        self.sn = sn
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_time is not None:
            result['ActiveTime'] = self.active_time

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version

        if self.mac is not None:
            result['Mac'] = self.mac

        if self.online_status is not None:
            result['OnlineStatus'] = self.online_status

        if self.sn is not None:
            result['Sn'] = self.sn

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveTime') is not None:
            self.active_time = m.get('ActiveTime')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')

        if m.get('Mac') is not None:
            self.mac = m.get('Mac')

        if m.get('OnlineStatus') is not None:
            self.online_status = m.get('OnlineStatus')

        if m.get('Sn') is not None:
            self.sn = m.get('Sn')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self

class QueryHotelRoomDetailResponseBodyResultAuthAccounts(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        auth_time: str = None,
    ):
        self.account_name = account_name
        self.auth_time = auth_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.auth_time is not None:
            result['AuthTime'] = self.auth_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AuthTime') is not None:
            self.auth_time = m.get('AuthTime')

        return self

