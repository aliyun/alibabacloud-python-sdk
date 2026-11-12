# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class CreateCustomImageRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_snapshot_id: str = None,
        description: str = None,
        image_name: str = None,
        instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        system_snapshot_id: str = None,
        tag: List[main_models.CreateCustomImageRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The **ClientToken** value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The ID of the data disk snapshot.
        self.data_snapshot_id = data_snapshot_id
        # The description of the image.
        self.description = description
        # The name of the custom image. The name must be 2 to 128 characters in length and must start with a letter, a Chinese character, or a digit. It can contain digits, colons (:), underscores (_), and hyphens (-). Default value: empty.
        # 
        # This parameter is required.
        self.image_name = image_name
        # The instance ID of the specified Simple Application Server.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID. You can call the [ListRegions](https://help.aliyun.com/document_detail/189315.html) operation to query available regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The ID of the system disk snapshot.
        self.system_snapshot_id = system_snapshot_id
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

        if self.data_snapshot_id is not None:
            result['DataSnapshotId'] = self.data_snapshot_id

        if self.description is not None:
            result['Description'] = self.description

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.system_snapshot_id is not None:
            result['SystemSnapshotId'] = self.system_snapshot_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DataSnapshotId') is not None:
            self.data_snapshot_id = m.get('DataSnapshotId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SystemSnapshotId') is not None:
            self.system_snapshot_id = m.get('SystemSnapshotId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateCustomImageRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateCustomImageRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N that is added to the custom image. Valid values of N: 1 to 20. The tag key cannot be an empty string. It can be up to 64 characters in length, and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        self.key = key
        # The value of tag N that is added to the custom image. Valid values of N: 1 to 20. The tag value can be an empty string. It can be up to 64 characters in length, and cannot contain http:// or https://.
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

