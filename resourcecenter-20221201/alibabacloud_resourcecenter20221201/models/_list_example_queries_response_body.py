# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class ListExampleQueriesResponseBody(DaraModel):
    def __init__(
        self,
        example_queries: List[main_models.ListExampleQueriesResponseBodyExampleQueries] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about the sample query templates.
        self.example_queries = example_queries
        # The maximum number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.example_queries:
            for v1 in self.example_queries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExampleQueries'] = []
        if self.example_queries is not None:
            for k1 in self.example_queries:
                result['ExampleQueries'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.example_queries = []
        if m.get('ExampleQueries') is not None:
            for k1 in m.get('ExampleQueries'):
                temp_model = main_models.ListExampleQueriesResponseBodyExampleQueries()
                self.example_queries.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListExampleQueriesResponseBodyExampleQueries(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        query_id: str = None,
    ):
        # The description of the template.
        self.description = description
        # The name of the template.
        self.name = name
        # The ID of the template.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        return self

