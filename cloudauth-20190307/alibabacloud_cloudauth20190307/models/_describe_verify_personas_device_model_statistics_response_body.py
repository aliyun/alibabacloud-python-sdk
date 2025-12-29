# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class DescribeVerifyPersonasDeviceModelStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.DescribeVerifyPersonasDeviceModelStatisticsResponseBodyResultObject = None,
    ):
        # ID of this request.
        self.request_id = request_id
        # Query result.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.DescribeVerifyPersonasDeviceModelStatisticsResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class DescribeVerifyPersonasDeviceModelStatisticsResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        all_device_cnt: int = None,
        items: List[main_models.DescribeVerifyPersonasDeviceModelStatisticsResponseBodyResultObjectItems] = None,
    ):
        # Total number of devices.
        self.all_device_cnt = all_device_cnt
        # List of data for different phone models.
        self.items = items

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_device_cnt is not None:
            result['AllDeviceCnt'] = self.all_device_cnt

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDeviceCnt') is not None:
            self.all_device_cnt = m.get('AllDeviceCnt')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeVerifyPersonasDeviceModelStatisticsResponseBodyResultObjectItems()
                self.items.append(temp_model.from_map(k1))

        return self

class DescribeVerifyPersonasDeviceModelStatisticsResponseBodyResultObjectItems(DaraModel):
    def __init__(
        self,
        device_cnt: int = None,
        device_model: str = None,
        device_rate: str = None,
    ):
        # Number of devices.
        self.device_cnt = device_cnt
        # Device model
        self.device_model = device_model
        # The ratio of this device model to the total number of devices.
        self.device_rate = device_rate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_cnt is not None:
            result['DeviceCnt'] = self.device_cnt

        if self.device_model is not None:
            result['DeviceModel'] = self.device_model

        if self.device_rate is not None:
            result['DeviceRate'] = self.device_rate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCnt') is not None:
            self.device_cnt = m.get('DeviceCnt')

        if m.get('DeviceModel') is not None:
            self.device_model = m.get('DeviceModel')

        if m.get('DeviceRate') is not None:
            self.device_rate = m.get('DeviceRate')

        return self

