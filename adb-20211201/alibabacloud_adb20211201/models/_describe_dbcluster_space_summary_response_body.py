# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterSpaceSummaryResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeDBClusterSpaceSummaryResponseBodyData = None,
        request_id: str = None,
    ):
        # The queried storage overview information.
        self.data = data
        # The request ID.
        self.request_id = request_id

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeDBClusterSpaceSummaryResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterSpaceSummaryResponseBodyData(DaraModel):
    def __init__(
        self,
        cold_data: main_models.DescribeDBClusterSpaceSummaryResponseBodyDataColdData = None,
        data_growth: main_models.DescribeDBClusterSpaceSummaryResponseBodyDataDataGrowth = None,
        hot_data: main_models.DescribeDBClusterSpaceSummaryResponseBodyDataHotData = None,
        total_size: str = None,
    ):
        # The cold data.
        self.cold_data = cold_data
        # The data growth.
        self.data_growth = data_growth
        # The hot data.
        self.hot_data = hot_data
        # The total data size. Unit: bytes.
        # 
        # >  Formula: Total data size = Hot data size+ Cold data size.
        self.total_size = total_size

    def validate(self):
        if self.cold_data:
            self.cold_data.validate()
        if self.data_growth:
            self.data_growth.validate()
        if self.hot_data:
            self.hot_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_data is not None:
            result['ColdData'] = self.cold_data.to_map()

        if self.data_growth is not None:
            result['DataGrowth'] = self.data_growth.to_map()

        if self.hot_data is not None:
            result['HotData'] = self.hot_data.to_map()

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdData') is not None:
            temp_model = main_models.DescribeDBClusterSpaceSummaryResponseBodyDataColdData()
            self.cold_data = temp_model.from_map(m.get('ColdData'))

        if m.get('DataGrowth') is not None:
            temp_model = main_models.DescribeDBClusterSpaceSummaryResponseBodyDataDataGrowth()
            self.data_growth = temp_model.from_map(m.get('DataGrowth'))

        if m.get('HotData') is not None:
            temp_model = main_models.DescribeDBClusterSpaceSummaryResponseBodyDataHotData()
            self.hot_data = temp_model.from_map(m.get('HotData'))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeDBClusterSpaceSummaryResponseBodyDataHotData(DaraModel):
    def __init__(
        self,
        data_size: int = None,
        index_size: int = None,
        other_size: int = None,
        primary_key_index_size: int = None,
        total_size: int = None,
    ):
        # The data size of table records. Unit: bytes.
        self.data_size = data_size
        # The data size of regular indexes. Unit: bytes.
        self.index_size = index_size
        # The data size of other data. Unit: bytes.
        self.other_size = other_size
        # The data size of primary key indexes. Unit: bytes.
        self.primary_key_index_size = primary_key_index_size
        # The hot data size. Unit: bytes.
        # 
        # >  Formula: Hot data size = Data size of table records + Data size of regular indexes + Data size of primary key indexes + Data size of other data.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.index_size is not None:
            result['IndexSize'] = self.index_size

        if self.other_size is not None:
            result['OtherSize'] = self.other_size

        if self.primary_key_index_size is not None:
            result['PrimaryKeyIndexSize'] = self.primary_key_index_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('IndexSize') is not None:
            self.index_size = m.get('IndexSize')

        if m.get('OtherSize') is not None:
            self.other_size = m.get('OtherSize')

        if m.get('PrimaryKeyIndexSize') is not None:
            self.primary_key_index_size = m.get('PrimaryKeyIndexSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class DescribeDBClusterSpaceSummaryResponseBodyDataDataGrowth(DaraModel):
    def __init__(
        self,
        day_growth: int = None,
        week_growth: int = None,
    ):
        # The data growth within the last day. Unit: bytes.
        # 
        # >  Formula: Data growth within the last day = Current data size - Data size one day ago.
        self.day_growth = day_growth
        # The daily data growth within the last seven days. Unit: bytes.
        # 
        # >  Formula: Daily data growth within the last seven days = (Current data size - Data size seven days ago)/7.
        self.week_growth = week_growth

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.day_growth is not None:
            result['DayGrowth'] = self.day_growth

        if self.week_growth is not None:
            result['WeekGrowth'] = self.week_growth

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DayGrowth') is not None:
            self.day_growth = m.get('DayGrowth')

        if m.get('WeekGrowth') is not None:
            self.week_growth = m.get('WeekGrowth')

        return self

class DescribeDBClusterSpaceSummaryResponseBodyDataColdData(DaraModel):
    def __init__(
        self,
        data_size: int = None,
        index_size: int = None,
        other_size: int = None,
        primary_key_index_size: int = None,
        total_size: int = None,
    ):
        # The data size of table records. Unit: bytes.
        self.data_size = data_size
        # The data size of regular indexes. Unit: bytes.
        self.index_size = index_size
        # The data size of other data. Unit: bytes.
        self.other_size = other_size
        # The data size of primary key indexes. Unit: bytes.
        self.primary_key_index_size = primary_key_index_size
        # The cold data size. Unit: bytes.
        # 
        # >  Formula: Cold data size = Data size of table records + Data size of regular indexes + Data size of primary key indexes + Data size of other data.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_size is not None:
            result['DataSize'] = self.data_size

        if self.index_size is not None:
            result['IndexSize'] = self.index_size

        if self.other_size is not None:
            result['OtherSize'] = self.other_size

        if self.primary_key_index_size is not None:
            result['PrimaryKeyIndexSize'] = self.primary_key_index_size

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSize') is not None:
            self.data_size = m.get('DataSize')

        if m.get('IndexSize') is not None:
            self.index_size = m.get('IndexSize')

        if m.get('OtherSize') is not None:
            self.other_size = m.get('OtherSize')

        if m.get('PrimaryKeyIndexSize') is not None:
            self.primary_key_index_size = m.get('PrimaryKeyIndexSize')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

