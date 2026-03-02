# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDatabasesRequest(DaraModel):
    def __init__(
        self,
        database_name: str = None,
    ):
        self.database_name = database_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['databaseName'] = self.database_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('databaseName') is not None:
            self.database_name = m.get('databaseName')

        return self

