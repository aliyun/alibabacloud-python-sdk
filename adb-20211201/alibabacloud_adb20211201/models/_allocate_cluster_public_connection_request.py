# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AllocateClusterPublicConnectionRequest(DaraModel):
    def __init__(
        self,
        connection_string_prefix: str = None,
        dbcluster_id: str = None,
        engine: str = None,
        resource_group_name: str = None,
    ):
        # The prefix of the public connection address.
        # 
        # - It must begin with a lowercase letter and can contain only lowercase letters, digits, and hyphens (-).
        # 
        # - It must be no more than 30 characters long.
        self.connection_string_prefix = connection_string_prefix
        # <props="china">The cluster ID of an Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The cluster ID of a Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The database engine. Valid values:
        # 
        # - **AnalyticDB** (default): the AnalyticDB for MySQL engine.
        # 
        # - **Clickhouse**: the wide table engine.
        self.engine = engine
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_string_prefix is not None:
            result['ConnectionStringPrefix'] = self.connection_string_prefix

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionStringPrefix') is not None:
            self.connection_string_prefix = m.get('ConnectionStringPrefix')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

