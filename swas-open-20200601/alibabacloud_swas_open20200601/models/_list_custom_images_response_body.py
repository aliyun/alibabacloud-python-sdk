# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListCustomImagesResponseBody(DaraModel):
    def __init__(
        self,
        custom_images: List[main_models.ListCustomImagesResponseBodyCustomImages] = None,
        page_number: str = None,
        page_size: str = None,
        request_id: str = None,
        total_count: str = None,
    ):
        # The custom images.
        self.custom_images = custom_images
        # The page number.
        self.page_number = page_number
        # The number of entries per page in Settings for the paged query.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.custom_images:
            for v1 in self.custom_images:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomImages'] = []
        if self.custom_images is not None:
            for k1 in self.custom_images:
                result['CustomImages'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_images = []
        if m.get('CustomImages') is not None:
            for k1 in m.get('CustomImages'):
                temp_model = main_models.ListCustomImagesResponseBodyCustomImages()
                self.custom_images.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomImagesResponseBodyCustomImages(DaraModel):
    def __init__(
        self,
        create_instances: List[str] = None,
        creation_time: str = None,
        data_snapshot_id: str = None,
        data_snapshot_name: str = None,
        description: str = None,
        image_id: str = None,
        in_share: bool = None,
        in_share_user: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        name: str = None,
        os_type: str = None,
        region_id: str = None,
        required_data_disk_size: int = None,
        required_system_disk_size: int = None,
        resource_group_id: str = None,
        source_image_name: str = None,
        source_image_version: str = None,
        status: str = None,
        system_snapshot_id: str = None,
        system_snapshot_name: str = None,
        tags: List[main_models.ListCustomImagesResponseBodyCustomImagesTags] = None,
        user_id: int = None,
    ):
        # The information about instances created from the image.
        self.create_instances = create_instances
        # The time when the snapshot was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The data cloud disk snapshot ID.
        self.data_snapshot_id = data_snapshot_id
        # The name of the data cloud disk snapshot.
        self.data_snapshot_name = data_snapshot_name
        # The description.
        self.description = description
        # The custom image ID.
        self.image_id = image_id
        # Indicates whether the custom image is shared to ECS.
        self.in_share = in_share
        # Indicates whether the custom image is shared across accounts.
        self.in_share_user = in_share_user
        # The instance ID of the simple application server from which the image was created.
        self.instance_id = instance_id
        # The name of the simple application server instance.
        self.instance_name = instance_name
        # The name of the custom image.
        self.name = name
        # The operating system type of the image.
        self.os_type = os_type
        # The region ID.
        self.region_id = region_id
        # The data cloud disk size of the image. Unit: GiB.
        self.required_data_disk_size = required_data_disk_size
        # The system cloud disk size of the image. Unit: GiB.
        self.required_system_disk_size = required_system_disk_size
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The name of the source image.
        self.source_image_name = source_image_name
        # The image version of the source image.
        self.source_image_version = source_image_version
        # The status of the custom image. Valid values:
        # 
        # - 0: copying.
        # 
        # - 1: active.
        # - 2: unavailable.
        # - 3: creation failed.
        # - 4: creating.
        self.status = status
        # The system cloud disk snapshot ID.
        self.system_snapshot_id = system_snapshot_id
        # The name of the system cloud disk snapshot.
        self.system_snapshot_name = system_snapshot_name
        # The tags of the custom images.
        self.tags = tags
        # The Alibaba Cloud account ID of the image owner.
        self.user_id = user_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_instances is not None:
            result['CreateInstances'] = self.create_instances

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_snapshot_id is not None:
            result['DataSnapshotId'] = self.data_snapshot_id

        if self.data_snapshot_name is not None:
            result['DataSnapshotName'] = self.data_snapshot_name

        if self.description is not None:
            result['Description'] = self.description

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.in_share is not None:
            result['InShare'] = self.in_share

        if self.in_share_user is not None:
            result['InShareUser'] = self.in_share_user

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.name is not None:
            result['Name'] = self.name

        if self.os_type is not None:
            result['OsType'] = self.os_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.required_data_disk_size is not None:
            result['RequiredDataDiskSize'] = self.required_data_disk_size

        if self.required_system_disk_size is not None:
            result['RequiredSystemDiskSize'] = self.required_system_disk_size

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.source_image_name is not None:
            result['SourceImageName'] = self.source_image_name

        if self.source_image_version is not None:
            result['SourceImageVersion'] = self.source_image_version

        if self.status is not None:
            result['Status'] = self.status

        if self.system_snapshot_id is not None:
            result['SystemSnapshotId'] = self.system_snapshot_id

        if self.system_snapshot_name is not None:
            result['SystemSnapshotName'] = self.system_snapshot_name

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateInstances') is not None:
            self.create_instances = m.get('CreateInstances')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataSnapshotId') is not None:
            self.data_snapshot_id = m.get('DataSnapshotId')

        if m.get('DataSnapshotName') is not None:
            self.data_snapshot_name = m.get('DataSnapshotName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InShare') is not None:
            self.in_share = m.get('InShare')

        if m.get('InShareUser') is not None:
            self.in_share_user = m.get('InShareUser')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OsType') is not None:
            self.os_type = m.get('OsType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequiredDataDiskSize') is not None:
            self.required_data_disk_size = m.get('RequiredDataDiskSize')

        if m.get('RequiredSystemDiskSize') is not None:
            self.required_system_disk_size = m.get('RequiredSystemDiskSize')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SourceImageName') is not None:
            self.source_image_name = m.get('SourceImageName')

        if m.get('SourceImageVersion') is not None:
            self.source_image_version = m.get('SourceImageVersion')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SystemSnapshotId') is not None:
            self.system_snapshot_id = m.get('SystemSnapshotId')

        if m.get('SystemSnapshotName') is not None:
            self.system_snapshot_name = m.get('SystemSnapshotName')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListCustomImagesResponseBodyCustomImagesTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ListCustomImagesResponseBodyCustomImagesTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the custom image.
        self.key = key
        # The tag value of the custom image.
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

