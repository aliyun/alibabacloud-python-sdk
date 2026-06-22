# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetDoctorHBaseRegionServerResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDoctorHBaseRegionServerResponseBodyData = None,
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
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDoctorHBaseRegionServerResponseBodyData(DaraModel):
    def __init__(
        self,
        metrics: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetrics = None,
    ):
        # The metric information.
        self.metrics = metrics

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        return self

class GetDoctorHBaseRegionServerResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        avg_gc: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsAvgGc = None,
        cache_ratio: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsCacheRatio = None,
        daily_read_request: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyReadRequest = None,
        daily_read_request_day_growth_ratio: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyReadRequestDayGrowthRatio = None,
        daily_write_request: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyWriteRequest = None,
        daily_write_request_day_growth_ratio: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio = None,
        region_count: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsRegionCount = None,
        total_read_request: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsTotalReadRequest = None,
        total_request: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsTotalRequest = None,
        total_write_request: main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsTotalWriteRequest = None,
    ):
        # The average garbage collection (GC) duration.
        self.avg_gc = avg_gc
        # The cache hit ratio.
        self.cache_ratio = cache_ratio
        # The number of daily read requests.
        self.daily_read_request = daily_read_request
        # The day-to-day increment rate of the number of daily read requests.
        self.daily_read_request_day_growth_ratio = daily_read_request_day_growth_ratio
        # The number of daily write requests.
        self.daily_write_request = daily_write_request
        # The day-to-day increment rate of the number of daily write requests.
        self.daily_write_request_day_growth_ratio = daily_write_request_day_growth_ratio
        # The number of regions.
        self.region_count = region_count
        # The cumulative number of read requests.
        self.total_read_request = total_read_request
        # The cumulative number of total requests.
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
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsAvgGc()
            self.avg_gc = temp_model.from_map(m.get('AvgGc'))

        if m.get('CacheRatio') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsCacheRatio()
            self.cache_ratio = temp_model.from_map(m.get('CacheRatio'))

        if m.get('DailyReadRequest') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyReadRequest()
            self.daily_read_request = temp_model.from_map(m.get('DailyReadRequest'))

        if m.get('DailyReadRequestDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyReadRequestDayGrowthRatio()
            self.daily_read_request_day_growth_ratio = temp_model.from_map(m.get('DailyReadRequestDayGrowthRatio'))

        if m.get('DailyWriteRequest') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyWriteRequest()
            self.daily_write_request = temp_model.from_map(m.get('DailyWriteRequest'))

        if m.get('DailyWriteRequestDayGrowthRatio') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio()
            self.daily_write_request_day_growth_ratio = temp_model.from_map(m.get('DailyWriteRequestDayGrowthRatio'))

        if m.get('RegionCount') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsRegionCount()
            self.region_count = temp_model.from_map(m.get('RegionCount'))

        if m.get('TotalReadRequest') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsTotalReadRequest()
            self.total_read_request = temp_model.from_map(m.get('TotalReadRequest'))

        if m.get('TotalRequest') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsTotalRequest()
            self.total_request = temp_model.from_map(m.get('TotalRequest'))

        if m.get('TotalWriteRequest') is not None:
            temp_model = main_models.GetDoctorHBaseRegionServerResponseBodyDataMetricsTotalWriteRequest()
            self.total_write_request = temp_model.from_map(m.get('TotalWriteRequest'))

        return self

class GetDoctorHBaseRegionServerResponseBodyDataMetricsTotalWriteRequest(DaraModel):
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

class GetDoctorHBaseRegionServerResponseBodyDataMetricsTotalRequest(DaraModel):
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

class GetDoctorHBaseRegionServerResponseBodyDataMetricsTotalReadRequest(DaraModel):
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

class GetDoctorHBaseRegionServerResponseBodyDataMetricsRegionCount(DaraModel):
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

class GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyWriteRequestDayGrowthRatio(DaraModel):
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

class GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyWriteRequest(DaraModel):
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

class GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyReadRequestDayGrowthRatio(DaraModel):
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

class GetDoctorHBaseRegionServerResponseBodyDataMetricsDailyReadRequest(DaraModel):
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

class GetDoctorHBaseRegionServerResponseBodyDataMetricsCacheRatio(DaraModel):
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

class GetDoctorHBaseRegionServerResponseBodyDataMetricsAvgGc(DaraModel):
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

