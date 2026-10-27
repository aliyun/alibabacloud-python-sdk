# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListIdentityProviderDepartmentsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        parent_department_id: str = None,
    ):
        # The number of departments to return per page. Valid values: 1 to 50. Default value: 50.
        self.max_results = max_results
        # The nextToken returned from the previous page. Do not specify this parameter for the first query. When continuing pagination, keep the identity provider and parentDepartmentId unchanged, and pass the token as is. An empty or missing return value indicates that there are no subsequent pages at the current hierarchy level.
        self.next_token = next_token
        # Queries the direct child departments of the specified department. If this parameter is not specified or is empty, the root hierarchy is queried, and all descendants are not recursively returned. When expanding a node in the list, pass the ID of the node, not its parentId.
        self.parent_department_id = parent_department_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.parent_department_id is not None:
            result['parentDepartmentId'] = self.parent_department_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('parentDepartmentId') is not None:
            self.parent_department_id = m.get('parentDepartmentId')

        return self

