# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class GetDoctorHBaseRegionResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetDoctorHBaseRegionResponseBodyData = None,
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
            temp_model = main_models.GetDoctorHBaseRegionResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetDoctorHBaseRegionResponseBodyData(DaraModel):
    def __init__(
        self,
        metrics: main_models.GetDoctorHBaseRegionResponseBodyDataMetrics = None,
        region_server_host: str = None,
        table_name: str = None,
    ):
        # Metrics information.
        self.metrics = metrics
        # Host of the RegionServer.
        self.region_server_host = region_server_host
        # Table name.
        self.table_name = table_name

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

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = main_models.GetDoctorHBaseRegionResponseBodyDataMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('RegionServerHost') is not None:
            self.region_server_host = m.get('RegionServerHost')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetDoctorHBaseRegionResponseBodyDataMetrics(DaraModel):
    def __init__(
        self,
        daily_read_request: main_models.GetDoctorHBaseRegionResponseBodyDataMetricsDailyReadRequest = None,
        daily_write_request: main_models.GetDoctorHBaseRegionResponseBodyDataMetricsDailyWriteRequest = None,
        store_file_count: main_models.GetDoctorHBaseRegionResponseBodyDataMetricsStoreFileCount = None,
        total_read_request: main_models.GetDoctorHBaseRegionResponseBodyDataMetricsTotalReadRequest = None,
        total_write_request: main_models.GetDoctorHBaseRegionResponseBodyDataMetricsTotalWriteRequest = None,
    ):
        # Number of read requests in a single day.
        self.daily_read_request = daily_read_request
        # Number of write requests in a single day.
        self.daily_write_request = daily_write_request
        # Store file count.
        self.store_file_count = store_file_count
        # Total read request count
        self.total_read_request = total_read_request
        # Total write request count
        self.total_write_request = total_write_request

    def validate(self):
        if self.daily_read_request:
            self.daily_read_request.validate()
        if self.daily_write_request:
            self.daily_write_request.validate()
        if self.store_file_count:
            self.store_file_count.validate()
        if self.total_read_request:
            self.total_read_request.validate()
        if self.total_write_request:
            self.total_write_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.daily_read_request is not None:
            result['DailyReadRequest'] = self.daily_read_request.to_map()

        if self.daily_write_request is not None:
            result['DailyWriteRequest'] = self.daily_write_request.to_map()

        if self.store_file_count is not None:
            result['StoreFileCount'] = self.store_file_count.to_map()

        if self.total_read_request is not None:
            result['TotalReadRequest'] = self.total_read_request.to_map()

        if self.total_write_request is not None:
            result['TotalWriteRequest'] = self.total_write_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DailyReadRequest') is not None:
            temp_model = main_models.GetDoctorHBaseRegionResponseBodyDataMetricsDailyReadRequest()
            self.daily_read_request = temp_model.from_map(m.get('DailyReadRequest'))

        if m.get('DailyWriteRequest') is not None:
            temp_model = main_models.GetDoctorHBaseRegionResponseBodyDataMetricsDailyWriteRequest()
            self.daily_write_request = temp_model.from_map(m.get('DailyWriteRequest'))

        if m.get('StoreFileCount') is not None:
            temp_model = main_models.GetDoctorHBaseRegionResponseBodyDataMetricsStoreFileCount()
            self.store_file_count = temp_model.from_map(m.get('StoreFileCount'))

        if m.get('TotalReadRequest') is not None:
            temp_model = main_models.GetDoctorHBaseRegionResponseBodyDataMetricsTotalReadRequest()
            self.total_read_request = temp_model.from_map(m.get('TotalReadRequest'))

        if m.get('TotalWriteRequest') is not None:
            temp_model = main_models.GetDoctorHBaseRegionResponseBodyDataMetricsTotalWriteRequest()
            self.total_write_request = temp_model.from_map(m.get('TotalWriteRequest'))

        return self

class GetDoctorHBaseRegionResponseBodyDataMetricsTotalWriteRequest(DaraModel):
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

class GetDoctorHBaseRegionResponseBodyDataMetricsTotalReadRequest(DaraModel):
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

class GetDoctorHBaseRegionResponseBodyDataMetricsStoreFileCount(DaraModel):
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

class GetDoctorHBaseRegionResponseBodyDataMetricsDailyWriteRequest(DaraModel):
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

class GetDoctorHBaseRegionResponseBodyDataMetricsDailyReadRequest(DaraModel):
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

