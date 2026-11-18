# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeNatGatewayCapacityReservationResponseBody(DaraModel):
    def __init__(
        self,
        capacity_reservation_status: main_models.DescribeNatGatewayCapacityReservationResponseBodyCapacityReservationStatus = None,
        decrease_requests_remaining: str = None,
        last_modified_time: int = None,
        nat_gateway_capacity: main_models.DescribeNatGatewayCapacityReservationResponseBodyNatGatewayCapacity = None,
        nat_gateway_id: str = None,
        nat_gateway_performance_values: main_models.DescribeNatGatewayCapacityReservationResponseBodyNatGatewayPerformanceValues = None,
        request_id: str = None,
    ):
        # The resource reservation status.
        self.capacity_reservation_status = capacity_reservation_status
        # The remaining number of times that you can downgrade or cancel the resource reservation.
        self.decrease_requests_remaining = decrease_requests_remaining
        # The time when the resource reservation was last modified.
        self.last_modified_time = last_modified_time
        # The number of capacity units (CUs) reserved for the NAT gateway.
        self.nat_gateway_capacity = nat_gateway_capacity
        # The ID of the NAT gateway to query.
        self.nat_gateway_id = nat_gateway_id
        # The performance metrics of the NAT gateway resource reservation.
        self.nat_gateway_performance_values = nat_gateway_performance_values
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.capacity_reservation_status:
            self.capacity_reservation_status.validate()
        if self.nat_gateway_capacity:
            self.nat_gateway_capacity.validate()
        if self.nat_gateway_performance_values:
            self.nat_gateway_performance_values.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_reservation_status is not None:
            result['CapacityReservationStatus'] = self.capacity_reservation_status.to_map()

        if self.decrease_requests_remaining is not None:
            result['DecreaseRequestsRemaining'] = self.decrease_requests_remaining

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.nat_gateway_capacity is not None:
            result['NatGatewayCapacity'] = self.nat_gateway_capacity.to_map()

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_performance_values is not None:
            result['NatGatewayPerformanceValues'] = self.nat_gateway_performance_values.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityReservationStatus') is not None:
            temp_model = main_models.DescribeNatGatewayCapacityReservationResponseBodyCapacityReservationStatus()
            self.capacity_reservation_status = temp_model.from_map(m.get('CapacityReservationStatus'))

        if m.get('DecreaseRequestsRemaining') is not None:
            self.decrease_requests_remaining = m.get('DecreaseRequestsRemaining')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('NatGatewayCapacity') is not None:
            temp_model = main_models.DescribeNatGatewayCapacityReservationResponseBodyNatGatewayCapacity()
            self.nat_gateway_capacity = temp_model.from_map(m.get('NatGatewayCapacity'))

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayPerformanceValues') is not None:
            temp_model = main_models.DescribeNatGatewayCapacityReservationResponseBodyNatGatewayPerformanceValues()
            self.nat_gateway_performance_values = temp_model.from_map(m.get('NatGatewayPerformanceValues'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeNatGatewayCapacityReservationResponseBodyNatGatewayPerformanceValues(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        cps: int = None,
        pps: int = None,
        session_count: int = None,
    ):
        # The bandwidth value. Unit: Gbit/s.
        self.bandwidth = bandwidth
        # The number of new connections per second.
        self.cps = cps
        # The number of packets per second.
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

class DescribeNatGatewayCapacityReservationResponseBodyNatGatewayCapacity(DaraModel):
    def __init__(
        self,
        capacity_units: float = None,
    ):
        # The number of load balancer capacity units (LCUs) reserved per hour.
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

class DescribeNatGatewayCapacityReservationResponseBodyCapacityReservationStatus(DaraModel):
    def __init__(
        self,
        reason: str = None,
        status: str = None,
    ):
        # The reason for the processing failure.
        self.reason = reason
        # The resource reservation status. Valid values:
        # 
        # - pending: The reservation is in progress.
        # 
        # - provisioned: The reservation is completed.
        # 
        # - failed: The reservation failed.
        # 
        # - deleting: The reservation is being deleted.
        # 
        # - deleted: The reservation is deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

