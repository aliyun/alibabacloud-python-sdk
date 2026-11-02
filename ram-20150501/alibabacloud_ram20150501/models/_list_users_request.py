# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListUsersRequest(DaraModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        # If the response is truncated, you can use the Marker parameter to retrieve the remaining items.
        self.marker = marker
        # The maximum number of entries to return. If the response is truncated because the maximum number of entries is reached, the IsTruncated response parameter is set to true.
        # 
        # Valid values: 1 to 1000. Default value: 100.
        self.max_items = max_items

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('MaxItems') is not None:
            self.max_items = m.get('MaxItems')

        return self

