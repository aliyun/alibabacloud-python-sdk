# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateQosCarResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        limit_type: str = None,
        max_bandwidth_abs: int = None,
        max_bandwidth_percent: int = None,
        min_bandwidth_abs: int = None,
        min_bandwidth_percent: int = None,
        percent_source_type: str = None,
        priority: int = None,
        qos_car_id: str = None,
        qos_id: str = None,
        request_id: str = None,
    ):
        # The description of the traffic throttling rule.
        self.description = description
        # The type of the traffic throttling rule. Valid values:
        # 
        # *   **Absolute**: throttles traffic based on a specific range of bandwidth.
        # *   **Percent**: throttles traffic based on a specific range of bandwidth percentage.
        self.limit_type = limit_type
        # The maximum bandwidth value. Unit: Mbit/s.
        # 
        # This parameter is returned when **LimitType** is set to **Absolute**.
        self.max_bandwidth_abs = max_bandwidth_abs
        # The maximum bandwidth percentage. Unit: percent (%).
        self.max_bandwidth_percent = max_bandwidth_percent
        # The minimum bandwidth value. Unit: Mbit/s.
        # 
        # This parameter is returned when **LimitType** is set to **Absolute**.
        self.min_bandwidth_abs = min_bandwidth_abs
        # The minimum bandwidth percentage. Unit: percent (%).
        self.min_bandwidth_percent = min_bandwidth_percent
        # The type of bandwidth when traffic is throttled based on bandwidth percentage. Valid values:
        # 
        # *   **CcnBandwidth**: CCN bandwidth
        # *   **InternetUpBandwidth**: total Internet bandwidth
        self.percent_source_type = percent_source_type
        # The priority value of the traffic throttling rule.
        self.priority = priority
        # The ID of the traffic throttling rule.
        self.qos_car_id = qos_car_id
        # The ID of the QoS policy.
        self.qos_id = qos_id
        # The ID of the request.
        self.request_id = request_id

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

        if self.percent_source_type is not None:
            result['PercentSourceType'] = self.percent_source_type

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.qos_car_id is not None:
            result['QosCarId'] = self.qos_car_id

        if self.qos_id is not None:
            result['QosId'] = self.qos_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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

        if m.get('PercentSourceType') is not None:
            self.percent_source_type = m.get('PercentSourceType')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QosCarId') is not None:
            self.qos_car_id = m.get('QosCarId')

        if m.get('QosId') is not None:
            self.qos_id = m.get('QosId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

