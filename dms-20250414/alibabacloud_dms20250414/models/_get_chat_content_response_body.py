# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetChatContentResponseBody(DaraModel):
    def __init__(
        self,
        category: str = None,
        checkpoint: int = None,
        content: str = None,
        content_type: str = None,
        event_type: str = None,
        level: int = None,
    ):
        self.category = category
        self.checkpoint = checkpoint
        self.content = content
        self.content_type = content_type
        self.event_type = event_type
        self.level = level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.checkpoint is not None:
            result['checkpoint'] = self.checkpoint

        if self.content is not None:
            result['content'] = self.content

        if self.content_type is not None:
            result['content_type'] = self.content_type

        if self.event_type is not None:
            result['event_type'] = self.event_type

        if self.level is not None:
            result['level'] = self.level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('checkpoint') is not None:
            self.checkpoint = m.get('checkpoint')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')

        if m.get('event_type') is not None:
            self.event_type = m.get('event_type')

        if m.get('level') is not None:
            self.level = m.get('level')

        return self

