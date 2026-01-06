# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiworkspace20210204 import models as main_models
from darabonba.model import DaraModel

class ListConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        connections: List[main_models.Connection] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The connection list.
        self.connections = connections
        # The maximum number of entries per page.
        self.max_results = max_results
        # The pagination token that indicates the start position from which to retrieve data on the next page.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of connections that meet the filter conditions.
        self.total_count = total_count

    def validate(self):
        if self.connections:
            for v1 in self.connections:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Connections'] = []
        if self.connections is not None:
            for k1 in self.connections:
                result['Connections'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.connections = []
        if m.get('Connections') is not None:
            for k1 in m.get('Connections'):
                temp_model = main_models.Connection()
                self.connections.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

