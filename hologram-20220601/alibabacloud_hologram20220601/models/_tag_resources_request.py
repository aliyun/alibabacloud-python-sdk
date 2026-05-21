# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hologram20220601 import models as main_models
from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_type: str = None,
        category: str = None,
        resource_ids: List[str] = None,
        tag_owner_uid: int = None,
        tags: List[main_models.TagResourcesRequestTags] = None,
    ):
        self.region_id = region_id
        self.resource_type = resource_type
        self.category = category
        self.resource_ids = resource_ids
        self.tag_owner_uid = tag_owner_uid
        self.tags = tags

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
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.category is not None:
            result['category'] = self.category

        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids

        if self.tag_owner_uid is not None:
            result['tagOwnerUid'] = self.tag_owner_uid

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')

        if m.get('tagOwnerUid') is not None:
            self.tag_owner_uid = m.get('tagOwnerUid')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.TagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class TagResourcesRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

