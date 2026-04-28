# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListShareLinkRequest(DaraModel):
    def __init__(
        self,
        creator: str = None,
        include_cancelled: bool = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        order_direction: str = None,
    ):
        # The creator of the share.
        self.creator = creator
        # Specifies whether to return the shares that are canceled.
        self.include_cancelled = include_cancelled
        # The maximum number of results to return. Valid values: 0 to 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The field by which to sort the returned results. Default value: created_at. Valid values:
        # 
        # *   share_name: sorts the results by the name of the share.
        # *   updated_at: sorts the results by the time when the share was modified.
        # *   description: sorts the results by the description of the share.
        # *   created_at: sorts the results by the time when the share was created.
        self.order_by = order_by
        # The order in which you want to sort the returned results. By default, order_direction is set to DESC if order_by is set to created_at or updated_at, and is set to ASC if order_by is set to other values. Valid values:
        # 
        # *   ASC: sorts the results in ascending order.
        # *   DESC: sorts the results in descending order.
        self.order_direction = order_direction

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['creator'] = self.creator

        if self.include_cancelled is not None:
            result['include_cancelled'] = self.include_cancelled

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.order_by is not None:
            result['order_by'] = self.order_by

        if self.order_direction is not None:
            result['order_direction'] = self.order_direction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('include_cancelled') is not None:
            self.include_cancelled = m.get('include_cancelled')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')

        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')

        return self

