# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AISearchQuery(DaraModel):
    def __init__(
        self,
        card: str = None,
        card_query: str = None,
        page: int = None,
        query: str = None,
        search_engine: str = None,
        search_plan: str = None,
        session_id: str = None,
        time_range: str = None,
    ):
        self.card = card
        self.card_query = card_query
        self.page = page
        self.query = query
        self.search_engine = search_engine
        self.search_plan = search_plan
        self.session_id = session_id
        self.time_range = time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.card is not None:
            result['card'] = self.card

        if self.card_query is not None:
            result['cardQuery'] = self.card_query

        if self.page is not None:
            result['page'] = self.page

        if self.query is not None:
            result['query'] = self.query

        if self.search_engine is not None:
            result['searchEngine'] = self.search_engine

        if self.search_plan is not None:
            result['searchPlan'] = self.search_plan

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.time_range is not None:
            result['timeRange'] = self.time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('card') is not None:
            self.card = m.get('card')

        if m.get('cardQuery') is not None:
            self.card_query = m.get('cardQuery')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('searchEngine') is not None:
            self.search_engine = m.get('searchEngine')

        if m.get('searchPlan') is not None:
            self.search_plan = m.get('searchPlan')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('timeRange') is not None:
            self.time_range = m.get('timeRange')

        return self

