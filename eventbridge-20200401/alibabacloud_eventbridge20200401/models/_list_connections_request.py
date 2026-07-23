# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListConnectionsRequest(DaraModel):
    def __init__(
        self,
        connection_name_prefix: str = None,
        max_results: int = None,
        next_token: str = None,
        type: str = None,
    ):
        # The name prefix of the connection configurations to query. Supports prefix matching.
        self.connection_name_prefix = connection_name_prefix
        # The maximum number of entries to return on each page. Can be used together with NextToken to implement pagination.
        # 
        # - Default value: 10
        self.max_results = max_results
        # When MaxResults is specified, NextToken is returned if there are more results to fetch.
        # 
        # - NextToken starts from 0 by default. Default value: 0.
        self.next_token = next_token
        # Filters query results by connection type. Valid values: Http, MySQL, PostgreSQL, Elasticsearch. If left empty, connections of all types are returned.
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

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

