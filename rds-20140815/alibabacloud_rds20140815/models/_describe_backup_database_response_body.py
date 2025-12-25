# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeBackupDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        database_names: str = None,
        request_id: str = None,
    ):
        # The name of the database. Format: "db1,db2".
        self.database_names = database_names
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_names is not None:
            result['DatabaseNames'] = self.database_names

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseNames') is not None:
            self.database_names = m.get('DatabaseNames')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

