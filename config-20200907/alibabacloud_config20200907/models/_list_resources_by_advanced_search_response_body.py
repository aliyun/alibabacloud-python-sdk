# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class ListResourcesByAdvancedSearchResponseBody(DaraModel):
    def __init__(
        self,
        query_results: main_models.ListResourcesByAdvancedSearchResponseBodyQueryResults = None,
        request_id: str = None,
    ):
        # The query result.
        self.query_results = query_results
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.query_results:
            self.query_results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_results is not None:
            result['QueryResults'] = self.query_results.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryResults') is not None:
            temp_model = main_models.ListResourcesByAdvancedSearchResponseBodyQueryResults()
            self.query_results = temp_model.from_map(m.get('QueryResults'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListResourcesByAdvancedSearchResponseBodyQueryResults(DaraModel):
    def __init__(
        self,
        query_result_list: main_models.ListResourcesByAdvancedSearchResponseBodyQueryResultsQueryResultList = None,
    ):
        # The queried resources. A maximum of 1,000 data records can be returned. To view more data, use the download URL of the resource file.
        self.query_result_list = query_result_list

    def validate(self):
        if self.query_result_list:
            self.query_result_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_result_list is not None:
            result['QueryResultList'] = self.query_result_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryResultList') is not None:
            temp_model = main_models.ListResourcesByAdvancedSearchResponseBodyQueryResultsQueryResultList()
            self.query_result_list = temp_model.from_map(m.get('QueryResultList'))

        return self

class ListResourcesByAdvancedSearchResponseBodyQueryResultsQueryResultList(DaraModel):
    def __init__(
        self,
        columns: List[str] = None,
        values: List[Any] = None,
    ):
        # The field names.
        self.columns = columns
        # The resource data.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.columns is not None:
            result['Columns'] = self.columns

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Columns') is not None:
            self.columns = m.get('Columns')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

