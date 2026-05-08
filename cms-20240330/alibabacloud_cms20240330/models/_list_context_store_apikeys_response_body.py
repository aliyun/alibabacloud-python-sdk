# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListContextStoreAPIKeysResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        results: List[main_models.ListContextStoreAPIKeysResponseBodyResults] = None,
        total: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.results = results
        self.total = total

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        result['results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['results'].append(k1.to_map() if k1 else None)

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        self.results = []
        if m.get('results') is not None:
            for k1 in m.get('results'):
                temp_model = main_models.ListContextStoreAPIKeysResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListContextStoreAPIKeysResponseBodyResults(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        context_store_name: str = None,
        create_time: str = None,
        name: str = None,
        workspace: str = None,
    ):
        self.api_key = api_key
        self.context_store_name = context_store_name
        # Use the UTC time format: yyyy-MM-ddTHH:mm:ssZ
        self.create_time = create_time
        self.name = name
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['apiKey'] = self.api_key

        if self.context_store_name is not None:
            result['contextStoreName'] = self.context_store_name

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.name is not None:
            result['name'] = self.name

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiKey') is not None:
            self.api_key = m.get('apiKey')

        if m.get('contextStoreName') is not None:
            self.context_store_name = m.get('contextStoreName')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

