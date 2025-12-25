# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_push20160801 import models as main_models
from darabonba.model import DaraModel

class CheckDevicesResponseBody(DaraModel):
    def __init__(
        self,
        device_check_infos: main_models.CheckDevicesResponseBodyDeviceCheckInfos = None,
        request_id: str = None,
    ):
        self.device_check_infos = device_check_infos
        self.request_id = request_id

    def validate(self):
        if self.device_check_infos:
            self.device_check_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_check_infos is not None:
            result['DeviceCheckInfos'] = self.device_check_infos.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceCheckInfos') is not None:
            temp_model = main_models.CheckDevicesResponseBodyDeviceCheckInfos()
            self.device_check_infos = temp_model.from_map(m.get('DeviceCheckInfos'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckDevicesResponseBodyDeviceCheckInfos(DaraModel):
    def __init__(
        self,
        device_check_info: List[main_models.CheckDevicesResponseBodyDeviceCheckInfosDeviceCheckInfo] = None,
    ):
        self.device_check_info = device_check_info

    def validate(self):
        if self.device_check_info:
            for v1 in self.device_check_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DeviceCheckInfo'] = []
        if self.device_check_info is not None:
            for k1 in self.device_check_info:
                result['DeviceCheckInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_check_info = []
        if m.get('DeviceCheckInfo') is not None:
            for k1 in m.get('DeviceCheckInfo'):
                temp_model = main_models.CheckDevicesResponseBodyDeviceCheckInfosDeviceCheckInfo()
                self.device_check_info.append(temp_model.from_map(k1))

        return self

class CheckDevicesResponseBodyDeviceCheckInfosDeviceCheckInfo(DaraModel):
    def __init__(
        self,
        available: bool = None,
        device_id: str = None,
    ):
        self.available = available
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available is not None:
            result['Available'] = self.available

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Available') is not None:
            self.available = m.get('Available')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        return self

