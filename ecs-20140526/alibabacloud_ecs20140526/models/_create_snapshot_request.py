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
        # The type of the snapshot. Valid values:
        # 
        # - Standard: a standard snapshot.
        # 
        # - Flash: a Flash Snapshot.
        # 
        # > This parameter is deprecated. standard snapshots for ESSD cloud disks now include the [Instant Access](https://help.aliyun.com/document_detail/193667.html) feature by default at no additional cost.
        self.category = category
        # A client-generated token to ensure request idempotence. The token must be unique for each request. The **ClientToken** value must be an ASCII string of up to 64 characters. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The snapshot description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # This parameter is empty by default.
        self.description = description
        # The ID of the cloud disk.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # Specifies whether to enable the Instant Access feature. Valid values:
        # 
        # - true: Enables the Instant Access feature. This feature can be enabled only for snapshots of ESSD cloud disks.
        # 
        # - false: Disables the Instant Access feature. A standard snapshot is created.
        # 
        # Default value: false.
        # 
        # > This parameter is deprecated. standard snapshots for ESSD cloud disks now include the [Instant Access](https://help.aliyun.com/document_detail/193667.html) feature by default at no additional cost.
        self.instant_access = instant_access
        # The retention period for the Instant Access feature, in days. The snapshot is automatically deleted when this retention period expires. This parameter takes effect only when `InstantAccess` is set to `true`. Valid values: 1 to 65,535.
        # 
        # Defaults to the value of `RetentionDays`.
        # 
        # > This parameter is deprecated. standard snapshots for ESSD cloud disks now include the [Instant Access](https://help.aliyun.com/document_detail/193667.html) feature by default at no additional cost.
        self.instant_access_retention_days = instant_access_retention_days
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the Resource Group to which the snapshot belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The retention period of the snapshot, in days. Valid values: 1 to 65,536. The snapshot is automatically deleted when the retention period expires.
        # 
        # If this parameter is not specified, the snapshot is retained indefinitely.
        self.retention_days = retention_days
        # The snapshot name must be 2 to 128 characters long. It must start with a letter or a Chinese character and can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # > The name cannot start with `http://` or `https://`. To avoid conflicts with auto snapshot names, the name cannot start with `auto`.
        self.snapshot_name = snapshot_name
        # > This parameter is not available for public use.
        self.storage_location_arn = storage_location_arn
        # The tags to add to the snapshot. You can add up to 20 tags.
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
        # The key of the tag.
        # 
        # > This parameter is not recommended. For better compatibility, use the Key parameter instead.
        self.key = key
        # The tag value. It can be an empty string, must be 128 characters or shorter, and cannot contain http\\:// or https\\://.
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

