# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMemoriesRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        app_id: str = None,
        page: int = None,
        page_size: int = None,
        run_id: str = None,
        user_id: str = None,
    ):
        self.agent_id = agent_id
        self.app_id = app_id
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
            result['agentId'] = self.agent_id

        if self.app_id is not None:
            result['appId'] = self.app_id

        if self.page is not None:
            result['page'] = self.page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.run_id is not None:
            result['runId'] = self.run_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('runId') is not None:
            self.run_id = m.get('runId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

