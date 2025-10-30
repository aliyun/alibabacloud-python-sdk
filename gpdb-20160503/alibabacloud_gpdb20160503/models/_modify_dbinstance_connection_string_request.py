# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceConnectionStringRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connection_string_prefix: str = None,
        current_connection_string: str = None,
        dbinstance_id: str = None,
        port: str = None,
    ):
        # Idempotence check. For more information, see [How to Ensure Idempotence](https://help.aliyun.com/document_detail/327176.html).
        self.client_token = client_token
        # The endpoint prefix of the instance.
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The current endpoint of the instance.
        # 
        # This parameter is required.
        self.current_connection_string = current_connection_string
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The port number. Example: 5432.
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

