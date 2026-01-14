# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
    ):
        # Whether to delete all tags.
        self.all = all
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs, in the JSON format.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of resource.
        # 
        # Set this parameter to **instance**. The value of this parameter cannot be changed.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of tags.
        self.tag_key = tag_key

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
            result['regionId'] = self.region_id

        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        return self

