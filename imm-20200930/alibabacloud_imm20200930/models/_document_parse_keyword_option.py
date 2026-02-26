# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DocumentParseKeywordOption(DaraModel):
    def __init__(
        self,
        count: int = None,
        extract: bool = None,
    ):
        self.count = count
        self.extract = extract

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.extract is not None:
            result['Extract'] = self.extract

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Extract') is not None:
            self.extract = m.get('Extract')

        return self

