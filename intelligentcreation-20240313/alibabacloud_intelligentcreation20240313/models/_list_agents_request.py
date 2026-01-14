# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgentsRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_scene: str = None,
        owner: str = None,
        page_number: int = None,
        page_size: int = None,
        status: int = None,
    ):
        self.agent_id = agent_id
        self.agent_scene = agent_scene
        self.owner = owner
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_scene is not None:
            result['agentScene'] = self.agent_scene

        if self.owner is not None:
            result['owner'] = self.owner

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentScene') is not None:
            self.agent_scene = m.get('agentScene')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self

