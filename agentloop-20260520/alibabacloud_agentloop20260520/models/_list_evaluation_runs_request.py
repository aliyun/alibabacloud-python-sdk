# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEvaluationRunsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        run_type: str = None,
        status: str = None,
    ):
        # The number of entries per page. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The pagination token for the next page.
        self.next_token = next_token
        # The run type filter condition.
        self.run_type = run_type
        # The run status filter condition.
        self.status = status

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

        if self.run_type is not None:
            result['runType'] = self.run_type

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('runType') is not None:
            self.run_type = m.get('runType')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

