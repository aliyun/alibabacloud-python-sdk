# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AiSearchRequest(DaraModel):
    def __init__(
        self,
        industry: str = None,
        page: int = None,
        query: str = None,
        session_id: str = None,
        time_range: str = None,
    ):
        self.industry = industry
        self.page = page
        # This parameter is required.
        self.query = query
        self.session_id = session_id
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.industry is not None:
            result['industry'] = self.industry

        if self.page is not None:
            result['page'] = self.page

        if self.query is not None:
            result['query'] = self.query

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('industry') is not None:
            self.industry = m.get('industry')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

