# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeBundlesResponseBody(DaraModel):
    def __init__(
        self,
        bundles: List[main_models.DescribeBundlesResponseBodyBundles] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The cloud computer templates.
        self.bundles = bundles
        # The token that is used for the next query. If this parameter is empty, all results have been returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.bundles:
            for v1 in self.bundles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Bundles'] = []
        if self.bundles is not None:
            for k1 in self.bundles:
                result['Bundles'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bundles = []
        if m.get('Bundles') is not None:
            for k1 in m.get('Bundles'):
                temp_model = main_models.DescribeBundlesResponseBodyBundles()
                self.bundles.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBundlesResponseBodyBundles(DaraModel):
    def __init__(
        self,
        bundle_id: str = None,
        bundle_name: str = None,
        bundle_type: str = None,
        creation_time: str = None,
        data_disk_category: str = None,
        description: str = None,
        desktop_type: str = None,
        desktop_type_attribute: main_models.DescribeBundlesResponseBodyBundlesDesktopTypeAttribute = None,
        desktop_type_family: str = None,
        disks: List[main_models.DescribeBundlesResponseBodyBundlesDisks] = None,
        image_id: str = None,
        image_name: str = None,
        image_status: str = None,
        language: str = None,
        os_type: str = None,
        platform: str = None,
        protocol_type: str = None,
        session_type: str = None,
        stock_state: str = None,
        system_disk_category: str = None,
        volume_encryption_enabled: bool = None,
        volume_encryption_key: str = None,
    ):
        # The ID of the cloud computer template.
        self.bundle_id = bundle_id
        # The name of the cloud computer template.
        self.bundle_name = bundle_name
        # The type of the cloud computer template.
        # 
        # Valid values:
        # 
        # *   SYSTEM: system template
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CUSTOM: custom template
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.bundle_type = bundle_type
        # The time when the cloud computer template was created.
        self.creation_time = creation_time
        # The category of the data disk.
        # 
        # Valid values:
        # 
        # *   cloud_efficiency: the ultra disk
        # *   cloud_auto: the standard SSD.
        # *   cloud_essd: the ESSD. Take note that only specific cloud computer types support ESSDs.
        self.data_disk_category = data_disk_category
        # The description of the cloud computer template.
        self.description = description
        # The instance type of the cloud computer.
        self.desktop_type = desktop_type
        # The details of the cloud computer instance type.
        self.desktop_type_attribute = desktop_type_attribute
        # The instance family of the cloud computer.
        # 
        # Valid values:
        # 
        # *   eds.graphics: graphical instance family
        # *   eds.hf: instance family with a high clock speed
        # *   eds.general: general-purpose instance family
        self.desktop_type_family = desktop_type_family
        # Details of the disks.
        self.disks = disks
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The status of the image.
        self.image_status = image_status
        # The OS language of the image.
        # 
        # Valid values:
        # 
        # *   en-US: English
        # *   zh-HK: Chinese, Traditional (Hong Kong, China)
        # *   zh-CN: Simplified Chinese
        # *   ja-JP: Japanese
        self.language = language
        # The type of the OS.
        # 
        # Valid values:
        # 
        # *   Linux
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.os_type = os_type
        # The OS.
        # 
        # Valid values:
        # 
        # *   Ubuntu
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows Server 2022
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   UOS
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CentOS
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows Server 2019
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Windows Server 2016
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.platform = platform
        # The protocol type.
        # 
        # Valid values:
        # 
        # *   HDX: HDX protocol
        # *   ASP: in-house ASP
        self.protocol_type = protocol_type
        # The session type.
        # 
        # Valid values:
        # 
        # *   0: single-session
        # *   1: multi-session
        self.session_type = session_type
        # The inventory status of the cloud computer instance type. This parameter is returned only if you set the `CheckStock` parameter to `true`.
        self.stock_state = stock_state
        # The category of the system disk.
        # 
        # Valid values:
        # 
        # *   cloud_efficiency: the ultra disk
        # *   cloud_auto: the standard SSD.
        # *   cloud_essd: the Enterprise SSD (ESSD). Take note that only specific cloud computer types support ESSDs.
        self.system_disk_category = system_disk_category
        # Indicates whether disk encryption is enabled.
        self.volume_encryption_enabled = volume_encryption_enabled
        # The ID of the Key Management Service (KMS) key that is used when disk encryption is enabled.
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        if self.desktop_type_attribute:
            self.desktop_type_attribute.validate()
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name

        if self.bundle_type is not None:
            result['BundleType'] = self.bundle_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_disk_category is not None:
            result['DataDiskCategory'] = self.data_disk_category

        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.desktop_type_attribute is not None:
            result['DesktopTypeAttribute'] = self.desktop_type_attribute.to_map()

        if self.desktop_type_family is not None:
            result['DesktopTypeFamily'] = self.desktop_type_family

        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_status is not None:
            result['ImageStatus'] = self.image_status

        if self.language is not None:
            result['Language'] = self.language

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.session_type is not None:
            result['SessionType'] = self.session_type

        if self.stock_state is not None:
            result['StockState'] = self.stock_state

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.volume_encryption_enabled is not None:
            result['VolumeEncryptionEnabled'] = self.volume_encryption_enabled

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')

        if m.get('BundleType') is not None:
            self.bundle_type = m.get('BundleType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataDiskCategory') is not None:
            self.data_disk_category = m.get('DataDiskCategory')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('DesktopTypeAttribute') is not None:
            temp_model = main_models.DescribeBundlesResponseBodyBundlesDesktopTypeAttribute()
            self.desktop_type_attribute = temp_model.from_map(m.get('DesktopTypeAttribute'))

        if m.get('DesktopTypeFamily') is not None:
            self.desktop_type_family = m.get('DesktopTypeFamily')

        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.DescribeBundlesResponseBodyBundlesDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageStatus') is not None:
            self.image_status = m.get('ImageStatus')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('SessionType') is not None:
            self.session_type = m.get('SessionType')

        if m.get('StockState') is not None:
            self.stock_state = m.get('StockState')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('VolumeEncryptionEnabled') is not None:
            self.volume_encryption_enabled = m.get('VolumeEncryptionEnabled')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        return self

class DescribeBundlesResponseBodyBundlesDisks(DaraModel):
    def __init__(
        self,
        disk_performance_level: str = None,
        disk_size: int = None,
        disk_type: str = None,
    ):
        # The PL of the disk.
        # 
        # Valid values:
        # 
        # *   PL1
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PL0
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PL3
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   PL2
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.disk_performance_level = disk_performance_level
        # The size of the disk. Unit: GiB.
        self.disk_size = disk_size
        # The type of the disk.
        # 
        # Valid values:
        # 
        # *   SYSTEM: system disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   DATA: data disk
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.disk_type = disk_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_performance_level is not None:
            result['DiskPerformanceLevel'] = self.disk_performance_level

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskPerformanceLevel') is not None:
            self.disk_performance_level = m.get('DiskPerformanceLevel')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        return self

class DescribeBundlesResponseBodyBundlesDesktopTypeAttribute(DaraModel):
    def __init__(
        self,
        cpu_count: int = None,
        gpu_count: float = None,
        gpu_spec: str = None,
        memory_size: int = None,
    ):
        # The number of vCPUs.
        self.cpu_count = cpu_count
        # The number of GPUs.
        self.gpu_count = gpu_count
        # The GPU type.
        self.gpu_spec = gpu_spec
        # The memory size. Unit: MiB.
        self.memory_size = memory_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count

        if self.gpu_count is not None:
            result['GpuCount'] = self.gpu_count

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')

        if m.get('GpuCount') is not None:
            self.gpu_count = m.get('GpuCount')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        return self

