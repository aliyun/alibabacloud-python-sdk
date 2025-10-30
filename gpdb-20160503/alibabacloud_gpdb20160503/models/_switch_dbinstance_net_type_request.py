# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SwitchDBInstanceNetTypeRequest(DaraModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        port: str = None,
    ):
        # The prefix of the custom endpoint.
        # 
        # *   The prefix can contain lowercase letters, digits, and hyphens (-) and must start with a lowercase letter.
        # *   The prefix can be up to 30 characters in length.
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/2361776.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The port number.
        # 
        # This parameter is required.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

