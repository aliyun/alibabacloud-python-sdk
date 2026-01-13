# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListActionPlansShrinkRequest(DaraModel):
    def __init__(
        self,
        action_plan_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # The IDs of the execution plans to be queried.
        self.action_plan_ids_shrink = action_plan_ids_shrink
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action_plan_ids_shrink is not None:
            result['ActionPlanIds'] = self.action_plan_ids_shrink

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActionPlanIds') is not None:
            self.action_plan_ids_shrink = m.get('ActionPlanIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

