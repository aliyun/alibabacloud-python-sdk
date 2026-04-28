# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class UpdateMemorySkillRequest(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        files: Dict[str, str] = None,
        name: str = None,
        user_id: str = None,
        version: str = None,
    ):
        self.agent_id = agent_id
        self.files = files
        self.name = name
        self.user_id = user_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id

        if self.files is not None:
            result['files'] = self.files

        if self.name is not None:
            result['name'] = self.name

        if self.user_id is not None:
            result['user_id'] = self.user_id

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')

        if m.get('files') is not None:
            self.files = m.get('files')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

