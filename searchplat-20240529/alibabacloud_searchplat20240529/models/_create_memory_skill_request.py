# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMemorySkillRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        user_id: str = None,
        zip_base_64: str = None,
    ):
        self.agent_id = agent_id
        self.user_id = user_id
        self.zip_base_64 = zip_base_64

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.zip_base_64 is not None:
            result['zip_base64'] = self.zip_base_64

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('zip_base64') is not None:
            self.zip_base_64 = m.get('zip_base64')

        return self

