# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCategoryDetailRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        source: str = None,
        target: str = None,
    ):
        # The list of category paths.
        self.category = category
        # The source dialect.
        self.source = source
        # The target dialect.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.source is not None:
            result['source'] = self.source

        if self.target is not None:
            result['target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('target') is not None:
            self.target = m.get('target')

        return self

