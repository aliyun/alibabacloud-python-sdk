# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SqlStatement(DaraModel):
    def __init__(
        self,
        index: int = None,
        message: str = None,
        sql_script: str = None,
        status_state: str = None,
        type: str = None,
    ):
        self.index = index
        self.message = message
        self.sql_script = sql_script
        self.status_state = status_state
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['index'] = self.index

        if self.message is not None:
            result['message'] = self.message

        if self.sql_script is not None:
            result['sqlScript'] = self.sql_script

        if self.status_state is not None:
            result['statusState'] = self.status_state

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('index') is not None:
            self.index = m.get('index')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('sqlScript') is not None:
            self.sql_script = m.get('sqlScript')

        if m.get('statusState') is not None:
            self.status_state = m.get('statusState')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

