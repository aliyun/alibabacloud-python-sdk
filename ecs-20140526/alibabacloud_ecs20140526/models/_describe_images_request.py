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
        usable: bool = None,
        usage: str = None,
    ):
        # The scenario in which the image is used. Valid values:
        # 
        # - CreateEcs (default): creates an instance.
        # - ChangeOS: replaces the system disk or changes the operating system.
        self.action_type = action_type
        # The architecture of the image. Valid values:
        self.architecture = architecture
        # Specifies whether to perform only a dry run for the request.
        self.dry_run = dry_run
        # The list of filter conditions for querying resources.
        self.filter = filter
        # The image family name. You can set this parameter to filter images that belong to the specified image family.
        # 
        # Default value: null.
        # > For information about image families associated with Alibaba Cloud official images, see [Public image overview](https://help.aliyun.com/document_detail/108393.html).
        self.image_family = image_family
        # The image ID.
        # 
        # <details>
        # <summary>Naming conventions for image IDs</summary>
        # 
        # - Public image: Named based on the operating system version, architecture, language, and release date. For example, the image ID of a Windows Server 2008 R2 Enterprise Edition 64-bit English image is win2008r2_64_ent_sp1_en-us_40G_alibase_20190318.vhd.
        # 
        # - Custom image, shared image, Alibaba Cloud Marketplace image, and community image: Starts with m.
        # 
        # </details>
        self.image_id = image_id
        # The name of the image. Fuzzy search is supported.
        self.image_name = image_name
        # The source of the image. Valid values:
        self.image_owner_alias = image_owner_alias
        # The Alibaba Cloud account ID to which the image belongs. This parameter takes effect only when you query shared images or community images.
        self.image_owner_id = image_owner_id
        # The instance type for which you want to query available images.
        self.instance_type = instance_type
        # Specifies whether to query published community images. Valid values:
        # 
        # - true: Queries published community images. If you set this parameter to true, you must set ImageOwnerAlias to others.
        # - false: Queries image types other than community images. The specific image type depends on the value of ImageOwnerAlias.
        # 
        # Default value: false.
        self.is_public = is_public
        # Specifies whether the image supports cloud-init.
        self.is_support_cloudinit = is_support_cloudinit
        # Specifies whether the image can run on I/O optimized instances.
        self.is_support_io_optimized = is_support_io_optimized
        # The operating system type of the image. Valid values:
        self.ostype = ostype
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the image resources.
        self.page_number = page_number
        # The number of entries per page in a paged query. Settings for paging determine how many rows are returned per page.
        self.page_size = page_size
        # The region ID of the image. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the enterprise resource group to which the custom image belongs. When you use this parameter to filter resources, the number of resources cannot exceed 1,000.
        # 
        # >Default resource group-based filtering is not supported.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Specifies whether the subscription image has expired.
        self.show_expired = show_expired
        # The ID of the snapshot used to create the custom image.
        self.snapshot_id = snapshot_id
        # The status of the image. Valid values:
        self.status = status
        # The list of tags.
        self.tag = tag
        # Indicates whether the image is available.
        # >An available image can be used immediately to create instances. For more available scenarios, see [Snapshot instant access](https://help.aliyun.com/document_detail/3044728.html).
        self.usable = usable
        # Specifies whether the image is running on an ECS instance. Valid values:
        # 
        # - instance: The image is in use by an ECS instance.
        # - none: The image is idle and not in use by any ECS instance.
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

        if self.usable is not None:
            result['Usable'] = self.usable

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

        if m.get('Usable') is not None:
            self.usable = m.get('Usable')

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
        # The filter key used to query resources. Valid values:
        # 
        # - CreationStartTime: queries information about resources that are created after the point in time specified by Filter.N.Value.
        # - CreationEndTime: queries information about resources that are created before the point in time specified by Filter.N.Value.
        # - NetworkType: queries information about resources of the specified network type.
        # - CpuOnlineUpgrade, CpuOnlineDowngrade, MemoryOnlineUpgrade, or MemoryOnlineDowngrade: queries the CPU or memory hot-plugging support of the specified image.
        # 
        # Default value: null.
        self.key = key
        # The filter value used when querying resources.
        # - When Filter.N.Key is `CreationStartTime` or `CreationEndTime`, the format is `yyyy-MM-ddTHH:mmZ` in the UTC+0 time zone.
        # - When Filter.N.Key is `NetworkType`, you can specify network type values such as `vpc` and `classic`.
        # 
        # - When Filter.N.Key is set to `CpuOnlineUpgrade`, `CpuOnlineDowngrade`, `MemoryOnlineUpgrade`, or `MemoryOnlineDowngrade`, the value can be `supported` or `unsupported`.
        # 
        # Default value: null.
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

