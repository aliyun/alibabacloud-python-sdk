# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetDoctorHBaseTableResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDoctorHBaseTableResponseBodyData = None,
        request_id: str = None,
    ):
        # Returned data.
        self.data = data
        # Request ID.
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
            temp_model = main_models.GetDoctorHBaseTableResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDoctorHBaseTableResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis: main_models.GetDoctorHBaseTableResponseBodyDataAnalysis = None,
        metrics: main_models.GetDoctorHBaseTableResponseBodyDataMetrics = None,
    ):
        # Diagnostic results.
        self.analysis = analysis
        # Metrics information.
        self.metrics = metrics

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Analysis') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataAnalysis()
            self.analysis = temp_model.from_map(m.get('Analysis'))

        if m.get('Metrics') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        return self

class GetDoctorHBaseTableResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        cold_access_day: main_models.GetDoctorHBaseTableResponseBodyDataMetricsColdAccessDay = None,
        cold_config_day: main_models.GetDoctorHBaseTableResponseBodyDataMetricsColdConfigDay = None,
        cold_data_size: main_models.GetDoctorHBaseTableResponseBodyDataMetricsColdDataSize = None,
        daily_read_request: main_models.GetDoctorHBaseTableResponseBodyDataMetricsDailyReadRequest = None,
        daily_read_request_day_growth_ratio: main_models.GetDoctorHBaseTableResponseBodyDataMetricsDailyReadRequestDayGrowthRatio = None,
        daily_write_request: main_models.GetDoctorHBaseTableResponseBodyDataMetricsDailyWriteRequest = None,
        daily_write_request_day_growth_ratio: main_models.GetDoctorHBaseTableResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio = None,
        freeze_config_day: main_models.GetDoctorHBaseTableResponseBodyDataMetricsFreezeConfigDay = None,
        freeze_data_size: main_models.GetDoctorHBaseTableResponseBodyDataMetricsFreezeDataSize = None,
        hot_data_size: main_models.GetDoctorHBaseTableResponseBodyDataMetricsHotDataSize = None,
        locality: main_models.GetDoctorHBaseTableResponseBodyDataMetricsLocality = None,
        read_request_balance: main_models.GetDoctorHBaseTableResponseBodyDataMetricsReadRequestBalance = None,
        region_balance: main_models.GetDoctorHBaseTableResponseBodyDataMetricsRegionBalance = None,
        region_count: main_models.GetDoctorHBaseTableResponseBodyDataMetricsRegionCount = None,
        region_count_day_growth_ratio: main_models.GetDoctorHBaseTableResponseBodyDataMetricsRegionCountDayGrowthRatio = None,
        region_server_count: main_models.GetDoctorHBaseTableResponseBodyDataMetricsRegionServerCount = None,
        request_balance: main_models.GetDoctorHBaseTableResponseBodyDataMetricsRequestBalance = None,
        store_file_count: main_models.GetDoctorHBaseTableResponseBodyDataMetricsStoreFileCount = None,
        store_file_count_day_growth_ratio: main_models.GetDoctorHBaseTableResponseBodyDataMetricsStoreFileCountDayGrowthRatio = None,
        table_size: main_models.GetDoctorHBaseTableResponseBodyDataMetricsTableSize = None,
        table_size_day_growth_ratio: main_models.GetDoctorHBaseTableResponseBodyDataMetricsTableSizeDayGrowthRatio = None,
        warm_config_day: main_models.GetDoctorHBaseTableResponseBodyDataMetricsWarmConfigDay = None,
        warm_data_size: main_models.GetDoctorHBaseTableResponseBodyDataMetricsWarmDataSize = None,
        write_request_balance: main_models.GetDoctorHBaseTableResponseBodyDataMetricsWriteRequestBalance = None,
    ):
        # Number of days the table has not been accessed.
        self.cold_access_day = cold_access_day
        # Cold data access days configuration.
        self.cold_config_day = cold_config_day
        # Cold data size.
        self.cold_data_size = cold_data_size
        # Number of read requests per day.
        self.daily_read_request = daily_read_request
        # Daily growth ratio of daily read requests.
        self.daily_read_request_day_growth_ratio = daily_read_request_day_growth_ratio
        # Number of write requests per day.
        self.daily_write_request = daily_write_request
        # Daily write request growth ratio.
        self.daily_write_request_day_growth_ratio = daily_write_request_day_growth_ratio
        # Configuration for the number of days cold data is accessed.
        self.freeze_config_day = freeze_config_day
        # Frozen data size.
        self.freeze_data_size = freeze_data_size
        # Hot data size.
        self.hot_data_size = hot_data_size
        # Locality rate.
        self.locality = locality
        # Read request balance.
        self.read_request_balance = read_request_balance
        # Region balance.
        self.region_balance = region_balance
        # Number of regions.
        self.region_count = region_count
        # Daily incremental ratio of regions
        self.region_count_day_growth_ratio = region_count_day_growth_ratio
        # Number of RegionServers.
        self.region_server_count = region_server_count
        # Request balance.
        self.request_balance = request_balance
        # Number of store files.
        self.store_file_count = store_file_count
        # Daily growth ratio of store file count.
        self.store_file_count_day_growth_ratio = store_file_count_day_growth_ratio
        # Table size.
        self.table_size = table_size
        # Daily growth ratio of table size.
        self.table_size_day_growth_ratio = table_size_day_growth_ratio
        # Warm data access days configuration.
        self.warm_config_day = warm_config_day
        # Warm data size.
        self.warm_data_size = warm_data_size
        # Write request balance.
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
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsColdAccessDay()
            self.cold_access_day = temp_model.from_map(m.get('ColdAccessDay'))

        if m.get('ColdConfigDay') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsColdConfigDay()
            self.cold_config_day = temp_model.from_map(m.get('ColdConfigDay'))

        if m.get('ColdDataSize') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsColdDataSize()
            self.cold_data_size = temp_model.from_map(m.get('ColdDataSize'))

        if m.get('DailyReadRequest') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsDailyReadRequest()
            self.daily_read_request = temp_model.from_map(m.get('DailyReadRequest'))

        if m.get('DailyReadRequestDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsDailyReadRequestDayGrowthRatio()
            self.daily_read_request_day_growth_ratio = temp_model.from_map(m.get('DailyReadRequestDayGrowthRatio'))

        if m.get('DailyWriteRequest') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsDailyWriteRequest()
            self.daily_write_request = temp_model.from_map(m.get('DailyWriteRequest'))

        if m.get('DailyWriteRequestDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio()
            self.daily_write_request_day_growth_ratio = temp_model.from_map(m.get('DailyWriteRequestDayGrowthRatio'))

        if m.get('FreezeConfigDay') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsFreezeConfigDay()
            self.freeze_config_day = temp_model.from_map(m.get('FreezeConfigDay'))

        if m.get('FreezeDataSize') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsFreezeDataSize()
            self.freeze_data_size = temp_model.from_map(m.get('FreezeDataSize'))

        if m.get('HotDataSize') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsHotDataSize()
            self.hot_data_size = temp_model.from_map(m.get('HotDataSize'))

        if m.get('Locality') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsLocality()
            self.locality = temp_model.from_map(m.get('Locality'))

        if m.get('ReadRequestBalance') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsReadRequestBalance()
            self.read_request_balance = temp_model.from_map(m.get('ReadRequestBalance'))

        if m.get('RegionBalance') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsRegionBalance()
            self.region_balance = temp_model.from_map(m.get('RegionBalance'))

        if m.get('RegionCount') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsRegionCount()
            self.region_count = temp_model.from_map(m.get('RegionCount'))

        if m.get('RegionCountDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsRegionCountDayGrowthRatio()
            self.region_count_day_growth_ratio = temp_model.from_map(m.get('RegionCountDayGrowthRatio'))

        if m.get('RegionServerCount') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsRegionServerCount()
            self.region_server_count = temp_model.from_map(m.get('RegionServerCount'))

        if m.get('RequestBalance') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsRequestBalance()
            self.request_balance = temp_model.from_map(m.get('RequestBalance'))

        if m.get('StoreFileCount') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsStoreFileCount()
            self.store_file_count = temp_model.from_map(m.get('StoreFileCount'))

        if m.get('StoreFileCountDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsStoreFileCountDayGrowthRatio()
            self.store_file_count_day_growth_ratio = temp_model.from_map(m.get('StoreFileCountDayGrowthRatio'))

        if m.get('TableSize') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsTableSize()
            self.table_size = temp_model.from_map(m.get('TableSize'))

        if m.get('TableSizeDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsTableSizeDayGrowthRatio()
            self.table_size_day_growth_ratio = temp_model.from_map(m.get('TableSizeDayGrowthRatio'))

        if m.get('WarmConfigDay') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsWarmConfigDay()
            self.warm_config_day = temp_model.from_map(m.get('WarmConfigDay'))

        if m.get('WarmDataSize') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsWarmDataSize()
            self.warm_data_size = temp_model.from_map(m.get('WarmDataSize'))

        if m.get('WriteRequestBalance') is not None:
            temp_model = main_models.GetDoctorHBaseTableResponseBodyDataMetricsWriteRequestBalance()
            self.write_request_balance = temp_model.from_map(m.get('WriteRequestBalance'))

        return self

class GetDoctorHBaseTableResponseBodyDataMetricsWriteRequestBalance(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
        self.name = name
        # Unit of the metric.
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

class GetDoctorHBaseTableResponseBodyDataMetricsWarmDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # Usage rate.
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

class GetDoctorHBaseTableResponseBodyDataMetricsWarmConfigDay(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Metric description.
        self.description = description
        # Metric name.
        self.name = name
        # Metric unit.
        self.unit = unit
        # Metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsTableSizeDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Metric description.
        self.description = description
        # Metric name.
        self.name = name
        # Metric unit.
        self.unit = unit
        # Metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsTableSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Description of the metric.
        self.description = description
        # Metric name.
        self.name = name
        # Unit of the metric
        self.unit = unit
        # Metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsStoreFileCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Metric description.
        self.description = description
        # Metric name.
        self.name = name
        # Metric unit.
        self.unit = unit
        # Metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsStoreFileCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
        self.name = name
        # Unit of the metric.
        self.unit = unit
        # Value of the metric.
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

class GetDoctorHBaseTableResponseBodyDataMetricsRequestBalance(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsRegionServerCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Metric description.
        self.description = description
        # Metric name.
        self.name = name
        # Metric unit.
        self.unit = unit
        # Usage.
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

class GetDoctorHBaseTableResponseBodyDataMetricsRegionCountDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Metric description.
        self.description = description
        # Metric name.
        self.name = name
        # Metric unit.
        self.unit = unit
        # Metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsRegionCount(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Metric description.
        self.description = description
        # Metric name.
        self.name = name
        # Metric unit.
        self.unit = unit
        # Metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsRegionBalance(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Description of the metric.
        self.description = description
        # Metric name.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsReadRequestBalance(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
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

class GetDoctorHBaseTableResponseBodyDataMetricsLocality(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
        self.name = name
        # Unit of the metric.
        self.unit = unit
        # Value of the metric.
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

class GetDoctorHBaseTableResponseBodyDataMetricsHotDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
        self.name = name
        # The unit of the metric.
        self.unit = unit
        # The metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsFreezeDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Metric description.
        self.description = description
        # Metric name.
        self.name = name
        # Metric unit.
        self.unit = unit
        # Metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsFreezeConfigDay(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
        self.name = name
        # Unit of the metric.
        self.unit = unit
        # Value of the metric.
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

class GetDoctorHBaseTableResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
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

class GetDoctorHBaseTableResponseBodyDataMetricsDailyWriteRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
        self.name = name
        # Unit of the metric.
        self.unit = unit
        # Value of the metric.
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

class GetDoctorHBaseTableResponseBodyDataMetricsDailyReadRequestDayGrowthRatio(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: float = None,
    ):
        # Description of the metric.
        self.description = description
        # Metric name.
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

class GetDoctorHBaseTableResponseBodyDataMetricsDailyReadRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the item.
        self.name = name
        # Unit of the metric.
        self.unit = unit
        # Value of the metric.
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

class GetDoctorHBaseTableResponseBodyDataMetricsColdDataSize(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Metric description.
        self.description = description
        # Metric name.
        self.name = name
        # Metric unit.
        self.unit = unit
        # Metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsColdConfigDay(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Description of the metric.
        self.description = description
        # Metric name.
        self.name = name
        # Unit of the metric.
        self.unit = unit
        # Metric value.
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

class GetDoctorHBaseTableResponseBodyDataMetricsColdAccessDay(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unit: str = None,
        value: int = None,
    ):
        # Description of the metric.
        self.description = description
        # Name of the metric.
        self.name = name
        # Unit of the metric.
        self.unit = unit
        # Value of the metric.
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

class GetDoctorHBaseTableResponseBodyDataAnalysis(DaraModel):
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
        # List of read hotspot regions.
        self.read_request_hotspot_region_list = read_request_hotspot_region_list
        # Description of read imbalance.
        self.read_request_unbalance_suggestion = read_request_unbalance_suggestion
        # List of read/write hotspot regions.
        self.request_hotspot_region_list = request_hotspot_region_list
        # Description of read/write imbalance.
        self.request_unbalance_suggestion = request_unbalance_suggestion
        # Table score.
        self.table_score = table_score
        # List of write hotspot regions.
        self.write_request_hotspot_region_list = write_request_hotspot_region_list
        # Description of write imbalance.
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

