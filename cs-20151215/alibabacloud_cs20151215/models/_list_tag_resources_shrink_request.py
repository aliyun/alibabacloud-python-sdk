# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
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
        self.resource_ids_shrink = resource_ids_shrink
        # The resource type. Set the value to `CLUSTER`.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of labels that you want to query. You can specify up to 20 labels.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['next_token'] = self.next_token

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.resource_ids_shrink is not None:
            result['resource_ids'] = self.resource_ids_shrink

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('resource_ids') is not None:
            self.resource_ids_shrink = m.get('resource_ids')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        return self

