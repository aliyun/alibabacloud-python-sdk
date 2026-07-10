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
        # The system architecture. After a data disk snapshot is specified as the system disk of the image, use this parameter to specify the system architecture of the system disk. Valid values:
        # 
        # - i386.
        # - x86_64.
        # - arm64.
        # 
        # Default value: x86_64.
        self.architecture = architecture
        # The boot mode of the image. Valid values:
        # 
        # - BIOS: BIOS boot mode.
        # - UEFI: UEFI boot mode.
        # - (Default) UEFI-Preferred: dual boot mode.  
        # 
        # <notice>
        # 
        # To prevent instances from failing to start due to an unsupported boot mode, make sure that you understand the boot modes supported by the target image before specifying this parameter. For more information about image boot modes, see [Image boot modes](~~2244655#b9caa9b8bb1wf~~).
        # 
        # </notice>
        self.boot_mode = boot_mode
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the image. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The image detection strategy. If this parameter is not specified, detection is not triggered. Only the Standard detection mode is supported. 
        # 
        # > Most Linux and Windows versions are supported. For more information about image detection items and operating system limitations, see [Image detection overview](https://help.aliyun.com/document_detail/439819.html) and [Operating system limitations for image detection](https://help.aliyun.com/document_detail/475800.html).
        self.detection_strategy = detection_strategy
        # The disk and snapshot information used to create the custom image. Use this parameter to specify snapshots when you want to create a custom image from system disk and data disk snapshots.
        self.disk_device_mapping = disk_device_mapping
        self.dry_run = dry_run
        # The image feature properties.
        self.features = features
        # The image family name. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with aliyun or acs:. It cannot contain http:// or https://. It can contain digits, colons (:), underscores (_), or hyphens (-).
        self.image_family = image_family
        # The image name. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with http:// or https://. It can contain digits, colons (:), underscores (_), or hyphens (-).
        self.image_name = image_name
        # The image version.
        # 
        # > If you specify an instance ID (`InstanceId`) and the image of the instance is an Alibaba Cloud Marketplace image or a custom image created from an Alibaba Cloud Marketplace image, this parameter must be the same as the `ImageVersion` of the current instance image or left empty.
        self.image_version = image_version
        # The instance ID. This parameter is required when you create a custom image from an instance.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The operating system distribution. After a data disk snapshot is specified as the system disk of the image, use this parameter to specify the operating system distribution of the system disk. Valid values:
        # 
        # - Aliyun
        # - Anolis
        # - CentOS
        # - Ubuntu
        # - CoreOS
        # - SUSE
        # - Debian
        # - OpenSUSE
        # - FreeBSD
        # - RedHat
        # - Kylin
        # - UOS
        # - Fedora
        # - Fedora CoreOS
        # - CentOS Stream
        # - AlmaLinux
        # - Rocky Linux
        # - Gentoo
        # - Customized Linux
        # - Others Linux
        # - Windows Server 2022
        # - Windows Server 2019
        # - Windows Server 2016
        # - Windows Server 2012
        # - Windows Server 2008
        # - Windows Server 2003
        # 
        # Default value: Others Linux.
        self.platform = platform
        # The region ID of the image. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the custom image belongs. If this parameter is not set, the created image belongs to the default resource group.
        # 
        # > If you invoke this operation as a Resource Access Management (RAM) user and `ResourceGroupId` is left empty, note that when the RAM user does not have permissions on the default resource group, the error message `Forbidden: User not authorized to operate on the specified resource` is returned. Set a resource group ID that the RAM user has permissions on, or grant the RAM user permissions on the default resource group before invoking this operation again.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The snapshot ID used to create the custom image.
        # 
        # > If you want to create a custom image only from the system disk snapshot of an instance, you can use this parameter or the `DiskDeviceMapping.N.SnapshotId` parameter. To include data disk snapshots, use only the `DiskDeviceMapping.N.SnapshotId` parameter to specify snapshots.
        self.snapshot_id = snapshot_id
        # The tags.
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
        # The tag key of the image. Valid values of N: 1 to 20. The tag key cannot be an empty string. It can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the image. Valid values of N: 1 to 20. The tag value can be an empty string. It can be up to 128 characters in length and cannot start with `acs:`. It cannot contain `http://` or `https://`.
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
        # The metadata access mode of the image. Valid values:
        # - v1: When you create an ECS instance from this image, you cannot set the metadata access mode to "security hardening mode only".
        # - v2: When you create an ECS instance from this image, you can set the metadata access mode to "security hardening mode only".
        # 
        # Default value: When creating an image from a snapshot, the default is v1. When creating an image from an instance, the default is the ImdsSupport value of the image used when the instance was created.
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
        # The device name in the custom image. Valid values:
        # 
        # - The device name of the system disk must be /dev/xvda.
        # 
        # - Data disk device names are sequentially ordered from /dev/xvdb to /dev/xvdz and cannot be duplicated.
        self.device = device
        # The type of the disk in the new image. You can use this parameter to specify a data disk snapshot as the system disk of the image. If this parameter is not specified, the disk type defaults to the type of the disk corresponding to the snapshot. Valid values:
        # 
        # - system: system disk. Only one system disk snapshot can be specified.
        # - data: data disk. Up to 16 data disk snapshots can be specified.
        self.disk_type = disk_type
        # The size of the disk, in GiB. The valid values and default value of DiskDeviceMapping.N.Size depend on DiskDeviceMapping.N.SnapshotId:
        # 
        # - If SnapshotId is not specified, the valid values and default value of Size are:
        #     - Basic disk: 5 to 2000 GiB. Default value: 5.
        #     - Other disk types: 20 to 32768 GiB. Default value: 20.
        # - If SnapshotId is specified, the value of Size must be greater than or equal to the size of the snapshot. Default value: the size of the snapshot.
        self.size = size
        # The snapshot ID.
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

