# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImagePipelinesResponseBody(DaraModel):
    def __init__(
        self,
        image_pipeline: main_models.DescribeImagePipelinesResponseBodyImagePipeline = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details of the image templates.
        self.image_pipeline = image_pipeline
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results. For information about how to use the return value, see the "Usage notes" section of this topic.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of image templates returned.
        self.total_count = total_count

    def validate(self):
        if self.image_pipeline:
            self.image_pipeline.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_pipeline is not None:
            result['ImagePipeline'] = self.image_pipeline.to_map()

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImagePipeline') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipeline()
            self.image_pipeline = temp_model.from_map(m.get('ImagePipeline'))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeImagePipelinesResponseBodyImagePipeline(DaraModel):
    def __init__(
        self,
        image_pipeline_set: List[main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSet] = None,
    ):
        self.image_pipeline_set = image_pipeline_set

    def validate(self):
        if self.image_pipeline_set:
            for v1 in self.image_pipeline_set:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImagePipelineSet'] = []
        if self.image_pipeline_set is not None:
            for k1 in self.image_pipeline_set:
                result['ImagePipelineSet'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_pipeline_set = []
        if m.get('ImagePipelineSet') is not None:
            for k1 in m.get('ImagePipelineSet'):
                temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSet()
                self.image_pipeline_set.append(temp_model.from_map(k1))

        return self

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSet(DaraModel):
    def __init__(
        self,
        add_accounts: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetAddAccounts = None,
        advanced_options: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetAdvancedOptions = None,
        base_image: str = None,
        base_image_type: str = None,
        build_content: str = None,
        creation_time: str = None,
        delete_instance_on_failure: bool = None,
        description: str = None,
        image_family: str = None,
        image_name: str = None,
        image_options: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptions = None,
        image_pipeline_id: str = None,
        import_image_options: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptions = None,
        instance_type: str = None,
        internet_max_bandwidth_out: int = None,
        name: str = None,
        nvme_support: str = None,
        repair_mode: str = None,
        resource_group_id: str = None,
        system_disk_size: int = None,
        tags: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetTags = None,
        test_content: str = None,
        to_region_ids: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetToRegionIds = None,
        v_switch_id: str = None,
    ):
        # The IDs of Alibaba Cloud accounts to which to share the image that will be created based on the image template.
        self.add_accounts = add_accounts
        # The advanced settings.
        self.advanced_options = advanced_options
        # The source image.
        # 
        # *   When `BaseImageType` is set to IMAGE, the value of this parameter is the ID of a custom image.
        # *   When `BaseImageType` is set to IMAGE_FAMILY, the value of this parameter is the name of an image family.
        self.base_image = base_image
        # The type of the source image. Valid values:
        # 
        # *   IMAGE: custom image
        # *   IMAGE_FAMILY: image family
        self.base_image_type = base_image_type
        # The content of the image template.
        self.build_content = build_content
        # The time when the image template was created.
        self.creation_time = creation_time
        # Indicates whether to release the intermediate instance when the image fails to be created.
        self.delete_instance_on_failure = delete_instance_on_failure
        # The description of the image template.
        self.description = description
        # The family of the image created based on the image template.
        # 
        # >  This parameter is no longer used. We recommend that you use ImageOptions.ImageFamily.
        self.image_family = image_family
        # The name prefix of the image created based on the image template.
        # 
        # >  This parameter is no longer used. We recommend that you use ImageOptions.ImageName.
        self.image_name = image_name
        # The attributes of the image created based on the image template.
        self.image_options = image_options
        # The ID of the image template.
        self.image_pipeline_id = image_pipeline_id
        # The attributes and settings of the imported image.
        self.import_image_options = import_image_options
        # The instance type.
        self.instance_type = instance_type
        # The size of the outbound public bandwidth for the intermediate instance. Unit: Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the image template.
        self.name = name
        # Indicates whether the image created based on the image template supports the Non-Volatile Memory Express (NVMe) protocol.
        # 
        # >  This parameter is no longer used. We recommend that you use ImageOptions.ImageFeatures.NvmeSupport.
        self.nvme_support = nvme_support
        # The repair mode of the image template.
        # 
        # Valid values:
        # 
        # *   Standard: the standard mode
        self.repair_mode = repair_mode
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The system disk size of the intermediate instance. Unit: GiB
        self.system_disk_size = system_disk_size
        # The tags of the image template.
        self.tags = tags
        # The content of the image test template.
        self.test_content = test_content
        # The IDs of regions to which to distribute the image that will be created based on the image template.
        self.to_region_ids = to_region_ids
        # The ID of the vSwitch in the virtual private cloud (VPC).
        self.v_switch_id = v_switch_id

    def validate(self):
        if self.add_accounts:
            self.add_accounts.validate()
        if self.advanced_options:
            self.advanced_options.validate()
        if self.image_options:
            self.image_options.validate()
        if self.import_image_options:
            self.import_image_options.validate()
        if self.tags:
            self.tags.validate()
        if self.to_region_ids:
            self.to_region_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_accounts is not None:
            result['AddAccounts'] = self.add_accounts.to_map()

        if self.advanced_options is not None:
            result['AdvancedOptions'] = self.advanced_options.to_map()

        if self.base_image is not None:
            result['BaseImage'] = self.base_image

        if self.base_image_type is not None:
            result['BaseImageType'] = self.base_image_type

        if self.build_content is not None:
            result['BuildContent'] = self.build_content

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

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

        if self.image_pipeline_id is not None:
            result['ImagePipelineId'] = self.image_pipeline_id

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

        if self.repair_mode is not None:
            result['RepairMode'] = self.repair_mode

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.test_content is not None:
            result['TestContent'] = self.test_content

        if self.to_region_ids is not None:
            result['ToRegionIds'] = self.to_region_ids.to_map()

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccounts') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetAddAccounts()
            self.add_accounts = temp_model.from_map(m.get('AddAccounts'))

        if m.get('AdvancedOptions') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetAdvancedOptions()
            self.advanced_options = temp_model.from_map(m.get('AdvancedOptions'))

        if m.get('BaseImage') is not None:
            self.base_image = m.get('BaseImage')

        if m.get('BaseImageType') is not None:
            self.base_image_type = m.get('BaseImageType')

        if m.get('BuildContent') is not None:
            self.build_content = m.get('BuildContent')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DeleteInstanceOnFailure') is not None:
            self.delete_instance_on_failure = m.get('DeleteInstanceOnFailure')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageOptions') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptions()
            self.image_options = temp_model.from_map(m.get('ImageOptions'))

        if m.get('ImagePipelineId') is not None:
            self.image_pipeline_id = m.get('ImagePipelineId')

        if m.get('ImportImageOptions') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptions()
            self.import_image_options = temp_model.from_map(m.get('ImportImageOptions'))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NvmeSupport') is not None:
            self.nvme_support = m.get('NvmeSupport')

        if m.get('RepairMode') is not None:
            self.repair_mode = m.get('RepairMode')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TestContent') is not None:
            self.test_content = m.get('TestContent')

        if m.get('ToRegionIds') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetToRegionIds()
            self.to_region_ids = temp_model.from_map(m.get('ToRegionIds'))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetToRegionIds(DaraModel):
    def __init__(
        self,
        to_region_id: List[str] = None,
    ):
        self.to_region_id = to_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.to_region_id is not None:
            result['ToRegionId'] = self.to_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ToRegionId') is not None:
            self.to_region_id = m.get('ToRegionId')

        return self

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetTagsTag] = None,
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
                temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptions(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        boot_mode: str = None,
        description: str = None,
        disk_device_mappings: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsDiskDeviceMappings = None,
        features: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsFeatures = None,
        image_name: str = None,
        import_image_tags: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsImportImageTags = None,
        license_type: str = None,
        ostype: str = None,
        platform: str = None,
        retain_imported_image: bool = None,
        retention_strategy: str = None,
        role_name: str = None,
    ):
        # The operating system architecture. Valid values:
        # 
        # *   x86_64
        # *   arm64
        self.architecture = architecture
        # The boot mode of the image. Valid values:
        # 
        # *   BIOS: BIOS mode
        # *   UEFI: Unified Extensible Firmware Interface (UEFI) mode
        self.boot_mode = boot_mode
        self.description = description
        # The information of disks from which the custom images are created.
        # 
        # *   When the value of N is 1, a custom image is created from the system disk.
        # *   When the value of N is an integer in the range of 2 to 17, a custom image is created from a data disk.
        self.disk_device_mappings = disk_device_mappings
        # The attributes of the custom image.
        self.features = features
        self.image_name = image_name
        self.import_image_tags = import_image_tags
        # The type of the license to use to activate the operating system after the image is imported. Valid values:
        # 
        # *   Auto: ECS detects the operating system of the image and allocates a license to the operating system In this mode, the system first checks whether a license allocated by an official Alibaba Cloud channel is specified in the `Platform`. If a license allocated by an official Alibaba Cloud channel is specified, the system allocates the license to the imported image. If no such license is specified, the Bring Your Own License (BYOL) mode is used.
        # *   Aliyun: The license allocated through an official Alibaba Cloud channel is used for the operating system distribution specified by `Platform`.
        # *   BYOL: The license that comes with the source operating system is used. When you use the BYOL license, make sure that your license key is supported by Alibaba Cloud.
        self.license_type = license_type
        # The operating system type. Valid values:
        # 
        # *   windows: Windows operating systems
        # *   linux: Linux operating systems
        self.ostype = ostype
        # The version of the operating system. Valid values:
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
        # *   Other Windows
        self.platform = platform
        # >  This parameter is in invitational preview.
        self.retain_imported_image = retain_imported_image
        self.retention_strategy = retention_strategy
        self.role_name = role_name

    def validate(self):
        if self.disk_device_mappings:
            self.disk_device_mappings.validate()
        if self.features:
            self.features.validate()
        if self.import_image_tags:
            self.import_image_tags.validate()

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

        if self.disk_device_mappings is not None:
            result['DiskDeviceMappings'] = self.disk_device_mappings.to_map()

        if self.features is not None:
            result['Features'] = self.features.to_map()

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.import_image_tags is not None:
            result['ImportImageTags'] = self.import_image_tags.to_map()

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

        if m.get('DiskDeviceMappings') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsDiskDeviceMappings()
            self.disk_device_mappings = temp_model.from_map(m.get('DiskDeviceMappings'))

        if m.get('Features') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsFeatures()
            self.features = temp_model.from_map(m.get('Features'))

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImportImageTags') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsImportImageTags()
            self.import_image_tags = temp_model.from_map(m.get('ImportImageTags'))

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

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsImportImageTags(DaraModel):
    def __init__(
        self,
        import_image_tag: List[main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsImportImageTagsImportImageTag] = None,
    ):
        self.import_image_tag = import_image_tag

    def validate(self):
        if self.import_image_tag:
            for v1 in self.import_image_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImportImageTag'] = []
        if self.import_image_tag is not None:
            for k1 in self.import_image_tag:
                result['ImportImageTag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_image_tag = []
        if m.get('ImportImageTag') is not None:
            for k1 in m.get('ImportImageTag'):
                temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsImportImageTagsImportImageTag()
                self.import_image_tag.append(temp_model.from_map(k1))

        return self

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsImportImageTagsImportImageTag(DaraModel):
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

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsFeatures(DaraModel):
    def __init__(
        self,
        imds_support: str = None,
        nvme_support: str = None,
    ):
        self.imds_support = imds_support
        # Indicates whether the image supports the NVMe protocol. Valid values:
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

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsDiskDeviceMappings(DaraModel):
    def __init__(
        self,
        disk_device_mapping: List[main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsDiskDeviceMappingsDiskDeviceMapping] = None,
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
                temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsDiskDeviceMappingsDiskDeviceMapping()
                self.disk_device_mapping.append(temp_model.from_map(k1))

        return self

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImportImageOptionsDiskDeviceMappingsDiskDeviceMapping(DaraModel):
    def __init__(
        self,
        disk_image_size: int = None,
        format: str = None,
        ossbucket: str = None,
        ossobject: str = None,
    ):
        # The size of disk N in the custom image after the image is imported.
        # 
        # You can use this parameter to specify the sizes of the system disk and data disks in the custom image. When you specify the size of the system disk, make sure that the specified size is greater than or equal to the size of the source image file. Unit: GiB. Valid values:
        # 
        # *   When N is set to 1, this parameter indicates the size of the system disk in the custom image. Valid values: 1 to 2048.
        # *   When N is set to an integer in the range of 2 to 17, this parameter indicates the size of a data disk in the custom image. Valid values: 1 to 2048.
        # 
        # After the image file is uploaded to an OSS bucket, you can view the size of the image file in the OSS bucket.
        self.disk_image_size = disk_image_size
        # The format of the image. Valid values:
        # 
        # *   RAW
        # *   VHD
        # *   QCOW2
        self.format = format
        # The Object Storage Service (OSS) bucket where the image file is stored.
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

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptions(DaraModel):
    def __init__(
        self,
        description: str = None,
        image_family: str = None,
        image_features: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptionsImageFeatures = None,
        image_name: str = None,
        image_tags: main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptionsImageTags = None,
    ):
        # The description of the image.
        self.description = description
        # The image family.
        self.image_family = image_family
        # The feature attributes of the image.
        self.image_features = image_features
        # The prefix of the image name.
        self.image_name = image_name
        # The tags of the image.
        self.image_tags = image_tags

    def validate(self):
        if self.image_features:
            self.image_features.validate()
        if self.image_tags:
            self.image_tags.validate()

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

        if self.image_tags is not None:
            result['ImageTags'] = self.image_tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageFeatures') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptionsImageFeatures()
            self.image_features = temp_model.from_map(m.get('ImageFeatures'))

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('ImageTags') is not None:
            temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptionsImageTags()
            self.image_tags = temp_model.from_map(m.get('ImageTags'))

        return self

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptionsImageTags(DaraModel):
    def __init__(
        self,
        image_tag: List[main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptionsImageTagsImageTag] = None,
    ):
        self.image_tag = image_tag

    def validate(self):
        if self.image_tag:
            for v1 in self.image_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageTag'] = []
        if self.image_tag is not None:
            for k1 in self.image_tag:
                result['ImageTag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_tag = []
        if m.get('ImageTag') is not None:
            for k1 in m.get('ImageTag'):
                temp_model = main_models.DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptionsImageTagsImageTag()
                self.image_tag.append(temp_model.from_map(k1))

        return self

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptionsImageTagsImageTag(DaraModel):
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

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetImageOptionsImageFeatures(DaraModel):
    def __init__(
        self,
        nvme_support: str = None,
    ):
        # Indicates whether the image supports the NVMe protocol. Valid values:
        # 
        # *   supported: The image supports the NVMe protocol. Instances created from the image also support the NVMe protocol.
        # *   unsupported: The image does not support the NVMe protocol. Instances created from the image do not support the NVMe protocol.
        # *   auto: The system automatically checks whether the image supports the NVMe protocol. The system automatically checks whether the NVMe driver is installed on your image before the image is built. If you install or uninstall the NVMe driver during the image building task, the check result may be incorrect. We recommend that you set the value to supported or unsupported based on the image building content.
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

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetAdvancedOptions(DaraModel):
    def __init__(
        self,
        image_name_suffix: str = None,
        retain_cloud_assistant: bool = None,
    ):
        # Indicates whether to disable the feature that automatically adds a suffix to the name of the image created based on the image template. Valid value:
        # 
        # *   disable
        self.image_name_suffix = image_name_suffix
        # Indicates whether to retain Cloud Assistant. During the image building process, the system automatically installs Cloud Assistant in the intermediate instance to run commands. You can choose whether to retain Cloud Assistant in the new image created based on the image template. Valid values:
        # 
        # *   true: retains Cloud Assistant.
        # *   false: does not retain Cloud Assistant.
        # 
        # >  This parameter does not affect Cloud Assistant that comes with your image.
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

class DescribeImagePipelinesResponseBodyImagePipelineImagePipelineSetAddAccounts(DaraModel):
    def __init__(
        self,
        add_account: List[str] = None,
    ):
        self.add_account = add_account

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_account is not None:
            result['AddAccount'] = self.add_account

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddAccount') is not None:
            self.add_account = m.get('AddAccount')

        return self

