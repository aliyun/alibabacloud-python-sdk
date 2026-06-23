# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tag_keys: List[str] = None,
    ):
        # Specifies whether to delete all custom tags. This parameter takes effect only when `tag_keys` is empty. Valid values:
        # 
        # - `true`: Delete all tags.
        # - `false`: Do not delete all tags.
        self.all = all
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of resource IDs. You can specify up to 50 resource IDs.
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The resource type.
        # 
        # CLUSTER: cluster.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of tag keys for the resource. You can specify up to 20 tag keys.
        # 
        # This parameter is required.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['all'] = self.all

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.tag_keys is not None:
            result['tag_keys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('resource_ids') is not None:
            self.resource_ids = m.get('resource_ids')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('tag_keys') is not None:
            self.tag_keys = m.get('tag_keys')

        return self

