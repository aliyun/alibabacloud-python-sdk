# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendDocumentAskQuestionRequest(DaraModel):
    def __init__(
        self,
        folder_id: str = None,
        prompt: str = None,
        session_id: str = None,
    ):
        # Folder ID, used to specify the range of documents for the query. If it is empty, it indicates that all documents under the default folder will be queried.
        self.folder_id = folder_id
        # The question queried by the user
        # 
        # This parameter is required.
        self.prompt = prompt
        # Q&A session ID, used to record multiple Q&A interactions of the same user. If it is empty, it indicates that sessions are not distinguished.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.folder_id is not None:
            result['folderId'] = self.folder_id

        if self.prompt is not None:
            result['prompt'] = self.prompt

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('folderId') is not None:
            self.folder_id = m.get('folderId')

        if m.get('prompt') is not None:
            self.prompt = m.get('prompt')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

