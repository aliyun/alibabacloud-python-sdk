# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adbai20250812 import models as main_models
from darabonba.model import DaraModel

class GetEmbodiedAIPlatformResourceUsageInfoResponseBody(DaraModel):
    def __init__(
        self,
        gpu_details: List[main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodyGpuDetails] = None,
        max_registered_devices: int = None,
        registered_device_count: int = None,
        request_id: str = None,
        slb_traffic: main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodySlbTraffic = None,
        storage_usage: main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodyStorageUsage = None,
    ):
        self.gpu_details = gpu_details
        self.max_registered_devices = max_registered_devices
        self.registered_device_count = registered_device_count
        # Id of the request
        self.request_id = request_id
        self.slb_traffic = slb_traffic
        self.storage_usage = storage_usage

    def validate(self):
        if self.gpu_details:
            for v1 in self.gpu_details:
                 if v1:
                    v1.validate()
        if self.slb_traffic:
            self.slb_traffic.validate()
        if self.storage_usage:
            self.storage_usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GpuDetails'] = []
        if self.gpu_details is not None:
            for k1 in self.gpu_details:
                result['GpuDetails'].append(k1.to_map() if k1 else None)

        if self.max_registered_devices is not None:
            result['MaxRegisteredDevices'] = self.max_registered_devices

        if self.registered_device_count is not None:
            result['RegisteredDeviceCount'] = self.registered_device_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.slb_traffic is not None:
            result['SlbTraffic'] = self.slb_traffic.to_map()

        if self.storage_usage is not None:
            result['StorageUsage'] = self.storage_usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.gpu_details = []
        if m.get('GpuDetails') is not None:
            for k1 in m.get('GpuDetails'):
                temp_model = main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodyGpuDetails()
                self.gpu_details.append(temp_model.from_map(k1))

        if m.get('MaxRegisteredDevices') is not None:
            self.max_registered_devices = m.get('MaxRegisteredDevices')

        if m.get('RegisteredDeviceCount') is not None:
            self.registered_device_count = m.get('RegisteredDeviceCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlbTraffic') is not None:
            temp_model = main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodySlbTraffic()
            self.slb_traffic = temp_model.from_map(m.get('SlbTraffic'))

        if m.get('StorageUsage') is not None:
            temp_model = main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodyStorageUsage()
            self.storage_usage = temp_model.from_map(m.get('StorageUsage'))

        return self

class GetEmbodiedAIPlatformResourceUsageInfoResponseBodyStorageUsage(DaraModel):
    def __init__(
        self,
        nas: main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodyStorageUsageNas = None,
        oss: main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodyStorageUsageOss = None,
    ):
        self.nas = nas
        self.oss = oss

    def validate(self):
        if self.nas:
            self.nas.validate()
        if self.oss:
            self.oss.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nas is not None:
            result['Nas'] = self.nas.to_map()

        if self.oss is not None:
            result['Oss'] = self.oss.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nas') is not None:
            temp_model = main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodyStorageUsageNas()
            self.nas = temp_model.from_map(m.get('Nas'))

        if m.get('Oss') is not None:
            temp_model = main_models.GetEmbodiedAIPlatformResourceUsageInfoResponseBodyStorageUsageOss()
            self.oss = temp_model.from_map(m.get('Oss'))

        return self

class GetEmbodiedAIPlatformResourceUsageInfoResponseBodyStorageUsageOss(DaraModel):
    def __init__(
        self,
        standard_storage_size: int = None,
    ):
        self.standard_storage_size = standard_storage_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.standard_storage_size is not None:
            result['StandardStorageSize'] = self.standard_storage_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StandardStorageSize') is not None:
            self.standard_storage_size = m.get('StandardStorageSize')

        return self

class GetEmbodiedAIPlatformResourceUsageInfoResponseBodyStorageUsageNas(DaraModel):
    def __init__(
        self,
        metered_size: int = None,
    ):
        self.metered_size = metered_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metered_size is not None:
            result['MeteredSize'] = self.metered_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MeteredSize') is not None:
            self.metered_size = m.get('MeteredSize')

        return self

class GetEmbodiedAIPlatformResourceUsageInfoResponseBodySlbTraffic(DaraModel):
    def __init__(
        self,
        total_bytes_in: int = None,
        total_bytes_out: int = None,
    ):
        self.total_bytes_in = total_bytes_in
        self.total_bytes_out = total_bytes_out

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.total_bytes_in is not None:
            result['TotalBytesIn'] = self.total_bytes_in

        if self.total_bytes_out is not None:
            result['TotalBytesOut'] = self.total_bytes_out

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalBytesIn') is not None:
            self.total_bytes_in = m.get('TotalBytesIn')

        if m.get('TotalBytesOut') is not None:
            self.total_bytes_out = m.get('TotalBytesOut')

        return self

class GetEmbodiedAIPlatformResourceUsageInfoResponseBodyGpuDetails(DaraModel):
    def __init__(
        self,
        gpu_model: str = None,
        total_count: int = None,
    ):
        self.gpu_model = gpu_model
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gpu_model is not None:
            result['GpuModel'] = self.gpu_model

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GpuModel') is not None:
            self.gpu_model = m.get('GpuModel')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

