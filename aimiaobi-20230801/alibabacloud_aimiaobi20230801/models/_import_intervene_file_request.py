# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportInterveneFileRequest(DaraModel):
    def __init__(
        self,
        agent_key: str = None,
        doc_name: str = None,
        file_key: str = None,
        file_url: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.doc_name = doc_name
        self.file_key = file_key
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key

        if self.doc_name is not None:
            result['DocName'] = self.doc_name

        if self.file_key is not None:
            result['FileKey'] = self.file_key

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')

        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')

        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        return self

