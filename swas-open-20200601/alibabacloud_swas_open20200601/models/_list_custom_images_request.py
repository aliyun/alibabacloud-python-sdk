# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListCustomImagesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        data_snapshot_id: str = None,
        image_ids: str = None,
        image_names: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        share: bool = None,
        system_snapshot_id: str = None,
        tag: List[main_models.ListCustomImagesRequestTag] = None,
    ):
        # The client token that is used to ensure the idempotence of the request. A client token is generated from your client and must be unique among different requests. **ClientToken** supports only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The data cloud disk snapshot ID.
        self.data_snapshot_id = data_snapshot_id
        # The image IDs of the simple application servers. The value can be a JSON array that consists of up to 100 instance IDs. Separate multiple instance IDs with commas (,).
        self.image_ids = image_ids
        # The image names of the simple application servers. The value can be a JSON array that consists of up to 100 instance IDs. Separate multiple instance IDs with commas (,).
        self.image_names = image_names
        # The instance ID of the simple application server from which the image was created.
        self.instance_id = instance_id
        # The page number of the snapshot list.
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page for a paged query.
        # 
        # - Maximum value: 100.
        # - Default value: 10.
        self.page_size = page_size
        # The region ID of the simple application servers. You can call [ListRegions](https://help.aliyun.com/document_detail/189315.html) to query the list of supported regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # Specifies whether to query shared images. Valid values:
        # 
        # - False: The response does not include shared images.
        # 
        # - True: Only shared images are returned.
        # 
        # If this parameter is not specified, all images are returned by default.
        self.share = share
        # The system cloud disk snapshot ID.
        self.system_snapshot_id = system_snapshot_id
        # The tags of the custom images.
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

        if self.image_ids is not None:
            result['ImageIds'] = self.image_ids

        if self.image_names is not None:
            result['ImageNames'] = self.image_names

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.share is not None:
            result['Share'] = self.share

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

        if m.get('ImageIds') is not None:
            self.image_ids = m.get('ImageIds')

        if m.get('ImageNames') is not None:
            self.image_names = m.get('ImageNames')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Share') is not None:
            self.share = m.get('Share')

        if m.get('SystemSnapshotId') is not None:
            self.system_snapshot_id = m.get('SystemSnapshotId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListCustomImagesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListCustomImagesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the custom image. Valid values of the tag key length: 1 to 64. Valid values of N: 1 to 20.
        self.key = key
        # The tag value of the custom image. Valid values of the tag value length: 1 to 64. Valid values of N: 1 to 20.
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

