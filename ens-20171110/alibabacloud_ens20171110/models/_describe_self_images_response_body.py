# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeSelfImagesResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        images: main_models.DescribeSelfImagesResponseBodyImages = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The HTTP status code that is returned.
        self.code = code
        # The image information.
        self.images = images
        # The page number.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 50. Default value: 10.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Images') is not None:
            temp_model = main_models.DescribeSelfImagesResponseBodyImages()
            self.images = temp_model.from_map(m.get('Images'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSelfImagesResponseBodyImages(DaraModel):
    def __init__(
        self,
        image: List[main_models.DescribeSelfImagesResponseBodyImagesImage] = None,
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
                temp_model = main_models.DescribeSelfImagesResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k1))

        return self

class DescribeSelfImagesResponseBodyImagesImage(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        compute_type: str = None,
        creation_time: str = None,
        disk_device_mappings: main_models.DescribeSelfImagesResponseBodyImagesImageDiskDeviceMappings = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        image_size: str = None,
        image_storage_size: str = None,
        instance_id: str = None,
        os_version: str = None,
        platform: str = None,
        region_id: str = None,
        snapshot_id: str = None,
        status: str = None,
    ):
        # The image architecture. Valid values:
        # 
        # *   i386
        # *   x86_64
        self.architecture = architecture
        # Computing type. ens_vm/ens: x86 computing. bare_metal: x86 bare machine or x86 bare metal. arm_vm: ARM computing. arm_bare_metal: ARM bare machine or ARM bare metal. pcfarm: heterogeneous computing.
        self.compute_type = compute_type
        # The image creation time. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The mappings between the disk and the snapshot in the image.
        self.disk_device_mappings = disk_device_mappings
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The source of the image. Valid values:
        # 
        # *   **others**: a custom image that is shared by other Alibaba Cloud accounts.
        # *   **self**: your own custom image.
        self.image_owner_alias = image_owner_alias
        # The size of the image. Unit: GiB.
        self.image_size = image_size
        # The size of the image storage.
        self.image_storage_size = image_storage_size
        # The ID of the instance.
        self.instance_id = instance_id
        # The operating system version.
        self.os_version = os_version
        # The platform.
        # 
        # *   centos
        # *   ubuntu
        # *   alios
        # *   debian
        # *   rhel
        # *   windows
        self.platform = platform
        # The ID of the region.
        self.region_id = region_id
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The state of the image.
        # 
        # *   Creating.
        # *   Packing.
        # *   Uploading.
        # *   Pack_failed.
        # *   Upload_failed.
        # *   Available: Only images in the Available state can be used and operated.
        # *   Unavailable.
        # *   Copying.
        self.status = status

    def validate(self):
        if self.disk_device_mappings:
            self.disk_device_mappings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.compute_type is not None:
            result['ComputeType'] = self.compute_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.disk_device_mappings is not None:
            result['DiskDeviceMappings'] = self.disk_device_mappings.to_map()

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias

        if self.image_size is not None:
            result['ImageSize'] = self.image_size

        if self.image_storage_size is not None:
            result['ImageStorageSize'] = self.image_storage_size

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.os_version is not None:
            result['OsVersion'] = self.os_version

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('ComputeType') is not None:
            self.compute_type = m.get('ComputeType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DiskDeviceMappings') is not None:
            temp_model = main_models.DescribeSelfImagesResponseBodyImagesImageDiskDeviceMappings()
            self.disk_device_mappings = temp_model.from_map(m.get('DiskDeviceMappings'))

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')

        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')

        if m.get('ImageStorageSize') is not None:
            self.image_storage_size = m.get('ImageStorageSize')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OsVersion') is not None:
            self.os_version = m.get('OsVersion')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeSelfImagesResponseBodyImagesImageDiskDeviceMappings(DaraModel):
    def __init__(
        self,
        disk_device_mapping: List[main_models.DescribeSelfImagesResponseBodyImagesImageDiskDeviceMappingsDiskDeviceMapping] = None,
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
                temp_model = main_models.DescribeSelfImagesResponseBodyImagesImageDiskDeviceMappingsDiskDeviceMapping()
                self.disk_device_mapping.append(temp_model.from_map(k1))

        return self

class DescribeSelfImagesResponseBodyImagesImageDiskDeviceMappingsDiskDeviceMapping(DaraModel):
    def __init__(
        self,
        format: str = None,
        size: str = None,
        type: str = None,
        image_id: str = None,
    ):
        # The format of the image.
        self.format = format
        # The size of the disk. Unit: GiB.
        self.size = size
        # The type of the disk. Valid values:
        # 
        # *   system: system disk.
        # *   data: data disk.
        self.type = type
        # The ID of image.
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

