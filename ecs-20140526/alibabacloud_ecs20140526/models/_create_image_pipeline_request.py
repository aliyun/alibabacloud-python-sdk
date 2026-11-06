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
        image_security_options: main_models.CreateImagePipelineRequestImageSecurityOptions = None,
        import_image_options: main_models.CreateImagePipelineRequestImportImageOptions = None,
        instance_type: str = None,
        internet_max_bandwidth_out: int = None,
        name: str = None,
        nvme_support: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        repair_item: List[str] = None,
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
        # The Alibaba Cloud account ID for image sharing of the destination image. Valid values of N: 1 to 20.
        self.add_account = add_account
        # The advanced settings.
        self.advanced_options = advanced_options
        # The source image.
        # - If BaseImageType is set to IMAGE, set this parameter to the image ID.
        # - If BaseImageType is set to IMAGE_FAMILY, set this parameter to the image family name.
        # - If BaseImageType is set to OSS, you do not need to specify this parameter.
        self.base_image = base_image
        # The source image type. Valid values:
        # 
        # - IMAGE: image.
        # - IMAGE_FAMILY: image family.
        # - OSS: OSS object.
        # 
        # This parameter is required.
        self.base_image_type = base_image_type
        # The content of the image build template. The content size cannot exceed 16 KB. For more information about supported commands, see [Commands supported by Image Builder](https://help.aliyun.com/document_detail/200206.html).
        self.build_content = build_content
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **ClientToken** parameter can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # Specifies whether to release the intermediate instance if the image build fails. Valid values:
        # 
        # - true: releases the instance.
        # - false: does not release the instance.
        # 
        # Default value: true.
        # 
        # > If the intermediate instance fails to start, the instance is not retained by default.
        self.delete_instance_on_failure = delete_instance_on_failure
        # The description. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The destination image family.
        # <notice>
        # This parameter is deprecated. Use ImageOptions.ImageFamily instead.
        # </notice>
        self.image_family = image_family
        # The prefix of the destination image name.
        # <notice>
        # This parameter is deprecated. Use ImageOptions.ImageName instead.
        # </notice>
        self.image_name = image_name
        # The properties of the destination image.
        self.image_options = image_options
        # The security-related properties and settings of the image.
        self.image_security_options = image_security_options
        # The properties and settings of the imported image. This parameter is required when BaseImageType is set to OSS.
        self.import_image_options = import_image_options
        # The instance type. You can call the [DescribeInstanceTypes](https://help.aliyun.com/document_detail/25620.html) operation to query available instance types.
        # 
        # If you do not specify this parameter, the system automatically selects an instance type with the minimum number of vCPUs and memory size based on resource availability. For example, the system selects the ecs.g6.large instance type by default. If ecs.g6.large is out of stock, the system selects ecs.g6.xlarge.
        self.instance_type = instance_type
        # The outbound public bandwidth of the intermediate instance. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the template. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character, and cannot start with `http://` or `https://`. It can contain letters, digits, Chinese characters, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # > If `Name` is not specified, the return value of `ImagePipelineId` is used by default.
        self.name = name
        # Specifies whether the destination image to be built supports NVMe.
        # <notice>
        # This parameter is deprecated. Use ImageOptions.ImageFeatures.NvmeSupport instead.
        # </notice>
        self.nvme_support = nvme_support
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The image repair items.
        # 
        # - Repair items supported by Linux:
        #    - fstab: repairs disk attach configuration issues.
        #    - grub: repairs GRUB boot configuration issues.
        #    - dhcp: repairs network DHCP issues.
        #    - selinux: repairs Security-Enhanced Linux (SELinux) issues.
        #    - growpart: repairs online automatic scale-out issues of the root partition.
        #    - cloudinit: installs the cloud-init initialization service.
        #    - aegis: installs the Security Center agent.
        #    - nvme: repairs NVMe driver issues.
        #    - virtio: repairs virtio driver issues.
        #    - standardizedtimezone: repairs standard time zone issues.
        # - Repair items supported by Windows:
        #    - bcd: repairs boot configuration data file issues.
        #    - hotfix: repairs Windows patch issues.
        #    - disk: repairs disk Settings issues.
        #    - update: repairs Windows Update process issues.
        #    - server: repairs service configuration issues.
        #    - bootmgr: repairs Windows Boot Manager issues.
        #    - vminit: repairs Windows initialization agent issues.
        #    - osloader: repairs Windows OS Loader issues.
        #    - virtio: repairs virtio driver issues.
        #    - standardizedtimezone: repairs standard time zone issues.
        self.repair_item = repair_item
        # The repair mode in the image template.
        # 
        # Valid values:
        # - Standard: standard repair mode.
        # 
        #   The standard repair package for Linux includes the following items:
        #   - GUESTOS.CloudInit
        #   - GUESTOS.Dhcp
        #   - GUESTOS.Virtio
        #   - GUESTOS.OnlineResizeFS
        #   - GUESTOS.Grub
        #   - GUESTOS.Fstab
        #   - GUESTOS.Nvme
        # 
        #   The standard repair package for Windows includes the following items:
        #   - GUESTOS.Virtio
        #   - GUESTOS.Update
        #   - GUESTOS.Hotfix
        #   - GUESTOS.Server
        #   - GUESTOS.Bcd
        #   - GUESTOS.Disk
        #   - GUESTOS.Bootmgr
        #   - GUESTOS.OSLoader
        #   - GUESTOS.Vminit
        # 
        # - All: full repair mode.
        # 
        #   The full repair package for Linux includes the following items in addition to those in the standard repair package:
        #   - GUESTOS.Selinux
        #   - GUESTOS.SecurityCenterAgent
        # 
        #   The full repair package for Windows includes the following items in addition to those in the standard repair package:
        #   - GUESTOS.Server
        # 
        # - Customized: custom repair mode. In this mode, the repair items in the repair package are specified by the RepairItem parameter.
        # 
        # > As detection and repair capabilities improve, the included repair items may increase. For more information about the specific meanings of repair items, see [Image check overview](https://help.aliyun.com/document_detail/439819.html).
        self.repair_mode = repair_mode
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The system disk size of the intermediate instance. Unit: GiB. Valid values: 20 to 500.
        # 
        # Default value: 40.
        self.system_disk_size = system_disk_size
        # The list of tags.
        self.tag = tag
        # The content of the image test template. The content size cannot exceed 16 KB. For more information about supported commands, see [Commands supported by Image Builder](https://help.aliyun.com/document_detail/200206.html).
        self.test_content = test_content
        # The list of regions to which the destination image is distributed. Valid values of N: 1 to 20.
        # 
        # If you do not specify this parameter, the image is created only in the current region by default.
        self.to_region_id = to_region_id
        # The vSwitch ID of the VPC.
        # 
        # If you do not specify this parameter, a new VPC and vSwitch are created by default. Make sure that your account has sufficient VPC resource quotas. For more information, see [Limits](https://help.aliyun.com/document_detail/27750.html).
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.advanced_options:
            self.advanced_options.validate()
        if self.image_options:
            self.image_options.validate()
        if self.image_security_options:
            self.image_security_options.validate()
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

        if self.image_security_options is not None:
            result['ImageSecurityOptions'] = self.image_security_options.to_map()

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

        if self.repair_item is not None:
            result['RepairItem'] = self.repair_item

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

        if m.get('ImageSecurityOptions') is not None:
            temp_model = main_models.CreateImagePipelineRequestImageSecurityOptions()
            self.image_security_options = temp_model.from_map(m.get('ImageSecurityOptions'))

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

        if m.get('RepairItem') is not None:
            self.repair_item = m.get('RepairItem')

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
        # The tag key. Valid values of N: 1 to 20. The tag key cannot be an empty string. It can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        self.key = key
        # The tag value. Valid values of N: 1 to 20. The tag value can be an empty string. It can be up to 128 characters in length and cannot start with acs:. It cannot contain http:// or https://.
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
        # The system architecture of the system disk. This parameter is required when you specify a data disk snapshot as the system disk of the image. Valid values:
        # 
        # - x86_64
        # - arm64
        # 
        # Default value: x86_64.
        self.architecture = architecture
        # The boot mode of the image. Valid values:
        # 
        # - BIOS: BIOS boot mode.
        # - UEFI: UEFI boot mode.
        # 
        # Default value: BIOS. If Architecture is set to arm64, the default value is UEFI, and only UEFI is supported.
        # 
        # <notice>
        # 
        # To prevent instances from failing to start due to unsupported boot modes, make sure that you understand the boot modes supported by the destination image before you specify this parameter. For more information about image boot modes, see [Image boot modes](~~2244655#b9caa9b8bb1wf~~).
        # 
        # </notice>
        self.boot_mode = boot_mode
        # The description of the imported image.
        self.description = description
        # The list of custom image information.
        # - If N is set to 1, the disk is a system disk.
        # - If N ranges from 2 to 17, the disk is a data disk.
        self.disk_device_mappings = disk_device_mappings
        # The properties related to image features.
        self.features = features
        # The name of the imported image.
        self.image_name = image_name
        # The list of tags for the image.
        self.import_image_tags = import_image_tags
        # The license type used to activate the operating system after the image is imported. Valid values:
        # 
        # - Auto: Alibaba Cloud detects the source operating system and assigns a license. In Auto mode, the system first checks whether the Platform you specified has a license from Alibaba Cloud official channels and assigns it to the imported image. If no such license is available, the system switches to the Bring Your Own License (BYOL) mode.
        # - Aliyun: uses a license from Alibaba Cloud official channels based on the Platform you specified.
        # - BYOL: uses the license provided by the source operating system. If you use BYOL, you must ensure that your license key is supported on Alibaba Cloud.
        # 
        # Default value: Auto.
        self.license_type = license_type
        # The operating system type. Valid values:
        # 
        # - windows
        # - linux
        # 
        # Default value: linux.
        self.ostype = ostype
        # The operating system version. Valid values:
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
        # - Other Windows
        # 
        # Default value: Others Linux if the operating system type is Linux, or Other Windows if the operating system type is Windows.
        self.platform = platform
        # <notice>
        # This parameter is deprecated. Use ImportImageOptions.RetentionStrategy instead.
        # </notice>
        self.retain_imported_image = retain_imported_image
        # The data retention policy for the imported image. Valid values:
        # 
        # - RetainOnlySuccessful: retains the image only if the build succeeds.
        # - RetainOnlyFailed: retains the image only if the build fails.
        # - RetainAlways: always retains the image regardless of the build result.
        # - RetainNever: never retains the image regardless of the build result.
        # 
        # Default value: RetainNever.
        self.retention_strategy = retention_strategy
        # The name of the RAM role used to import the image.
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
        # The tag key of the image.
        self.key = key
        # The tag value of the image.
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
        # The metadata access mode of the image. Valid values:
        # 
        # - v1: When you create an ECS instance by using this image, you cannot set the metadata access mode to "Reinforced mode only".
        # 
        # - v2: When you create an ECS instance by using this image, you can set the metadata access mode to "Reinforced mode only".
        # 
        # Default value: v1.
        self.imds_support = imds_support
        # Specifies whether the imported original image supports NVMe. Valid values:
        # - supported: supported. This indicates that instances created by using this image support the NVMe protocol.
        # - unsupported: not supported. This indicates that instances created by using this image do not support the NVMe protocol.
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
        # The size of the custom image after the image is imported.
        # 
        # The space consists of the system disk and data disks. You must ensure that the system disk size is greater than or equal to the size of the imported image file. Valid values:
        # 
        # - If N is set to 1, the disk is a system disk. Valid values: 1 to 2048. Unit: GiB.
        # - If N ranges from 2 to 17, the disk is a data disk. Valid values: 1 to 2048. Unit: GiB.
        # 
        # After you upload the source image file to OSS, you can view the size of the image file in the OSS bucket.
        self.disk_image_size = disk_image_size
        # The image format. Valid values:
        # 
        # - RAW
        # - VHD
        # - QCOW2
        # 
        # Default value: none. This indicates that Alibaba Cloud automatically detects the image format and uses the detected format.
        self.format = format
        # The OSS bucket where the image file is stored.
        self.ossbucket = ossbucket
        # The name (key) of the image file saved in the OSS bucket after the image is uploaded.
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

class CreateImagePipelineRequestImageSecurityOptions(DaraModel):
    def __init__(
        self,
        security_scan_mode: str = None,
    ):
        # The security scan mode. Valid values:
        # 
        # - agentless: uses the agentless scan mode of Security Center.
        self.security_scan_mode = security_scan_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_scan_mode is not None:
            result['SecurityScanMode'] = self.security_scan_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityScanMode') is not None:
            self.security_scan_mode = m.get('SecurityScanMode')

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
        # The description. The description must be 2 to 256 characters in length and cannot start with http:// or https://.
        self.description = description
        # The target image family. The value must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with aliyun or acs:. It cannot contain http:// or https://. It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.image_family = image_family
        # The properties related to destination image features.
        self.image_features = image_features
        # The prefix of the target image name. It must be 2 to 64 characters in length, start with a letter or a Chinese character, and cannot start with `http://` or `https://`. It can contain Chinese characters, letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # The final image name is automatically generated by the system by concatenating the prefix and the build task ID (`ExecutionId`) in the format of `{ImageName}_{ExecutionId}`.
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
        # The tag key. Valid values of N: 1 to 20. The tag key cannot be an empty string. It can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        self.key = key
        # The tag value. Valid values of N: 1 to 20. The tag value can be an empty string. It can be up to 128 characters in length and cannot start with acs:. It cannot contain http:// or https://.
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
        # Specifies whether the destination image to be built supports NVMe. Valid values:
        # - supported: supported. This indicates that instances created by using this image support the NVMe protocol.
        # - unsupported: not supported. This indicates that instances created by using this image do not support the NVMe protocol.
        # - auto: automatic detection. The system automatically detects whether the NVMe driver is installed in your image. This detection occurs before the build phase. If you install or uninstall the NVMe driver during the build, the detection result may be inaccurate. We recommend that you set this parameter to supported or unsupported based on the build content.
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
        # Specifies whether to disable the automatic addition of a suffix to the destination image name. Valid values:
        # - disable: disables the automatic addition.
        self.image_name_suffix = image_name_suffix
        # Specifies whether to retain Cloud Assistant. During the build process, the system automatically installs Cloud Assistant on the intermediate instance to execute commands. You can choose whether to retain it in the destination image. Valid values:
        # - true: retains Cloud Assistant.
        # - false: does not retain Cloud Assistant.
        # 
        # Default value: false.
        # > This setting does not affect the Cloud Assistant that is pre-installed in your image.
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

