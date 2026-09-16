# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConnectionsRequest(DaraModel):
    def __init__(
        self,
        connection_name_prefix: str = None,
        exclude_type: str = None,
        max_results: int = None,
        next_token: str = None,
        type: str = None,
    ):
        # The prefix of the connection configuration name. Supports fuzzy match by prefix.
        self.connection_name_prefix = connection_name_prefix
        # 排除单个连接类型，取值范围与 Type 相同。传入单个类型名称，不支持数组或逗号分隔的多个值。例如传入 Http 可排除 HTTP 类型的连接。未传或传入空字符串时不排除任何类型；与 Type 相同时返回空列表。分页与总数均在过滤后计算。
        self.exclude_type = exclude_type
        # The maximum number of entries to return per request. You can use this parameter together with NextToken to implement paging.
        # 
        # - Default value: 10.
        self.max_results = max_results
        # The pagination token. If the number of results exceeds the value of MaxResults, a NextToken value is returned.
        # 
        # - The NextToken value starts from 0. Default value: 0.
        self.next_token = next_token
        # Filters query results by connection type. Valid values: Http, MySQL, PostgreSQL, Elasticsearch, OSS_TABLES, SLS, OTS, MaxCompute, MongoDB, Redis, SQLServer, ClickHouse, Oracle, Hive, Iceberg, and lakehouse. If this parameter is not specified, all types are returned.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_name_prefix is not None:
            result['ConnectionNamePrefix'] = self.connection_name_prefix

        if self.exclude_type is not None:
            result['ExcludeType'] = self.exclude_type

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionNamePrefix') is not None:
            self.connection_name_prefix = m.get('ConnectionNamePrefix')

        if m.get('ExcludeType') is not None:
            self.exclude_type = m.get('ExcludeType')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

