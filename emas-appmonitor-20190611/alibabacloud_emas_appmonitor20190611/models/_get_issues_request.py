# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class GetIssuesRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        filter: main_models.GetIssuesRequestFilter = None,
        name: str = None,
        order_by: str = None,
        order_type: str = None,
        os: str = None,
        page_index: int = None,
        page_size: int = None,
        status: int = None,
        time_range: main_models.GetIssuesRequestTimeRange = None,
    ):
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.biz_module = biz_module
        self.filter = filter
        self.name = name
        self.order_by = order_by
        self.order_type = order_type
        self.os = os
        self.page_index = page_index
        self.page_size = page_size
        self.status = status
        # This parameter is required.
        self.time_range = time_range

    def validate(self):
        if self.filter:
            self.filter.validate()
        if self.time_range:
            self.time_range.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.biz_module is not None:
            result['BizModule'] = self.biz_module

        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.os is not None:
            result['Os'] = self.os

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.status is not None:
            result['Status'] = self.status

        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')

        if m.get('Filter') is not None:
            temp_model = main_models.GetIssuesRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TimeRange') is not None:
            temp_model = main_models.GetIssuesRequestTimeRange()
            self.time_range = temp_model.from_map(m.get('TimeRange'))

        return self

class GetIssuesRequestTimeRange(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        granularity: int = None,
        granularity_unit: str = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.granularity = granularity
        self.granularity_unit = granularity_unit
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.granularity is not None:
            result['Granularity'] = self.granularity

        if self.granularity_unit is not None:
            result['GranularityUnit'] = self.granularity_unit

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Granularity') is not None:
            self.granularity = m.get('Granularity')

        if m.get('GranularityUnit') is not None:
            self.granularity_unit = m.get('GranularityUnit')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetIssuesRequestFilter(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        sub_filters: List[str] = None,
        values: List[Any] = None,
    ):
        self.key = key
        self.operator = operator
        self.sub_filters = sub_filters
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.sub_filters is not None:
            result['SubFilters'] = self.sub_filters

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('SubFilters') is not None:
            self.sub_filters = m.get('SubFilters')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

