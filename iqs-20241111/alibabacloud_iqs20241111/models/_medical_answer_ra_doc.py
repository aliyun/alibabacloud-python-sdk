# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MedicalAnswerRaDoc(DaraModel):
    def __init__(
        self,
        content: str = None,
        raw_url: str = None,
        title: str = None,
        type: str = None,
    ):
        self.content = content
        self.raw_url = raw_url
        self.title = title
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.raw_url is not None:
            result['rawUrl'] = self.raw_url

        if self.title is not None:
            result['title'] = self.title

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('rawUrl') is not None:
            self.raw_url = m.get('rawUrl')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

