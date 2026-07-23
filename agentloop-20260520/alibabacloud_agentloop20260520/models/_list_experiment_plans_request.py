# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListExperimentPlansRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        max_results: int = None,
        next_token: str = None,
        offset: int = None,
        plan_name: str = None,
        status: str = None,
    ):
        # The number of entries to return. Default value: 20.
        self.limit = limit
        # Optional. Use `offset` and `limit` for pagination instead.
        self.max_results = max_results
        # Optional. Use `offset` and `limit` for pagination instead.
        self.next_token = next_token
        # The offset. Default value: 0.
        self.offset = offset
        # Fuzzy match by plan name.
        self.plan_name = plan_name
        # Filters by exact status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.offset is not None:
            result['offset'] = self.offset

        if self.plan_name is not None:
            result['planName'] = self.plan_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('planName') is not None:
            self.plan_name = m.get('planName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

