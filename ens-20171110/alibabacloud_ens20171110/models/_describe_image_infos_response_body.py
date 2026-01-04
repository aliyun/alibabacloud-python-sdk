# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeImageInfosResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        images: main_models.DescribeImageInfosResponseBodyImages = None,
        request_id: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The information about images.
        self.images = images
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.images is not None:
            result['Images'] = self.images.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Images') is not None:
            temp_model = main_models.DescribeImageInfosResponseBodyImages()
            self.images = temp_model.from_map(m.get('Images'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageInfosResponseBodyImages(DaraModel):
    def __init__(
        self,
        image: List[main_models.DescribeImageInfosResponseBodyImagesImage] = None,
    ):
        self.image = image

    def validate(self):
        if self.image:
            for v1 in self.image:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Image'] = []
        if self.image is not None:
            for k1 in self.image:
                result['Image'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image = []
        if m.get('Image') is not None:
            for k1 in m.get('Image'):
                temp_model = main_models.DescribeImageInfosResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k1))

        return self

class DescribeImageInfosResponseBodyImagesImage(DaraModel):
    def __init__(
        self,
        compute_type: str = None,
        description: str = None,
        disk_device_mappings: main_models.DescribeImageInfosResponseBodyImagesImageDiskDeviceMappings = None,
        image_id: str = None,
        image_size: str = None,
        image_version: str = None,
        osname: str = None,
        ostype: str = None,
        region_id: str = None,
    ):
        # The computing type of the image. Valid values:
        # 
        # *   ens_vm: x86 computing.
        # *   arm_vm: ARM computing.
        # *   bare_metal: x86 bare machine.
        # *   pcfarm: heterogeneous computing.
        self.compute_type = compute_type
        # The description of the image.
        self.description = description
        # The mappings between disks and snapshots in the image.
        self.disk_device_mappings = disk_device_mappings
        # The ID of the image.
        self.image_id = image_id
        # The size of the image. Unit: GiB.
        self.image_size = image_size
        # The version of the image.
        self.image_version = image_version
        # The type of the image. Valid values: **centos**, **debian**, **ubuntu**, and **windows**.
        self.osname = osname
        # The type of the operating system.
        self.ostype = ostype
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        if self.disk_device_mappings:
            self.disk_device_mappings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compute_type is not None:
            result['ComputeType'] = self.compute_type

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_device_mappings is not None:
            result['DiskDeviceMappings'] = self.disk_device_mappings.to_map()

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.osname is not None:
            result['OSName'] = self.osname

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputeType') is not None:
            self.compute_type = m.get('ComputeType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskDeviceMappings') is not None:
            temp_model = main_models.DescribeImageInfosResponseBodyImagesImageDiskDeviceMappings()
            self.disk_device_mappings = temp_model.from_map(m.get('DiskDeviceMappings'))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('OSName') is not None:
            self.osname = m.get('OSName')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeImageInfosResponseBodyImagesImageDiskDeviceMappings(DaraModel):
    def __init__(
        self,
        disk_device_mapping: List[main_models.DescribeImageInfosResponseBodyImagesImageDiskDeviceMappingsDiskDeviceMapping] = None,
    ):
        self.disk_device_mapping = disk_device_mapping

    def validate(self):
        if self.disk_device_mapping:
            for v1 in self.disk_device_mapping:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DiskDeviceMapping'] = []
        if self.disk_device_mapping is not None:
            for k1 in self.disk_device_mapping:
                result['DiskDeviceMapping'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.disk_device_mapping = []
        if m.get('DiskDeviceMapping') is not None:
            for k1 in m.get('DiskDeviceMapping'):
                temp_model = main_models.DescribeImageInfosResponseBodyImagesImageDiskDeviceMappingsDiskDeviceMapping()
                self.disk_device_mapping.append(temp_model.from_map(k1))

        return self

class DescribeImageInfosResponseBodyImagesImageDiskDeviceMappingsDiskDeviceMapping(DaraModel):
    def __init__(
        self,
        format: str = None,
        size: str = None,
        type: str = None,
        image_id: str = None,
    ):
        # The format of the image.
        self.format = format
        # The size of the image. Unit: GB.
        self.size = size
        # The type of the disk. Valid values: System and Data.
        self.type = type
        # The ID of the image.
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.format is not None:
            result['Format'] = self.format

        if self.size is not None:
            result['Size'] = self.size

        if self.type is not None:
            result['Type'] = self.type

        if self.image_id is not None:
            result['imageId'] = self.image_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('imageId') is not None:
            self.image_id = m.get('imageId')

        return self

