# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class SearchMemoriesRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        filters: Dict[str, Any] = None,
        query: str = None,
        rerank: bool = None,
        retrieve_level: str = None,
        run_id: str = None,
        search_type: str = None,
        threshold: float = None,
        top_k: int = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.app_id = app_id
        self.filters = filters
        self.query = query
        self.rerank = rerank
        self.retrieve_level = retrieve_level
        self.run_id = run_id
        self.search_type = search_type
        self.threshold = threshold
        self.top_k = top_k
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.filters is not None:
            result['filters'] = self.filters

        if self.query is not None:
            result['query'] = self.query

        if self.rerank is not None:
            result['rerank'] = self.rerank

        if self.retrieve_level is not None:
            result['retrieveLevel'] = self.retrieve_level

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.search_type is not None:
            result['searchType'] = self.search_type

        if self.threshold is not None:
            result['threshold'] = self.threshold

        if self.top_k is not None:
            result['topK'] = self.top_k

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('filters') is not None:
            self.filters = m.get('filters')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('rerank') is not None:
            self.rerank = m.get('rerank')

        if m.get('retrieveLevel') is not None:
            self.retrieve_level = m.get('retrieveLevel')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('searchType') is not None:
            self.search_type = m.get('searchType')

        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

