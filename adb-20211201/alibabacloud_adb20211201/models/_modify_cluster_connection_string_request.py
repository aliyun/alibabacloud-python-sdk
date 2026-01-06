# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyClusterConnectionStringRequest(DaraModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        current_connection_string: str = None,
        dbcluster_id: str = None,
        port: int = None,
    ):
        # The prefix of the public endpoint.
        # 
        # *   The prefix can contain lowercase letters, digits, and hyphens (-). It must start with a lowercase letter.
        # *   The prefix can be up to 30 characters in length.
        # 
        # This parameter is required.
        self.connection_string_prefix = connection_string_prefix
        # The public endpoint of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.current_connection_string = current_connection_string
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The port number. Set the value to **3306**.
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

        if self.current_connection_string is not None:
            result['CurrentConnectionString'] = self.current_connection_string

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('CurrentConnectionString') is not None:
            self.current_connection_string = m.get('CurrentConnectionString')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

