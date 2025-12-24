# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImageFromFamilyResponseBody(DaraModel):
    def __init__(
        self,
        image: main_models.DescribeImageFromFamilyResponseBodyImage = None,
        request_id: str = None,
    ):
        # The image information.
        self.image = image
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['Image'] = self.image.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            temp_model = main_models.DescribeImageFromFamilyResponseBodyImage()
            self.image = temp_model.from_map(m.get('Image'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeImageFromFamilyResponseBodyImage(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        creation_time: str = None,
        description: str = None,
        disk_device_mappings: main_models.DescribeImageFromFamilyResponseBodyImageDiskDeviceMappings = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        image_version: str = None,
        is_copied: bool = None,
        is_self_shared: str = None,
        is_subscribed: bool = None,
        is_support_cloudinit: bool = None,
        is_support_io_optimized: bool = None,
        osname: str = None,
        ostype: str = None,
        platform: str = None,
        product_code: str = None,
        progress: str = None,
        size: int = None,
        status: str = None,
        tags: main_models.DescribeImageFromFamilyResponseBodyImageTags = None,
        usage: str = None,
    ):
        # The architecture of the image. Valid values:
        # 
        # *   i386
        # *   x86_64
        self.architecture = architecture
        # The time when the image was created.
        self.creation_time = creation_time
        # The description of the volume.
        self.description = description
        # The mappings between the disk and the snapshot in the image.
        self.disk_device_mappings = disk_device_mappings
        # The name of the image family.
        self.image_family = image_family
        # The image ID.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The alias of the image owner. Valid values:
        # 
        # *   system: public images provided by Alibaba Cloud
        # *   self: your custom images
        # *   others: shared images from other Alibaba Cloud accounts
        # *   marketplace: Alibaba Cloud Marketplace images
        self.image_owner_alias = image_owner_alias
        # The image version.
        self.image_version = image_version
        # Indicates whether the image is a copy of another image.
        self.is_copied = is_copied
        # Indicates whether the custom image was shared to other Alibaba Cloud accounts.
        self.is_self_shared = is_self_shared
        # Indicates whether you have subscribed to the service terms of the image product corresponding to the image product code.
        self.is_subscribed = is_subscribed
        # Indicates whether cloud-init is supported.
        self.is_support_cloudinit = is_support_cloudinit
        # Indicates whether the image can be used on I/O optimized instances.
        self.is_support_io_optimized = is_support_io_optimized
        # The display name of the operating system in Chinese.
        self.osname = osname
        # The type of the operating system. Valid values:
        # 
        # *   windows
        # *   linux
        self.ostype = ostype
        # The operating system.
        self.platform = platform
        # The product code of the Alibaba Cloud Marketplace image.
        self.product_code = product_code
        # The image creation progress in percentage.
        self.progress = progress
        # The size of the image. Unit: GiB.
        self.size = size
        # The state of the image. Valid values:
        # 
        # *   UnAvailable
        # *   Available
        # *   Creating
        # *   CreateFailed
        self.status = status
        # The tags of the image.
        self.tags = tags
        # Indicates whether the image has been used to create ECS instances. Valid values:
        # 
        # *   instance: The image was used to create one or more ECS instances.
        # *   none: The image was not used to create ECS instances.
        self.usage = usage

    def validate(self):
        if self.disk_device_mappings:
            self.disk_device_mappings.validate()
        if self.tags:
            self.tags.validate()

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

        if self.disk_device_mappings is not None:
            result['DiskDeviceMappings'] = self.disk_device_mappings.to_map()

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.is_copied is not None:
            result['IsCopied'] = self.is_copied

        if self.is_self_shared is not None:
            result['IsSelfShared'] = self.is_self_shared

        if self.is_subscribed is not None:
            result['IsSubscribed'] = self.is_subscribed

        if self.is_support_cloudinit is not None:
            result['IsSupportCloudinit'] = self.is_support_cloudinit

        if self.is_support_io_optimized is not None:
            result['IsSupportIoOptimized'] = self.is_support_io_optimized

        if self.osname is not None:
            result['OSName'] = self.osname

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

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

        if m.get('DiskDeviceMappings') is not None:
            temp_model = main_models.DescribeImageFromFamilyResponseBodyImageDiskDeviceMappings()
            self.disk_device_mappings = temp_model.from_map(m.get('DiskDeviceMappings'))

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('IsCopied') is not None:
            self.is_copied = m.get('IsCopied')

        if m.get('IsSelfShared') is not None:
            self.is_self_shared = m.get('IsSelfShared')

        if m.get('IsSubscribed') is not None:
            self.is_subscribed = m.get('IsSubscribed')

        if m.get('IsSupportCloudinit') is not None:
            self.is_support_cloudinit = m.get('IsSupportCloudinit')

        if m.get('IsSupportIoOptimized') is not None:
            self.is_support_io_optimized = m.get('IsSupportIoOptimized')

        if m.get('OSName') is not None:
            self.osname = m.get('OSName')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeImageFromFamilyResponseBodyImageTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class DescribeImageFromFamilyResponseBodyImageTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeImageFromFamilyResponseBodyImageTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeImageFromFamilyResponseBodyImageTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeImageFromFamilyResponseBodyImageTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the custom image.
        self.tag_key = tag_key
        # The tag value of the custom image.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeImageFromFamilyResponseBodyImageDiskDeviceMappings(DaraModel):
    def __init__(
        self,
        disk_device_mapping: List[main_models.DescribeImageFromFamilyResponseBodyImageDiskDeviceMappingsDiskDeviceMapping] = None,
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
                temp_model = main_models.DescribeImageFromFamilyResponseBodyImageDiskDeviceMappingsDiskDeviceMapping()
                self.disk_device_mapping.append(temp_model.from_map(k1))

        return self

class DescribeImageFromFamilyResponseBodyImageDiskDeviceMappingsDiskDeviceMapping(DaraModel):
    def __init__(
        self,
        device: str = None,
        format: str = None,
        import_ossbucket: str = None,
        import_ossobject: str = None,
        size: str = None,
        snapshot_id: str = None,
        type: str = None,
    ):
        # The device name of the disk. Example: /dev/xvdb.
        # 
        # >  This parameter will be removed in the future. To ensure compatibility, we recommend that you use other parameters.
        self.device = device
        # The image format.
        self.format = format
        # The OSS bucket that contains the imported image file.
        self.import_ossbucket = import_ossbucket
        # The OSS object to which the imported image belongs.
        self.import_ossobject = import_ossobject
        # The size of the disk. Unit: GiB.
        self.size = size
        # The snapshot ID.
        self.snapshot_id = snapshot_id
        # The image type.
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

        if self.format is not None:
            result['Format'] = self.format

        if self.import_ossbucket is not None:
            result['ImportOSSBucket'] = self.import_ossbucket

        if self.import_ossobject is not None:
            result['ImportOSSObject'] = self.import_ossobject

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('ImportOSSBucket') is not None:
            self.import_ossbucket = m.get('ImportOSSBucket')

        if m.get('ImportOSSObject') is not None:
            self.import_ossobject = m.get('ImportOSSObject')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

