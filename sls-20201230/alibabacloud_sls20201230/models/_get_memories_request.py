# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class GetMemoriesRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        limit: int = None,
        metadata: Dict[str, Any] = None,
        page: int = None,
        page_size: int = None,
        run_id: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.app_id = app_id
        self.limit = limit
        self.metadata = metadata
        self.page = page
        self.page_size = page_size
        self.run_id = run_id
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

        if self.limit is not None:
            result['limit'] = self.limit

        if self.metadata is not None:
            result['metadata'] = self.metadata

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['page_size'] = self.page_size

        if self.run_id is not None:
            result['run_id'] = self.run_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('metadata') is not None:
            self.metadata = m.get('metadata')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')

        if m.get('run_id') is not None:
            self.run_id = m.get('run_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        return self

