# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateBundleRequest(DaraModel):
    def __init__(
        self,
        bundle_name: str = None,
        description: str = None,
        desktop_type: str = None,
        image_id: str = None,
        language: str = None,
        region_id: str = None,
        root_disk_performance_level: str = None,
        root_disk_size_gib: int = None,
        user_disk_performance_level: str = None,
        user_disk_size_gib: List[int] = None,
    ):
        # The name of the cloud computer template.
        self.bundle_name = bundle_name
        # The description of the cloud computer template.
        self.description = description
        # The instance type of the cloud computers. You can call the [DescribeBundles](https://help.aliyun.com/document_detail/436974.html) operation to query cloud computer templates and obtain the instance types supported by the cloud computers from the `DesktopType` response parameter.
        # 
        # >  If you want the template to use a non-GPU-accelerated image, you can only select a non-GPU-accelerated instance type. If you want the template to use a GPU-accelerated image, you can only select a GPU-accelerated instance type.
        # 
        # This parameter is required.
        self.desktop_type = desktop_type
        # The ID of the image.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The OS language. This parameter is available only for system images. Valid values:
        # 
        # *   zh-CN: Simplified Chinese
        # *   zh-HK: Traditional Chinese (Hong Kong)
        # *   en-US: American English
        # *   ja-JP: Japanese
        self.language = language
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The performance level (PL) of the system disk. When the cloud computer instance type that is specified by the DesktopType parameter is set to a graphical instance type or instance type with a high clock speed, you can set the performance level of the disks. For more information about the differences among disks at different PLs, see [Enhanced SSDs](https://help.aliyun.com/document_detail/122389.html).
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
        self.root_disk_performance_level = root_disk_performance_level
        # The size of the system disk. Unit: GiB. The value of this parameter must be consistent with the system disk size supported by the cloud computer instance type. For more information, see [Overview](https://help.aliyun.com/document_detail/188609.html).
        # 
        # This parameter is required.
        self.root_disk_size_gib = root_disk_size_gib
        # The PL of the data disk. When the cloud computer instance type that is specified by the DesktopType parameter is set to a graphical instance type or instance type with a high clock speed, you can set the performance level of the disks. For more information about the differences among disks at different PLs, see [Enhanced SSDs](https://help.aliyun.com/document_detail/122389.html).
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
        self.user_disk_performance_level = user_disk_performance_level
        # The data disk sizes. You can configure only one data disk.
        # 
        # This parameter is required.
        self.user_disk_size_gib = user_disk_size_gib

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_name is not None:
            result['BundleName'] = self.bundle_name

        if self.description is not None:
            result['Description'] = self.description

        if self.desktop_type is not None:
            result['DesktopType'] = self.desktop_type

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.language is not None:
            result['Language'] = self.language

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.root_disk_performance_level is not None:
            result['RootDiskPerformanceLevel'] = self.root_disk_performance_level

        if self.root_disk_size_gib is not None:
            result['RootDiskSizeGib'] = self.root_disk_size_gib

        if self.user_disk_performance_level is not None:
            result['UserDiskPerformanceLevel'] = self.user_disk_performance_level

        if self.user_disk_size_gib is not None:
            result['UserDiskSizeGib'] = self.user_disk_size_gib

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleName') is not None:
            self.bundle_name = m.get('BundleName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DesktopType') is not None:
            self.desktop_type = m.get('DesktopType')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RootDiskPerformanceLevel') is not None:
            self.root_disk_performance_level = m.get('RootDiskPerformanceLevel')

        if m.get('RootDiskSizeGib') is not None:
            self.root_disk_size_gib = m.get('RootDiskSizeGib')

        if m.get('UserDiskPerformanceLevel') is not None:
            self.user_disk_performance_level = m.get('UserDiskPerformanceLevel')

        if m.get('UserDiskSizeGib') is not None:
            self.user_disk_size_gib = m.get('UserDiskSizeGib')

        return self

