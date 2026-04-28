# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class SearchMemoryRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        enhancements: Dict[str, Any] = None,
        query: str = None,
        run_id: str = None,
        size: int = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.enhancements = enhancements
        # This parameter is required.
        self.query = query
        self.run_id = run_id
        self.size = size
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

        if self.enhancements is not None:
            result['enhancements'] = self.enhancements

        if self.query is not None:
            result['query'] = self.query

        if self.run_id is not None:
            result['run_id'] = self.run_id

        if self.size is not None:
            result['size'] = self.size

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('enhancements') is not None:
            self.enhancements = m.get('enhancements')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

