# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ChatStreamRequest(DaraModel):
    def __init__(
        self,
        document_ids: List[int] = None,
        question: str = None,
        session_id: str = None,
    ):
        self.document_ids = document_ids
        # Q&A content.
        # 
        # This parameter is required.
        self.question = question
        # - Q&A session ID.
        # - Historical sessions can be retrieved through GetSessionList.
        # - A new session can also be created via CreateChatSession.
        # 
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_ids is not None:
            result['documentIds'] = self.document_ids

        if self.question is not None:
            result['question'] = self.question

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentIds') is not None:
            self.document_ids = m.get('documentIds')

        if m.get('question') is not None:
            self.question = m.get('question')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

