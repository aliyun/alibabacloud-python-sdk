# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBatchesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        project_name: str = None,
        sort: str = None,
        state: str = None,
        tag_selector: str = None,
    ):
        # The maximum number of results to return. Valid values: 0 to 100.
        # 
        # If you do not specify this parameter or set the parameter to 0, the default value of 100 is used.
        self.max_results = max_results
        # The pagination token.
        # 
        # The pagination token is used in the next request to retrieve a new page of results if the total number of results exceeds the value of the MaxResults parameter. The next call to the operation returns results lexicographically after the NextToken parameter value.
        # 
        # You do not need to specify this parameter in your initial request.
        self.next_token = next_token
        # The sort order. Valid values:
        # 
        # *   ASC: sorts the results in ascending order. This is the default sort order.
        # *   DES: sorts the results in descending order.
        self.order = order
        # The name of the project.[](~~478153~~)
        # 
        # This parameter is required.
        self.project_name = project_name
        # The sort field. Valid values:
        # 
        # *   CreateTime
        # *   UpdateTime
        self.sort = sort
        # The task status.
        # 
        # *   Ready: The task is newly created and ready.
        # *   Running: The task is running.
        # *   Failed: The task failed and cannot be automatically recovered.
        # *   Suspended: The task is suspended.
        # *   Succeeded: The task is successful.
        self.state = state
        # The custom tag. You can use this parameter to query tasks that have the specified tag.
        self.tag_selector = tag_selector

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.sort is not None:
            result['Sort'] = self.sort

        if self.state is not None:
            result['State'] = self.state

        if self.tag_selector is not None:
            result['TagSelector'] = self.tag_selector

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Sort') is not None:
            self.sort = m.get('Sort')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TagSelector') is not None:
            self.tag_selector = m.get('TagSelector')

        return self

