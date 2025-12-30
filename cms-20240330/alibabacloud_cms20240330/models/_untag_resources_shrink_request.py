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
        self.all = all
        # This parameter is required.
        self.resource_id_shrink = resource_id_shrink
        # This parameter is required.
        self.resource_type = resource_type
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

