# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_swas_open20200601 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.ListTagResourcesRequestTag] = None,
    ):
        # The client token that you want to use to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The **token** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html)
        self.client_token = client_token
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource. You can specify up to 50 resource IDs.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # - instance
        # 
        # - snapshot
        # 
        # - customimage
        # 
        # - command
        # 
        # - firewallrule
        # 
        # - disk
        # 
        # This parameter is required.
        self.resource_type = resource_type
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

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListTagResourcesRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag that you want to add to a resource. The tag key can be 1 to 64 characters in length.
        self.key = key
        # The value of the tag that you want to add to a resource. The tag value can be 1 to 64 characters in length.
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

