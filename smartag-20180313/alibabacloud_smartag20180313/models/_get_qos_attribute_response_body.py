# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class GetQosAttributeResponseBody(DaraModel):
    def __init__(
        self,
        error_config_smart_agcount: int = None,
        qos_cars: List[main_models.GetQosAttributeResponseBodyQosCars] = None,
        qos_description: str = None,
        qos_name: str = None,
        qos_policies: List[main_models.GetQosAttributeResponseBodyQosPolicies] = None,
        request_id: str = None,
    ):
        # The number of Smart Access Gateway (SAG) instances that have exceptional configurations.
        self.error_config_smart_agcount = error_config_smart_agcount
        # The traffic throttling rule applied to the QoS policies that have exceptional configurations.
        self.qos_cars = qos_cars
        # The description of the QoS policy.
        self.qos_description = qos_description
        # The name of the QoS policy.
        self.qos_name = qos_name
        # List of QoS policies based on 5-tuple.
        self.qos_policies = qos_policies
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.qos_cars:
            for v1 in self.qos_cars:
                 if v1:
                    v1.validate()
        if self.qos_policies:
            for v1 in self.qos_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_config_smart_agcount is not None:
            result['ErrorConfigSmartAGCount'] = self.error_config_smart_agcount

        result['QosCars'] = []
        if self.qos_cars is not None:
            for k1 in self.qos_cars:
                result['QosCars'].append(k1.to_map() if k1 else None)

        if self.qos_description is not None:
            result['QosDescription'] = self.qos_description

        if self.qos_name is not None:
            result['QosName'] = self.qos_name

        result['QosPolicies'] = []
        if self.qos_policies is not None:
            for k1 in self.qos_policies:
                result['QosPolicies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorConfigSmartAGCount') is not None:
            self.error_config_smart_agcount = m.get('ErrorConfigSmartAGCount')

        self.qos_cars = []
        if m.get('QosCars') is not None:
            for k1 in m.get('QosCars'):
                temp_model = main_models.GetQosAttributeResponseBodyQosCars()
                self.qos_cars.append(temp_model.from_map(k1))

        if m.get('QosDescription') is not None:
            self.qos_description = m.get('QosDescription')

        if m.get('QosName') is not None:
            self.qos_name = m.get('QosName')

        self.qos_policies = []
        if m.get('QosPolicies') is not None:
            for k1 in m.get('QosPolicies'):
                temp_model = main_models.GetQosAttributeResponseBodyQosPolicies()
                self.qos_policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetQosAttributeResponseBodyQosPolicies(DaraModel):
    def __init__(
        self,
        dest_cidr: str = None,
        dest_port_range: str = None,
        end_time: int = None,
        ip_protocol: str = None,
        priority: int = None,
        qos_policie_description: str = None,
        qos_policie_name: str = None,
        source_cidr: str = None,
        source_port_range: str = None,
        start_time: int = None,
    ):
        # The range of the destination CIDR block.
        self.dest_cidr = dest_cidr
        # The range of destination ports.
        # 
        # Valid values: **1** to **65535** and **-1**.
        # 
        # Examples of the format of the destination port range:
        # 
        # *   **1/200**: a port range from 1 to 200.
        # *   **80/80**: port 80.
        # *   **-1/-1**: all ports.
        self.dest_port_range = dest_port_range
        # The end time of the valid time of the 5-tuple.
        # 
        # The time must be in UTC+8.
        self.end_time = end_time
        # The type of the protocol that is applied to the 5-tuple rule.
        self.ip_protocol = ip_protocol
        # The priority of the traffic throttling rule that is applied to the 5-tuple.rule.
        # 
        # A smaller value indicates a higher priority.
        self.priority = priority
        # The description of the 5-tuple.
        self.qos_policie_description = qos_policie_description
        # The name of the 5-tuple.
        self.qos_policie_name = qos_policie_name
        # The range of the source CIDR block.
        self.source_cidr = source_cidr
        # The range of source ports.
        # 
        # Valid values: **1** to **65535** and **-1**.
        # 
        # Examples of the format of the source port range:
        # 
        # *   **1/200**: a port range from 1 to 200.
        # *   **80/80**: port 80.
        # *   **-1/-1**: all ports.
        self.source_port_range = source_port_range
        # The start time of the valid time of the 5-tuple.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dest_cidr is not None:
            result['DestCidr'] = self.dest_cidr

        if self.dest_port_range is not None:
            result['DestPortRange'] = self.dest_port_range

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ip_protocol is not None:
            result['IpProtocol'] = self.ip_protocol

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.qos_policie_description is not None:
            result['QosPolicieDescription'] = self.qos_policie_description

        if self.qos_policie_name is not None:
            result['QosPolicieName'] = self.qos_policie_name

        if self.source_cidr is not None:
            result['SourceCidr'] = self.source_cidr

        if self.source_port_range is not None:
            result['SourcePortRange'] = self.source_port_range

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestCidr') is not None:
            self.dest_cidr = m.get('DestCidr')

        if m.get('DestPortRange') is not None:
            self.dest_port_range = m.get('DestPortRange')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IpProtocol') is not None:
            self.ip_protocol = m.get('IpProtocol')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('QosPolicieDescription') is not None:
            self.qos_policie_description = m.get('QosPolicieDescription')

        if m.get('QosPolicieName') is not None:
            self.qos_policie_name = m.get('QosPolicieName')

        if m.get('SourceCidr') is not None:
            self.source_cidr = m.get('SourceCidr')

        if m.get('SourcePortRange') is not None:
            self.source_port_range = m.get('SourcePortRange')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetQosAttributeResponseBodyQosCars(DaraModel):
    def __init__(
        self,
        limit_type: str = None,
        max_bandwidth_abs: int = None,
        max_bandwidth_percent: int = None,
        min_bandwidth_abs: int = None,
        min_bandwidth_percent: int = None,
        percent_source_type: str = None,
        priority: int = None,
        qos_car_description: str = None,
        qos_car_id: str = None,
        qos_car_name: str = None,
    ):
        # The type of traffic throttling. Valid values:
        # 
        # *   **Absolute**: throttles traffic based on a specific range of bandwidth.
        # *   **Percent**: throttles traffic based on a specific range of bandwidth percentage.
        self.limit_type = limit_type
        # The maximum bandwidth. Unit: Mbit/s.
        self.max_bandwidth_abs = max_bandwidth_abs
        # The maximum bandwidth percentage that the traffic is throttled to.
        self.max_bandwidth_percent = max_bandwidth_percent
        # The minimum bandwidth. Unit: Mbit/s.
        self.min_bandwidth_abs = min_bandwidth_abs
        # The minimum bandwidth percentage.
        self.min_bandwidth_percent = min_bandwidth_percent
        # Bandwidth type when traffic is throttled to a percentage of the total bandwidth of the network.
        # 
        # *   **CcnBandwidth**: Cloud Connect Network (CCN) bandwidth.
        # *   **InternetUpBandwidth**: Internet upstream bandwidth.
        self.percent_source_type = percent_source_type
        # The priority of the traffic throttling rule.
        # 
        # Valid values are from **1** to **3**. A smaller value indicates a higher priority.
        self.priority = priority
        # The description of the traffic throttling rule.
        self.qos_car_description = qos_car_description
        # The ID of the traffic throttling rule.
        self.qos_car_id = qos_car_id
        # The name of the traffic throttling rule.
        self.qos_car_name = qos_car_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.qos_car_description is not None:
            result['QosCarDescription'] = self.qos_car_description

        if self.qos_car_id is not None:
            result['QosCarId'] = self.qos_car_id

        if self.qos_car_name is not None:
            result['QosCarName'] = self.qos_car_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('QosCarDescription') is not None:
            self.qos_car_description = m.get('QosCarDescription')

        if m.get('QosCarId') is not None:
            self.qos_car_id = m.get('QosCarId')

        if m.get('QosCarName') is not None:
            self.qos_car_name = m.get('QosCarName')

        return self

