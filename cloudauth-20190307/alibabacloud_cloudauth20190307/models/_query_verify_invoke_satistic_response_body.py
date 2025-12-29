# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class QueryVerifyInvokeSatisticResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        items: List[main_models.QueryVerifyInvokeSatisticResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        total_page: int = None,
    ):
        # Response code, **200** indicates a successful response.
        self.code = code
        # Current page number.
        self.current_page = current_page
        # List of returned data.
        self.items = items
        # Number of items per page.
        self.page_size = page_size
        # ID of the request
        self.request_id = request_id
        # Whether the response was successful.
        self.success = success
        # Total count.
        self.total_count = total_count
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.QueryVerifyInvokeSatisticResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class QueryVerifyInvokeSatisticResponseBodyItems(DaraModel):
    def __init__(
        self,
        data: List[main_models.QueryVerifyInvokeSatisticResponseBodyItemsData] = None,
        statistics_date: str = None,
    ):
        # List of statistical data.
        self.data = data
        # Statistics date.
        self.statistics_date = statistics_date

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.statistics_date is not None:
            result['StatisticsDate'] = self.statistics_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.QueryVerifyInvokeSatisticResponseBodyItemsData()
                self.data.append(temp_model.from_map(k1))

        if m.get('StatisticsDate') is not None:
            self.statistics_date = m.get('StatisticsDate')

        return self

class QueryVerifyInvokeSatisticResponseBodyItemsData(DaraModel):
    def __init__(
        self,
        statistics_count: str = None,
        statistics_type: str = None,
    ):
        # Number of occurrences of the statistic.
        self.statistics_count = statistics_count
        # ProductCode。
        self.statistics_type = statistics_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.statistics_count is not None:
            result['StatisticsCount'] = self.statistics_count

        if self.statistics_type is not None:
            result['StatisticsType'] = self.statistics_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StatisticsCount') is not None:
            self.statistics_count = m.get('StatisticsCount')

        if m.get('StatisticsType') is not None:
            self.statistics_type = m.get('StatisticsType')

        return self

