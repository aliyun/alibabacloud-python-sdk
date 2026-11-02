# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListRolesShrinkRequest(DaraModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
        tag_shrink: str = None,
    ):
        # The marker used to retrieve the remaining results when the response is truncated.
        self.marker = marker
        # The maximum number of entries to return. If the number of entries exceeds this value, the response is truncated and the `IsTruncated` parameter is set to `true`.
        # 
        # Valid values: 1 to 1000. Default value: 100.
        self.max_items = max_items
        # The tags.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.marker is not None:
            result['Marker'] = self.marker

        if self.max_items is not None:
            result['MaxItems'] = self.max_items

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

