# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetDoctorHBaseClusterResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDoctorHBaseClusterResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
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
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDoctorHBaseClusterResponseBodyData(DaraModel):
    def __init__(
        self,
        analysis: main_models.GetDoctorHBaseClusterResponseBodyDataAnalysis = None,
        metrics: main_models.GetDoctorHBaseClusterResponseBodyDataMetrics = None,
    ):
        # The analysis result.
        self.analysis = analysis
        # The metric information.
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
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataAnalysis()
            self.analysis = temp_model.from_map(m.get('Analysis'))

        if m.get('Metrics') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        return self

class GetDoctorHBaseClusterResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        avg_load: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsAvgLoad = None,
        daily_read_request: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsDailyReadRequest = None,
        daily_write_request: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsDailyWriteRequest = None,
        mem_heap: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsMemHeap = None,
        normal_avg_load: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsNormalAvgLoad = None,
        region_balance: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsRegionBalance = None,
        region_count: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsRegionCount = None,
        region_server_count: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsRegionServerCount = None,
        store_file_count: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsStoreFileCount = None,
        table_count: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTableCount = None,
        total_data_size: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTotalDataSize = None,
        total_read_request: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTotalReadRequest = None,
        total_request: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTotalRequest = None,
        total_write_request: main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTotalWriteRequest = None,
    ):
        # The average load.
        self.avg_load = avg_load
        # The number of read requests in a day.
        self.daily_read_request = daily_read_request
        # The number of write requests in a day.
        self.daily_write_request = daily_write_request
        # The memory size.
        self.mem_heap = mem_heap
        # The normal average load.
        self.normal_avg_load = normal_avg_load
        # The region balance degree.
        self.region_balance = region_balance
        # The number of regions.
        self.region_count = region_count
        # The number of region servers.
        self.region_server_count = region_server_count
        # The number of StoreFiles.
        self.store_file_count = store_file_count
        # The number of tables.
        self.table_count = table_count
        # The size of the cluster.
        self.total_data_size = total_data_size
        # The total number of read requests.
        self.total_read_request = total_read_request
        # The total number of requests in the cluster.
        self.total_request = total_request
        # The total number of write requests.
        self.total_write_request = total_write_request

    def validate(self):
        if self.avg_load:
            self.avg_load.validate()
        if self.daily_read_request:
            self.daily_read_request.validate()
        if self.daily_write_request:
            self.daily_write_request.validate()
        if self.mem_heap:
            self.mem_heap.validate()
        if self.normal_avg_load:
            self.normal_avg_load.validate()
        if self.region_balance:
            self.region_balance.validate()
        if self.region_count:
            self.region_count.validate()
        if self.region_server_count:
            self.region_server_count.validate()
        if self.store_file_count:
            self.store_file_count.validate()
        if self.table_count:
            self.table_count.validate()
        if self.total_data_size:
            self.total_data_size.validate()
        if self.total_read_request:
            self.total_read_request.validate()
        if self.total_request:
            self.total_request.validate()
        if self.total_write_request:
            self.total_write_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_load is not None:
            result['AvgLoad'] = self.avg_load.to_map()

        if self.daily_read_request is not None:
            result['DailyReadRequest'] = self.daily_read_request.to_map()

        if self.daily_write_request is not None:
            result['DailyWriteRequest'] = self.daily_write_request.to_map()

        if self.mem_heap is not None:
            result['MemHeap'] = self.mem_heap.to_map()

        if self.normal_avg_load is not None:
            result['NormalAvgLoad'] = self.normal_avg_load.to_map()

        if self.region_balance is not None:
            result['RegionBalance'] = self.region_balance.to_map()

        if self.region_count is not None:
            result['RegionCount'] = self.region_count.to_map()

        if self.region_server_count is not None:
            result['RegionServerCount'] = self.region_server_count.to_map()

        if self.store_file_count is not None:
            result['StoreFileCount'] = self.store_file_count.to_map()

        if self.table_count is not None:
            result['TableCount'] = self.table_count.to_map()

        if self.total_data_size is not None:
            result['TotalDataSize'] = self.total_data_size.to_map()

        if self.total_read_request is not None:
            result['TotalReadRequest'] = self.total_read_request.to_map()

        if self.total_request is not None:
            result['TotalRequest'] = self.total_request.to_map()

        if self.total_write_request is not None:
            result['TotalWriteRequest'] = self.total_write_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgLoad') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsAvgLoad()
            self.avg_load = temp_model.from_map(m.get('AvgLoad'))

        if m.get('DailyReadRequest') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsDailyReadRequest()
            self.daily_read_request = temp_model.from_map(m.get('DailyReadRequest'))

        if m.get('DailyWriteRequest') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsDailyWriteRequest()
            self.daily_write_request = temp_model.from_map(m.get('DailyWriteRequest'))

        if m.get('MemHeap') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsMemHeap()
            self.mem_heap = temp_model.from_map(m.get('MemHeap'))

        if m.get('NormalAvgLoad') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsNormalAvgLoad()
            self.normal_avg_load = temp_model.from_map(m.get('NormalAvgLoad'))

        if m.get('RegionBalance') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsRegionBalance()
            self.region_balance = temp_model.from_map(m.get('RegionBalance'))

        if m.get('RegionCount') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsRegionCount()
            self.region_count = temp_model.from_map(m.get('RegionCount'))

        if m.get('RegionServerCount') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsRegionServerCount()
            self.region_server_count = temp_model.from_map(m.get('RegionServerCount'))

        if m.get('StoreFileCount') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsStoreFileCount()
            self.store_file_count = temp_model.from_map(m.get('StoreFileCount'))

        if m.get('TableCount') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTableCount()
            self.table_count = temp_model.from_map(m.get('TableCount'))

        if m.get('TotalDataSize') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTotalDataSize()
            self.total_data_size = temp_model.from_map(m.get('TotalDataSize'))

        if m.get('TotalReadRequest') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTotalReadRequest()
            self.total_read_request = temp_model.from_map(m.get('TotalReadRequest'))

        if m.get('TotalRequest') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTotalRequest()
            self.total_request = temp_model.from_map(m.get('TotalRequest'))

        if m.get('TotalWriteRequest') is not None:
            temp_model = main_models.GetDoctorHBaseClusterResponseBodyDataMetricsTotalWriteRequest()
            self.total_write_request = temp_model.from_map(m.get('TotalWriteRequest'))

        return self

class GetDoctorHBaseClusterResponseBodyDataMetricsTotalWriteRequest(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsTotalRequest(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsTotalReadRequest(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsTotalDataSize(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsTableCount(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsStoreFileCount(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsRegionServerCount(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsRegionCount(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsRegionBalance(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsNormalAvgLoad(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsMemHeap(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsDailyWriteRequest(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsDailyReadRequest(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataMetricsAvgLoad(DaraModel):
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

class GetDoctorHBaseClusterResponseBodyDataAnalysis(DaraModel):
    def __init__(
        self,
        hbase_score: int = None,
    ):
        # The overall score of the HBase cluster.
        self.hbase_score = hbase_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hbase_score is not None:
            result['HbaseScore'] = self.hbase_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HbaseScore') is not None:
            self.hbase_score = m.get('HbaseScore')

        return self

