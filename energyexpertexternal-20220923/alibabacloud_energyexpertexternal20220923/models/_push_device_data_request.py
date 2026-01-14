# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class PushDeviceDataRequest(DaraModel):
    def __init__(
        self,
        device_type: str = None,
        devices: List[main_models.PushDeviceDataRequestDevices] = None,
    ):
        # The type of the device. [View device type definitions](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/Deviceappendixes-en.pdf)
        # 
        # This parameter is required.
        self.device_type = device_type
        # List of devices to which data is pushed.
        # 
        # This parameter is required.
        self.devices = devices

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
        if self.device_type is not None:
            result['deviceType'] = self.device_type

        result['devices'] = []
        if self.devices is not None:
            for k1 in self.devices:
                result['devices'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deviceType') is not None:
            self.device_type = m.get('deviceType')

        self.devices = []
        if m.get('devices') is not None:
            for k1 in m.get('devices'):
                temp_model = main_models.PushDeviceDataRequestDevices()
                self.devices.append(temp_model.from_map(k1))

        return self

class PushDeviceDataRequestDevices(DaraModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        device_id: str = None,
        record_time: str = None,
    ):
        # Measuring point information To avoid accuracy problems, the measurement point data is uniformly transmitted to the string. The function of missing required fields cannot be used normally. Some functions may be affected due to the lack of recommend fields. For details, please refer to the notes of equipment measuring points in the appendix. [Reference Point Definition](https://carbon-doc.oss-cn-hangzhou.aliyuncs.com/Deviceappendixes-en.pdf
        # )
        # 
        # This parameter is required.
        self.data = data
        # If the deviceType parameter is set to 12, 13, or 17, you must set the system_id parameter. The field name is still device_id. If the deviceType parameter is set to 15 or 16, no Other situations will be transmitted.
        # 
        # This parameter is required.
        self.device_id = device_id
        # Data generation time of measuring point.
        # 
        # This parameter is required.
        self.record_time = record_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data

        if self.device_id is not None:
            result['deviceId'] = self.device_id

        if self.record_time is not None:
            result['recordTime'] = self.record_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')

        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')

        if m.get('recordTime') is not None:
            self.record_time = m.get('recordTime')

        return self

