# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryScriptHotWordListRequest(DaraModel):
    def __init__(
        self,
        hot_word: str = None,
        page_number: int = None,
        page_size: int = None,
        script_record_id: str = None,
    ):
        self.hot_word = hot_word
        self.page_number = page_number
        self.page_size = page_size
        self.script_record_id = script_record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hot_word is not None:
            result['hotWord'] = self.hot_word

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hotWord') is not None:
            self.hot_word = m.get('hotWord')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        return self

