# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImagesResponseBody(DaraModel):
    def __init__(
        self,
        images: main_models.DescribeImagesResponseBodyImages = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information of the images.
        self.images = images
        # The page number returned.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID of the image.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The total number of images.
        self.total_count = total_count

    def validate(self):
        if self.images:
            self.images.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.images is not None:
            result['Images'] = self.images.to_map()

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
        if m.get('Images') is not None:
            temp_model = main_models.DescribeImagesResponseBodyImages()
            self.images = temp_model.from_map(m.get('Images'))

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

class DescribeImagesResponseBodyImages(DaraModel):
    def __init__(
        self,
        image: List[main_models.DescribeImagesResponseBodyImagesImage] = None,
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
                temp_model = main_models.DescribeImagesResponseBodyImagesImage()
                self.image.append(temp_model.from_map(k1))

        return self

class DescribeImagesResponseBodyImagesImage(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        boot_mode: str = None,
        creation_time: str = None,
        description: str = None,
        detection_options: main_models.DescribeImagesResponseBodyImagesImageDetectionOptions = None,
        disk_device_mappings: main_models.DescribeImagesResponseBodyImagesImageDiskDeviceMappings = None,
        features: main_models.DescribeImagesResponseBodyImagesImageFeatures = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        image_owner_id: int = None,
        image_version: str = None,
        is_copied: bool = None,
        is_public: bool = None,
        is_self_shared: str = None,
        is_subscribed: bool = None,
        is_support_cloudinit: bool = None,
        is_support_io_optimized: bool = None,
        license_type: str = None,
        login_as_non_root_supported: bool = None,
        osname: str = None,
        osname_en: str = None,
        ostype: str = None,
        platform: str = None,
        product_code: str = None,
        progress: str = None,
        resource_group_id: str = None,
        size: int = None,
        status: str = None,
        supplier_name: str = None,
        tags: main_models.DescribeImagesResponseBodyImagesImageTags = None,
        usage: str = None,
    ):
        # The architecture of the image. Valid values:
        # 
        # *   i386
        # *   x86_64
        # *   arm64
        self.architecture = architecture
        # The boot mode of the image. Valid values:
        # 
        # *   BIOS: Basic Input/Output System (BIOS)
        # *   UEFI: Unified Extensible Firmware Interface (UEFI)
        # *   UEFI-Preferred: BIOS and UEFI
        # 
        # For information about the image boot modes, see [Image boot modes](~~2244655#b9caa9b8bb1wf~~).
        self.boot_mode = boot_mode
        # The time when the image was created.
        self.creation_time = creation_time
        # The description of the image.
        self.description = description
        # Details about the check performed on the image.
        self.detection_options = detection_options
        # The mappings between disks and snapshots in the image.
        self.disk_device_mappings = disk_device_mappings
        # The feature attributes of the image.
        self.features = features
        # The name of the image family.
        self.image_family = image_family
        # The ID of the image.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # The source of the image. Valid values:
        # 
        # *   system: a public image provided by Alibaba Cloud
        # *   self: a custom image that you created
        # *   others: a shared image from another Alibaba Cloud account or a community image published by another Alibaba Cloud account
        # *   marketplace: an Alibaba Cloud Marketplace image
        self.image_owner_alias = image_owner_alias
        # The ID of the Alibaba Cloud account to which the image belongs. This parameter takes effect only if you query shared images or community images.
        self.image_owner_id = image_owner_id
        # The version of the image.
        self.image_version = image_version
        # Indicates whether the image is a copy of another image.
        self.is_copied = is_copied
        # Indicates whether the image is publicly available. Publicly available images include public images provided by Alibaba Cloud and custom images published as community images. Valid values:
        # 
        # *   true: The image is publicly available.
        # *   false: The image is publicly unavailable.
        self.is_public = is_public
        # Indicates whether the custom image was shared to other Alibaba Cloud accounts.
        self.is_self_shared = is_self_shared
        # Indicates whether you accepted the Terms of Service of the image service that corresponds to the product code.
        self.is_subscribed = is_subscribed
        # Indicates whether the image supports cloud-init.
        self.is_support_cloudinit = is_support_cloudinit
        # Indicates whether the image can be used on I/O optimized instances.
        self.is_support_io_optimized = is_support_io_optimized
        self.license_type = license_type
        # Indicates whether the image supports logons of non-root users. Valid values:
        # 
        # *   true: The image supports logons of non-root users.
        # *   false: The image does not support logons of non-root users.
        self.login_as_non_root_supported = login_as_non_root_supported
        # The display name of the operating system in Chinese.
        self.osname = osname
        # The display name of the operating system in English.
        self.osname_en = osname_en
        # The type of the operating system. Valid values:
        # 
        # *   windows
        # *   linux
        self.ostype = ostype
        # The operating system platform.
        self.platform = platform
        # The Alibaba Cloud Marketplace product code of the image.
        self.product_code = product_code
        # The creation progress of the image. Unit: percent (%).
        self.progress = progress
        # The ID of the resource group to which the image belongs.
        self.resource_group_id = resource_group_id
        # The size of the image. Unit: GiB.
        # 
        # >  If the image contains data disk snapshots, this parameter indicates only the size of the system disk snapshot contained in the image.
        self.size = size
        # The state of the image. Valid values:
        # 
        # *   UnAvailable: The image is unavailable.
        # *   Available: The image is available.
        # *   Creating: The image is being created.
        # *   CreateFailed: The image failed to be created.
        self.status = status
        # The name of the supplier that published the community image.
        self.supplier_name = supplier_name
        # The tags of the image.
        self.tags = tags
        # Indicates whether the image was used to create ECS instances. Valid values:
        # 
        # *   instance: The image was used to create one or more ECS instances.
        # *   none: The image was not used to create ECS instances.
        self.usage = usage

    def validate(self):
        if self.detection_options:
            self.detection_options.validate()
        if self.disk_device_mappings:
            self.disk_device_mappings.validate()
        if self.features:
            self.features.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.boot_mode is not None:
            result['BootMode'] = self.boot_mode

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.detection_options is not None:
            result['DetectionOptions'] = self.detection_options.to_map()

        if self.disk_device_mappings is not None:
            result['DiskDeviceMappings'] = self.disk_device_mappings.to_map()

        if self.features is not None:
            result['Features'] = self.features.to_map()

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias

        if self.image_owner_id is not None:
            result['ImageOwnerId'] = self.image_owner_id

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.is_copied is not None:
            result['IsCopied'] = self.is_copied

        if self.is_public is not None:
            result['IsPublic'] = self.is_public

        if self.is_self_shared is not None:
            result['IsSelfShared'] = self.is_self_shared

        if self.is_subscribed is not None:
            result['IsSubscribed'] = self.is_subscribed

        if self.is_support_cloudinit is not None:
            result['IsSupportCloudinit'] = self.is_support_cloudinit

        if self.is_support_io_optimized is not None:
            result['IsSupportIoOptimized'] = self.is_support_io_optimized

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

        if self.login_as_non_root_supported is not None:
            result['LoginAsNonRootSupported'] = self.login_as_non_root_supported

        if self.osname is not None:
            result['OSName'] = self.osname

        if self.osname_en is not None:
            result['OSNameEn'] = self.osname_en

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.size is not None:
            result['Size'] = self.size

        if self.status is not None:
            result['Status'] = self.status

        if self.supplier_name is not None:
            result['SupplierName'] = self.supplier_name

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DetectionOptions') is not None:
            temp_model = main_models.DescribeImagesResponseBodyImagesImageDetectionOptions()
            self.detection_options = temp_model.from_map(m.get('DetectionOptions'))

        if m.get('DiskDeviceMappings') is not None:
            temp_model = main_models.DescribeImagesResponseBodyImagesImageDiskDeviceMappings()
            self.disk_device_mappings = temp_model.from_map(m.get('DiskDeviceMappings'))

        if m.get('Features') is not None:
            temp_model = main_models.DescribeImagesResponseBodyImagesImageFeatures()
            self.features = temp_model.from_map(m.get('Features'))

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')

        if m.get('ImageOwnerId') is not None:
            self.image_owner_id = m.get('ImageOwnerId')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('IsCopied') is not None:
            self.is_copied = m.get('IsCopied')

        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')

        if m.get('IsSelfShared') is not None:
            self.is_self_shared = m.get('IsSelfShared')

        if m.get('IsSubscribed') is not None:
            self.is_subscribed = m.get('IsSubscribed')

        if m.get('IsSupportCloudinit') is not None:
            self.is_support_cloudinit = m.get('IsSupportCloudinit')

        if m.get('IsSupportIoOptimized') is not None:
            self.is_support_io_optimized = m.get('IsSupportIoOptimized')

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

        if m.get('LoginAsNonRootSupported') is not None:
            self.login_as_non_root_supported = m.get('LoginAsNonRootSupported')

        if m.get('OSName') is not None:
            self.osname = m.get('OSName')

        if m.get('OSNameEn') is not None:
            self.osname_en = m.get('OSNameEn')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplierName') is not None:
            self.supplier_name = m.get('SupplierName')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeImagesResponseBodyImagesImageTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class DescribeImagesResponseBodyImagesImageTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeImagesResponseBodyImagesImageTagsTag] = None,
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
                temp_model = main_models.DescribeImagesResponseBodyImagesImageTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeImagesResponseBodyImagesImageTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the image.
        self.tag_key = tag_key
        # The tag value of the image.
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

class DescribeImagesResponseBodyImagesImageFeatures(DaraModel):
    def __init__(
        self,
        cpu_online_downgrade: str = None,
        cpu_online_upgrade: str = None,
        imds_support: str = None,
        memory_online_downgrade: str = None,
        memory_online_upgrade: str = None,
        nvme_support: str = None,
    ):
        self.cpu_online_downgrade = cpu_online_downgrade
        self.cpu_online_upgrade = cpu_online_upgrade
        # The image metadata access mode. Valid values:
        # 
        # *   v1: You cannot set the image metadata access mode to security hardening when you create instances from the image.
        # *   v2: You can set the image metadata access mode to security hardening when you create instances from the image.
        # 
        # [Overview of instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.imds_support = imds_support
        self.memory_online_downgrade = memory_online_downgrade
        self.memory_online_upgrade = memory_online_upgrade
        # Indicates whether the image supports the Non-Volatile Memory Express (NVMe) protocol. Valid values:
        # 
        # *   supported: The image supports the NVMe protocol. Instances created from the image also support the NVMe protocol.
        # *   unsupported: The image does not support the NVMe protocol. Instances created from the image do not support the NVMe protocol.
        self.nvme_support = nvme_support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_online_downgrade is not None:
            result['CpuOnlineDowngrade'] = self.cpu_online_downgrade

        if self.cpu_online_upgrade is not None:
            result['CpuOnlineUpgrade'] = self.cpu_online_upgrade

        if self.imds_support is not None:
            result['ImdsSupport'] = self.imds_support

        if self.memory_online_downgrade is not None:
            result['MemoryOnlineDowngrade'] = self.memory_online_downgrade

        if self.memory_online_upgrade is not None:
            result['MemoryOnlineUpgrade'] = self.memory_online_upgrade

        if self.nvme_support is not None:
            result['NvmeSupport'] = self.nvme_support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuOnlineDowngrade') is not None:
            self.cpu_online_downgrade = m.get('CpuOnlineDowngrade')

        if m.get('CpuOnlineUpgrade') is not None:
            self.cpu_online_upgrade = m.get('CpuOnlineUpgrade')

        if m.get('ImdsSupport') is not None:
            self.imds_support = m.get('ImdsSupport')

        if m.get('MemoryOnlineDowngrade') is not None:
            self.memory_online_downgrade = m.get('MemoryOnlineDowngrade')

        if m.get('MemoryOnlineUpgrade') is not None:
            self.memory_online_upgrade = m.get('MemoryOnlineUpgrade')

        if m.get('NvmeSupport') is not None:
            self.nvme_support = m.get('NvmeSupport')

        return self

class DescribeImagesResponseBodyImagesImageDiskDeviceMappings(DaraModel):
    def __init__(
        self,
        disk_device_mapping: List[main_models.DescribeImagesResponseBodyImagesImageDiskDeviceMappingsDiskDeviceMapping] = None,
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
                temp_model = main_models.DescribeImagesResponseBodyImagesImageDiskDeviceMappingsDiskDeviceMapping()
                self.disk_device_mapping.append(temp_model.from_map(k1))

        return self

class DescribeImagesResponseBodyImagesImageDiskDeviceMappingsDiskDeviceMapping(DaraModel):
    def __init__(
        self,
        device: str = None,
        encrypted: bool = None,
        format: str = None,
        import_ossbucket: str = None,
        import_ossobject: str = None,
        progress: str = None,
        remain_time: int = None,
        size: str = None,
        snapshot_id: str = None,
        type: str = None,
    ):
        # The device name of the disk. Example: /dev/xvdb.
        self.device = device
        # >  This parameter is in invitational preview.
        self.encrypted = encrypted
        # The format of the image.
        self.format = format
        # The Object Storage Service (OSS) bucket that contains the imported image file.
        self.import_ossbucket = import_ossbucket
        # The OSS object that corresponds to the imported image file.
        self.import_ossobject = import_ossobject
        # The progress of the image copy task.
        self.progress = progress
        # The remaining time of the image copy task. Unit: seconds.
        self.remain_time = remain_time
        # The size of the disk. Unit: GiB.
        self.size = size
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id
        # The type of the image.
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

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.format is not None:
            result['Format'] = self.format

        if self.import_ossbucket is not None:
            result['ImportOSSBucket'] = self.import_ossbucket

        if self.import_ossobject is not None:
            result['ImportOSSObject'] = self.import_ossobject

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.remain_time is not None:
            result['RemainTime'] = self.remain_time

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

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('ImportOSSBucket') is not None:
            self.import_ossbucket = m.get('ImportOSSBucket')

        if m.get('ImportOSSObject') is not None:
            self.import_ossobject = m.get('ImportOSSObject')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('RemainTime') is not None:
            self.remain_time = m.get('RemainTime')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeImagesResponseBodyImagesImageDetectionOptions(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeImagesResponseBodyImagesImageDetectionOptionsItems = None,
        status: str = None,
    ):
        # The check items.
        self.items = items
        # The state of the image check task. Valid values:
        # 
        # *   Processing
        # *   Finished
        self.status = status

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeImagesResponseBodyImagesImageDetectionOptionsItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeImagesResponseBodyImagesImageDetectionOptionsItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.DescribeImagesResponseBodyImagesImageDetectionOptionsItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.DescribeImagesResponseBodyImagesImageDetectionOptionsItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class DescribeImagesResponseBodyImagesImageDetectionOptionsItemsItem(DaraModel):
    def __init__(
        self,
        name: str = None,
        risk_code: str = None,
        risk_level: str = None,
        value: str = None,
    ):
        # The name of the check item.
        self.name = name
        # The risk that the check item may have.
        self.risk_code = risk_code
        # The severity of the risk that the check item of the imported custom image has. If the check item is at risk, this parameter is returned. If the check item is not at risk, this parameter is not returned.
        # 
        # Valid values:
        # 
        # *   High: The check item is a high-risk item that may affect the startup of the instance. We recommend that you handle the risk.
        # *   Medium: The check item is a medium-risk item that may affect the startup performance or configurations of the instance. We recommend that you handle the risk.
        self.risk_level = risk_level
        # The result of the check item.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.risk_code is not None:
            result['RiskCode'] = self.risk_code

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RiskCode') is not None:
            self.risk_code = m.get('RiskCode')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

