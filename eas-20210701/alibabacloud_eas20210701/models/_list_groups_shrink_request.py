# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGroupsShrinkRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        labels_shrink: str = None,
        order: str = None,
        page_number: str = None,
        page_size: str = None,
        sort: str = None,
        traffic_mode: str = None,
        workspace_id: str = None,
    ):
        # The filter name. Fuzzy match is supported.
        self.filter = filter
        # The user-defined labels.
        self.labels_shrink = labels_shrink
        # The sort order of the results.
        self.order = order
        # The current page number of the service group list. Default value: 1.
        self.page_number = page_number
        # The number of service groups to display on each page in a paged query. Settings for paging default to 100.
        self.page_size = page_size
        # The field by which to sort the results.
        self.sort = sort
        # The traffic allocation method used to filter service groups.
        self.traffic_mode = traffic_mode
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.labels_shrink is not None:
            result['Labels'] = self.labels_shrink

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.traffic_mode is not None:
            result['TrafficMode'] = self.traffic_mode

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('Labels') is not None:
            self.labels_shrink = m.get('Labels')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('TrafficMode') is not None:
            self.traffic_mode = m.get('TrafficMode')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

