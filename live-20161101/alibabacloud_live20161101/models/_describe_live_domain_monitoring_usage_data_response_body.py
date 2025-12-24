# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveDomainMonitoringUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        instance_id: str = None,
        monitoring_data: main_models.DescribeLiveDomainMonitoringUsageDataResponseBodyMonitoringData = None,
        region: str = None,
        request_id: str = None,
        start_time: str = None,
    ):
        # The domain name.
        self.domain_name = domain_name
        # The end of the time range.
        self.end_time = end_time
        # The ID of the monitoring session.
        self.instance_id = instance_id
        # The live monitoring data.
        self.monitoring_data = monitoring_data
        # The region of the live center.
        self.region = region
        # The request ID.
        self.request_id = request_id
        # The beginning of the time range.
        self.start_time = start_time

    def validate(self):
        if self.monitoring_data:
            self.monitoring_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.monitoring_data is not None:
            result['MonitoringData'] = self.monitoring_data.to_map()

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MonitoringData') is not None:
            temp_model = main_models.DescribeLiveDomainMonitoringUsageDataResponseBodyMonitoringData()
            self.monitoring_data = temp_model.from_map(m.get('MonitoringData'))

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class DescribeLiveDomainMonitoringUsageDataResponseBodyMonitoringData(DaraModel):
    def __init__(
        self,
        monitoring_data_item: List[main_models.DescribeLiveDomainMonitoringUsageDataResponseBodyMonitoringDataMonitoringDataItem] = None,
    ):
        self.monitoring_data_item = monitoring_data_item

    def validate(self):
        if self.monitoring_data_item:
            for v1 in self.monitoring_data_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MonitoringDataItem'] = []
        if self.monitoring_data_item is not None:
            for k1 in self.monitoring_data_item:
                result['MonitoringDataItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitoring_data_item = []
        if m.get('MonitoringDataItem') is not None:
            for k1 in m.get('MonitoringDataItem'):
                temp_model = main_models.DescribeLiveDomainMonitoringUsageDataResponseBodyMonitoringDataMonitoringDataItem()
                self.monitoring_data_item.append(temp_model.from_map(k1))

        return self

class DescribeLiveDomainMonitoringUsageDataResponseBodyMonitoringDataMonitoringDataItem(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        duration: int = None,
        instance_id: str = None,
        region: str = None,
        resolution: str = None,
        time_stamp: str = None,
    ):
        # The domain name. This field is valid only when you specify domain for the **SplitBy** parameter.
        self.domain_name = domain_name
        # The duration. Unit: minutes.
        self.duration = duration
        # The ID of the monitoring session. This field is valid only when you specify instance for the **SplitBy** parameter.
        self.instance_id = instance_id
        # The region of the live center. This field is valid only when you specify Region for the **SplitBy** parameter.
        self.region = region
        # The resolution. This field is valid only when you specify resolution for the **SplitBy** parameter.
        self.resolution = resolution
        # The timestamp of the returned data.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resolution is not None:
            result['Resolution'] = self.resolution

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Resolution') is not None:
            self.resolution = m.get('Resolution')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

