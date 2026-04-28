# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SearchShareLinkRequest(DaraModel):
    def __init__(
        self,
        creators: List[str] = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        order_direction: str = None,
        query: str = None,
        return_total_count: bool = None,
    ):
        # The creators of shares. Set this parameter to a user ID. If you do not specify this parameter, Drive and Photo Service automatically queries shares based on your permissions. If you are a drive administrator or the super administrator, the shares created by all members are queried. If you are a team administrator, the shares created by all team members are queried. If you are a common user, only the shares created by yourself are queried.
        # 
        # If you specify this parameter, this parameter must be set to the ID of the super administrator, a drive administrator, or a team administrator.
        self.creators = creators
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
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
        # The query condition that is used to search for share URLs. You can use the following fields to specify query conditions: created_at: queries a share URL based on the time when the share URL was created. updated_at: queries a share URL based on the time when the share URL was modified. share_name_for_fuzzy: queries a share URL based on the name of the share. A fuzzy match is supported. status: queries a share URL based on the status of the share. Valid values: enabled and disabled. A value of enabled indicates that the share is valid. A value of disabled indicates that the share is canceled. expired_time: queries a share URL based on the expiration time of the share. If the share never expires, set this field to 1970-01-01T00:00:00. Otherwise, set this field to 1970-01-02T00:00:00.
        self.query = query
        # Specifies whether to return the total number of returned results.
        self.return_total_count = return_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creators is not None:
            result['creators'] = self.creators

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.order_by is not None:
            result['order_by'] = self.order_by

        if self.order_direction is not None:
            result['order_direction'] = self.order_direction

        if self.query is not None:
            result['query'] = self.query

        if self.return_total_count is not None:
            result['return_total_count'] = self.return_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creators') is not None:
            self.creators = m.get('creators')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')

        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('return_total_count') is not None:
            self.return_total_count = m.get('return_total_count')

        return self

