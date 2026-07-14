# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ExecuteQueryRequest(DaraModel):
    def __init__(
        self,
        from_: int = None,
        length: int = None,
        max_output_length: int = None,
        offset: int = None,
        query: str = None,
        to: int = None,
        type: str = None,
        version: str = None,
    ):
        self.from_ = from_
        self.length = length
        self.max_output_length = max_output_length
        self.offset = offset
        # The query entered by the user.
        # 
        # This parameter is required.
        self.query = query
        self.to = to
        # The statement type. Currently, only SQL is supported.
        # 
        # This parameter is required.
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['from'] = self.from_

        if self.length is not None:
            result['length'] = self.length

        if self.max_output_length is not None:
            result['maxOutputLength'] = self.max_output_length

        if self.offset is not None:
            result['offset'] = self.offset

        if self.query is not None:
            result['query'] = self.query

        if self.to is not None:
            result['to'] = self.to

        if self.type is not None:
            result['type'] = self.type

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('length') is not None:
            self.length = m.get('length')

        if m.get('maxOutputLength') is not None:
            self.max_output_length = m.get('maxOutputLength')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('to') is not None:
            self.to = m.get('to')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

