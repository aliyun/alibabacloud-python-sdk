# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifySQLCollectorPolicyRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        sqlcollector_status: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Specifies whether to enable or disable SQL collection.
        # 
        # *   Enable: enables SQL collection.
        # *   Disabled: disables SQL collection.
        # 
        # This parameter is required.
        self.sqlcollector_status = sqlcollector_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.sqlcollector_status is not None:
            result['SQLCollectorStatus'] = self.sqlcollector_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('SQLCollectorStatus') is not None:
            self.sqlcollector_status = m.get('SQLCollectorStatus')

        return self

