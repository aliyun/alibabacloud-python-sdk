# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tag_keys_shrink: str = None,
    ):
        # Specifies whether to remove all custom labels. This parameter takes effect only when `tag_keys` is left empty. Valid values:
        # 
        # *   `true`: Remove all custom labels.
        # *   `false`: Do not remove all custom labels.
        self.all = all
        # The region ID of the resources.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of resource IDs.
        # 
        # This parameter is required.
        self.resource_ids_shrink = resource_ids_shrink
        # The type of resource. Set the value to `CLUSTER`.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The list of keys of the labels that you want to remove.
        # 
        # This parameter is required.
        self.tag_keys_shrink = tag_keys_shrink

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

        if self.resource_ids_shrink is not None:
            result['resource_ids'] = self.resource_ids_shrink

        if self.resource_type is not None:
            result['resource_type'] = self.resource_type

        if self.tag_keys_shrink is not None:
            result['tag_keys'] = self.tag_keys_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('resource_ids') is not None:
            self.resource_ids_shrink = m.get('resource_ids')

        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')

        if m.get('tag_keys') is not None:
            self.tag_keys_shrink = m.get('tag_keys')

        return self

