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
        metadata: Dict[str, Any] = None,
        query: str = None,
        rerank: bool = None,
        run_id: str = None,
        top_k: int = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.app_id = app_id
        self.metadata = metadata
        self.query = query
        self.rerank = rerank
        self.run_id = run_id
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
            result['agent_id'] = self.agent_id

        if self.app_id is not None:
            result['app_id'] = self.app_id

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.query is not None:
            result['query'] = self.query

        if self.rerank is not None:
            result['rerank'] = self.rerank

        if self.run_id is not None:
            result['run_id'] = self.run_id

        if self.top_k is not None:
            result['top_k'] = self.top_k

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('rerank') is not None:
            self.rerank = m.get('rerank')

        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')

        if m.get('top_k') is not None:
            self.top_k = m.get('top_k')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

