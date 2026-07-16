# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListDoctorHBaseRegionServersResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDoctorHBaseRegionServersResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned data.
        self.data = data
        # The maximum number of entries that are returned.
        self.max_results = max_results
        # A pagination token.
        self.next_token = next_token
        # The request ID.
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
                temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyData()
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

class ListDoctorHBaseRegionServersResponseBodyData(DaraModel):
    def __init__(
        self,
        metrics: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetrics = None,
        region_server_host: str = None,
    ):
        # The metric information.
        self.metrics = metrics
        # The RegionServer host.
        self.region_server_host = region_server_host

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        if self.region_server_host is not None:
            result['RegionServerHost'] = self.region_server_host

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('RegionServerHost') is not None:
            self.region_server_host = m.get('RegionServerHost')

        return self

class ListDoctorHBaseRegionServersResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        avg_gc: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsAvgGc = None,
        cache_ratio: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsCacheRatio = None,
        daily_read_request: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyReadRequest = None,
        daily_read_request_day_growth_ratio: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyReadRequestDayGrowthRatio = None,
        daily_write_request: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyWriteRequest = None,
        daily_write_request_day_growth_ratio: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio = None,
        region_count: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsRegionCount = None,
        total_read_request: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsTotalReadRequest = None,
        total_request: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsTotalRequest = None,
        total_write_request: main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsTotalWriteRequest = None,
    ):
        # The average garbage collection (GC) duration.
        self.avg_gc = avg_gc
        # The cache hit ratio.
        self.cache_ratio = cache_ratio
        # The number of daily read requests.
        self.daily_read_request = daily_read_request
        # The growth rate of the number of daily read requests.
        self.daily_read_request_day_growth_ratio = daily_read_request_day_growth_ratio
        # The number of daily write requests.
        self.daily_write_request = daily_write_request
        # The growth rate of the number of daily write requests.
        self.daily_write_request_day_growth_ratio = daily_write_request_day_growth_ratio
        # The number of regions.
        self.region_count = region_count
        # The cumulative number of read requests.
        self.total_read_request = total_read_request
        # The cumulative number of all requests.
        self.total_request = total_request
        # The cumulative number of write requests.
        self.total_write_request = total_write_request

    def validate(self):
        if self.avg_gc:
            self.avg_gc.validate()
        if self.cache_ratio:
            self.cache_ratio.validate()
        if self.daily_read_request:
            self.daily_read_request.validate()
        if self.daily_read_request_day_growth_ratio:
            self.daily_read_request_day_growth_ratio.validate()
        if self.daily_write_request:
            self.daily_write_request.validate()
        if self.daily_write_request_day_growth_ratio:
            self.daily_write_request_day_growth_ratio.validate()
        if self.region_count:
            self.region_count.validate()
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
        if self.avg_gc is not None:
            result['AvgGc'] = self.avg_gc.to_map()

        if self.cache_ratio is not None:
            result['CacheRatio'] = self.cache_ratio.to_map()

        if self.daily_read_request is not None:
            result['DailyReadRequest'] = self.daily_read_request.to_map()

        if self.daily_read_request_day_growth_ratio is not None:
            result['DailyReadRequestDayGrowthRatio'] = self.daily_read_request_day_growth_ratio.to_map()

        if self.daily_write_request is not None:
            result['DailyWriteRequest'] = self.daily_write_request.to_map()

        if self.daily_write_request_day_growth_ratio is not None:
            result['DailyWriteRequestDayGrowthRatio'] = self.daily_write_request_day_growth_ratio.to_map()

        if self.region_count is not None:
            result['RegionCount'] = self.region_count.to_map()

        if self.total_read_request is not None:
            result['TotalReadRequest'] = self.total_read_request.to_map()

        if self.total_request is not None:
            result['TotalRequest'] = self.total_request.to_map()

        if self.total_write_request is not None:
            result['TotalWriteRequest'] = self.total_write_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgGc') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsAvgGc()
            self.avg_gc = temp_model.from_map(m.get('AvgGc'))

        if m.get('CacheRatio') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsCacheRatio()
            self.cache_ratio = temp_model.from_map(m.get('CacheRatio'))

        if m.get('DailyReadRequest') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyReadRequest()
            self.daily_read_request = temp_model.from_map(m.get('DailyReadRequest'))

        if m.get('DailyReadRequestDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyReadRequestDayGrowthRatio()
            self.daily_read_request_day_growth_ratio = temp_model.from_map(m.get('DailyReadRequestDayGrowthRatio'))

        if m.get('DailyWriteRequest') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyWriteRequest()
            self.daily_write_request = temp_model.from_map(m.get('DailyWriteRequest'))

        if m.get('DailyWriteRequestDayGrowthRatio') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio()
            self.daily_write_request_day_growth_ratio = temp_model.from_map(m.get('DailyWriteRequestDayGrowthRatio'))

        if m.get('RegionCount') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsRegionCount()
            self.region_count = temp_model.from_map(m.get('RegionCount'))

        if m.get('TotalReadRequest') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsTotalReadRequest()
            self.total_read_request = temp_model.from_map(m.get('TotalReadRequest'))

        if m.get('TotalRequest') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsTotalRequest()
            self.total_request = temp_model.from_map(m.get('TotalRequest'))

        if m.get('TotalWriteRequest') is not None:
            temp_model = main_models.ListDoctorHBaseRegionServersResponseBodyDataMetricsTotalWriteRequest()
            self.total_write_request = temp_model.from_map(m.get('TotalWriteRequest'))

        return self

class ListDoctorHBaseRegionServersResponseBodyDataMetricsTotalWriteRequest(DaraModel):
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

class ListDoctorHBaseRegionServersResponseBodyDataMetricsTotalRequest(DaraModel):
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

class ListDoctorHBaseRegionServersResponseBodyDataMetricsTotalReadRequest(DaraModel):
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

class ListDoctorHBaseRegionServersResponseBodyDataMetricsRegionCount(DaraModel):
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

class ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio(DaraModel):
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

class ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyWriteRequest(DaraModel):
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

class ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyReadRequestDayGrowthRatio(DaraModel):
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

class ListDoctorHBaseRegionServersResponseBodyDataMetricsDailyReadRequest(DaraModel):
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

class ListDoctorHBaseRegionServersResponseBodyDataMetricsCacheRatio(DaraModel):
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

class ListDoctorHBaseRegionServersResponseBodyDataMetricsAvgGc(DaraModel):
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

