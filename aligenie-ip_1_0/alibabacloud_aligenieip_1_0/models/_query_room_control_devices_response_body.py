# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class QueryRoomControlDevicesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.QueryRoomControlDevicesResponseBodyResult] = None,
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
                temp_model = main_models.QueryRoomControlDevicesResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class QueryRoomControlDevicesResponseBodyResult(DaraModel):
    def __init__(
        self,
        devices: List[main_models.QueryRoomControlDevicesResponseBodyResultDevices] = None,
        location: str = None,
        location_name: str = None,
    ):
        self.devices = devices
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
                temp_model = main_models.QueryRoomControlDevicesResponseBodyResultDevices()
                self.devices.append(temp_model.from_map(k1))

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('LocationName') is not None:
            self.location_name = m.get('LocationName')

        return self

class QueryRoomControlDevicesResponseBodyResultDevices(DaraModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        connect_type: str = None,
        dn: str = None,
        device_name: str = None,
        device_status: str = None,
        multi_key_switch_ext: main_models.QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt = None,
        name: str = None,
        number: str = None,
        pk: str = None,
    ):
        self.alias_list = alias_list
        self.connect_type = connect_type
        self.dn = dn
        self.device_name = device_name
        self.device_status = device_status
        self.multi_key_switch_ext = multi_key_switch_ext
        self.name = name
        self.number = number
        self.pk = pk

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

        if self.connect_type is not None:
            result['ConnectType'] = self.connect_type

        if self.dn is not None:
            result['DN'] = self.dn

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.multi_key_switch_ext is not None:
            result['MultiKeySwitchExt'] = self.multi_key_switch_ext.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.number is not None:
            result['Number'] = self.number

        if self.pk is not None:
            result['PK'] = self.pk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliasList') is not None:
            self.alias_list = m.get('AliasList')

        if m.get('ConnectType') is not None:
            self.connect_type = m.get('ConnectType')

        if m.get('DN') is not None:
            self.dn = m.get('DN')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('MultiKeySwitchExt') is not None:
            temp_model = main_models.QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt()
            self.multi_key_switch_ext = temp_model.from_map(m.get('MultiKeySwitchExt'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Number') is not None:
            self.number = m.get('Number')

        if m.get('PK') is not None:
            self.pk = m.get('PK')

        return self

class QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExt(DaraModel):
    def __init__(
        self,
        switch_list: List[main_models.QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList] = None,
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
                temp_model = main_models.QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList()
                self.switch_list.append(temp_model.from_map(k1))

        return self

class QueryRoomControlDevicesResponseBodyResultDevicesMultiKeySwitchExtSwitchList(DaraModel):
    def __init__(
        self,
        alias_list: List[str] = None,
        category: str = None,
        device_index: int = None,
        device_name: str = None,
        device_status: str = None,
        element_code: str = None,
        location: str = None,
    ):
        self.alias_list = alias_list
        self.category = category
        self.device_index = device_index
        self.device_name = device_name
        self.device_status = device_status
        self.element_code = element_code
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

        if self.device_status is not None:
            result['DeviceStatus'] = self.device_status

        if self.element_code is not None:
            result['ElementCode'] = self.element_code

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

        if m.get('DeviceStatus') is not None:
            self.device_status = m.get('DeviceStatus')

        if m.get('ElementCode') is not None:
            self.element_code = m.get('ElementCode')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        return self

