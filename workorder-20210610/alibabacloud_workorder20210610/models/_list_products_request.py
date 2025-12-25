# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProductsRequest(DaraModel):
    def __init__(
        self,
        language: str = None,
        name: str = None,
    ):
        # The language that you use, supporting English, Chinese, and Japanese. Valid values: en, zh, and jp, which indicate English, Chinese, and Japanese, respectively.
        self.language = language
        # The name of the product. Fuzzy search is supported. This parameter is optional.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.language is not None:
            result['Language'] = self.language

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Language') is not None:
            self.language = m.get('Language')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

