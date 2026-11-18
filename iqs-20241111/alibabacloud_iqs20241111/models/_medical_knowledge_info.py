# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MedicalKnowledgeInfo(DaraModel):
    def __init__(
        self,
        content: str = None,
        url: str = None,
    ):
        # The structured text composed of the entity name and its properties.
        self.content = content
        # The source link of the entity property content.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

