# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SaveSortScriptFileRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        version: int = None,
    ):
        # The script content that is encoded in the Base64 format.
        self.content = content
        # The version number of the script content.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

