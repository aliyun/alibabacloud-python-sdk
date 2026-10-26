# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UploadAgentConversationLogResponseBody(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        id: str = None,
        sandbox_path: str = None,
        size: int = None,
    ):
        self.file_name = file_name
        self.id = id
        self.sandbox_path = sandbox_path
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.id is not None:
            result['id'] = self.id

        if self.sandbox_path is not None:
            result['sandboxPath'] = self.sandbox_path

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('sandboxPath') is not None:
            self.sandbox_path = m.get('sandboxPath')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

