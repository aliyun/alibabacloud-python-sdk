# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteAITeacherGrammarCheckRequest(DaraModel):
    def __init__(
        self,
        content: str = None,
        user_id: str = None,
    ):
        # The sentence to check.
        # 
        # This parameter is required.
        self.content = content
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

