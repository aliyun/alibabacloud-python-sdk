# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceSSLRequest(DaraModel):
    def __init__(
        self,
        connection_string: str = None,
        dbinstance_id: str = None,
        sslenabled: int = None,
    ):
        # The encrypted endpoint. By default, the wildcards are used for instances that are hosted on ECS instances. This way, the endpoints that can be resolved to the same IP address are encrypted.
        self.connection_string = connection_string
        # The ID of the instance.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The status of SSL encryption. Valid values:
        # 
        # *   0: disables SSL encryption.
        # *   1: enables SSL encryption.
        # *   2: updates SSL encryption.
        # 
        # This parameter is required.
        self.sslenabled = sslenabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.sslenabled is not None:
            result['SSLEnabled'] = self.sslenabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('SSLEnabled') is not None:
            self.sslenabled = m.get('SSLEnabled')

        return self

