# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateAgentConversationResponseBody(DaraModel):
    def __init__(
        self,
        conversation_id: str = None,
        id: str = None,
        share_scope: str = None,
        title: str = None,
        updated_at: str = None,
    ):
        self.conversation_id = conversation_id
        self.id = id
        self.share_scope = share_scope
        self.title = title
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conversation_id is not None:
            result['conversationId'] = self.conversation_id

        if self.id is not None:
            result['id'] = self.id

        if self.share_scope is not None:
            result['shareScope'] = self.share_scope

        if self.title is not None:
            result['title'] = self.title

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conversationId') is not None:
            self.conversation_id = m.get('conversationId')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('shareScope') is not None:
            self.share_scope = m.get('shareScope')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

