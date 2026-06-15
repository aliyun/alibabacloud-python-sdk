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
        # - BIOS: the BIOS boot mode.
        # 
        # - UEFI: the UEFI boot mode.
        # 
        # Default value: BIOS. If you set `Architecture` to `arm64`, the value of this parameter defaults to UEFI and can only be set to UEFI.
        # 
        # >Notice: 
        # 
        # To prevent startup failures, ensure the boot mode you specify is supported by the image. For more information, see [Image boot modes](~~2244655#b9caa9b8bb1wf~~).
        self.boot_mode = boot_mode
        # A client-generated token that ensures the idempotence of a request. The token must be unique across requests. The token can contain only ASCII characters and must be no more than 64 characters long. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the image. The description must be 2 to 256 characters long and cannot start with `http://` or `https://`. Both English and Chinese characters are supported.
        self.description = description
        # The policy for checking the image. If you do not specify this parameter, the system does not check the image. This parameter supports only the standard detection mode. Set the value to `Standard`.
        # 
        # > This feature is supported on most Linux and Windows versions. For more information about the check items and the operating systems that support this feature, see [Image detection overview](https://help.aliyun.com/document_detail/439819.html) and [Operating system limitations for image detection](https://help.aliyun.com/document_detail/475800.html).
        self.detection_strategy = detection_strategy
        # A list of disk device mappings for the custom image.
        self.disk_device_mapping = disk_device_mapping
        # Specifies whether to perform a dry run for the request. Valid values:
        # 
        # - `true`: performs a check request without executing the actual operation. The system checks whether the request parameters are valid, the request format is correct, and the required permissions are granted. If the check fails, the system returns an error message. If the check succeeds, the system returns the `DryRunOperation` error code.
        # 
        # - `false`: sends a normal request. After the request passes the check, the system returns a 2xx HTTP status code and performs the operation.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # The properties of image features.
        self.features = features
        # The name of the image. The name must be 2 to 128 characters long and start with a letter or a Chinese character. It can contain digits, periods (.), colons (:), underscores (_), and hyphens (-). The name cannot start with `aliyun` or `acs:` or contain `http://` or `https://`.
        self.image_name = image_name
        # The license type. This parameter sets the licensing model for instances that are created from the image by calling the [RunInstances](https://help.aliyun.com/document_detail/2679677.html) operation. This parameter applies only to Windows Server images. Valid values:
        # 
        # - Aliyun: Uses a license provided by Alibaba Cloud. When you start an instance created from this image, the system attempts to automatically connect to the Alibaba Cloud KMS server for activation. The fees for the instance include the cost of the Windows Server license.
        # 
        # - BYOL: Bring Your Own License. When you start an instance created from this image, Alibaba Cloud does not provide activation. You must use your own license key to manually activate the operating system. The fees for the instance do not include the cost of the Windows Server license.
        # 
        # Default value: Aliyun.
        self.license_type = license_type
        # The operating system type. Valid values:
        # 
        # - `windows`: You must also set the `LicenseType` parameter.
        # 
        # - `linux`
        # 
        # Default value: linux.
        self.ostype = ostype
        self.owner_id = owner_id
        # The operating system distribution. Valid values:
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
        # - Other Windows
        # 
        # Default value: Others Linux.
        self.platform = platform
        # The ID of the region where the source custom image is located. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the imported image belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The name of the RAM role used to import the image.
        self.role_name = role_name
        # The Alibaba Cloud Resource Name (ARN) of the CloudBox, which uniquely identifies the cloud storage location.
        # 
        # > You must specify this parameter only when you import an image file from OSS ON CloudBox. If you do not use OSS ON CloudBox, do not specify this parameter. For more information, see [What is OSS ON CloudBox?](https://help.aliyun.com/document_detail/430190.html).
        # 
        # The ARN must be in the `arn:acs:cloudbox:{RegionId}:{AliUid}:cloudbox/{CloudBoxId}` format. Replace `{RegionId}` with the ID of the region where the CloudBox is located, `{AliUid}` with the ID of your Alibaba Cloud account, and `{CloudBoxId}` with the ID of the CloudBox.
        self.storage_location_arn = storage_location_arn
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
        # The key of tag N. Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters long and cannot start with `aliyun` or `acs:` or contain `http://` or `https://`.
        self.key = key
        # The value of tag N. Valid values of N: 1 to 20. The tag value can be an empty string. It can be up to 128 characters long, cannot start with `acs:`, and cannot contain `http://` or `https://`.
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
        # The metadata access mode of the image. Valid values:
        # 
        # - v1: When you create an ECS instance from the image, you cannot set the metadata access mode to Security-Hardened Mode.
        # 
        # - v2: When you create an ECS instance from the image, you can set the metadata access mode to Security-Hardened Mode.
        # 
        # Default value: v1.
        self.imds_support = imds_support
        # Specifies whether the image supports NVMe. Valid values:
        # 
        # - supported: Instances created from the image support the NVMe protocol.
        # 
        # - unsupported: Instances created from the image do not support the NVMe protocol.
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
        # The device name of the disk (`DiskDeviceMapping.N.Device`) in the custom image.
        # 
        # > This parameter is being phased out. To ensure compatibility, we recommend that you avoid using this parameter.
        self.device = device
        # The size of the disk, in GiB.
        # 
        # The system disk size must be greater than or equal to the size of the imported image file. Valid values:
        # 
        # - For N=1, the disk is a system disk. The value must be in the range of 1 to 2,048.
        # 
        # - For N=2 to 17, the disk is a data disk. The value must be in the range of 1 to 2,048.
        # 
        # After you upload the source image file to an OSS bucket, you can view the size of the file in the bucket.
        # 
        # > This parameter is being deprecated. For better compatibility, we recommend that you use the `DiskDeviceMapping.N.DiskImageSize` parameter.
        self.disk_im_size = disk_im_size
        # The size of the disk after the image is imported, in GiB.
        # 
        # The value of this parameter for the system disk must be greater than or equal to the size of the image file. Valid values:
        # 
        # - For N=1, the disk is a system disk. The value must be in the range of 1 to 2,048.
        # 
        # - For N=2 to 17, the disk is a data disk. The value must be in the range of 1 to 2,048.
        # 
        # After you upload the source image file to an OSS bucket, you can view the size of the file in the bucket.
        self.disk_image_size = disk_image_size
        # The format of the image file. Valid values:
        # 
        # - RAW
        # 
        # - VHD
        # 
        # - QCOW2
        # 
        # - VMDK (This feature is in invitation-only preview.)
        # 
        # Default value: None. If you leave this parameter empty, Alibaba Cloud automatically detects the image format and uses the detected format.
        self.format = format
        # The OSS bucket where the image file is stored.
        # 
        # > Before you import an image from an OSS bucket for the first time, you must add a RAM policy as described in the **Description** section of this topic. Otherwise, the API returns the `NoSetRoletoECSServiceAccount` error.
        self.ossbucket = ossbucket
        # The object key of the image file in the OSS bucket.
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

