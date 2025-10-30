# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateJDBCDataSourceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        data_source_description: str = None,
        data_source_name: str = None,
        data_source_type: str = None,
        jdbcconnection_string: str = None,
        jdbcpassword: str = None,
        jdbcuser_name: str = None,
        region_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Data source description.
        self.data_source_description = data_source_description
        # The name of data soruce
        self.data_source_name = data_source_name
        # The type of the data source.
        self.data_source_type = data_source_type
        # The JDBC connection string.
        self.jdbcconnection_string = jdbcconnection_string
        # The password of the database account.
        self.jdbcpassword = jdbcpassword
        # The name of the database account.
        self.jdbcuser_name = jdbcuser_name
        # The region ID of the instance.
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

        if self.data_source_description is not None:
            result['DataSourceDescription'] = self.data_source_description

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.data_source_type is not None:
            result['DataSourceType'] = self.data_source_type

        if self.jdbcconnection_string is not None:
            result['JDBCConnectionString'] = self.jdbcconnection_string

        if self.jdbcpassword is not None:
            result['JDBCPassword'] = self.jdbcpassword

        if self.jdbcuser_name is not None:
            result['JDBCUserName'] = self.jdbcuser_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DataSourceDescription') is not None:
            self.data_source_description = m.get('DataSourceDescription')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DataSourceType') is not None:
            self.data_source_type = m.get('DataSourceType')

        if m.get('JDBCConnectionString') is not None:
            self.jdbcconnection_string = m.get('JDBCConnectionString')

        if m.get('JDBCPassword') is not None:
            self.jdbcpassword = m.get('JDBCPassword')

        if m.get('JDBCUserName') is not None:
            self.jdbcuser_name = m.get('JDBCUserName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

