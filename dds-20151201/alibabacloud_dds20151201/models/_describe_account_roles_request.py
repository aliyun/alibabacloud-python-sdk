# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccountRolesRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
    ):
        # The ID of the ApsaraDB for MongoDB instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database to which the custom role belongs.
        self.dbname = dbname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        return self

