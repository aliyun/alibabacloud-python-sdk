# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteDBInstanceIPArrayRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        iparray_name: str = None,
    ):
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # This parameter is required.
        self.iparray_name = iparray_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.iparray_name is not None:
            result['IPArrayName'] = self.iparray_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IPArrayName') is not None:
            self.iparray_name = m.get('IPArrayName')

        return self

