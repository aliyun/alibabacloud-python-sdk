# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eventbridge20200401 import models as main_models
from darabonba.model import DaraModel

class QueryAskLumaLogResult(DaraModel):
    def __init__(
        self,
        entries: List[main_models.AskLumaLogEntry] = None,
        has_more: bool = None,
        last_key: str = None,
    ):
        self.entries = entries
        self.has_more = has_more
        self.last_key = last_key

    def validate(self):
        if self.entries:
            for v1 in self.entries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Entries'] = []
        if self.entries is not None:
            for k1 in self.entries:
                result['Entries'].append(k1.to_map() if k1 else None)

        if self.has_more is not None:
            result['HasMore'] = self.has_more

        if self.last_key is not None:
            result['LastKey'] = self.last_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.entries = []
        if m.get('Entries') is not None:
            for k1 in m.get('Entries'):
                temp_model = main_models.AskLumaLogEntry()
                self.entries.append(temp_model.from_map(k1))

        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')

        if m.get('LastKey') is not None:
            self.last_key = m.get('LastKey')

        return self

