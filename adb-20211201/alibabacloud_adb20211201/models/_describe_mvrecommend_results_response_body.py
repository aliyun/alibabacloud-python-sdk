# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeMVRecommendResultsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeMVRecommendResultsResponseBodyData = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned data.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeMVRecommendResultsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeMVRecommendResultsResponseBodyData(DaraModel):
    def __init__(
        self,
        mv_recommend_result_models: List[main_models.OpenStructMVRecommendResultModel] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.mv_recommend_result_models = mv_recommend_result_models
        # The page number. Default value: **1**.
        self.page_number = page_number
        # The number of entries returned per page. Valid values:
        # 
        # *   **30** (default).
        # *   **50**.
        # *   **100**.
        self.page_size = page_size
        # The total number of entries.
        self.total_count = total_count

    def validate(self):
        if self.mv_recommend_result_models:
            for v1 in self.mv_recommend_result_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MvRecommendResultModels'] = []
        if self.mv_recommend_result_models is not None:
            for k1 in self.mv_recommend_result_models:
                result['MvRecommendResultModels'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mv_recommend_result_models = []
        if m.get('MvRecommendResultModels') is not None:
            for k1 in m.get('MvRecommendResultModels'):
                temp_model = main_models.OpenStructMVRecommendResultModel()
                self.mv_recommend_result_models.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

