# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetIpcDeviceInfoResponseBody(DaraModel):
    def __init__(
        self,
        device_infos: List[main_models.GetIpcDeviceInfoResponseBodyDeviceInfos] = None,
        request_id: str = None,
        total: int = None,
    ):
        self.device_infos = device_infos
        self.request_id = request_id
        self.total = total

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
        result['DeviceInfos'] = []
        if self.device_infos is not None:
            for k1 in self.device_infos:
                result['DeviceInfos'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_infos = []
        if m.get('DeviceInfos') is not None:
            for k1 in m.get('DeviceInfos'):
                temp_model = main_models.GetIpcDeviceInfoResponseBodyDeviceInfos()
                self.device_infos.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class GetIpcDeviceInfoResponseBodyDeviceInfos(DaraModel):
    def __init__(
        self,
        capability: str = None,
        device_id: str = None,
        expire_time: str = None,
    ):
        self.capability = capability
        self.device_id = device_id
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capability is not None:
            result['Capability'] = self.capability

        if self.device_id is not None:
            result['DeviceId'] = self.device_id

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            self.capability = m.get('Capability')

        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        return self

