# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSAMLProvidersRequest(DaraModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        # The `marker`. If part of a previous response is truncated, you can use this parameter to obtain the truncated part.
        self.marker = marker
        # The number of entries to return. If a response is truncated because it reaches the value of `MaxItems`, the value of `IsTruncated` will be `true`.
        # 
        # Valid values: 1 to 100. Default value: 100.
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

