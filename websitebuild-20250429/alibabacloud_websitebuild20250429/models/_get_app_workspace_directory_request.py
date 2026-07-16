# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAppWorkspaceDirectoryRequest(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        deep: int = None,
        file_path: str = None,
    ):
        # The session ID.
        self.conversation_id = conversation_id
        # The directory depth. This parameter is optional. If set to null or 0, all levels are returned.
        self.deep = deep
        # The directory path. This parameter is optional.
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.deep is not None:
            result['Deep'] = self.deep

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('Deep') is not None:
            self.deep = m.get('Deep')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        return self

