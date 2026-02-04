# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListNormalizationCategoriesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_categories: List[main_models.ListNormalizationCategoriesResponseBodyNormalizationCategories] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_categories = normalization_categories
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.normalization_categories:
            for v1 in self.normalization_categories:
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

        result['NormalizationCategories'] = []
        if self.normalization_categories is not None:
            for k1 in self.normalization_categories:
                result['NormalizationCategories'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.normalization_categories = []
        if m.get('NormalizationCategories') is not None:
            for k1 in m.get('NormalizationCategories'):
                temp_model = main_models.ListNormalizationCategoriesResponseBodyNormalizationCategories()
                self.normalization_categories.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNormalizationCategoriesResponseBodyNormalizationCategories(DaraModel):
    def __init__(
        self,
        normalization_category_id: str = None,
        normalization_category_name: str = None,
    ):
        self.normalization_category_id = normalization_category_id
        self.normalization_category_name = normalization_category_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id

        if self.normalization_category_name is not None:
            result['NormalizationCategoryName'] = self.normalization_category_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')

        if m.get('NormalizationCategoryName') is not None:
            self.normalization_category_name = m.get('NormalizationCategoryName')

        return self

