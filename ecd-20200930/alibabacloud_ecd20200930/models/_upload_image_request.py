# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadImageRequest(DaraModel):
    def __init__(
        self,
        boot_mode: str = None,
        data_disk_size: int = None,
        description: str = None,
        enable_security_check: bool = None,
        gpu_category: bool = None,
        gpu_driver_type: str = None,
        image_name: str = None,
        license_type: str = None,
        os_type: str = None,
        oss_object_path: str = None,
        protocol_type: str = None,
        region_id: str = None,
        system_disk_size: str = None,
    ):
        self.boot_mode = boot_mode
        # The data cloud disk size. Valid values: 80 to 500. Unit: GiB.
        self.data_disk_size = data_disk_size
        # The description of the image. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable security check.
        self.enable_security_check = enable_security_check
        # Specifies whether the image is a GPU image.
        self.gpu_category = gpu_category
        # The type of the pre-installed GPU driver.
        self.gpu_driver_type = gpu_driver_type
        # The image name. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. It can contain digits, colons (:), underscores (_), or hyphens (-).
        # 
        # This parameter is required.
        self.image_name = image_name
        # The license type used to activate the operating system after the image is imported. Valid values:
        # 
        # - Auto: Alibaba Cloud detects the source operating system and assigns a license. In automatic mode, the system first checks whether an Alibaba Cloud official license is available for the `Platform` you specified and assigns it to the imported image. If no such license is available, the system switches to BYOL (Bring Your Own License) mode.
        # - Aliyun: Uses an Alibaba Cloud official license based on the `Platform` you specified.
        # - BYOL: Uses the license that comes with the source operating system. When you use BYOL, make sure that your license key supports use on Alibaba Cloud.
        # 
        # Default value: Auto.
        # 
        # > Systems such as Windows 10 cannot be activated through Alibaba Cloud. Set `LicenseType` to BYOL for custom activation.
        self.license_type = license_type
        # The operating system type.
        self.os_type = os_type
        # The OSS object path of the image file.
        # 
        # This parameter is required.
        self.oss_object_path = oss_object_path
        # The protocol type.
        self.protocol_type = protocol_type
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The system cloud disk size. Unit: GiB.
        # 
        # > The system cloud disk size cannot be smaller than the image file size.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boot_mode is not None:
            result['BootMode'] = self.boot_mode

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_security_check is not None:
            result['EnableSecurityCheck'] = self.enable_security_check

        if self.gpu_category is not None:
            result['GpuCategory'] = self.gpu_category

        if self.gpu_driver_type is not None:
            result['GpuDriverType'] = self.gpu_driver_type

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.oss_object_path is not None:
            result['OssObjectPath'] = self.oss_object_path

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableSecurityCheck') is not None:
            self.enable_security_check = m.get('EnableSecurityCheck')

        if m.get('GpuCategory') is not None:
            self.gpu_category = m.get('GpuCategory')

        if m.get('GpuDriverType') is not None:
            self.gpu_driver_type = m.get('GpuDriverType')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('OssObjectPath') is not None:
            self.oss_object_path = m.get('OssObjectPath')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

