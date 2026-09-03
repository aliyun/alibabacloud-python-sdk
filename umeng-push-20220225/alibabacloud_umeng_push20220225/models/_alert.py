# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Alert(DaraModel):
    def __init__(
        self,
        body: str = None,
        subtitle: str = None,
        title: str = None,
    ):
        self.body = body
        self.subtitle = subtitle
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.subtitle is not None:
            result['subtitle'] = self.subtitle

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('subtitle') is not None:
            self.subtitle = m.get('subtitle')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

