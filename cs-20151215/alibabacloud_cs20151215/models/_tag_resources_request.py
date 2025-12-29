# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class TagResourcesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tags: List[main_models.Tag] = None,
    ):
        # The ID of the region in which the resource resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of resource IDs.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The type of resources that you want to label. Set the value to `CLUSTER`.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to add to the resources in key-value pairs. You can add up to 20 key-value pairs. Note:
        # 
        # *   The values cannot be empty strings. A value must be 1 to 128 characters in length.
        # *   A key or value cannot start with `aliyun` or `acs:`.
        # *   A key or value cannot contain `http://` or `https://`.
        # 
        # This parameter is required.
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
            result['region_id'] = self.region_id

        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('resource_ids') is not None:
            self.resource_ids = m.get('resource_ids')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        return self

