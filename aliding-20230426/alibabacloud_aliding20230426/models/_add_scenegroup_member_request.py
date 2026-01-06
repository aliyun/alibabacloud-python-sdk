# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddScenegroupMemberRequest(DaraModel):
    def __init__(
        self,
        open_conversation_id: str = None,
        user_ids: str = None,
    ):
        # This parameter is required.
        self.open_conversation_id = open_conversation_id
        # This parameter is required.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_conversation_id is not None:
            result['OpenConversationId'] = self.open_conversation_id

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenConversationId') is not None:
            self.open_conversation_id = m.get('OpenConversationId')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

