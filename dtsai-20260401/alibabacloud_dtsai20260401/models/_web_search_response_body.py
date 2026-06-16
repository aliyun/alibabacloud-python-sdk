# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dtsai20260401 import models as main_models
from darabonba.model import DaraModel

class WebSearchResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        query: str = None,
        request_id: str = None,
        search_result: List[main_models.WebSearchResponseBodySearchResult] = None,
        success: bool = None,
        total_results: int = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.http_status_code = http_status_code
        self.query = query
        self.request_id = request_id
        self.search_result = search_result
        self.success = success
        self.total_results = total_results

    def validate(self):
        if self.search_result:
            for v1 in self.search_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.query is not None:
            result['Query'] = self.query

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SearchResult'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['SearchResult'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        if self.total_results is not None:
            result['TotalResults'] = self.total_results

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.WebSearchResponseBodySearchResult()
                self.search_result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalResults') is not None:
            self.total_results = m.get('TotalResults')

        return self



class WebSearchResponseBodySearchResult(DaraModel):
    def __init__(
        self,
        snippet: str = None,
        title: str = None,
        url: str = None,
    ):
        self.snippet = snippet
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.snippet is not None:
            result['Snippet'] = self.snippet

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Snippet') is not None:
            self.snippet = m.get('Snippet')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

