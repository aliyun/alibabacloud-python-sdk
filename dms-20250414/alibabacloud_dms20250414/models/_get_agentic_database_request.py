# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAgenticDatabaseRequest(DaraModel):
    def __init__(
        self,
        database_uuid: str = None,
    ):
        # The UUID of the database. You can obtain this value by calling ListAgenticDatabase or SearchAgenticDatabase.
        # 
        # This parameter is required.
        self.database_uuid = database_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_uuid is not None:
            result['DatabaseUuid'] = self.database_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseUuid') is not None:
            self.database_uuid = m.get('DatabaseUuid')

        return self

