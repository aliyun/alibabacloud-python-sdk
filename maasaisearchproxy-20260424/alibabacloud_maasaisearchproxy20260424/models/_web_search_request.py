# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class WebSearchRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        exclude_domain: List[str] = None,
        include_domain: List[str] = None,
        limit: int = None,
        query: str = None,
        region: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.exclude_domain = exclude_domain
        self.include_domain = include_domain
        self.limit = limit
        self.query = query
        self.region = region
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.exclude_domain is not None:
            result['excludeDomain'] = self.exclude_domain

        if self.include_domain is not None:
            result['includeDomain'] = self.include_domain

        if self.limit is not None:
            result['limit'] = self.limit

        if self.query is not None:
            result['query'] = self.query

        if self.region is not None:
            result['region'] = self.region

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('excludeDomain') is not None:
            self.exclude_domain = m.get('excludeDomain')

        if m.get('includeDomain') is not None:
            self.include_domain = m.get('includeDomain')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

