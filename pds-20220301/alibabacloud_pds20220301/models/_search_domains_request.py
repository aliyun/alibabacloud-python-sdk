# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchDomainsRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
        name: str = None,
        order_by: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is empty.
        self.marker = marker
        # The name of the domain. Fuzzy search is supported.
        self.name = name
        # The sorting rule. Set the value to created_at, which specifies that the results are sorted based on the time when the domain was created.
        self.order_by = order_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.name is not None:
            result['name'] = self.name

        if self.order_by is not None:
            result['order_by'] = self.order_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')

        return self

