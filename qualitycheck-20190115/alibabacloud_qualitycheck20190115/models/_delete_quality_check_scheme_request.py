# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteQualityCheckSchemeRequest(DaraModel):
    def __init__(
        self,
        base_me_agent_id: int = None,
        json_str: str = None,
    ):
        # baseMeAgentId
        self.base_me_agent_id = base_me_agent_id
        self.json_str = json_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_me_agent_id is not None:
            result['BaseMeAgentId'] = self.base_me_agent_id

        if self.json_str is not None:
            result['jsonStr'] = self.json_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseMeAgentId') is not None:
            self.base_me_agent_id = m.get('BaseMeAgentId')

        if m.get('jsonStr') is not None:
            self.json_str = m.get('jsonStr')

        return self

