# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTriggersRequest(DaraModel):
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
        # The maximum number of entries to return. Valid values: 0 to 100.
        # 
        # Default value: 100.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of triggers is greater than the value of MaxResults, you must specify NextToken.
        # 
        # You do not need to specify this parameter for the first request.
        self.next_token = next_token
        # The sort order. Default value: DESC.
        # 
        # *   ASC (default): ascending order.
        # *   DESC: descending order.
        self.order = order
        # The name of the project. You can obtain the name of the project from the response of the [CreateProject](https://help.aliyun.com/document_detail/478153.html) operation.
        # 
        # This parameter is required.
        self.project_name = project_name
        # The sort field. Valid values:
        # 
        # *   CreateTime: the point in time when the trigger is created.
        # *   UpdateTime: the most recent point in time when the trigger is updated.
        self.sort = sort
        # The status of the trigger. Valid values:
        # 
        # *   Ready: The trigger is ready.
        # *   Running: The trigger is running.
        # *   Failed: The trigger failed and cannot be automatically recovered.
        # *   Suspended: The trigger is suspended.
        # *   Succeeded: The trigger is complete.
        self.state = state
        # The custom tag. You can specify this parameter only if you specified Tags when you called the CreateTrigger operation.
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

