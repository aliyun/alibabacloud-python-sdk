# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateSnapshotRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        client_token: str = None,
        description: str = None,
        disk_id: str = None,
        instant_access: bool = None,
        instant_access_retention_days: int = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        retention_days: int = None,
        snapshot_name: str = None,
        storage_location_arn: str = None,
        tag: List[main_models.CreateSnapshotRequestTag] = None,
    ):
        # The snapshot type. Valid values:
        # 
        # - Standard: standard snapshot.
        # - Flash: local snapshot.
        # 
        # > This parameter is about to be deprecated. Standard snapshots for enterprise SSD disks (excluding standard SSD) have been upgraded to [active by default](https://help.aliyun.com/document_detail/193667.html). No additional configuration is required, and no extra costs are incurred.
        self.category = category
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that the value is unique among different requests. The **ClientToken** parameter can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The description of the snapshot. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        self.description = description
        # The ID of the cloud disk. You can call the DescribeDisks operation and filter by InstanceId to query the cloud disks attached to the instance. The cloud disk used to create a snapshot must be in the In Use or Available state. An available cloud disk must have been previously attached to an ECS instance.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Specifies whether to enable the snapshot instant access feature. Valid values:
        # - true: enables the feature. Only enterprise SSD disks (excluding standard SSD) support this feature.
        # - false: disables the feature. A standard snapshot is created.
        # 
        # Default value: false.
        # 
        # > This parameter is deprecated. Standard snapshots for enterprise SSD disks (excluding standard SSD) have been upgraded to [active by default](https://help.aliyun.com/document_detail/193667.html). No additional configuration is required, and no extra costs are incurred.
        self.instant_access = instant_access
        # Settings for the retention period of the snapshot instant access feature. The snapshot is subject to automatic release when the retention period expires. This parameter takes effect only when `InstantAccess` is set to `true`. Unit: days. Valid values: 1 to 65535.
        # 
        # Default value: the value of the `RetentionDays` parameter.
        # 
        # > This parameter is deprecated. Standard snapshots for enterprise SSD disks (excluding standard SSD) have been upgraded to [active by default](https://help.aliyun.com/document_detail/193667.html). No additional configuration is required, and no extra costs are incurred.
        self.instant_access_retention_days = instant_access_retention_days
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the resource group to which the snapshot belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # Settings for the retention period of the snapshot. Unit: days. Valid values: 1 to 65536. The snapshot is subject to automatic release when the retention period expires.
        # 
        # Default value: empty, which indicates that the snapshot is not subject to automatic release.
        self.retention_days = retention_days
        # The name of the snapshot. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and can contain Unicode letters (including English and Chinese characters) and ASCII digits (0-9). It can contain colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # > It cannot start with http:// or https://. To prevent name conflicts with automatic snapshots, it cannot start with `auto`.
        self.snapshot_name = snapshot_name
        # > This parameter is not available.
        self.storage_location_arn = storage_location_arn
        # The list of tags.
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
        if self.category is not None:
            result['Category'] = self.category

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.instant_access is not None:
            result['InstantAccess'] = self.instant_access

        if self.instant_access_retention_days is not None:
            result['InstantAccessRetentionDays'] = self.instant_access_retention_days

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.retention_days is not None:
            result['RetentionDays'] = self.retention_days

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        if self.storage_location_arn is not None:
            result['StorageLocationArn'] = self.storage_location_arn

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('InstantAccess') is not None:
            self.instant_access = m.get('InstantAccess')

        if m.get('InstantAccessRetentionDays') is not None:
            self.instant_access_retention_days = m.get('InstantAccessRetentionDays')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RetentionDays') is not None:
            self.retention_days = m.get('RetentionDays')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

        if m.get('StorageLocationArn') is not None:
            self.storage_location_arn = m.get('StorageLocationArn')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateSnapshotRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateSnapshotRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N of the snapshot. Valid values of N: 1 to 20. If this parameter is specified, it cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.key = key
        # The value of tag N of the snapshot. Valid values of N: 1 to 20. If this parameter is specified, it can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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

