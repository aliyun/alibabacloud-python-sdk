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
        # The scenario in which the image is used. Valid values:
        # 
        # *   CreateEcs: instance creation
        # *   ChangeOS: replacement of the system disk or OS
        self.action_type = action_type
        # The architecture of the image. Valid values:
        # 
        # *   i386
        # *   x86_64
        # *   arm64
        self.architecture = architecture
        # Specifies whether to perform only a dry run without performing the actual request.
        # 
        # *   true: performs only a dry run. The system checks whether your AccessKey pair is valid, whether RAM users are granted required permissions, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # *   false: performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        # 
        # Default value: false.
        self.dry_run = dry_run
        # The filter conditions used to query resources.
        self.filter = filter
        # The name of the image family. You can set this parameter to query images of the specified image family.
        # 
        # This parameter is empty by default.
        # 
        # >  For information about image families that are associated with Alibaba Cloud official images, see [Overview of public images](https://help.aliyun.com/document_detail/108393.html).
        self.image_family = image_family
        # The ID of the image.
        # 
        # **Naming rules for image IDs**
        # 
        # *   IDs of public images are named after the operating system version numbers, architectures, languages, and release dates of the images. For example, the ID of a Windows Server 2008 R2 Enterprise 64-bit (English) public image is win2008r2_64_ent_sp1_en-us_40G_alibase_20190318.vhd.
        # *   IDs of custom images, shared images, Alibaba Cloud Marketplace images, and community images start with m.
        self.image_id = image_id
        # The image name. Fuzzy match is supported.
        self.image_name = image_name
        # The image source. Valid values:
        # 
        # *   system: images that are provided by Alibaba Cloud and are not released in Alibaba Cloud Marketplace, which are different from public images in the Elastic Compute Service (ECS) console.
        # 
        # *   self: your custom images
        # 
        # *   others: shared images (images shared by other Alibaba Cloud accounts) and community images (publicly available custom images that are published by other Alibaba Cloud accounts). Take note of the following items:
        # 
        #     *   To query community images, you must set IsPublic to true.
        #     *   To query shared images, you must set IsPublic to false or leave IsPublic empty.
        # 
        # *   marketplace: images released by Alibaba Cloud or independent software vendors (ISVs) in the Alibaba Cloud Marketplace, which must be purchased together with ECS instances. Take note of the billing details of the images.
        # 
        # This parameter is empty by default.
        # 
        # > By default, this parameter is empty, which indicates that the following images are queried: public images provided by Alibaba Cloud, custom images in your repository, shared images from other Alibaba Cloud accounts, and community images that are published by other Alibaba Cloud accounts.
        self.image_owner_alias = image_owner_alias
        # The ID of the Alibaba Cloud account to which the image belongs. This parameter takes effect only if you query shared images or community images.
        self.image_owner_id = image_owner_id
        # The instance type for which the image can be used.
        self.instance_type = instance_type
        # Specifies whether to query published community images. Valid values:
        # 
        # *   true: queries published community images. When you set this parameter to true, you must set ImageOwnerAlias to others.
        # *   false: queries image types other than the community images type. The specific image types to be queried are determined by the ImageOwnerAlias value.
        # 
        # Default value: false.
        self.is_public = is_public
        # Specifies whether the image supports cloud-init.
        self.is_support_cloudinit = is_support_cloudinit
        # Specifies whether the image can be used on I/O optimized instances.
        self.is_support_io_optimized = is_support_io_optimized
        # The operating system type of the image. Valid values:
        # 
        # *   windows
        # *   linux
        self.ostype = ostype
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number to return.
        # 
        # Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the image. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which the custom image belongs. If you specify this parameter to query resources, up to 1,000 resources that belong to the specified resource group can be returned.
        # 
        # > Resources in the default resource group are displayed in the response regardless of whether you specify this parameter.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether the subscription image has expired.
        self.show_expired = show_expired
        # The ID of the snapshot used to create the custom image.
        self.snapshot_id = snapshot_id
        # The status of the image. By default, if you do not specify this parameter, only images in the Available state are returned. Valid values:
        # 
        # *   Creating: The image is being created.
        # *   Waiting: The image is waiting to be processed.
        # *   Available: The image is available.
        # *   UnAvailable: The image is unavailable.
        # *   CreateFailed: The image fails to be created.
        # *   Deprecated: The image is no longer used.
        # 
        # Default value: Available. You can specify multiple values for this parameter. Separate the values with commas (,).
        self.status = status
        # The tags list.
        self.tag = tag
        # Specifies whether the image is running on an Elastic Compute Service (ECS) instance. Valid values:
        # 
        # *   instance: The image is already in use and running on an ECS instance.
        # *   none: The image is idle.
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
        # The tag N key of the image. Valid values of N: 1 to 20.
        # 
        # Up to 1,000 resources that match the specified tags can be returned in the response. To query more than 1,000 resources that match the specified tags, call the [ListTagResources](https://help.aliyun.com/document_detail/110425.html) operation.
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
        # The key of filter N used to query resources. Valid values:
        # 
        # *   If you set this parameter to `CreationStartTime`, you can query the resources that were created after the point in time specified by `Filter.N.Value`.
        # *   If you set this parameter to `CreationEndTime`, you can query the resources that were created before the point in time specified by `Filter.N.Value`.
        # *   If you set this parameter to `NetworkType`, you can query resources of the specified network type.
        self.key = key
        # The value of filter N used to query resources. Valid values:
        # 
        # *   When `Filter.N.Key` is set to `CreationStartTime` or `CreationEndTime`, the format is `yyyy-MM-ddTHH:mmZ` in the UTC+0 time zone.
        # *   When `Filter.N.Key` is set to `NetworkType`, the valid values can be `vpc` or `classic`.
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

