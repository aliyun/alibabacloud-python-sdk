# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
    ):
        # The IDs of the resources whose tags you want to query. You must specify at least one of resourceId and tags.
        self.resource_id_shrink = resource_id_shrink
        # The type of the resource. Valid values:
        # 
        # *   project
        # *   logstore
        # *   dashboard
        # *   machinegroup
        # *   logtailconfig
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags that you want to use to filter resources based on exact match. Each tag is a key-value pair. You must specify at least one of resourceId and tags.
        # 
        # You can enter up to 20 tags.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        return self

