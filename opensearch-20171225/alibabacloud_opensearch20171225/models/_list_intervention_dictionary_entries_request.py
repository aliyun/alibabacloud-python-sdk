# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInterventionDictionaryEntriesRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        word: str = None,
    ):
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page. Default value: 10.
        self.page_size = page_size
        # The intervention entry.
        self.word = word

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.word is not None:
            result['word'] = self.word

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('word') is not None:
            self.word = m.get('word')

        return self

