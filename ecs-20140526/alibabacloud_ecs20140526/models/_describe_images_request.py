# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeImagesRequest(DaraModel):
    def __init__(
        self,
        action_type: str = None,
        architecture: str = None,
        dry_run: bool = None,
        filter: List[main_models.DescribeImagesRequestFilter] = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        image_owner_alias: str = None,
        image_owner_id: int = None,
        instance_type: str = None,
        is_public: bool = None,
        is_support_cloudinit: bool = None,
        is_support_io_optimized: bool = None,
        ostype: str = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        show_expired: bool = None,
        snapshot_id: str = None,
        status: str = None,
        tag: List[main_models.DescribeImagesRequestTag] = None,
        usage: str = None,
    ):
        # The scenario in which the image will be used. Valid values:
        # 
        # - CreateEcs (default): Create an instance.
        # 
        # - ChangeOS: Replace the system disk or change the operating system.
        self.action_type = action_type
        # The architecture of the image. Valid values:
        # 
        # - i386
        # 
        # - x86_64
        # 
        # - arm64
        self.architecture = architecture
        # Specifies whether to perform a dry run of the request.
        # 
        # - true: Sends a dry run request without querying resource status. The system checks whether the AccessKey is valid, whether the Resource Access Management (RAM) user is authorized, and whether all required parameters are specified. If the check fails, an error is returned. If the check passes, the error code DryRunOperation is returned.
        # 
        # - false: Sends a normal request. After the check passes, an HTTP 2XX status code is returned and the resource status is queried directly.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # A list of filter conditions for querying resources.
        self.filter = filter
        # The name of the image family. When querying images, you can use this parameter to filter images belonging to the specified image family.
        # 
        # Default value: empty.
        # 
        # > For information about image families associated with official Alibaba Cloud images, see [Overview of public images](https://help.aliyun.com/document_detail/108393.html).
        self.image_family = image_family
        # The image ID.
        # 
        # <details>
        # 
        # <summary>
        # 
        # Naming convention for image IDs
        # 
        # </summary>
        # 
        # - Public images: Named based on the operating system version, architecture, language, and published date. For example, the image ID for Windows Server 2008 R2 Enterprise Edition, 64-bit English system is `win2008r2_64_ent_sp1_en-us_40G_alibase_20190318.vhd`.
        # 
        # - Custom images, shared images, Alibaba Cloud Marketplace images, and community images: Start with the letter `m`.
        # 
        # </details>
        self.image_id = image_id
        # The name of the image. Fuzzy search is supported.
        self.image_name = image_name
        # The source of the image. Valid values:
        # 
        # - system: Images provided by Alibaba Cloud that are not published on Alibaba Cloud Marketplace. This differs from the "public image" concept in the console.
        # 
        # - self: Your custom images.
        # 
        # - others: Includes shared images (images directly shared with you by other Alibaba Cloud users) and community images (custom images fully publicly shared by any Alibaba Cloud user). Note the following:
        # 
        #   - To find community images, IsPublic must be true.
        # 
        #   - To find shared images, IsPublic must be set to false or omitted.
        # 
        # - marketplace: Images published on Alibaba Cloud Marketplace by Alibaba Cloud or third-party ISVs, which must be purchased together with ECS instances. Please review the pricing details of Alibaba Cloud Marketplace images yourself.
        # 
        # Default value: empty.
        # 
        # > An empty value returns results with ImageOwnerAlias values of system, self, and others.
        self.image_owner_alias = image_owner_alias
        # The Alibaba Cloud account ID to which the image belongs. This parameter takes effect only when you query shared images and community images.
        self.image_owner_id = image_owner_id
        # Queries images that can be used with the specified instance type.
        self.instance_type = instance_type
        # Specifies whether to query published community images. Valid values:
        # 
        # - true: Queries published community images. When this parameter is set to true, ImageOwnerAlias must be set to others.
        # 
        # - false: Queries other image types excluding community images, depending on the value of the ImageOwnerAlias parameter.
        # 
        # Default Value: false.
        self.is_public = is_public
        # Indicates whether the image supports cloud-init.
        self.is_support_cloudinit = is_support_cloudinit
        # Indicates whether the image can run on I/O optimized instances.
        self.is_support_io_optimized = is_support_io_optimized
        # The operating system type of the image. Valid values:
        # 
        # - windows
        # 
        # - linux
        self.ostype = ostype
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the image resource list.
        # 
        # Starting value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page in a paged query.
        # 
        # Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID to which the image belongs. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to view the latest list of Alibaba Cloud regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the enterprise resource group to which the custom image belongs. When using this parameter to filter resources, the number of resources cannot exceed 1,000.
        # 
        # > Filtering by the default resource group is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Indicates whether subscription-based images have exceeded their usage period.
        self.show_expired = show_expired
        # The custom image created from a specific snapshot ID.
        self.snapshot_id = snapshot_id
        # Queries images in the specified status. If this parameter is not configured, only images in the Available status are returned by default. Valid values:
        # 
        # - Creating: The image is being created.
        # 
        # - Waiting: The image is queued for multitasking.
        # 
        # - Available (default): The image is available for your use.
        # 
        # - UnAvailable: The image is unavailable for your use.
        # 
        # - CreateFailed: The image creation failed.
        # 
        # - Deprecated: The image has been deprecated.
        # 
        # Default value: Available. This parameter supports multiple values separated by commas (,).
        self.status = status
        # The list of tags.
        self.tag = tag
        # Indicates whether the image is already running on an ECS instance. Valid values:
        # 
        # - instance: The image is in use by one or more ECS instances.
        # 
        # - none: The image is idle and not used by any ECS instance.
        self.usage = usage

    def validate(self):
        if self.filter:
            for v1 in self.filter:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_type is not None:
            result['ActionType'] = self.action_type

        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['Filter'] = []
        if self.filter is not None:
            for k1 in self.filter:
                result['Filter'].append(k1.to_map() if k1 else None)

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

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.is_public is not None:
            result['IsPublic'] = self.is_public

        if self.is_support_cloudinit is not None:
            result['IsSupportCloudinit'] = self.is_support_cloudinit

        if self.is_support_io_optimized is not None:
            result['IsSupportIoOptimized'] = self.is_support_io_optimized

        if self.ostype is not None:
            result['OSType'] = self.ostype

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.show_expired is not None:
            result['ShowExpired'] = self.show_expired

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.status is not None:
            result['Status'] = self.status

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.usage is not None:
            result['Usage'] = self.usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionType') is not None:
            self.action_type = m.get('ActionType')

        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.filter = []
        if m.get('Filter') is not None:
            for k1 in m.get('Filter'):
                temp_model = main_models.DescribeImagesRequestFilter()
                self.filter.append(temp_model.from_map(k1))

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

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('IsPublic') is not None:
            self.is_public = m.get('IsPublic')

        if m.get('IsSupportCloudinit') is not None:
            self.is_support_cloudinit = m.get('IsSupportCloudinit')

        if m.get('IsSupportIoOptimized') is not None:
            self.is_support_io_optimized = m.get('IsSupportIoOptimized')

        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ShowExpired') is not None:
            self.show_expired = m.get('ShowExpired')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeImagesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('Usage') is not None:
            self.usage = m.get('Usage')

        return self

class DescribeImagesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the image. Valid values of N: 1 to 20.
        # 
        # When you use one tag to filter resources, the number of resources retrieved under this tag cannot exceed 1,000. When you use multiple tags to filter resources, the number of resources that are attached with all specified tags cannot exceed 1,000. If the resource count exceeds 1,000, use the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) API to query the resources.
        self.key = key
        # The tag value of the image. Valid values of N: 1 to 20.
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

class DescribeImagesRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The filter key used when querying resources. Valid values:
        # 
        # - If this parameter is set to `CreationStartTime`, you can query resources created after the specified time point (`Filter.N.Value`).
        # 
        # - If this parameter is set to `CreationEndTime`, you can query resources created before the specified time point (`Filter.N.Value`).
        # 
        # - If this parameter is set to `NetworkType`, you can query resources of the specified network type.
        # 
        # - If this parameter is set to any of `CpuOnlineUpgrade`, `CpuOnlineDowngrade`, `MemoryOnlineUpgrade`, or `MemoryOnlineDowngrade`, you can query the hot-swapping support status of CPU or memory for the specified image.
        # 
        # Default Value: null.
        self.key = key
        # The filter value used when querying resources.
        # 
        # - When (`Filter.N.Key`) is `CreationStartTime` or `CreationEndTime`, the format is `yyyy-MM-ddTHH:mmZ` in UTC+0 time zone.
        # 
        # - When (`Filter.N.Key`) is `NetworkType`, valid values include `vpc`, `classic`, etc.
        # 
        # - When (`Filter.N.Key`) is `CpuOnlineUpgrade`, `CpuOnlineDowngrade`, `MemoryOnlineUpgrade`, or `MemoryOnlineDowngrade`, the value can be `supported` or `unsupported`.
        # 
        # Default Value: null.
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

