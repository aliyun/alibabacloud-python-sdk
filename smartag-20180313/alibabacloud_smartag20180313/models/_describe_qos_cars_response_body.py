# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeQosCarsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        qos_cars: main_models.DescribeQosCarsResponseBodyQosCars = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        self.qos_cars = qos_cars
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.qos_cars:
            self.qos_cars.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.qos_cars is not None:
            result['QosCars'] = self.qos_cars.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QosCars') is not None:
            temp_model = main_models.DescribeQosCarsResponseBodyQosCars()
            self.qos_cars = temp_model.from_map(m.get('QosCars'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeQosCarsResponseBodyQosCars(DaraModel):
    def __init__(
        self,
        qos_car: List[main_models.DescribeQosCarsResponseBodyQosCarsQosCar] = None,
    ):
        self.qos_car = qos_car

    def validate(self):
        if self.qos_car:
            for v1 in self.qos_car:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QosCar'] = []
        if self.qos_car is not None:
            for k1 in self.qos_car:
                result['QosCar'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qos_car = []
        if m.get('QosCar') is not None:
            for k1 in m.get('QosCar'):
                temp_model = main_models.DescribeQosCarsResponseBodyQosCarsQosCar()
                self.qos_car.append(temp_model.from_map(k1))

        return self

class DescribeQosCarsResponseBodyQosCarsQosCar(DaraModel):
    def __init__(
        self,
        description: str = None,
        limit_type: str = None,
        max_bandwidth_abs: int = None,
        max_bandwidth_percent: int = None,
        min_bandwidth_abs: int = None,
        min_bandwidth_percent: int = None,
        name: str = None,
        percent_source_type: str = None,
        priority: int = None,
        qos_car_id: str = None,
        qos_id: str = None,
    ):
        self.description = description
        self.limit_type = limit_type
        self.max_bandwidth_abs = max_bandwidth_abs
        self.max_bandwidth_percent = max_bandwidth_percent
        self.min_bandwidth_abs = min_bandwidth_abs
        self.min_bandwidth_percent = min_bandwidth_percent
        self.name = name
        self.percent_source_type = percent_source_type
        self.priority = priority
        self.qos_car_id = qos_car_id
        self.qos_id = qos_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.limit_type is not None:
            result['LimitType'] = self.limit_type

        if self.max_bandwidth_abs is not None:
            result['MaxBandwidthAbs'] = self.max_bandwidth_abs

        if self.max_bandwidth_percent is not None:
            result['MaxBandwidthPercent'] = self.max_bandwidth_percent

        if self.min_bandwidth_abs is not None:
            result['MinBandwidthAbs'] = self.min_bandwidth_abs

        if self.min_bandwidth_percent is not None:
            result['MinBandwidthPercent'] = self.min_bandwidth_percent

        if self.name is not None:
            result['Name'] = self.name

        if self.percent_source_type is not None:
            result['PercentSourceType'] = self.percent_source_type

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.qos_car_id is not None:
            result['QosCarId'] = self.qos_car_id

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        if m.get('MaxBandwidthAbs') is not None:
            self.max_bandwidth_abs = m.get('MaxBandwidthAbs')

        if m.get('MaxBandwidthPercent') is not None:
            self.max_bandwidth_percent = m.get('MaxBandwidthPercent')

        if m.get('MinBandwidthAbs') is not None:
            self.min_bandwidth_abs = m.get('MinBandwidthAbs')

        if m.get('MinBandwidthPercent') is not None:
            self.min_bandwidth_percent = m.get('MinBandwidthPercent')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PercentSourceType') is not None:
            self.percent_source_type = m.get('PercentSourceType')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QosCarId') is not None:
            self.qos_car_id = m.get('QosCarId')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        return self

