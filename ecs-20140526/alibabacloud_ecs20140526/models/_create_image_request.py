# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateImageRequest(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        boot_mode: str = None,
        client_token: str = None,
        description: str = None,
        detection_strategy: str = None,
        disk_device_mapping: List[main_models.CreateImageRequestDiskDeviceMapping] = None,
        dry_run: bool = None,
        features: main_models.CreateImageRequestFeatures = None,
        image_family: str = None,
        image_name: str = None,
        image_version: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        platform: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        snapshot_id: str = None,
        tag: List[main_models.CreateImageRequestTag] = None,
    ):
        # The system disk architecture. If you create the image\\"s system disk from a data disk snapshot, you must specify this parameter to identify the system disk architecture. Valid values:
        # 
        # - i386
        # 
        # - x86_64
        # 
        # - arm64
        # 
        # Default value: x86_64.
        self.architecture = architecture
        # The boot mode of the image. Valid values:
        # 
        # - BIOS: BIOS boot mode.
        # 
        # - UEFI: UEFI boot mode.
        # 
        # - UEFI-Preferred: The image supports both BIOS and UEFI boot modes. The UEFI boot mode is preferred. This is the default value.
        # 
        # >Notice: 
        # 
        # If you specify a boot mode that the image does not support, instances created from the image may fail to start. Before you specify this parameter, ensure you know the boot modes that the image supports. For more information, see [Boot modes](~~2244655#b9caa9b8bb1wf~~).
        self.boot_mode = boot_mode
        # A client-generated token to ensure the request is idempotent. You must ensure that the token is unique across different requests. The `ClientToken` value can contain only ASCII characters and cannot exceed 64 characters. For more information, see [How to ensure idempotency](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The image description. It must be 2 to 256 characters long and cannot start with http\\:// or https\\://.
        self.description = description
        # The image check policy. If you do not specify this parameter, no check is performed. Only the Standard mode is supported.
        # 
        # > This feature is supported for most Linux and Windows versions. For more information about the check items and the operating systems that support this feature, see [Overview of image check](https://help.aliyun.com/document_detail/439819.html) and [Operating systems that support image check](https://help.aliyun.com/document_detail/475800.html).
        self.detection_strategy = detection_strategy
        # The mappings between disks and snapshots used to create the custom image. If you need to create a custom image from a system disk snapshot and data disk snapshots, specify this parameter.
        self.disk_device_mapping = disk_device_mapping
        # Specifies whether to perform a dry run to check the request. Valid values:
        # 
        # - true: performs a dry run but does not create the image. The system checks whether your AccessKey pair is valid, whether RAM users are granted permissions, and whether the required parameters are specified. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # 
        # - false: Sends the request to perform the operation. If the request is valid, a 2xx HTTP status code is returned and the image is created.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # The image attributes.
        self.features = features
        # The name of the image family. The name must be 2 to 128 characters long and start with a letter or a Chinese character. It cannot start with aliyun or acs:, nor contain http\\:// or https\\://. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        self.image_family = image_family
        # The name of the image. The name must be 2 to 128 characters long. It must start with a letter or a Chinese character and must not start with http\\:// or https\\://. The name can contain digits, colons (:), underscores (_), and hyphens (-).
        self.image_name = image_name
        # The version of the image.
        # 
        # > If you specify an instance ID (`InstanceId`) and the instance was created from an Alibaba Cloud Marketplace image (or a custom image based on a Marketplace image), this parameter must match the `ImageVersion` of the instance\\"s image or be left empty.
        self.image_version = image_version
        # The ID of the instance. This parameter is required when you create a custom image from an instance.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The operating system distribution. You must specify this parameter to identify the operating system distribution when you use a data disk snapshot to create the image\\"s system disk. Valid values:
        # 
        # - Aliyun
        # 
        # - Anolis
        # 
        # - CentOS
        # 
        # - Ubuntu
        # 
        # - CoreOS
        # 
        # - SUSE
        # 
        # - Debian
        # 
        # - OpenSUSE
        # 
        # - FreeBSD
        # 
        # - RedHat
        # 
        # - Kylin
        # 
        # - UOS
        # 
        # - Fedora
        # 
        # - Fedora CoreOS
        # 
        # - CentOS Stream
        # 
        # - AlmaLinux
        # 
        # - Rocky Linux
        # 
        # - Gentoo
        # 
        # - Customized Linux
        # 
        # - Others Linux
        # 
        # - Windows Server 2022
        # 
        # - Windows Server 2019
        # 
        # - Windows Server 2016
        # 
        # - Windows Server 2012
        # 
        # - Windows Server 2008
        # 
        # - Windows Server 2003
        # 
        # Default value: Others Linux.
        self.platform = platform
        # The ID of the region where the image will be created. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to get the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which to add the custom image. If you do not specify this parameter, the image is added to the default resource group.
        # 
        # > As a RAM user, you must have the required permissions to call this operation. If you leave `ResourceGroupId` empty, the `Forbidden: User not authorized to operate on the specified resource` error is returned if you lack permissions on the default resource group. To resolve this issue, specify the ID of a resource group for which you have permissions, or ask an administrator to grant you permissions on the default resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the snapshot used to create the custom image.
        # 
        # > If you create a custom image from only a system disk snapshot, you can use either this parameter or the `DiskDeviceMapping.N.SnapshotId` parameter. If you want to include data disk snapshots, you must use the `DiskDeviceMapping.N.SnapshotId` parameter to specify the snapshots.
        self.snapshot_id = snapshot_id
        # The tags to add to the image.
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

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

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

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

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
                temp_model = main_models.CreateImageRequestDiskDeviceMapping()
                self.disk_device_mapping.append(temp_model.from_map(k1))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Features') is not None:
            temp_model = main_models.CreateImageRequestFeatures()
            self.features = temp_model.from_map(m.get('Features'))

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

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

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateImageRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateImageRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the image.
        # 
        # > For compatibility, we recommend that you use the `Tag.N.Key` parameter.
        self.key = key
        # The value of tag N to add to the image. Valid values of N: 1 to 20. The tag value can be an empty string, up to 128 characters long, and cannot start with `acs:` or contain `http://` or `https://`.
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

class CreateImageRequestFeatures(DaraModel):
    def __init__(
        self,
        imds_support: str = None,
    ):
        # The instance metadata access mode. Valid values:
        # 
        # - v1: The normal mode. When you create an ECS instance from an image that has the metadata access mode set to this value, you cannot configure the instance metadata access mode as Enforced.
        # 
        # - v2: The enforced mode. When you create an ECS instance from an image that has the metadata access mode set to this value, you can configure the instance metadata access mode as Enforced.
        # 
        # Default value: v1 if you create the image from a snapshot. If you create the image from an instance, the value is inherited from the source instance\\"s image.
        self.imds_support = imds_support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.imds_support is not None:
            result['ImdsSupport'] = self.imds_support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImdsSupport') is not None:
            self.imds_support = m.get('ImdsSupport')

        return self

class CreateImageRequestDiskDeviceMapping(DaraModel):
    def __init__(
        self,
        device: str = None,
        disk_type: str = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        # The device name of the disk in the custom image. Valid values:
        # 
        # - The device name of the system disk must be /dev/xvda.
        # 
        # - The device names of data disks are assigned in sequence from /dev/xvdb to /dev/xvdz and cannot be repeated.
        self.device = device
        # The type of the disk in the image. You can specify this parameter to use a data disk snapshot as the system disk of the image. If you do not specify this parameter, the disk type is determined by the type of the source snapshot. Valid values:
        # 
        # - system: system disk. You can specify only one system disk snapshot.
        # 
        # - data: data disk. You can specify a maximum of 16 data disk snapshots.
        self.disk_type = disk_type
        # The size of the cloud disk, in GiB. The valid values and default value of `DiskDeviceMapping.N.Size` vary based on whether `DiskDeviceMapping.N.SnapshotId` is specified.
        # 
        # - If `DiskDeviceMapping.N.SnapshotId` is not specified, the value of this parameter depends on the disk type:
        # 
        #   - For basic disks, the value range is 5 to 2,000 and the default value is 5.
        # 
        #   - For other disk types, the value range is 20 to 32,768 and the default value is 20.
        # 
        # - If `DiskDeviceMapping.N.SnapshotId` is specified, the value of `DiskDeviceMapping.N.Size` must be greater than or equal to the snapshot\\"s size. The default value is the snapshot\\"s size.
        self.size = size
        # The ID of the snapshot.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device is not None:
            result['Device'] = self.device

        if self.disk_type is not None:
            result['DiskType'] = self.disk_type

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskType') is not None:
            self.disk_type = m.get('DiskType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

