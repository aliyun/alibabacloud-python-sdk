# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeDesktopOversoldGroupRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        oversold_group_ids: List[str] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.oversold_group_ids = oversold_group_ids

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

        if self.oversold_group_ids is not None:
            result['OversoldGroupIds'] = self.oversold_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('OversoldGroupIds') is not None:
            self.oversold_group_ids = m.get('OversoldGroupIds')

        return self

