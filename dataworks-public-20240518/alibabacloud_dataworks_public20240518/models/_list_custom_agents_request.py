# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCustomAgentsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        q: str = None,
        visibility: List[str] = None,
    ):
        # The maximum number of entries to return for this request.
        self.max_results = max_results
        # The pagination token. Do not specify this parameter for the first query. For subsequent queries, specify the `NextToken` value returned from the previous query to retrieve the next page.
        self.next_token = next_token
        # The search keyword used to perform a fuzzy match on agent names.
        self.q = q
        # The visibility levels used to filter results. You can specify multiple values.
        self.visibility = visibility

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

        if self.q is not None:
            result['Q'] = self.q

        if self.visibility is not None:
            result['Visibility'] = self.visibility

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Q') is not None:
            self.q = m.get('Q')

        if m.get('Visibility') is not None:
            self.visibility = m.get('Visibility')

        return self

