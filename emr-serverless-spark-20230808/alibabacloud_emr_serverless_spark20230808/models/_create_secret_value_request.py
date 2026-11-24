# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSecretValueRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        content: str = None,
        name: str = None,
    ):
        # The comment.
        self.comment = comment
        # The content of the ciphertext.
        self.content = content
        # The name of the ciphertext.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.content is not None:
            result['content'] = self.content

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

