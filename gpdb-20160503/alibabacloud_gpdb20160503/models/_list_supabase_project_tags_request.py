# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class ListSupabaseProjectTagsRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[main_models.ListSupabaseProjectTagsRequestTag] = None,
    ):
        # The token for the next page of results. This token is returned in the `NextToken` parameter of a previous request.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The instance ID.
        # 
        # > You must specify at least one of the `ResourceId` and `Tag` parameters.
        self.resource_id = resource_id
        # The resource type. Set the value to `instance`.
        self.resource_type = resource_type
        # A list of tags.
        # 
        # > You must specify at least one of the `ResourceId` and `Tag` parameters.
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
                temp_model = main_models.ListSupabaseProjectTagsRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListSupabaseProjectTagsRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The key can be 1 to 64 characters in length.
        # 
        # The `Tag.N` parameter specifies a key-value pair to filter Supabase instances.
        # 
        # N is an integer from 1 to 20.
        # 
        # - If you specify only `Tag.N.Key`, the operation returns all instances that have the specified tag key.
        # 
        # - If you specify only `Tag.N.Value`, an `InvalidParameter.TagValue` error is returned.
        # 
        # - If you specify multiple tag key-value pairs, the operation returns only Supabase instances that match all the specified pairs.
        self.key = key
        # The tag value. The value can be 1 to 128 characters in length.
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

