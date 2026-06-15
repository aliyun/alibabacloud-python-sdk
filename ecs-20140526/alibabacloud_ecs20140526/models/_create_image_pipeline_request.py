# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateImagePipelineRequest(DaraModel):
    def __init__(
        self,
        add_account: List[int] = None,
        advanced_options: main_models.CreateImagePipelineRequestAdvancedOptions = None,
        base_image: str = None,
        base_image_type: str = None,
        build_content: str = None,
        client_token: str = None,
        delete_instance_on_failure: bool = None,
        description: str = None,
        image_family: str = None,
        image_name: str = None,
        image_options: main_models.CreateImagePipelineRequestImageOptions = None,
        import_image_options: main_models.CreateImagePipelineRequestImportImageOptions = None,
        instance_type: str = None,
        internet_max_bandwidth_out: int = None,
        name: str = None,
        nvme_support: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        repair_mode: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        system_disk_size: int = None,
        tag: List[main_models.CreateImagePipelineRequestTag] = None,
        test_content: str = None,
        to_region_id: List[str] = None,
        v_switch_id: str = None,
    ):
        # The IDs of the Alibaba Cloud accounts to share the destination images with. You can specify up to 20 account IDs.
        self.add_account = add_account
        # The advanced settings.
        self.advanced_options = advanced_options
        # The base image. The value of this parameter varies based on the value of `BaseImageType`:
        # 
        # - If `BaseImageType` is `IMAGE`, specify the ID of the base image.
        # 
        # - If `BaseImageType` is `IMAGE_FAMILY`, specify the name of the base image family.
        # 
        # - If `BaseImageType` is `OSS`, this parameter is not required.
        self.base_image = base_image
        # The type of the base image. Valid values:
        # 
        # - IMAGE: An ECS image.
        # 
        # - IMAGE_FAMILY: An image family.
        # 
        # - OSS: An OSS object.
        # 
        # This parameter is required.
        self.base_image_type = base_image_type
        # The content of the image build template. The content can be up to 16 KB in size. For more information about the supported commands, see [Command reference for Image Builder](https://help.aliyun.com/document_detail/200206.html).
        self.build_content = build_content
        # A client-generated, globally unique token to ensure the idempotence of the request. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Determines whether to release the intermediate instance when the image build fails. Valid values:
        # 
        # - true: The instance is released.
        # 
        # - false: The instance is not released.
        # 
        # Default value: true.
        # 
        # > If an intermediate instance cannot be started, it is not retained by default.
        self.delete_instance_on_failure = delete_instance_on_failure
        # The description of the image pipeline template. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the destination image family.
        # >Notice: This parameter is deprecated. Use `ImageOptions.ImageFamily` instead.
        self.image_family = image_family
        # The prefix of the destination image name.
        # >Notice: This parameter is deprecated. Use `ImageOptions.ImageName` instead.
        self.image_name = image_name
        # The properties of the destination image.
        self.image_options = image_options
        # The settings for importing an image. This parameter is required when `BaseImageType` is set to `OSS`.
        self.import_image_options = import_image_options
        # The instance type of the intermediate instance. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query instance types.
        # 
        # If you do not specify this parameter, the system automatically selects an instance type with the minimum vCPUs and memory, subject to inventory. For example, `ecs.g6.large` is selected by default. If `ecs.g6.large` is out of stock, `ecs.g6.xlarge` is selected.
        self.instance_type = instance_type
        # The outbound public bandwidth of the intermediate instance. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the image pipeline. It must be 2 to 128 characters long, start with a letter or a Chinese character, and cannot start with `http://` or `https://`. Allowed characters include letters, digits, Chinese characters, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # > If you do not specify this parameter, the value of `ImagePipelineId` is used as the name.
        self.name = name
        # Specifies whether the destination image supports NVMe.
        # >Notice: This parameter is deprecated. Use `ImageOptions.ImageFeatures.NvmeSupport` instead.
        self.nvme_support = nvme_support
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The image repair mode in the image template.
        # 
        # Valid values:
        # 
        # - Standard: The standard mode.
        # 
        #   The check items for Linux systems include the following:
        # 
        #   - GUESTOS.CloudInit
        # 
        #   - GUESTOS.Dhcp
        # 
        #   - GUESTOS.Virtio
        # 
        #   - GUESTOS.OnlineResizeFS
        # 
        #   - GUESTOS.Grub
        # 
        #   - GUESTOS.Fstab
        # 
        #   The check items for Windows systems include the following:
        # 
        #   - GUESTOS.Virtio
        # 
        #   - GUESTOS.Update
        # 
        #   - GUESTOS.Hotfix
        # 
        #   - GUESTOS.Server
        # 
        # > The repair items may change as the check and repair capabilities are improved. For more information about each repair item, see [Image check overview](https://help.aliyun.com/document_detail/439819.html).
        self.repair_mode = repair_mode
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The size of the system disk of the intermediate instance. Unit: GiB. Valid values: 20 to 500.
        # 
        # Default value: 40.
        self.system_disk_size = system_disk_size
        # The tags to add to the image pipeline.
        self.tag = tag
        # The content of the image test template. The content can be up to 16 KB in size. For more information about the supported commands, see [Command reference for Image Builder](https://help.aliyun.com/document_detail/200206.html).
        self.test_content = test_content
        # The IDs of destination regions for image distribution. You can specify up to 20 region IDs.
        # 
        # If you do not specify this parameter, the images are created only in the current region.
        self.to_region_id = to_region_id
        # The ID of the VSwitch in the VPC that is used to launch the intermediate instance.
        # 
        # If you do not specify this parameter, a new VPC and VSwitch are created. Ensure that you have a sufficient quota of VPC resources. For more information, see [Usage limits](https://help.aliyun.com/document_detail/27750.html).
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()
        if self.image_options:
            self.image_options.validate()
        if self.import_image_options:
            self.import_image_options.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_account is not None:
            result['AddAccount'] = self.add_account

        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()

        if self.base_image is not None:
            result['BaseImage'] = self.base_image

        if self.base_image_type is not None:
            result['BaseImageType'] = self.base_image_type

        if self.build_content is not None:
            result['BuildContent'] = self.build_content

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.delete_instance_on_failure is not None:
            result['DeleteInstanceOnFailure'] = self.delete_instance_on_failure

        if self.description is not None:
            result['Description'] = self.description

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.image_options is not None:
            result['ImageOptions'] = self.image_options.to_map()

        if self.import_image_options is not None:
            result['ImportImageOptions'] = self.import_image_options.to_map()

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.name is not None:
            result['Name'] = self.name

        if self.nvme_support is not None:
            result['NvmeSupport'] = self.nvme_support

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.repair_mode is not None:
            result['RepairMode'] = self.repair_mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.test_content is not None:
            result['TestContent'] = self.test_content

        if self.to_region_id is not None:
            result['ToRegionId'] = self.to_region_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccount') is not None:
            self.add_account = m.get('AddAccount')

        if m.get('AdvancedOptions') is not None:
            temp_model = main_models.CreateImagePipelineRequestAdvancedOptions()
            self.advanced_options = temp_model.from_map(m.get('AdvancedOptions'))

        if m.get('BaseImage') is not None:
            self.base_image = m.get('BaseImage')

        if m.get('BaseImageType') is not None:
            self.base_image_type = m.get('BaseImageType')

        if m.get('BuildContent') is not None:
            self.build_content = m.get('BuildContent')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeleteInstanceOnFailure') is not None:
            self.delete_instance_on_failure = m.get('DeleteInstanceOnFailure')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageOptions') is not None:
            temp_model = main_models.CreateImagePipelineRequestImageOptions()
            self.image_options = temp_model.from_map(m.get('ImageOptions'))

        if m.get('ImportImageOptions') is not None:
            temp_model = main_models.CreateImagePipelineRequestImportImageOptions()
            self.import_image_options = temp_model.from_map(m.get('ImportImageOptions'))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NvmeSupport') is not None:
            self.nvme_support = m.get('NvmeSupport')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RepairMode') is not None:
            self.repair_mode = m.get('RepairMode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateImagePipelineRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TestContent') is not None:
            self.test_content = m.get('TestContent')

        if m.get('ToRegionId') is not None:
            self.to_region_id = m.get('ToRegionId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class CreateImagePipelineRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N, where N is from 1 to 20. The tag key must be 1 to 128 characters in length. It cannot start with `aliyun` or `acs:` or contain `http://` or `https://`.
        self.key = key
        # The value of tag N, where N is from 1 to 20. The tag value can be empty or up to 128 characters long. It cannot start with `acs:` or contain `http://` or `https://`.
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

class CreateImagePipelineRequestImportImageOptions(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        boot_mode: str = None,
        description: str = None,
        disk_device_mappings: List[main_models.CreateImagePipelineRequestImportImageOptionsDiskDeviceMappings] = None,
        features: main_models.CreateImagePipelineRequestImportImageOptionsFeatures = None,
        image_name: str = None,
        import_image_tags: List[main_models.CreateImagePipelineRequestImportImageOptionsImportImageTags] = None,
        license_type: str = None,
        ostype: str = None,
        platform: str = None,
        retain_imported_image: bool = None,
        retention_strategy: str = None,
        role_name: str = None,
    ):
        # The architecture of the image to import. Valid values:
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
        # Default value: BIOS. If `Architecture` is set to `arm64`, the default value is UEFI and this parameter can be set only to UEFI.
        # 
        # >Notice: 
        # 
        # To prevent startup failures, ensure the boot mode is supported by the image.
        self.boot_mode = boot_mode
        self.description = description
        # The information about the disks of the custom image.
        # 
        # - When N is 1, the disk is a system disk.
        # 
        # - When N is a value from 2 to 17, the disk is a data disk.
        self.disk_device_mappings = disk_device_mappings
        # The image feature attributes.
        self.features = features
        self.image_name = image_name
        self.import_image_tags = import_image_tags
        # The license type used to activate the operating system after the image is imported. Valid values:
        # 
        # - Auto: Alibaba Cloud attempts to assign a license based on the detected operating system. If an official Alibaba Cloud license for the specified `Platform` is unavailable, the system defaults to BYOL.
        # 
        # - Aliyun: A license from an official Alibaba Cloud channel is used based on the specified `Platform`.
        # 
        # - BYOL: The license that comes with the base operating system is used. When you use the BYOL mode, you must make sure that your license key is supported in Alibaba Cloud.
        # 
        # Default value: Auto.
        self.license_type = license_type
        # The type of the operating system. Valid values:
        # 
        # - windows
        # 
        # - linux
        # 
        # Default value: linux.
        self.ostype = ostype
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
        # Default value: Others Linux if OSType is set to Linux, or Other Windows if OSType is set to Windows.
        self.platform = platform
        # > This parameter is in invitational preview.
        self.retain_imported_image = retain_imported_image
        self.retention_strategy = retention_strategy
        self.role_name = role_name

    def validate(self):
        if self.disk_device_mappings:
            for v1 in self.disk_device_mappings:
                 if v1:
                    v1.validate()
        if self.features:
            self.features.validate()
        if self.import_image_tags:
            for v1 in self.import_image_tags:
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

        if self.description is not None:
            result['Description'] = self.description

        result['DiskDeviceMappings'] = []
        if self.disk_device_mappings is not None:
            for k1 in self.disk_device_mappings:
                result['DiskDeviceMappings'].append(k1.to_map() if k1 else None)

        if self.features is not None:
            result['Features'] = self.features.to_map()

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        result['ImportImageTags'] = []
        if self.import_image_tags is not None:
            for k1 in self.import_image_tags:
                result['ImportImageTags'].append(k1.to_map() if k1 else None)

        if self.license_type is not None:
            result['LicenseType'] = self.license_type

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.platform is not None:
            result['Platform'] = self.platform

        if self.retain_imported_image is not None:
            result['RetainImportedImage'] = self.retain_imported_image

        if self.retention_strategy is not None:
            result['RetentionStrategy'] = self.retention_strategy

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('BootMode') is not None:
            self.boot_mode = m.get('BootMode')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.disk_device_mappings = []
        if m.get('DiskDeviceMappings') is not None:
            for k1 in m.get('DiskDeviceMappings'):
                temp_model = main_models.CreateImagePipelineRequestImportImageOptionsDiskDeviceMappings()
                self.disk_device_mappings.append(temp_model.from_map(k1))

        if m.get('Features') is not None:
            temp_model = main_models.CreateImagePipelineRequestImportImageOptionsFeatures()
            self.features = temp_model.from_map(m.get('Features'))

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        self.import_image_tags = []
        if m.get('ImportImageTags') is not None:
            for k1 in m.get('ImportImageTags'):
                temp_model = main_models.CreateImagePipelineRequestImportImageOptionsImportImageTags()
                self.import_image_tags.append(temp_model.from_map(k1))

        if m.get('LicenseType') is not None:
            self.license_type = m.get('LicenseType')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('Platform') is not None:
            self.platform = m.get('Platform')

        if m.get('RetainImportedImage') is not None:
            self.retain_imported_image = m.get('RetainImportedImage')

        if m.get('RetentionStrategy') is not None:
            self.retention_strategy = m.get('RetentionStrategy')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        return self

class CreateImagePipelineRequestImportImageOptionsImportImageTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
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

class CreateImagePipelineRequestImportImageOptionsFeatures(DaraModel):
    def __init__(
        self,
        imds_support: str = None,
        nvme_support: str = None,
    ):
        self.imds_support = imds_support
        # Specifies whether the base image to be imported supports NVMe. Valid values:
        # 
        # - supported: Instances created from this image support the NVMe protocol.
        # 
        # - unsupported: Instances created from this image do not support the NVMe protocol.
        # 
        # Default value: unsupported.
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

class CreateImagePipelineRequestImportImageOptionsDiskDeviceMappings(DaraModel):
    def __init__(
        self,
        disk_image_size: int = None,
        format: str = None,
        ossbucket: str = None,
        ossobject: str = None,
    ):
        # The size of the disk to create from the image file, in GiB. For the system disk, this value must be greater than or equal to the size of the image file.
        # 
        # Valid values:
        # 
        # - When N is 1, the disk is the system disk. The size of the system disk can range from 1 GiB to 2,048 GiB.
        # 
        # - When N is a value from 2 to 17, the disk is a data disk. The size of a data disk can range from 1 GiB to 2,048 GiB.
        # 
        # After you upload the base image file to an OSS bucket, you can view the size of the image file in the bucket.
        self.disk_image_size = disk_image_size
        # The format of the image. Valid values:
        # 
        # - RAW
        # 
        # - VHD
        # 
        # - QCOW2
        # 
        # Default value: If left empty, the system automatically detects the image format.
        self.format = format
        # The OSS bucket that contains the image file.
        self.ossbucket = ossbucket
        # The name (key) of the image file that is stored in the OSS bucket.
        self.ossobject = ossobject

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('DiskImageSize') is not None:
            self.disk_image_size = m.get('DiskImageSize')

        if m.get('Format') is not None:
            self.format = m.get('Format')

        if m.get('OSSBucket') is not None:
            self.ossbucket = m.get('OSSBucket')

        if m.get('OSSObject') is not None:
            self.ossobject = m.get('OSSObject')

        return self

class CreateImagePipelineRequestImageOptions(DaraModel):
    def __init__(
        self,
        description: str = None,
        image_family: str = None,
        image_features: main_models.CreateImagePipelineRequestImageOptionsImageFeatures = None,
        image_name: str = None,
        image_tags: List[main_models.CreateImagePipelineRequestImageOptionsImageTags] = None,
    ):
        # The description of the destination image. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the destination image family. The name must be 2 to 128 characters long and start with a letter or a Chinese character. It cannot start with `aliyun` or `acs:` or contain `http://` or `https://`. Allowed characters include letters, digits, Chinese characters, colons (:), underscores (_), and hyphens (-).
        self.image_family = image_family
        # The feature attributes of the destination image.
        self.image_features = image_features
        # The prefix of the destination image name. The prefix must be 2 to 64 characters in length. It must start with a letter or a Chinese character. It cannot start with `http://` or `https://`. It can contain Chinese characters, letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # The complete image name is automatically generated by concatenating the prefix and the build task ID (`ExecutionId`) in the `{ImageName}_{ExecutionId}` format.
        self.image_name = image_name
        # The tags of the destination image.
        self.image_tags = image_tags

    def validate(self):
        if self.image_features:
            self.image_features.validate()
        if self.image_tags:
            for v1 in self.image_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_features is not None:
            result['ImageFeatures'] = self.image_features.to_map()

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        result['ImageTags'] = []
        if self.image_tags is not None:
            for k1 in self.image_tags:
                result['ImageTags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageFeatures') is not None:
            temp_model = main_models.CreateImagePipelineRequestImageOptionsImageFeatures()
            self.image_features = temp_model.from_map(m.get('ImageFeatures'))

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        self.image_tags = []
        if m.get('ImageTags') is not None:
            for k1 in m.get('ImageTags'):
                temp_model = main_models.CreateImagePipelineRequestImageOptionsImageTags()
                self.image_tags.append(temp_model.from_map(k1))

        return self

class CreateImagePipelineRequestImageOptionsImageTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The tag key must be 1 to 128 characters in length, cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`.
        self.key = key
        # The value of the tag. The tag value can be empty or up to 128 characters long. It cannot start with `acs:` and cannot contain `http://` or `https://`.
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

class CreateImagePipelineRequestImageOptionsImageFeatures(DaraModel):
    def __init__(
        self,
        nvme_support: str = None,
    ):
        # Specifies whether the destination image supports NVMe. Valid values:
        # 
        # - supported: Instances created from this image support the NVMe protocol.
        # 
        # - unsupported: Instances created from this image do not support the NVMe protocol.
        # 
        # - auto: The system automatically checks whether the NVMe driver is installed on your image. This check is performed before the build phase. If you install or uninstall the NVMe driver during the build, the result may be inaccurate. We recommend that you set this parameter to supported or unsupported based on the build content.
        self.nvme_support = nvme_support

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nvme_support is not None:
            result['NvmeSupport'] = self.nvme_support

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NvmeSupport') is not None:
            self.nvme_support = m.get('NvmeSupport')

        return self

class CreateImagePipelineRequestAdvancedOptions(DaraModel):
    def __init__(
        self,
        image_name_suffix: str = None,
        retain_cloud_assistant: bool = None,
    ):
        # Specifies whether to disable the feature that automatically appends a suffix to the destination image name. Valid values:
        # 
        # - disable: Disables the feature.
        self.image_name_suffix = image_name_suffix
        # Specifies whether to retain Cloud Assistant in the destination image. During the image building process, Cloud Assistant is automatically installed on the intermediate instance to run commands. You can select whether to retain Cloud Assistant after the process is complete. Valid values:
        # 
        # - true: Retain Cloud Assistant.
        # 
        # - false: Do not retain Cloud Assistant.
        # 
        # Default value: false.
        # 
        # > This setting does not affect the Cloud Assistant client that is already installed in your image.
        self.retain_cloud_assistant = retain_cloud_assistant

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_name_suffix is not None:
            result['ImageNameSuffix'] = self.image_name_suffix

        if self.retain_cloud_assistant is not None:
            result['RetainCloudAssistant'] = self.retain_cloud_assistant

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageNameSuffix') is not None:
            self.image_name_suffix = m.get('ImageNameSuffix')

        if m.get('RetainCloudAssistant') is not None:
            self.retain_cloud_assistant = m.get('RetainCloudAssistant')

        return self

