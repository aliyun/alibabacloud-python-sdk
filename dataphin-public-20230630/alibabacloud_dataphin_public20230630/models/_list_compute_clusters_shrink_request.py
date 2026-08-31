# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListComputeClustersShrinkRequest(DaraModel):
    def __init__(
        self,
        list_query_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        op_tenant_id: int = None,
        op_user_id: str = None,
    ):
        # The query conditions.
        # 
        # This parameter is required.
        self.list_query_shrink = list_query_shrink
        # The maximum number of records to return in this response.
        self.max_results = max_results
        # The pagination token for the next page. An empty value indicates that no more results are available.
        self.next_token = next_token
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The ID of the operator user.
        self.op_user_id = op_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_query_shrink is not None:
            result['ListQuery'] = self.list_query_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListQuery') is not None:
            self.list_query_shrink = m.get('ListQuery')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        return self

