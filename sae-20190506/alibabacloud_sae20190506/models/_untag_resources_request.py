# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        delete_all: bool = None,
        region_id: str = None,
        resource_ids: str = None,
        resource_type: str = None,
        tag_keys: str = None,
    ):
        # Specifies whether to remove all the specified tags. This parameter takes effect only if the TagKeys parameter is specified. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.delete_all = delete_all
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of resources. Separate multiple resource IDs with comma (,).
        # 
        # This parameter is required.
        self.resource_ids = resource_ids
        # The type of the resource. Set the value to `application`.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys. Separate multiple tag keys with commas (,).
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delete_all is not None:
            result['DeleteAll'] = self.delete_all

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeleteAll') is not None:
            self.delete_all = m.get('DeleteAll')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')

        return self

