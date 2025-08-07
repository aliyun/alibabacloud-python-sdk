# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 


class Identifier(DaraModel):
    def __init__(
        self,
        database: str = None,
        object: str = None,
    ):
        self.database = database
        self.object = object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database is not None:
            result['database'] = self.database

        if self.object is not None:
            result['object'] = self.object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('database') is not None:
            self.database = m.get('database')

        if m.get('object') is not None:
            self.object = m.get('object')

        return self

