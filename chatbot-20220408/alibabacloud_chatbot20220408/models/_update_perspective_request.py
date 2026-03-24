# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdatePerspectiveRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        name: str = None,
        perspective_id: str = None,
    ):
        self.agent_key = agent_key
        self.name = name
        self.perspective_id = perspective_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.name is not None:
            result['Name'] = self.name

        if self.perspective_id is not None:
            result['PerspectiveId'] = self.perspective_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PerspectiveId') is not None:
            self.perspective_id = m.get('PerspectiveId')

        return self

