# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDBInstanceConnectionStringRequest(DaraModel):
    def __init__(
        self,
        computing_group_id: str = None,
        connection_string: str = None,
        connection_string_prefix: str = None,
        dbinstance_id: str = None,
        dbinstance_net_type: str = None,
        disable_ports: str = None,
        region_id: str = None,
    ):
        self.computing_group_id = computing_group_id
        # The endpoint of the cluster.
        self.connection_string = connection_string
        # The prefix of the endpoint that is used to connect to the database.
        self.connection_string_prefix = connection_string_prefix
        # The cluster ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.dbinstance_net_type = dbinstance_net_type
        # *   The database ports that you want to disable. Separate multiple ports with commas (,).
        # 
        # *   This parameter is supported only for clusters whose minor engine version is 24.10.1.11098_1 or later.
        # 
        #     **
        # 
        #     **Note** If you create a cluster whose minor engine version is earlier than 24.10.1.11098_1 and you update the minor engine version to 24.10.1.11098_1 or later, the cluster still does not support this parameter.
        self.disable_ports = disable_ports
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.computing_group_id is not None:
            result['ComputingGroupId'] = self.computing_group_id

        if self.connection_string is not None:
            result['ConnectionString'] = self.connection_string

        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbinstance_net_type is not None:
            result['DBInstanceNetType'] = self.dbinstance_net_type

        if self.disable_ports is not None:
            result['DisablePorts'] = self.disable_ports

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComputingGroupId') is not None:
            self.computing_group_id = m.get('ComputingGroupId')

        if m.get('ConnectionString') is not None:
            self.connection_string = m.get('ConnectionString')

        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBInstanceNetType') is not None:
            self.dbinstance_net_type = m.get('DBInstanceNetType')

        if m.get('DisablePorts') is not None:
            self.disable_ports = m.get('DisablePorts')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

