# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ViewSchemaChange(DaraModel):
    def __init__(
        self,
        action: str = None,
        comment: str = None,
        dialect: str = None,
        key: str = None,
        query: str = None,
        value: str = None,
    ):
        self.action = action
        # required in UpdateComment
        self.comment = comment
        # required in AddDialect/UpdateDialect/DropDialect
        self.dialect = dialect
        # required in SetOption/RemoveOption
        self.key = key
        # required in AddDialect/UpdateDialect
        self.query = query
        # required in SetOption
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['action'] = self.action

        if self.comment is not None:
            result['comment'] = self.comment

        if self.dialect is not None:
            result['dialect'] = self.dialect

        if self.key is not None:
            result['key'] = self.key

        if self.query is not None:
            result['query'] = self.query

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')

        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('dialect') is not None:
            self.dialect = m.get('dialect')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

