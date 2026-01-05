# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ModifyCapacityReservationRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        minimum_load_balancer_capacity: main_models.ModifyCapacityReservationRequestMinimumLoadBalancerCapacity = None,
        reset_capacity_reservation: bool = None,
    ):
        self.client_token = client_token
        self.dry_run = dry_run
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.minimum_load_balancer_capacity = minimum_load_balancer_capacity
        self.reset_capacity_reservation = reset_capacity_reservation

    def validate(self):
        if self.minimum_load_balancer_capacity:
            self.minimum_load_balancer_capacity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.minimum_load_balancer_capacity is not None:
            result['MinimumLoadBalancerCapacity'] = self.minimum_load_balancer_capacity.to_map()

        if self.reset_capacity_reservation is not None:
            result['ResetCapacityReservation'] = self.reset_capacity_reservation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('MinimumLoadBalancerCapacity') is not None:
            temp_model = main_models.ModifyCapacityReservationRequestMinimumLoadBalancerCapacity()
            self.minimum_load_balancer_capacity = temp_model.from_map(m.get('MinimumLoadBalancerCapacity'))

        if m.get('ResetCapacityReservation') is not None:
            self.reset_capacity_reservation = m.get('ResetCapacityReservation')

        return self

class ModifyCapacityReservationRequestMinimumLoadBalancerCapacity(DaraModel):
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

