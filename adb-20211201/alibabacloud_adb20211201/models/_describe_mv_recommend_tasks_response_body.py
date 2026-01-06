# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeMvRecommendTasksResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeMvRecommendTasksResponseBodyData = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The data returned.
        self.data = data
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of entries that are returned.
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
            temp_model = main_models.DescribeMvRecommendTasksResponseBodyData()
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

class DescribeMvRecommendTasksResponseBodyData(DaraModel):
    def __init__(
        self,
        mv_recommend_task_models: List[main_models.OpenStructMvRecommendTaskModel] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of recommended tasks for materialized views.
        self.mv_recommend_task_models = mv_recommend_task_models
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The total number of entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.mv_recommend_task_models:
            for v1 in self.mv_recommend_task_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MvRecommendTaskModels'] = []
        if self.mv_recommend_task_models is not None:
            for k1 in self.mv_recommend_task_models:
                result['MvRecommendTaskModels'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mv_recommend_task_models = []
        if m.get('MvRecommendTaskModels') is not None:
            for k1 in m.get('MvRecommendTaskModels'):
                temp_model = main_models.OpenStructMvRecommendTaskModel()
                self.mv_recommend_task_models.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

