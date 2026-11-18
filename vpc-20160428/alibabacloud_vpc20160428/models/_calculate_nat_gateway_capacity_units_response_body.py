# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CalculateNatGatewayCapacityUnitsResponseBody(DaraModel):
    def __init__(
        self,
        nat_gateway_capacity: main_models.CalculateNatGatewayCapacityUnitsResponseBodyNatGatewayCapacity = None,
        nat_gateway_performance_values: main_models.CalculateNatGatewayCapacityUnitsResponseBodyNatGatewayPerformanceValues = None,
        request_id: str = None,
    ):
        # The details of the calculated equivalent reserved CUs.
        self.nat_gateway_capacity = nat_gateway_capacity
        # The details of the calculated equivalent resource reservation metrics.
        self.nat_gateway_performance_values = nat_gateway_performance_values
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.nat_gateway_capacity:
            self.nat_gateway_capacity.validate()
        if self.nat_gateway_performance_values:
            self.nat_gateway_performance_values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nat_gateway_capacity is not None:
            result['NatGatewayCapacity'] = self.nat_gateway_capacity.to_map()

        if self.nat_gateway_performance_values is not None:
            result['NatGatewayPerformanceValues'] = self.nat_gateway_performance_values.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NatGatewayCapacity') is not None:
            temp_model = main_models.CalculateNatGatewayCapacityUnitsResponseBodyNatGatewayCapacity()
            self.nat_gateway_capacity = temp_model.from_map(m.get('NatGatewayCapacity'))

        if m.get('NatGatewayPerformanceValues') is not None:
            temp_model = main_models.CalculateNatGatewayCapacityUnitsResponseBodyNatGatewayPerformanceValues()
            self.nat_gateway_performance_values = temp_model.from_map(m.get('NatGatewayPerformanceValues'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CalculateNatGatewayCapacityUnitsResponseBodyNatGatewayPerformanceValues(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        cps: int = None,
        pps: int = None,
        session_count: int = None,
    ):
        # The bandwidth. Unit: Gbit/s.
        self.bandwidth = bandwidth
        # The maximum number of new connections per second.
        self.cps = cps
        # The number of packets per second. Unit: pps.
        self.pps = pps
        # The number of sessions.
        self.session_count = session_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.cps is not None:
            result['Cps'] = self.cps

        if self.pps is not None:
            result['Pps'] = self.pps

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Cps') is not None:
            self.cps = m.get('Cps')

        if m.get('Pps') is not None:
            self.pps = m.get('Pps')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        return self

class CalculateNatGatewayCapacityUnitsResponseBodyNatGatewayCapacity(DaraModel):
    def __init__(
        self,
        capacity_units: float = None,
    ):
        # The number of reserved LCUs per hour.
        self.capacity_units = capacity_units

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_units is not None:
            result['CapacityUnits'] = self.capacity_units

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityUnits') is not None:
            self.capacity_units = m.get('CapacityUnits')

        return self

