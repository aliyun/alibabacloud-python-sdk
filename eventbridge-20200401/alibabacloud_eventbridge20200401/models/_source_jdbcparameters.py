# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SourceJDBCParameters(DaraModel):
    def __init__(
        self,
        batch_size: int = None,
        custom_query: str = None,
        incrementing_column: str = None,
        jdbc_url: str = None,
        network: str = None,
        password: str = None,
        polling_interval: int = None,
        query_mode: str = None,
        query_timeout: int = None,
        security_group_id: str = None,
        table_name: str = None,
        timestamp_column: str = None,
        username: str = None,
        v_switch_ids: str = None,
        vpc_id: str = None,
    ):
        # The maximum number of rows returned per query. Default value: 1000. Maximum value: 10000.
        self.batch_size = batch_size
        # The custom SQL query statement (advanced mode). This parameter is mutually exclusive with TableName.
        self.custom_query = custom_query
        # The incrementing column name. Required when QueryMode is set to `incrementing` or `timestamp_incrementing`.
        self.incrementing_column = incrementing_column
        # The JDBC connection URL. ClickHouse example: `jdbc:clickhouse://host:8123/database`; MySQL example: `jdbc:mysql://host:3306/database`. The system automatically identifies the database type.
        self.jdbc_url = jdbc_url
        # The network type. Valid values: `PublicNetwork` (public network); `PrivateNetwork` (VPC private network, requires VpcId, VSwitchIds, and SecurityGroupId to be configured).
        self.network = network
        # The database password.
        self.password = password
        # The polling interval, in seconds. Minimum value: 10. Default value: 60.
        self.polling_interval = polling_interval
        # The query mode. Valid values: `bulk` (full query); `incrementing` (incrementing column tracking); `timestamp` (timestamp tracking); `timestamp_incrementing` (timestamp and incrementing column dual tracking).
        self.query_mode = query_mode
        # The SQL query timeout period, in seconds. Default value: 30. Maximum value: 300.
        self.query_timeout = query_timeout
        # The security group ID. Required when Network is set to PrivateNetwork.
        self.security_group_id = security_group_id
        # The target table name. This parameter is mutually exclusive with CustomQuery. Required when custom SQL is not used.
        self.table_name = table_name
        # The timestamp column name. Required when QueryMode is set to `timestamp` or `timestamp_incrementing`.
        self.timestamp_column = timestamp_column
        # The database username.
        self.username = username
        # The vSwitch ID. Required when Network is set to PrivateNetwork.
        self.v_switch_ids = v_switch_ids
        # The VPC ID. Required when Network is set to PrivateNetwork.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size

        if self.custom_query is not None:
            result['CustomQuery'] = self.custom_query

        if self.incrementing_column is not None:
            result['IncrementingColumn'] = self.incrementing_column

        if self.jdbc_url is not None:
            result['JdbcUrl'] = self.jdbc_url

        if self.network is not None:
            result['Network'] = self.network

        if self.password is not None:
            result['Password'] = self.password

        if self.polling_interval is not None:
            result['PollingInterval'] = self.polling_interval

        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode

        if self.query_timeout is not None:
            result['QueryTimeout'] = self.query_timeout

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.timestamp_column is not None:
            result['TimestampColumn'] = self.timestamp_column

        if self.username is not None:
            result['Username'] = self.username

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')

        if m.get('CustomQuery') is not None:
            self.custom_query = m.get('CustomQuery')

        if m.get('IncrementingColumn') is not None:
            self.incrementing_column = m.get('IncrementingColumn')

        if m.get('JdbcUrl') is not None:
            self.jdbc_url = m.get('JdbcUrl')

        if m.get('Network') is not None:
            self.network = m.get('Network')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PollingInterval') is not None:
            self.polling_interval = m.get('PollingInterval')

        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')

        if m.get('QueryTimeout') is not None:
            self.query_timeout = m.get('QueryTimeout')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TimestampColumn') is not None:
            self.timestamp_column = m.get('TimestampColumn')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

