# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddScriptHotWordRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        hot_word: str = None,
        script_record_id: str = None,
    ):
        self.description = description
        self.hot_word = hot_word
        self.script_record_id = script_record_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.hot_word is not None:
            result['hotWord'] = self.hot_word

        if self.script_record_id is not None:
            result['scriptRecordId'] = self.script_record_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('hotWord') is not None:
            self.hot_word = m.get('hotWord')

        if m.get('scriptRecordId') is not None:
            self.script_record_id = m.get('scriptRecordId')

        return self

