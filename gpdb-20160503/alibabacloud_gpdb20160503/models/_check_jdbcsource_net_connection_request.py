# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckJDBCSourceNetConnectionRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        data_source_id: str = None,
        jdbc_connection_string: str = None,
        region_id: str = None,
    ):
        # Instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Either DataSourceId or JdbcConnectionString must be specified as input, otherwise an error will occur. If both parameters are specified, JdbcConnectionString will be used preferentially.
        self.data_source_id = data_source_id
        # JDBC connection string.
        self.jdbc_connection_string = jdbc_connection_string
        # The ID of the region where the instance is located.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.jdbc_connection_string is not None:
            result['JdbcConnectionString'] = self.jdbc_connection_string

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('JdbcConnectionString') is not None:
            self.jdbc_connection_string = m.get('JdbcConnectionString')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

