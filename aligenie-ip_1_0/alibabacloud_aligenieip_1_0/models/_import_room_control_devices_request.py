# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class ImportRoomControlDevicesRequest(DaraModel):
    def __init__(
        self,
        enable_infrared_device_import: str = None,
        enable_mesh_device_import: str = None,
        hotel_id: str = None,
        location_devices: List[main_models.ImportRoomControlDevicesRequestLocationDevices] = None,
        room_no: str = None,
    ):
        self.enable_infrared_device_import = enable_infrared_device_import
        self.enable_mesh_device_import = enable_mesh_device_import
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.location_devices = location_devices
        # This parameter is required.
        self.room_no = room_no

    def validate(self):
        if self.location_devices:
            for v1 in self.location_devices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_infrared_device_import is not None:
            result['EnableInfraredDeviceImport'] = self.enable_infrared_device_import

        if self.enable_mesh_device_import is not None:
            result['EnableMeshDeviceImport'] = self.enable_mesh_device_import

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        result['LocationDevices'] = []
        if self.location_devices is not None:
            for k1 in self.location_devices:
                result['LocationDevices'].append(k1.to_map() if k1 else None)

        if self.room_no is not None:
            result['RoomNo'] = self.room_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInfraredDeviceImport') is not None:
            self.enable_infrared_device_import = m.get('EnableInfraredDeviceImport')

        if m.get('EnableMeshDeviceImport') is not None:
            self.enable_mesh_device_import = m.get('EnableMeshDeviceImport')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        self.location_devices = []
        if m.get('LocationDevices') is not None:
            for k1 in m.get('LocationDevices'):
                temp_model = main_models.ImportRoomControlDevicesRequestLocationDevices()
                self.location_devices.append(temp_model.from_map(k1))

        if m.get('RoomNo') is not None:
            self.room_no = m.get('RoomNo')

        return self

class ImportRoomControlDevicesRequestLocationDevices(DaraModel):
    def __init__(
        self,
        devices: List[main_models.ImportRoomControlDevicesRequestLocationDevicesDevices] = None,
        location: str = None,
        location_name: str = None,
    ):
        self.devices = devices
        # This parameter is required.
        self.location = location
        self.location_name = location_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.devices = []
        if m.get('Devices') is not None:
            for k1 in m.get('Devices'):
                temp_model = main_models.ImportRoomControlDevicesRequestLocationDevicesDevices()
                self.devices.append(temp_model.from_map(k1))

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        return self

class ImportRoomControlDevicesRequestLocationDevicesDevices(DaraModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        brand: str = None,
        city: str = None,
        connect_type: str = None,
        device_name: str = None,
        dn: str = None,
        infrared_id: str = None,
        infrared_index: str = None,
        infrared_version: str = None,
        multi_key_switch_ext: main_models.ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt = None,
        name: str = None,
        number: str = None,
        pk: str = None,
        province: str = None,
        service_provider: str = None,
    ):
        self.alias_list = alias_list
        self.brand = brand
        self.city = city
        self.connect_type = connect_type
        # This parameter is required.
        self.device_name = device_name
        self.dn = dn
        self.infrared_id = infrared_id
        self.infrared_index = infrared_index
        self.infrared_version = infrared_version
        self.multi_key_switch_ext = multi_key_switch_ext
        # This parameter is required.
        self.name = name
        self.number = number
        self.pk = pk
        self.province = province
        self.service_provider = service_provider

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

        if m.get('Dn') is not None:
            self.dn = m.get('Dn')

        if m.get('InfraredId') is not None:
            self.infrared_id = m.get('InfraredId')

        if m.get('InfraredIndex') is not None:
            self.infrared_index = m.get('InfraredIndex')

        if m.get('InfraredVersion') is not None:
            self.infrared_version = m.get('InfraredVersion')

        if m.get('MultiKeySwitchExt') is not None:
            temp_model = main_models.ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt()
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

        return self

class ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExt(DaraModel):
    def __init__(
        self,
        switch_list: List[main_models.ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList] = None,
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
                temp_model = main_models.ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList()
                self.switch_list.append(temp_model.from_map(k1))

        return self

class ImportRoomControlDevicesRequestLocationDevicesDevicesMultiKeySwitchExtSwitchList(DaraModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        category: str = None,
        device_index: int = None,
        device_name: str = None,
        location: str = None,
    ):
        self.alias_list = alias_list
        self.category = category
        self.device_index = device_index
        self.device_name = device_name
        self.location = location

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

        if self.location is not None:
            result['Location'] = self.location

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

        if m.get('Location') is not None:
            self.location = m.get('Location')

        return self

