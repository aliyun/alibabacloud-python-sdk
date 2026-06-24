# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAppFileRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        conversation_id: str = None,
        file_path: str = None,
    ):
        # The file content.
        self.content = content
        # The session ID.
        self.conversation_id = conversation_id
        # The file path.
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.conversation_id is not None:
            result['ConversationId'] = self.conversation_id

        if self.file_path is not None:
            result['FilePath'] = self.file_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ConversationId') is not None:
            self.conversation_id = m.get('ConversationId')

        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')

        return self

