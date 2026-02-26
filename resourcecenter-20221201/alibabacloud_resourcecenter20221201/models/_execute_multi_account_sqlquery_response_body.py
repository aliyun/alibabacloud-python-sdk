# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class ExecuteMultiAccountSQLQueryResponseBody(DaraModel):
    def __init__(
        self,
        columns: List[main_models.ExecuteMultiAccountSQLQueryResponseBodyColumns] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        rows: List[Any] = None,
    ):
        # The columns.
        self.columns = columns
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # An array of search results.
        self.rows = rows

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.rows is not None:
            result['Rows'] = self.rows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.ExecuteMultiAccountSQLQueryResponseBodyColumns()
                self.columns.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Rows') is not None:
            self.rows = m.get('Rows')

        return self

class ExecuteMultiAccountSQLQueryResponseBodyColumns(DaraModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the column.
        self.name = name
        # The type of the column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

