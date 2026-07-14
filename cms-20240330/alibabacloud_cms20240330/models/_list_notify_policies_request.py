# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNotifyPoliciesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        order_by: str = None,
        order_desc: str = None,
        workspace: str = None,
    ):
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The policy name used for fuzzy filtering.
        self.name = name
        # The pagination token. Leave this parameter empty for the first page. For subsequent pages, set this parameter to the nextToken value returned in the previous response.
        self.next_token = next_token
        # The field used for sorting. Valid values: createTime, updateTime, and name.
        self.order_by = order_by
        # Specifies whether to sort results in descending order. Valid values:
        # - true: descending order.
        # - false: ascending order.
        self.order_desc = order_desc
        # The workspace ID. This parameter is used to isolate notify policy resources across different business spaces.
        # 
        # This parameter is required.
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.order_by is not None:
            result['orderBy'] = self.order_by

        if self.order_desc is not None:
            result['orderDesc'] = self.order_desc

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('orderBy') is not None:
            self.order_by = m.get('orderBy')

        if m.get('orderDesc') is not None:
            self.order_desc = m.get('orderDesc')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

