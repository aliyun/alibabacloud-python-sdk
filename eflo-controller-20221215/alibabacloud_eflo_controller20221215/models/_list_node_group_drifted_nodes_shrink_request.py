# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodeGroupDriftedNodesShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        node_group_id: str = None,
        node_ids_shrink: str = None,
    ):
        # The maximum number of entries per page for a paged query. Valid values: 1 to 500. Default value: 100.
        self.max_results = max_results
        # The pagination token. Set this parameter to the NextToken value returned in the previous call. You do not need to set this parameter for the first request.
        self.next_token = next_token
        # The ID of the node group.
        # 
        # This parameter is required.
        self.node_group_id = node_group_id
        # Limits the check scope. If not specified, all nodes in the node group are checked. <warning>If the model is a super node, pass the TrayNode ID.</warning>
        self.node_ids_shrink = node_ids_shrink

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

        if self.node_group_id is not None:
            result['NodeGroupId'] = self.node_group_id

        if self.node_ids_shrink is not None:
            result['NodeIds'] = self.node_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NodeGroupId') is not None:
            self.node_group_id = m.get('NodeGroupId')

        if m.get('NodeIds') is not None:
            self.node_ids_shrink = m.get('NodeIds')

        return self

