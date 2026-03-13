# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModuleAgentInfosAttributeShowInfoMapValue(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        text: str = None,
    ):
        self.code = code
        self.name = name
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.name is not None:
            result['name'] = self.name

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

