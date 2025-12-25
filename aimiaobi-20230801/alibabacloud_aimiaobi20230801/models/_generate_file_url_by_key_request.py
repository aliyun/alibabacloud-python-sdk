# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GenerateFileUrlByKeyRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        file_key: str = None,
        file_name: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.file_key = file_key
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.file_name is not None:
            result['FileName'] = self.file_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        return self

