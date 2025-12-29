# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ListTagResourcesRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tags: List[main_models.Tag] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of cluster IDs.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The resource type. Set the value to `CLUSTER`.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of labels that you want to query. You can specify up to 20 labels.
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
        if self.next_token is not None:
            result['next_token'] = self.next_token

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
        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

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

