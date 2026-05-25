# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_emas_appmonitor20190611 import models as main_models
from darabonba.model import DaraModel

class GetErrorsRequest(DaraModel):
    def __init__(
        self,
        app_key: int = None,
        biz_module: str = None,
        digest_hash: str = None,
        filter: main_models.GetErrorsRequestFilter = None,
        os: str = None,
        page_index: int = None,
        page_size: int = None,
        time_range: main_models.GetErrorsRequestTimeRange = None,
        utdid: str = None,
    ):
        # appKey
        # 
        # This parameter is required.
        self.app_key = app_key
        # This parameter is required.
        self.biz_module = biz_module
        self.digest_hash = digest_hash
        self.filter = filter
        self.os = os
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size
        # This parameter is required.
        self.time_range = time_range
        # utdid
        self.utdid = utdid

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

        if self.digest_hash is not None:
            result['DigestHash'] = self.digest_hash

        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.os is not None:
            result['Os'] = self.os

        if self.page_index is not None:
            result['PageIndex'] = self.page_index

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.time_range is not None:
            result['TimeRange'] = self.time_range.to_map()

        if self.utdid is not None:
            result['Utdid'] = self.utdid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('BizModule') is not None:
            self.biz_module = m.get('BizModule')

        if m.get('DigestHash') is not None:
            self.digest_hash = m.get('DigestHash')

        if m.get('Filter') is not None:
            temp_model = main_models.GetErrorsRequestFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('Os') is not None:
            self.os = m.get('Os')

        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TimeRange') is not None:
            temp_model = main_models.GetErrorsRequestTimeRange()
            self.time_range = temp_model.from_map(m.get('TimeRange'))

        if m.get('Utdid') is not None:
            self.utdid = m.get('Utdid')

        return self

class GetErrorsRequestTimeRange(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
    ):
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetErrorsRequestFilter(DaraModel):
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

