# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class IndexJsonKey(DaraModel):
    def __init__(
        self,
        alias: str = None,
        case_sensitive: bool = None,
        chn: bool = None,
        doc_value: bool = None,
        token: List[str] = None,
        type: str = None,
    ):
        self.alias = alias
        self.case_sensitive = case_sensitive
        self.chn = chn
        self.doc_value = doc_value
        self.token = token
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['alias'] = self.alias

        if self.case_sensitive is not None:
            result['caseSensitive'] = self.case_sensitive

        if self.chn is not None:
            result['chn'] = self.chn

        if self.doc_value is not None:
            result['doc_value'] = self.doc_value

        if self.token is not None:
            result['token'] = self.token

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias') is not None:
            self.alias = m.get('alias')

        if m.get('caseSensitive') is not None:
            self.case_sensitive = m.get('caseSensitive')

        if m.get('chn') is not None:
            self.chn = m.get('chn')

        if m.get('doc_value') is not None:
            self.doc_value = m.get('doc_value')

        if m.get('token') is not None:
            self.token = m.get('token')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

