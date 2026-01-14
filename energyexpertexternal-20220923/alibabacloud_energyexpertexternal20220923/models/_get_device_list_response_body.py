# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetDeviceListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetDeviceListResponseBodyData = None,
        http_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The data returned.
        self.data = data
        # The HTTP status code.
        self.http_code = http_code
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetDeviceListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetDeviceListResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        device_list: List[main_models.GetDeviceListResponseBodyDataDeviceList] = None,
        factory_id: str = None,
        http_code: int = None,
        success: bool = None,
    ):
        # The code returned for the request.
        self.code = code
        # The devices.
        self.device_list = device_list
        # The ID of the site.
        self.factory_id = factory_id
        # The HTTP status code.
        self.http_code = http_code
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.device_list:
            for v1 in self.device_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        result['deviceList'] = []
        if self.device_list is not None:
            for k1 in self.device_list:
                result['deviceList'].append(k1.to_map() if k1 else None)

        if self.factory_id is not None:
            result['factoryId'] = self.factory_id

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        self.device_list = []
        if m.get('deviceList') is not None:
            for k1 in m.get('deviceList'):
                temp_model = main_models.GetDeviceListResponseBodyDataDeviceList()
                self.device_list.append(temp_model.from_map(k1))

        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetDeviceListResponseBodyDataDeviceList(DaraModel):
    def __init__(
        self,
        device_id: str = None,
        device_name: str = None,
        first_type_name: str = None,
        info: main_models.GetDeviceListResponseBodyDataDeviceListInfo = None,
        parent_device: str = None,
        second_type_name: str = None,
    ):
        # The device ID.
        self.device_id = device_id
        # The device name.
        self.device_name = device_name
        # The level 1 meter type.
        self.first_type_name = first_type_name
        # The device information.
        self.info = info
        # The ID of the parent device.
        self.parent_device = parent_device
        # The level 2 meter type.
        self.second_type_name = second_type_name

    def validate(self):
        if self.info:
            self.info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_id is not None:
            result['deviceId'] = self.device_id

        if self.device_name is not None:
            result['deviceName'] = self.device_name

        if self.first_type_name is not None:
            result['firstTypeName'] = self.first_type_name

        if self.info is not None:
            result['info'] = self.info.to_map()

        if self.parent_device is not None:
            result['parentDevice'] = self.parent_device

        if self.second_type_name is not None:
            result['secondTypeName'] = self.second_type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')

        if m.get('deviceName') is not None:
            self.device_name = m.get('deviceName')

        if m.get('firstTypeName') is not None:
            self.first_type_name = m.get('firstTypeName')

        if m.get('info') is not None:
            temp_model = main_models.GetDeviceListResponseBodyDataDeviceListInfo()
            self.info = temp_model.from_map(m.get('info'))

        if m.get('parentDevice') is not None:
            self.parent_device = m.get('parentDevice')

        if m.get('secondTypeName') is not None:
            self.second_type_name = m.get('secondTypeName')

        return self

class GetDeviceListResponseBodyDataDeviceListInfo(DaraModel):
    def __init__(
        self,
        const_kva: int = None,
        ct: int = None,
        magnification: int = None,
        pressure: int = None,
        pt: int = None,
    ):
        # The rated capacity.
        # Unit is kVA.
        self.const_kva = const_kva
        # The transformation ratio of current.
        self.ct = ct
        # The magnification ratio.
        self.magnification = magnification
        # The high and low voltage.
        self.pressure = pressure
        # The transformation ratio of voltage.
        self.pt = pt

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.const_kva is not None:
            result['constKva'] = self.const_kva

        if self.ct is not None:
            result['ct'] = self.ct

        if self.magnification is not None:
            result['magnification'] = self.magnification

        if self.pressure is not None:
            result['pressure'] = self.pressure

        if self.pt is not None:
            result['pt'] = self.pt

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('constKva') is not None:
            self.const_kva = m.get('constKva')

        if m.get('ct') is not None:
            self.ct = m.get('ct')

        if m.get('magnification') is not None:
            self.magnification = m.get('magnification')

        if m.get('pressure') is not None:
            self.pressure = m.get('pressure')

        if m.get('pt') is not None:
            self.pt = m.get('pt')

        return self

