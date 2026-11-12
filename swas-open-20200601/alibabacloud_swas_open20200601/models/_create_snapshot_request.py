# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class CreateSnapshotRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        disk_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        snapshot_name: str = None,
        tag: List[main_models.CreateSnapshotRequestTag] = None,
    ):
        # Ensures the idempotence of the request. You can generate the value from your client to ensure that the value is unique across different requests. **ClientToken** only supports ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the disk.
        # 
        # This parameter is required.
        self.disk_id = disk_id
        # The region ID of the Simple Application Server instance to which the specified disk belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The name of the snapshot. The name must be 2 to 50 characters in length and must start with a letter or a Chinese character. It cannot start with `http://` or `https://`. It can contain Chinese characters, English letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.snapshot_name = snapshot_name
        # The list of tags. You can specify up to 20 tags.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.snapshot_name is not None:
            result['SnapshotName'] = self.snapshot_name

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SnapshotName') is not None:
            self.snapshot_name = m.get('SnapshotName')

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
        # The tag key specified for the snapshot. Valid values of N: 1 to 20.
        # 
        # The tag key cannot be an empty string once specified. It can be up to 64 characters in length and cannot start with aliyun or acs:. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value specified for the snapshot. Valid values of N: 1 to 20.
        # 
        # The tag value can be an empty string. It can be up to 64 characters in length and cannot contain `http://` or `https://`.
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

