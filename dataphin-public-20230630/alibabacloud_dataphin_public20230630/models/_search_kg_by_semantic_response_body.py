# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class SearchKgBySemanticResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.SearchKgBySemanticResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The search results.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.SearchKgBySemanticResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class SearchKgBySemanticResponseBodyData(DaraModel):
    def __init__(
        self,
        search_results: List[main_models.SearchKgBySemanticResponseBodyDataSearchResults] = None,
        total_count: int = None,
    ):
        # The list of search results.
        self.search_results = search_results
        # The total number of results.
        self.total_count = total_count

    def validate(self):
        if self.search_results:
            for v1 in self.search_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SearchResults'] = []
        if self.search_results is not None:
            for k1 in self.search_results:
                result['SearchResults'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_results = []
        if m.get('SearchResults') is not None:
            for k1 in m.get('SearchResults'):
                temp_model = main_models.SearchKgBySemanticResponseBodyDataSearchResults()
                self.search_results.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchKgBySemanticResponseBodyDataSearchResults(DaraModel):
    def __init__(
        self,
        item_id: str = None,
        item_type_code: str = None,
        matched_property_code: str = None,
        matched_property_value: str = None,
        similarity_score: float = None,
    ):
        # The ID of the matched entity record.
        self.item_id = item_id
        # The entity type code.
        self.item_type_code = item_type_code
        # The property code that matched the semantic search.
        self.matched_property_code = matched_property_code
        # The actual value of the matched property.
        self.matched_property_value = matched_property_value
        # The similarity score ranging from 0.0 to 1.0, based on cosine similarity.
        self.similarity_score = similarity_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_id is not None:
            result['ItemId'] = self.item_id

        if self.item_type_code is not None:
            result['ItemTypeCode'] = self.item_type_code

        if self.matched_property_code is not None:
            result['MatchedPropertyCode'] = self.matched_property_code

        if self.matched_property_value is not None:
            result['MatchedPropertyValue'] = self.matched_property_value

        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemId') is not None:
            self.item_id = m.get('ItemId')

        if m.get('ItemTypeCode') is not None:
            self.item_type_code = m.get('ItemTypeCode')

        if m.get('MatchedPropertyCode') is not None:
            self.matched_property_code = m.get('MatchedPropertyCode')

        if m.get('MatchedPropertyValue') is not None:
            self.matched_property_value = m.get('MatchedPropertyValue')

        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')

        return self

