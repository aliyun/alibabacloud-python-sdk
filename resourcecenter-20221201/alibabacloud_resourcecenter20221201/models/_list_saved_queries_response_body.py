# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcecenter20221201 import models as main_models
from darabonba.model import DaraModel

class ListSavedQueriesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        saved_queries: List[main_models.ListSavedQueriesResponseBodySavedQueries] = None,
    ):
        # The maximum number of entries returned on each page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the custom query templates.
        self.saved_queries = saved_queries

    def validate(self):
        if self.saved_queries:
            for v1 in self.saved_queries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SavedQueries'] = []
        if self.saved_queries is not None:
            for k1 in self.saved_queries:
                result['SavedQueries'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.saved_queries = []
        if m.get('SavedQueries') is not None:
            for k1 in m.get('SavedQueries'):
                temp_model = main_models.ListSavedQueriesResponseBodySavedQueries()
                self.saved_queries.append(temp_model.from_map(k1))

        return self

class ListSavedQueriesResponseBodySavedQueries(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        query_id: str = None,
        update_time: str = None,
    ):
        # The time when the template was created. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the template.
        self.description = description
        # The name of the template.
        self.name = name
        # The ID of the template.
        self.query_id = query_id
        # The time when the template was last updated. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.query_id is not None:
            result['QueryId'] = self.query_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

