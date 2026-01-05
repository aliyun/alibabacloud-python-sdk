# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class DescribeCapacityReservationResponseBody(DaraModel):
    def __init__(
        self,
        capacity_reservation_state: List[main_models.DescribeCapacityReservationResponseBodyCapacityReservationState] = None,
        decrease_requests_remaining: int = None,
        last_modified_time: str = None,
        minimum_load_balancer_capacity: main_models.DescribeCapacityReservationResponseBodyMinimumLoadBalancerCapacity = None,
        request_id: str = None,
    ):
        self.capacity_reservation_state = capacity_reservation_state
        self.decrease_requests_remaining = decrease_requests_remaining
        self.last_modified_time = last_modified_time
        self.minimum_load_balancer_capacity = minimum_load_balancer_capacity
        self.request_id = request_id

    def validate(self):
        if self.capacity_reservation_state:
            for v1 in self.capacity_reservation_state:
                 if v1:
                    v1.validate()
        if self.minimum_load_balancer_capacity:
            self.minimum_load_balancer_capacity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CapacityReservationState'] = []
        if self.capacity_reservation_state is not None:
            for k1 in self.capacity_reservation_state:
                result['CapacityReservationState'].append(k1.to_map() if k1 else None)

        if self.decrease_requests_remaining is not None:
            result['DecreaseRequestsRemaining'] = self.decrease_requests_remaining

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.minimum_load_balancer_capacity is not None:
            result['MinimumLoadBalancerCapacity'] = self.minimum_load_balancer_capacity.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.capacity_reservation_state = []
        if m.get('CapacityReservationState') is not None:
            for k1 in m.get('CapacityReservationState'):
                temp_model = main_models.DescribeCapacityReservationResponseBodyCapacityReservationState()
                self.capacity_reservation_state.append(temp_model.from_map(k1))

        if m.get('DecreaseRequestsRemaining') is not None:
            self.decrease_requests_remaining = m.get('DecreaseRequestsRemaining')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('MinimumLoadBalancerCapacity') is not None:
            temp_model = main_models.DescribeCapacityReservationResponseBodyMinimumLoadBalancerCapacity()
            self.minimum_load_balancer_capacity = temp_model.from_map(m.get('MinimumLoadBalancerCapacity'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCapacityReservationResponseBodyMinimumLoadBalancerCapacity(DaraModel):
    def __init__(
        self,
        capacity_units: int = None,
    ):
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

class DescribeCapacityReservationResponseBodyCapacityReservationState(DaraModel):
    def __init__(
        self,
        availability_zone: str = None,
        effective_capacity_units: float = None,
        reason: str = None,
        status: str = None,
    ):
        self.availability_zone = availability_zone
        self.effective_capacity_units = effective_capacity_units
        self.reason = reason
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.availability_zone is not None:
            result['AvailabilityZone'] = self.availability_zone

        if self.effective_capacity_units is not None:
            result['EffectiveCapacityUnits'] = self.effective_capacity_units

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailabilityZone') is not None:
            self.availability_zone = m.get('AvailabilityZone')

        if m.get('EffectiveCapacityUnits') is not None:
            self.effective_capacity_units = m.get('EffectiveCapacityUnits')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

