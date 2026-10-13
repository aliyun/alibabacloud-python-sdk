# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListFaultReportsShrinkRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        nodes_shrink: str = None,
        status: str = None,
    ):
        # The maximum number of results to return.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The list of nodes.
        self.nodes_shrink = nodes_shrink
        # The status of the fault report.
        self.status = status

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

        if self.nodes_shrink is not None:
            result['Nodes'] = self.nodes_shrink

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Nodes') is not None:
            self.nodes_shrink = m.get('Nodes')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

