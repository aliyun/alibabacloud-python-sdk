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
        # The cloud computer specifications. You can call [DescribeBundles](https://help.aliyun.com/document_detail/436974.html) to query cloud computer templates and obtain the supported cloud computer specifications from the `DesktopType` parameter in the response.
        # 
        # > Non-GPU images can only use non-GPU specifications, and GPU images can only use GPU specifications.
        # 
        # This parameter is required.
        self.desktop_type = desktop_type
        # The image ID.
        # 
        # This parameter is required.
        self.image_id = image_id
        # The operating system language. Currently, only system images are supported. Valid values:
        # 
        # - zh-CN: Simplified Chinese.
        # - zh-HK: Traditional Chinese (Hong Kong (China)).
        # - en-US: English.
        # - ja-JP: Japanese.
        self.language = language
        # The region ID. You can call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The performance level of the system cloud disk. When the cloud computer specifications are set to graphics or high frequency, you can configure the cloud disk performance level. For more information about the differences between performance levels, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html). Settings: standard SSD and ESSD cloud disks are supported.
        self.root_disk_performance_level = root_disk_performance_level
        # The system disk size. Unit: GiB. The supported system disk sizes correspond to the specifications. For more information, see [Overview of cloud computer specifications](https://help.aliyun.com/document_detail/188609.html).
        # 
        # This parameter is required.
        self.root_disk_size_gib = root_disk_size_gib
        # The performance level of the data cloud disk. When the cloud computer specifications are set to graphics or high frequency, you can configure the cloud disk performance level. For more information about the differences between performance levels, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html). Settings: standard SSD and ESSD cloud disks are supported.
        self.user_disk_performance_level = user_disk_performance_level
        # The list of data disk sizes. Currently, only one data disk can be configured.
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

