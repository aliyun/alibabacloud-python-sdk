# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAgenticDataSourcesRequest(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        host: str = None,
        instance_source: str = None,
        max_results: int = None,
        next_token: str = None,
        port: int = None,
        schema: str = None,
        search_key: str = None,
        state: int = None,
    ):
        # Filters data sources by type. If you leave this parameter empty, no restriction is applied. Valid values: MYSQL, POSTGRESQL, ORACLE, SQLSERVER, MARIADB, POLARDB, POLARDB_POSTGRESQL, POLARDB_ORACLE, OCEANBASEX, DRDS, ADB_MYSQL, ADB_POSTGRESQL, CLICKHOUSE, SELECTDB, STARROCKS, HOLOGRES, MAXCOMPUTE, ES_REST, and TRINO.
        self.db_type = db_type
        # Filters data sources by endpoint. If you leave this parameter empty, no restriction is applied.
        self.host = host
        # Filters data sources by source. If you leave this parameter empty, no restriction is applied. Valid values:
        # - RDS: ApsaraDB instance
        # - PUBLIC_OWN: self-managed database on the public network
        # - ECS_OWN: self-managed database on an ECS instance
        # - GATEWAY: connected through Database Gateway
        # - VPC_IDC: connected over a VPC or IDC
        self.instance_source = instance_source
        # The number of entries to return per page. Default value: 20. Maximum value: 200.
        self.max_results = max_results
        # The pagination cursor. Leave this parameter empty when you query the first page. When you query subsequent pages, pass the NextToken value returned from the previous request.
        self.next_token = next_token
        # Filters data sources by connection port. If you leave this parameter empty, no restriction is applied.
        self.port = port
        # Filters data sources by connection target name. The meaning of this parameter varies based on the data source type. If you leave this parameter empty, no restriction is applied.
        self.schema = schema
        # Performs a fuzzy search by data source name or endpoint. If you leave this parameter empty, no fuzzy search is performed.
        self.search_key = search_key
        # Filters data sources by status. If you leave this parameter empty, no restriction is applied. Valid values:
        # - 0: normal
        # - -1: deleted
        # - -2: disabled
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.port is not None:
            result['Port'] = self.port

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

