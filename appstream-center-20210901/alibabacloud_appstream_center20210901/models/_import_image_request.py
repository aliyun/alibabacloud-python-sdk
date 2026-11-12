# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportImageRequest(DaraModel):
    def __init__(
        self,
        biz_region_id: str = None,
        biz_type: int = None,
        boot_mode: str = None,
        description: str = None,
        enable_security_check: bool = None,
        gpu_category: bool = None,
        gpu_driver_type: str = None,
        image_name: str = None,
        license_type: str = None,
        os_type: str = None,
        oss_object_path: str = None,
        product_type: str = None,
        protocol_type: str = None,
        system_disk_size: int = None,
    ):
        # The business region ID. Example: cn-hangzhou.
        self.biz_region_id = biz_region_id
        # The business line to which the image belongs. Default value: 1.
        self.biz_type = biz_type
        # The boot mode of the image. Valid values:
        # - BIOS: legacy BIOS boot.
        # - UEFI: UEFI boot.
        self.boot_mode = boot_mode
        # The description of the image.
        self.description = description
        # Specifies whether to enable the image security check. Valid values:
        # - true: enables the security check.
        # - false: disables the security check.
        self.enable_security_check = enable_security_check
        # Specifies whether the image is a GPU image. Valid values:
        # - true: yes.
        # - false: no.
        self.gpu_category = gpu_category
        # The GPU driver type. Valid values:
        # - gpu_grid9: GRID 9 driver.
        # - gpu_grid12: GRID 12 driver.
        # - gpu_custom: custom driver.
        self.gpu_driver_type = gpu_driver_type
        # The name of the image after it is imported. This parameter cannot be empty.
        self.image_name = image_name
        # The operating system license type. Valid values:
        # - Auto: automatically selected.
        # - Aliyun: provided by Alibaba Cloud.
        # - BYOL: Bring Your Own License.
        # Default value: Auto.
        self.license_type = license_type
        # The operating system type of the image file. It must be consistent with the actual operating system of the image, such as Windows or Linux.
        self.os_type = os_type
        # The complete OSS object URL of the image file to be imported, including the bucket domain name and file path. The file must be uploaded before you call this operation. Example: https://BucketName.oss-cn-hangzhou.aliyuncs.com/FilePath.
        self.oss_object_path = oss_object_path
        # The product type. Currently, only CloudDesktop (cloud desktop) is supported.
        self.product_type = product_type
        # The connection protocol of the image. Valid values: ASP and HDX. Default value: ASP.
        self.protocol_type = protocol_type
        # The size of the system cloud disk. Unit: GiB.
        self.system_disk_size = system_disk_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.boot_mode is not None:
            result['BootMode'] = self.boot_mode

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

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.protocol_type is not None:
            result['ProtocolType'] = self.protocol_type

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')

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

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('ProtocolType') is not None:
            self.protocol_type = m.get('ProtocolType')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        return self

