# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRCImageListResponseBody(DaraModel):
    def __init__(
        self,
        images: List[main_models.DescribeRCImageListResponseBodyImages] = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the images.
        self.images = images
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The total number of images.
        self.total_count = total_count

    def validate(self):
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.DescribeRCImageListResponseBodyImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRCImageListResponseBodyImages(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        creation_time: str = None,
        description: str = None,
        disk_device_mappings: List[main_models.DescribeRCImageListResponseBodyImagesDiskDeviceMappings] = None,
        image_id: str = None,
        image_name: str = None,
        image_version: str = None,
        is_public: bool = None,
        is_support_rds_custom: bool = None,
        osname: str = None,
        osname_en: str = None,
        ostype: str = None,
        platform: str = None,
        size: int = None,
        status: str = None,
        usage: str = None,
    ):
        # The image architecture. Valid values:
        # 
        # *   x86_64
        # *   arm64
        self.architecture = architecture
        # The time when the image was created.
        self.creation_time = creation_time
        # The description of the image.
        self.description = description
        self.disk_device_mappings = disk_device_mappings
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The image version.
        self.image_version = image_version
        # Indicates whether the image is a public image. Public images include public images provided by Alibaba Cloud and custom images published as community images.
        # 
        # *   **true**: The image is a public image.
        # *   **false**: The image is not a public image.
        self.is_public = is_public
        self.is_support_rds_custom = is_support_rds_custom
        # The display name of the operating system in Chinese.
        self.osname = osname
        # The display name of the operating system in English.
        self.osname_en = osname_en
        # The type of the operating system. Valid values:
        # 
        # *   **windows**
        # *   **linux**
        self.ostype = ostype
        self.platform = platform
        # The image size. Unit: GiB.
        self.size = size
        # The image status. Valid values:
        # 
        # *   **Unavailable**
        # *   **Available**
        # *   **Creating**
        # *   **CreateFailed**
        self.status = status
        # Indicates whether the image is used by the RDS Custom instance. Valid values:
        # 
        # *   **instance**: The image is used to create one or more RDS Custom instances.
        # *   **none**: The image is not used to create RDS Custom instances.
        self.usage = usage

    def validate(self):
        if self.disk_device_mappings:
            for v1 in self.disk_device_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        result['DiskDeviceMappings'] = []
        if self.disk_device_mappings is not None:
            for k1 in self.disk_device_mappings:
                result['DiskDeviceMappings'].append(k1.to_map() if k1 else None)

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.is_public is not None:
            result['IsPublic'] = self.is_public

        if self.is_support_rds_custom is not None:
            result['IsSupportRdsCustom'] = self.is_support_rds_custom

        if self.osname is not None:
            result['OSName'] = self.osname

        if self.osname_en is not None:
            result['OSNameEn'] = self.osname_en

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.disk_device_mappings = []
        if m.get('DiskDeviceMappings') is not None:
            for k1 in m.get('DiskDeviceMappings'):
                temp_model = main_models.DescribeRCImageListResponseBodyImagesDiskDeviceMappings()
                self.disk_device_mappings.append(temp_model.from_map(k1))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')

        if m.get('IsSupportRdsCustom') is not None:
            self.is_support_rds_custom = m.get('IsSupportRdsCustom')

        if m.get('OSName') is not None:
            self.osname = m.get('OSName')

        if m.get('OSNameEn') is not None:
            self.osname_en = m.get('OSNameEn')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class DescribeRCImageListResponseBodyImagesDiskDeviceMappings(DaraModel):
    def __init__(
        self,
        device: str = None,
        size: str = None,
        type: str = None,
    ):
        self.device = device
        self.size = size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device is not None:
            result['Device'] = self.device

        if self.size is not None:
            result['Size'] = self.size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

