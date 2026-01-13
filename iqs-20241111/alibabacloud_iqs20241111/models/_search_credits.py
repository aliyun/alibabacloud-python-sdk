# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SearchCredits(DaraModel):
    def __init__(
        self,
        generic_text_search: int = None,
        lite_advanced_text_search: int = None,
    ):
        self.generic_text_search = generic_text_search
        self.lite_advanced_text_search = lite_advanced_text_search

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generic_text_search is not None:
            result['genericTextSearch'] = self.generic_text_search

        if self.lite_advanced_text_search is not None:
            result['liteAdvancedTextSearch'] = self.lite_advanced_text_search

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('genericTextSearch') is not None:
            self.generic_text_search = m.get('genericTextSearch')

        if m.get('liteAdvancedTextSearch') is not None:
            self.lite_advanced_text_search = m.get('liteAdvancedTextSearch')

        return self

