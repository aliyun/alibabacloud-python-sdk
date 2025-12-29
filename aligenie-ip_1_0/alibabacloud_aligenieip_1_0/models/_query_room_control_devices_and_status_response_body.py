# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class QueryRoomControlDevicesAndStatusResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.QueryRoomControlDevicesAndStatusResponseBodyResult] = None,
        status_code: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.status_code = status_code

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

        if self.status_code is not None:
            result['StatusCode'] = self.status_code

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
                temp_model = main_models.QueryRoomControlDevicesAndStatusResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')

        return self

class QueryRoomControlDevicesAndStatusResponseBodyResult(DaraModel):
    def __init__(
        self,
        devices: List[main_models.QueryRoomControlDevicesAndStatusResponseBodyResultDevices] = None,
        location: str = None,
        location_name: str = None,
        room_no: str = None,
    ):
        self.devices = devices
        self.location = location
        self.location_name = location_name
        self.room_no = room_no

    def validate(self):
        if self.devices:
            for v1 in self.devices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Devices'] = []
        if self.devices is not None:
            for k1 in self.devices:
                result['Devices'].append(k1.to_map() if k1 else None)

        if self.location is not None:
            result['Location'] = self.location

        if self.location_name is not None:
            result['LocationName'] = self.location_name

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k1 in m.get('Devices'):
                temp_model = main_models.QueryRoomControlDevicesAndStatusResponseBodyResultDevices()
                self.devices.append(temp_model.from_map(k1))

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

class QueryRoomControlDevicesAndStatusResponseBodyResultDevices(DaraModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        brand: str = None,
        city: str = None,
        connect_type: str = None,
        device_name: str = None,
        device_status: str = None,
        dn: str = None,
        infrared_id: str = None,
        infrared_index: str = None,
        infrared_version: str = None,
        multi_key_switch_ext: main_models.QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExt = None,
        name: str = None,
        number: str = None,
        pk: str = None,
        province: str = None,
        service_provider: str = None,
        status: Dict[str, str] = None,
    ):
        self.alias_list = alias_list
        self.brand = brand
        self.city = city
        self.connect_type = connect_type
        self.device_name = device_name
        self.device_status = device_status
        self.dn = dn
        self.infrared_id = infrared_id
        self.infrared_index = infrared_index
        self.infrared_version = infrared_version
        self.multi_key_switch_ext = multi_key_switch_ext
        self.name = name
        self.number = number
        self.pk = pk
        self.province = province
        self.service_provider = service_provider
        self.status = status

    def validate(self):
        if self.multi_key_switch_ext:
            self.multi_key_switch_ext.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list

        if self.brand is not None:
            result['Brand'] = self.brand

        if self.city is not None:
            result['City'] = self.city

        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.dn is not None:
            result['Dn'] = self.dn

        if self.infrared_id is not None:
            result['InfraredId'] = self.infrared_id

        if self.infrared_index is not None:
            result['InfraredIndex'] = self.infrared_index

        if self.infrared_version is not None:
            result['InfraredVersion'] = self.infrared_version

        if self.multi_key_switch_ext is not None:
            result['MultiKeySwitchExt'] = self.multi_key_switch_ext.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.number is not None:
            result['Number'] = self.number

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.province is not None:
            result['Province'] = self.province

        if self.service_provider is not None:
            result['ServiceProvider'] = self.service_provider

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')

        if m.get('Brand') is not None:
            self.brand = m.get('Brand')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('Dn') is not None:
            self.dn = m.get('Dn')

        if m.get('InfraredId') is not None:
            self.infrared_id = m.get('InfraredId')

        if m.get('InfraredIndex') is not None:
            self.infrared_index = m.get('InfraredIndex')

        if m.get('InfraredVersion') is not None:
            self.infrared_version = m.get('InfraredVersion')

        if m.get('MultiKeySwitchExt') is not None:
            temp_model = main_models.QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExt()
            self.multi_key_switch_ext = temp_model.from_map(m.get('MultiKeySwitchExt'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        if m.get('ServiceProvider') is not None:
            self.service_provider = m.get('ServiceProvider')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExt(DaraModel):
    def __init__(
        self,
        switch_list: List[main_models.QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExtSwitchList] = None,
    ):
        self.switch_list = switch_list

    def validate(self):
        if self.switch_list:
            for v1 in self.switch_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SwitchList'] = []
        if self.switch_list is not None:
            for k1 in self.switch_list:
                result['SwitchList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.switch_list = []
        if m.get('SwitchList') is not None:
            for k1 in m.get('SwitchList'):
                temp_model = main_models.QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExtSwitchList()
                self.switch_list.append(temp_model.from_map(k1))

        return self

class QueryRoomControlDevicesAndStatusResponseBodyResultDevicesMultiKeySwitchExtSwitchList(DaraModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        category: str = None,
        device_index: int = None,
        device_name: str = None,
        device_status: str = None,
        element_code: str = None,
        location: str = None,
        status: Dict[str, str] = None,
        tags: List[str] = None,
    ):
        self.alias_list = alias_list
        self.category = category
        self.device_index = device_index
        self.device_name = device_name
        self.device_status = device_status
        self.element_code = element_code
        self.location = location
        self.status = status
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias_list is not None:
            result['AliasList'] = self.alias_list

        if self.category is not None:
            result['Category'] = self.category

        if self.device_index is not None:
            result['DeviceIndex'] = self.device_index

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.element_code is not None:
            result['ElementCode'] = self.element_code

        if self.location is not None:
            result['Location'] = self.location

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeviceIndex') is not None:
            self.device_index = m.get('DeviceIndex')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('ElementCode') is not None:
            self.element_code = m.get('ElementCode')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

