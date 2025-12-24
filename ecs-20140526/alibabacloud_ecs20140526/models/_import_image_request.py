# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ImportImageRequest(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        boot_mode: str = None,
        client_token: str = None,
        description: str = None,
        detection_strategy: str = None,
        disk_device_mapping: List[main_models.ImportImageRequestDiskDeviceMapping] = None,
        dry_run: bool = None,
        features: main_models.ImportImageRequestFeatures = None,
        image_name: str = None,
        license_type: str = None,
        ostype: str = None,
        owner_id: int = None,
        platform: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_name: str = None,
        storage_location_arn: str = None,
        tag: List[main_models.ImportImageRequestTag] = None,
    ):
        # The system architecture. Valid values:
        # 
        # *   i386
        # *   x86_64
        # *   arm64
        # 
        # Default value: x86_64.
        self.architecture = architecture
        # The boot mode of the image. Valid values:
        # 
        # *   BIOS
        # *   UEFI
        # 
        # Default value: BIOS. If you set `Architecture` to arm64, set this parameter to UEFI.
        # 
        # > Make sure that you are aware of the boot modes supported by the specified image, as thehe modified boot mode needs to be supported by the image. This way, instances that use this image can start.
        self.boot_mode = boot_mode
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. **The token can contain only ASCII characters and cannot exceed 64 characters in length.** For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The image description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The mode in which to check the image. If you do not specify this parameter, the image is not checked. Only the standard check mode is supported.
        # 
        # >  This parameter is supported for most Linux and Windows operating system versions. For more information about image check items and operating system limits for image check, see [Overview](https://help.aliyun.com/document_detail/439819.html) and [Operating system limits for image check](https://help.aliyun.com/document_detail/475800.html).
        self.detection_strategy = detection_strategy
        # Details about the custom images.
        self.disk_device_mapping = disk_device_mapping
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   true: performs only a dry run. The system checks the request for potential issues, including invalid AccessKey pairs, unauthorized RAM users, and missing parameter values. If the request fails the dry run, an error message is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   false: performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # The attributes of the image.
        self.features = features
        # The image name. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `acs:` or `aliyun`. The name cannot contain `http://` or `https://`. The name can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-).
        self.image_name = image_name
        # The type of the license used to activate the operating system after the image is imported. Valid values:
        # 
        # *   Auto: ECS checks the operating system of the image and allocates a license to the operating system. ECS first checks whether the operating system distribution specified by `Platform` has a license allocated through an official Alibaba Cloud channel. If yes, the allocated license is used. If no, the license that comes with the source operating system is used.
        # *   Aliyun: The license allocated through an official Alibaba Cloud channel is used for the operating system distribution specified by `Platform`.
        # *   BYOL: The license that comes with the source operating system is used. In this case, make sure that your license key is eligible for use in Alibaba Cloud.
        # 
        # Default value: Auto.
        self.license_type = license_type
        # The operating system platform. Valid values:
        # 
        # *   windows
        # *   linux
        # 
        # Default value: linux.
        self.ostype = ostype
        self.owner_id = owner_id
        # The operating system distribution. Valid values:
        # 
        # *   Aliyun
        # *   Anolis
        # *   CentOS
        # *   Ubuntu
        # *   CoreOS
        # *   SUSE
        # *   Debian
        # *   OpenSUSE
        # *   FreeBSD
        # *   RedHat
        # *   Kylin
        # *   UOS
        # *   Fedora
        # *   Fedora CoreOS
        # *   CentOS Stream
        # *   AlmaLinux
        # *   Rocky Linux
        # *   Gentoo
        # *   Customized Linux
        # *   Others Linux
        # *   Windows Server 2022
        # *   Windows Server 2019
        # *   Windows Server 2016
        # *   Windows Server 2012
        # *   Windows Server 2008
        # *   Windows Server 2003
        # 
        # Default value: Others Linux.
        self.platform = platform
        # The region ID of the source image. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which to assign the image.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the RAM role used to import the image.
        self.role_name = role_name
        # The Alibaba Cloud Resource Name (ARN) of the cloud box, which is used to uniquely identify a storage location in the cloud.
        # 
        # >  Specify this parameter only if you import an image from OSS on CloudBox. Otherwise, you do not need to specify this parameter. For more information, see [What is OSS on CloudBox?](https://help.aliyun.com/document_detail/430190.html)
        # 
        # The ARN must be in the following format: `arn:acs:cloudbox:{RegionId}:{AliUid}:cloudbox/{CloudBoxId}`. Replace `{RegionId}` with the region ID of the cloud box, `{AliUid}` with the ID of the Alibaba Cloud account to which the cloud box belongs, and `{CloudBoxId}` with the ID of the cloud box.
        self.storage_location_arn = storage_location_arn
        # The image tags.
        self.tag = tag

    def validate(self):
        if self.disk_device_mapping:
            for v1 in self.disk_device_mapping:
                 if v1:
                    v1.validate()
        if self.features:
            self.features.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.boot_mode is not None:
            result['BootMode'] = self.boot_mode

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.detection_strategy is not None:
            result['DetectionStrategy'] = self.detection_strategy

        result['DiskDeviceMapping'] = []
        if self.disk_device_mapping is not None:
            for k1 in self.disk_device_mapping:
                result['DiskDeviceMapping'].append(k1.to_map() if k1 else None)

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.features is not None:
            result['Features'] = self.features.to_map()

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.storage_location_arn is not None:
            result['StorageLocationArn'] = self.storage_location_arn

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DetectionStrategy') is not None:
            self.detection_strategy = m.get('DetectionStrategy')

        self.disk_device_mapping = []
        if m.get('DiskDeviceMapping') is not None:
            for k1 in m.get('DiskDeviceMapping'):
                temp_model = main_models.ImportImageRequestDiskDeviceMapping()
                self.disk_device_mapping.append(temp_model.from_map(k1))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Features') is not None:
            temp_model = main_models.ImportImageRequestFeatures()
            self.features = temp_model.from_map(m.get('Features'))

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('StorageLocationArn') is not None:
            self.storage_location_arn = m.get('StorageLocationArn')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ImportImageRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ImportImageRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the image. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag key cannot start with `acs:` or `aliyun`.
        self.key = key
        # The value of tag N of the image. Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. The tag value cannot start with `acs:`.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ImportImageRequestFeatures(DaraModel):
    def __init__(
        self,
        imds_support: str = None,
        nvme_support: str = None,
    ):
        # The metadata access mode version of the image. Valid values:
        # 
        # *   v1: You cannot set the metadata access mode to security hardening when you create instances from the image.
        # *   v2: You can set the metadata access mode to security hardening when you create instances from the image.
        # 
        # Default value: v1.
        self.imds_support = imds_support
        # Specifies whether the image supports the Non-Volatile Memory Express (NVMe) protocol. Valid values:
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
        if self.imds_support is not None:
            result['ImdsSupport'] = self.imds_support

        if self.nvme_support is not None:
            result['NvmeSupport'] = self.nvme_support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImdsSupport') is not None:
            self.imds_support = m.get('ImdsSupport')

        if m.get('NvmeSupport') is not None:
            self.nvme_support = m.get('NvmeSupport')

        return self

class ImportImageRequestDiskDeviceMapping(DaraModel):
    def __init__(
        self,
        device: str = None,
        disk_im_size: int = None,
        disk_image_size: int = None,
        format: str = None,
        ossbucket: str = None,
        ossobject: str = None,
    ):
        # The device name of disk N in the custom image.
        # 
        # >  This parameter will be removed in the future. We recommend that you do not use this parameter to ensure future compatibility.
        self.device = device
        # The size of disk N in the custom image. Unit: GiB.
        # 
        # You can use this parameter to specify the sizes of the system disk and data disks in the custom image. When you specify the size of the system disk, make sure that the specified size is greater than or equal to the size of the imported image file. Unit: GiB. Valid values:
        # 
        # *   When the N value is 1, this parameter specifies the size of the system disk in the custom image. Valid values: 1 to 2048.
        # *   When the N value is an integer in the range of 2 to 17, this parameter specifies the size of a data disk in the custom image. Valid values: 1 to 2048.
        # 
        # After the image file is uploaded to an OSS bucket, you can view the size of the image file in the OSS bucket.
        # 
        # >  This parameter will be removed in the future. We recommend that you use `DiskDeviceMapping.N.DiskImageSize` to ensure future compatibility.
        self.disk_im_size = disk_im_size
        # The size of disk N in the custom image after the source image is imported.
        # 
        # You can use this parameter to specify the sizes of the system disk and data disks in the custom image. When you specify the size of the system disk, make sure that the specified size is greater than or equal to the size of the imported image file. Unit: GiB. Valid values:
        # 
        # *   When the N value is 1, this parameter specifies the size of the system disk in the custom image. Valid values: 1 to 2048.
        # *   When the N value is an integer in the range of 2 to 17, this parameter specifies the size of a data disk in the custom image. Valid values: 1 to 2048.
        # 
        # After the image file is uploaded to an OSS bucket, you can view the size of the image file in the OSS bucket.
        self.disk_image_size = disk_image_size
        # The format of the source image. Valid values:
        # 
        # *   RAW
        # *   VHD
        # *   QCOW2
        # *   VMDK (invitational preview)
        # 
        # This parameter is empty by default, which indicates that the system checks the image format and uses the check result as the value of this parameter.
        self.format = format
        # The Object Storage Service (OSS) bucket where the image file is stored.
        # 
        # >  Before you import images for the first time, you must use RAM to authorize ECS to access your OSS buckets. If ECS is not authorized to access your OSS buckets, the `NoSetRoletoECSServiceAcount` error code is returned when you call the ImportImage operation. For more information, see **Usage notes**.
        self.ossbucket = ossbucket
        # The name (key) of the object that the image file is stored as in the OSS bucket.
        self.ossobject = ossobject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device is not None:
            result['Device'] = self.device

        if self.disk_im_size is not None:
            result['DiskImSize'] = self.disk_im_size

        if self.disk_image_size is not None:
            result['DiskImageSize'] = self.disk_image_size

        if self.format is not None:
            result['Format'] = self.format

        if self.ossbucket is not None:
            result['OSSBucket'] = self.ossbucket

        if self.ossobject is not None:
            result['OSSObject'] = self.ossobject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskImSize') is not None:
            self.disk_im_size = m.get('DiskImSize')

        if m.get('DiskImageSize') is not None:
            self.disk_image_size = m.get('DiskImageSize')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSObject') is not None:
            self.ossobject = m.get('OSSObject')

        return self

