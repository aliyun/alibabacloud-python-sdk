# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UntagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        resource_id_shrink: str = None,
        resource_type: str = None,
        tag_key_shrink: str = None,
    ):
        # Specifies whether to remove all tags from the specified one or more resources. This parameter takes effect only if the tagKey parameter is not specified. Valid values: true and false. Default value: false.
        self.all = all
        # The resource IDs. You can specify a maximum number of 50 IDs.
        # 
        # This parameter is required.
        self.resource_id_shrink = resource_id_shrink
        # The resource type.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The keys of tags. You can specify a maximum number of 20 keys.
        self.tag_key_shrink = tag_key_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['all'] = self.all

        if self.resource_id_shrink is not None:
            result['resourceId'] = self.resource_id_shrink

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        if self.tag_key_shrink is not None:
            result['tagKey'] = self.tag_key_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')

        if m.get('resourceId') is not None:
            self.resource_id_shrink = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        if m.get('tagKey') is not None:
            self.tag_key_shrink = m.get('tagKey')

        return self

