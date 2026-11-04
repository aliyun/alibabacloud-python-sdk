# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryGbSubDeviceListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryGbSubDeviceListResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.error_message = error_message
        self.request_id = request_id
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
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryGbSubDeviceListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryGbSubDeviceListResponseBodyData(DaraModel):
    def __init__(
        self,
        gb_sub_device_list: List[main_models.QueryGbSubDeviceListResponseBodyDataGbSubDeviceList] = None,
        total: int = None,
    ):
        self.gb_sub_device_list = gb_sub_device_list
        self.total = total

    def validate(self):
        if self.gb_sub_device_list:
            for v1 in self.gb_sub_device_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GbSubDeviceList'] = []
        if self.gb_sub_device_list is not None:
            for k1 in self.gb_sub_device_list:
                result['GbSubDeviceList'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gb_sub_device_list = []
        if m.get('GbSubDeviceList') is not None:
            for k1 in m.get('GbSubDeviceList'):
                temp_model = main_models.QueryGbSubDeviceListResponseBodyDataGbSubDeviceList()
                self.gb_sub_device_list.append(temp_model.from_map(k1))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class QueryGbSubDeviceListResponseBodyDataGbSubDeviceList(DaraModel):
    def __init__(
        self,
        device_enable: int = None,
        device_id: str = None,
        device_name: str = None,
        iot_id: str = None,
        product_key: str = None,
    ):
        self.device_enable = device_enable
        self.device_id = device_id
        self.device_name = device_name
        self.iot_id = iot_id
        self.product_key = product_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_enable is not None:
            result['DeviceEnable'] = self.device_enable

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.device_name is not None:
            result['DeviceName'] = self.device_name

        if self.iot_id is not None:
            result['IotId'] = self.iot_id

        if self.product_key is not None:
            result['ProductKey'] = self.product_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceEnable') is not None:
            self.device_enable = m.get('DeviceEnable')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')

        if m.get('IotId') is not None:
            self.iot_id = m.get('IotId')

        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')

        return self

