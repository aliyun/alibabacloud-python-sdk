# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatSessionInfo(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        main_account_id: int = None,
        session_id: str = None,
    ):
        self.created_at = created_at
        self.main_account_id = main_account_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.main_account_id is not None:
            result['mainAccountId'] = self.main_account_id

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('mainAccountId') is not None:
            self.main_account_id = m.get('mainAccountId')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

