# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorHBaseTablesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDoctorHBaseTablesResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The data returned.
        self.data = data
        # The maximum number of entries returned.
        self.max_results = max_results
        # The page number of the next page returned.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListDoctorHBaseTablesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDoctorHBaseTablesResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis: main_models.ListDoctorHBaseTablesResponseBodyDataAnalysis = None,
        metrics: main_models.ListDoctorHBaseTablesResponseBodyDataMetrics = None,
        table_name: str = None,
    ):
        # The diagnosis result.
        self.analysis = analysis
        # The metric information.
        self.metrics = metrics
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        if self.analysis:
            self.analysis.validate()
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysis is not None:
            result['Analysis'] = self.analysis.to_map()

        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analysis') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataAnalysis()
            self.analysis = temp_model.from_map(m.get('Analysis'))

        if m.get('Metrics') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        cold_access_day: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsColdAccessDay = None,
        cold_config_day: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsColdConfigDay = None,
        cold_data_size: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsColdDataSize = None,
        daily_read_request: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsDailyReadRequest = None,
        daily_read_request_day_growth_ratio: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsDailyReadRequestDayGrowthRatio = None,
        daily_write_request: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsDailyWriteRequest = None,
        daily_write_request_day_growth_ratio: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio = None,
        freeze_config_day: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsFreezeConfigDay = None,
        freeze_data_size: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsFreezeDataSize = None,
        hot_data_size: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsHotDataSize = None,
        locality: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsLocality = None,
        read_request_balance: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsReadRequestBalance = None,
        region_balance: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRegionBalance = None,
        region_count: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRegionCount = None,
        region_count_day_growth_ratio: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRegionCountDayGrowthRatio = None,
        region_server_count: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRegionServerCount = None,
        request_balance: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRequestBalance = None,
        store_file_count: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsStoreFileCount = None,
        store_file_count_day_growth_ratio: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsStoreFileCountDayGrowthRatio = None,
        table_size: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsTableSize = None,
        table_size_day_growth_ratio: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsTableSizeDayGrowthRatio = None,
        warm_config_day: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsWarmConfigDay = None,
        warm_data_size: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsWarmDataSize = None,
        write_request_balance: main_models.ListDoctorHBaseTablesResponseBodyDataMetricsWriteRequestBalance = None,
    ):
        # The number of days during which the table was not accessed.
        self.cold_access_day = cold_access_day
        # The number of consecutive days without access to data before the data is considered as very cold data.
        self.cold_config_day = cold_config_day
        # The size of cold data.
        self.cold_data_size = cold_data_size
        # The total number of read requests for the table in a day.
        self.daily_read_request = daily_read_request
        # The daily increment ratio of the number of read requests in a day.
        self.daily_read_request_day_growth_ratio = daily_read_request_day_growth_ratio
        # The total number of write requests for the table in a day.
        self.daily_write_request = daily_write_request
        # The daily increment ratio of the number of write requests in a day.
        self.daily_write_request_day_growth_ratio = daily_write_request_day_growth_ratio
        # The number of consecutive days without access to data before the data was considered as very cold data.
        self.freeze_config_day = freeze_config_day
        # The size of very cold data.
        self.freeze_data_size = freeze_data_size
        # The size of hot data.
        self.hot_data_size = hot_data_size
        # The localization rate.
        self.locality = locality
        # The read balancing degree.
        self.read_request_balance = read_request_balance
        # The balancing degree.
        self.region_balance = region_balance
        # The number of regions that host the table.
        self.region_count = region_count
        # The daily increment ratio of the number of regions.
        self.region_count_day_growth_ratio = region_count_day_growth_ratio
        # The number of region servers that host the table.
        self.region_server_count = region_server_count
        # The request balancing degree.
        self.request_balance = request_balance
        # The number of StoreFiles.
        self.store_file_count = store_file_count
        # The daily increment ratio of the number of StoreFiles.
        self.store_file_count_day_growth_ratio = store_file_count_day_growth_ratio
        # The size of the table.
        self.table_size = table_size
        # The daily increment ratio of the table size.
        self.table_size_day_growth_ratio = table_size_day_growth_ratio
        # The number of consecutive days without access to data before the data is considered as cold data.
        self.warm_config_day = warm_config_day
        # The size of warm data.
        self.warm_data_size = warm_data_size
        # The write balancing degree.
        self.write_request_balance = write_request_balance

    def validate(self):
        if self.cold_access_day:
            self.cold_access_day.validate()
        if self.cold_config_day:
            self.cold_config_day.validate()
        if self.cold_data_size:
            self.cold_data_size.validate()
        if self.daily_read_request:
            self.daily_read_request.validate()
        if self.daily_read_request_day_growth_ratio:
            self.daily_read_request_day_growth_ratio.validate()
        if self.daily_write_request:
            self.daily_write_request.validate()
        if self.daily_write_request_day_growth_ratio:
            self.daily_write_request_day_growth_ratio.validate()
        if self.freeze_config_day:
            self.freeze_config_day.validate()
        if self.freeze_data_size:
            self.freeze_data_size.validate()
        if self.hot_data_size:
            self.hot_data_size.validate()
        if self.locality:
            self.locality.validate()
        if self.read_request_balance:
            self.read_request_balance.validate()
        if self.region_balance:
            self.region_balance.validate()
        if self.region_count:
            self.region_count.validate()
        if self.region_count_day_growth_ratio:
            self.region_count_day_growth_ratio.validate()
        if self.region_server_count:
            self.region_server_count.validate()
        if self.request_balance:
            self.request_balance.validate()
        if self.store_file_count:
            self.store_file_count.validate()
        if self.store_file_count_day_growth_ratio:
            self.store_file_count_day_growth_ratio.validate()
        if self.table_size:
            self.table_size.validate()
        if self.table_size_day_growth_ratio:
            self.table_size_day_growth_ratio.validate()
        if self.warm_config_day:
            self.warm_config_day.validate()
        if self.warm_data_size:
            self.warm_data_size.validate()
        if self.write_request_balance:
            self.write_request_balance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cold_access_day is not None:
            result['ColdAccessDay'] = self.cold_access_day.to_map()

        if self.cold_config_day is not None:
            result['ColdConfigDay'] = self.cold_config_day.to_map()

        if self.cold_data_size is not None:
            result['ColdDataSize'] = self.cold_data_size.to_map()

        if self.daily_read_request is not None:
            result['DailyReadRequest'] = self.daily_read_request.to_map()

        if self.daily_read_request_day_growth_ratio is not None:
            result['DailyReadRequestDayGrowthRatio'] = self.daily_read_request_day_growth_ratio.to_map()

        if self.daily_write_request is not None:
            result['DailyWriteRequest'] = self.daily_write_request.to_map()

        if self.daily_write_request_day_growth_ratio is not None:
            result['DailyWriteRequestDayGrowthRatio'] = self.daily_write_request_day_growth_ratio.to_map()

        if self.freeze_config_day is not None:
            result['FreezeConfigDay'] = self.freeze_config_day.to_map()

        if self.freeze_data_size is not None:
            result['FreezeDataSize'] = self.freeze_data_size.to_map()

        if self.hot_data_size is not None:
            result['HotDataSize'] = self.hot_data_size.to_map()

        if self.locality is not None:
            result['Locality'] = self.locality.to_map()

        if self.read_request_balance is not None:
            result['ReadRequestBalance'] = self.read_request_balance.to_map()

        if self.region_balance is not None:
            result['RegionBalance'] = self.region_balance.to_map()

        if self.region_count is not None:
            result['RegionCount'] = self.region_count.to_map()

        if self.region_count_day_growth_ratio is not None:
            result['RegionCountDayGrowthRatio'] = self.region_count_day_growth_ratio.to_map()

        if self.region_server_count is not None:
            result['RegionServerCount'] = self.region_server_count.to_map()

        if self.request_balance is not None:
            result['RequestBalance'] = self.request_balance.to_map()

        if self.store_file_count is not None:
            result['StoreFileCount'] = self.store_file_count.to_map()

        if self.store_file_count_day_growth_ratio is not None:
            result['StoreFileCountDayGrowthRatio'] = self.store_file_count_day_growth_ratio.to_map()

        if self.table_size is not None:
            result['TableSize'] = self.table_size.to_map()

        if self.table_size_day_growth_ratio is not None:
            result['TableSizeDayGrowthRatio'] = self.table_size_day_growth_ratio.to_map()

        if self.warm_config_day is not None:
            result['WarmConfigDay'] = self.warm_config_day.to_map()

        if self.warm_data_size is not None:
            result['WarmDataSize'] = self.warm_data_size.to_map()

        if self.write_request_balance is not None:
            result['WriteRequestBalance'] = self.write_request_balance.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColdAccessDay') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsColdAccessDay()
            self.cold_access_day = temp_model.from_map(m.get('ColdAccessDay'))

        if m.get('ColdConfigDay') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsColdConfigDay()
            self.cold_config_day = temp_model.from_map(m.get('ColdConfigDay'))

        if m.get('ColdDataSize') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsColdDataSize()
            self.cold_data_size = temp_model.from_map(m.get('ColdDataSize'))

        if m.get('DailyReadRequest') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsDailyReadRequest()
            self.daily_read_request = temp_model.from_map(m.get('DailyReadRequest'))

        if m.get('DailyReadRequestDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsDailyReadRequestDayGrowthRatio()
            self.daily_read_request_day_growth_ratio = temp_model.from_map(m.get('DailyReadRequestDayGrowthRatio'))

        if m.get('DailyWriteRequest') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsDailyWriteRequest()
            self.daily_write_request = temp_model.from_map(m.get('DailyWriteRequest'))

        if m.get('DailyWriteRequestDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio()
            self.daily_write_request_day_growth_ratio = temp_model.from_map(m.get('DailyWriteRequestDayGrowthRatio'))

        if m.get('FreezeConfigDay') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsFreezeConfigDay()
            self.freeze_config_day = temp_model.from_map(m.get('FreezeConfigDay'))

        if m.get('FreezeDataSize') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsFreezeDataSize()
            self.freeze_data_size = temp_model.from_map(m.get('FreezeDataSize'))

        if m.get('HotDataSize') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsHotDataSize()
            self.hot_data_size = temp_model.from_map(m.get('HotDataSize'))

        if m.get('Locality') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsLocality()
            self.locality = temp_model.from_map(m.get('Locality'))

        if m.get('ReadRequestBalance') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsReadRequestBalance()
            self.read_request_balance = temp_model.from_map(m.get('ReadRequestBalance'))

        if m.get('RegionBalance') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRegionBalance()
            self.region_balance = temp_model.from_map(m.get('RegionBalance'))

        if m.get('RegionCount') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRegionCount()
            self.region_count = temp_model.from_map(m.get('RegionCount'))

        if m.get('RegionCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRegionCountDayGrowthRatio()
            self.region_count_day_growth_ratio = temp_model.from_map(m.get('RegionCountDayGrowthRatio'))

        if m.get('RegionServerCount') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRegionServerCount()
            self.region_server_count = temp_model.from_map(m.get('RegionServerCount'))

        if m.get('RequestBalance') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsRequestBalance()
            self.request_balance = temp_model.from_map(m.get('RequestBalance'))

        if m.get('StoreFileCount') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsStoreFileCount()
            self.store_file_count = temp_model.from_map(m.get('StoreFileCount'))

        if m.get('StoreFileCountDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsStoreFileCountDayGrowthRatio()
            self.store_file_count_day_growth_ratio = temp_model.from_map(m.get('StoreFileCountDayGrowthRatio'))

        if m.get('TableSize') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsTableSize()
            self.table_size = temp_model.from_map(m.get('TableSize'))

        if m.get('TableSizeDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsTableSizeDayGrowthRatio()
            self.table_size_day_growth_ratio = temp_model.from_map(m.get('TableSizeDayGrowthRatio'))

        if m.get('WarmConfigDay') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsWarmConfigDay()
            self.warm_config_day = temp_model.from_map(m.get('WarmConfigDay'))

        if m.get('WarmDataSize') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsWarmDataSize()
            self.warm_data_size = temp_model.from_map(m.get('WarmDataSize'))

        if m.get('WriteRequestBalance') is not None:
            temp_model = main_models.ListDoctorHBaseTablesResponseBodyDataMetricsWriteRequestBalance()
            self.write_request_balance = temp_model.from_map(m.get('WriteRequestBalance'))

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsWriteRequestBalance(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsWarmDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsWarmConfigDay(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsTableSizeDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsTableSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsStoreFileCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsStoreFileCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsRequestBalance(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsRegionServerCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsRegionCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsRegionCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsRegionBalance(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsReadRequestBalance(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsLocality(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsHotDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsFreezeDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsFreezeConfigDay(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsDailyWriteRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsDailyReadRequestDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsDailyReadRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsColdDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsColdConfigDay(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataMetricsColdAccessDay(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # The description of the metric.
        self.description = description
        # The name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unit is not None:
            result['Unit'] = self.unit

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unit') is not None:
            self.unit = m.get('Unit')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListDoctorHBaseTablesResponseBodyDataAnalysis(DaraModel):
    def __init__(
        self,
        read_request_hotspot_region_list: List[str] = None,
        read_request_unbalance_suggestion: str = None,
        request_hotspot_region_list: List[str] = None,
        request_unbalance_suggestion: str = None,
        table_score: int = None,
        write_request_hotspot_region_list: List[str] = None,
        write_request_unbalance_suggestion: str = None,
    ):
        # The regions that have read hotspot issues.
        self.read_request_hotspot_region_list = read_request_hotspot_region_list
        # The description of read imbalance.
        self.read_request_unbalance_suggestion = read_request_unbalance_suggestion
        # The regions that have read/write hotspot issues.
        self.request_hotspot_region_list = request_hotspot_region_list
        # The description of read/write imbalance.
        self.request_unbalance_suggestion = request_unbalance_suggestion
        # The score of the table.
        self.table_score = table_score
        # The regions that have write hotspot issues.
        self.write_request_hotspot_region_list = write_request_hotspot_region_list
        # The description of write imbalance.
        self.write_request_unbalance_suggestion = write_request_unbalance_suggestion

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.read_request_hotspot_region_list is not None:
            result['ReadRequestHotspotRegionList'] = self.read_request_hotspot_region_list

        if self.read_request_unbalance_suggestion is not None:
            result['ReadRequestUnbalanceSuggestion'] = self.read_request_unbalance_suggestion

        if self.request_hotspot_region_list is not None:
            result['RequestHotspotRegionList'] = self.request_hotspot_region_list

        if self.request_unbalance_suggestion is not None:
            result['RequestUnbalanceSuggestion'] = self.request_unbalance_suggestion

        if self.table_score is not None:
            result['TableScore'] = self.table_score

        if self.write_request_hotspot_region_list is not None:
            result['WriteRequestHotspotRegionList'] = self.write_request_hotspot_region_list

        if self.write_request_unbalance_suggestion is not None:
            result['WriteRequestUnbalanceSuggestion'] = self.write_request_unbalance_suggestion

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReadRequestHotspotRegionList') is not None:
            self.read_request_hotspot_region_list = m.get('ReadRequestHotspotRegionList')

        if m.get('ReadRequestUnbalanceSuggestion') is not None:
            self.read_request_unbalance_suggestion = m.get('ReadRequestUnbalanceSuggestion')

        if m.get('RequestHotspotRegionList') is not None:
            self.request_hotspot_region_list = m.get('RequestHotspotRegionList')

        if m.get('RequestUnbalanceSuggestion') is not None:
            self.request_unbalance_suggestion = m.get('RequestUnbalanceSuggestion')

        if m.get('TableScore') is not None:
            self.table_score = m.get('TableScore')

        if m.get('WriteRequestHotspotRegionList') is not None:
            self.write_request_hotspot_region_list = m.get('WriteRequestHotspotRegionList')

        if m.get('WriteRequestUnbalanceSuggestion') is not None:
            self.write_request_unbalance_suggestion = m.get('WriteRequestUnbalanceSuggestion')

        return self

