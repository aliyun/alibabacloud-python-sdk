# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGroupsRequest(DaraModel):
    def __init__(
        self,
        marker: str = None,
        max_items: int = None,
    ):
        # The token for querying the next page of results. You do not need to specify `Marker` for the first API call.
        # 
        # If the total number of returned entries exceeds the `MaxItems` limit during the first API call, the data is truncated and only `MaxItems` entries are returned. In this case, the `IsTruncated` response parameter is `true` and a `Marker` is returned. You can use the `Marker` returned from the previous call to continue calling the API with the other request parameters unchanged to query the truncated data. You can repeat this process until `IsTruncated` is `false`, which indicates that all data has been queried.
        self.marker = marker
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 100.
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

