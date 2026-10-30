# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class ModifyTransitRouterCapacityReservationsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        deployment_sets: List[main_models.ModifyTransitRouterCapacityReservationsRequestDeploymentSets] = None,
        minimum_transit_router_capacities: List[main_models.ModifyTransitRouterCapacityReservationsRequestMinimumTransitRouterCapacities] = None,
        reset_capacity_reservations: List[main_models.ModifyTransitRouterCapacityReservationsRequestResetCapacityReservations] = None,
        transit_router_id: str = None,
        version: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the token on your client to ensure that the token is unique across different requests. The client token only supports ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID of the API request as the client token. The request ID may be different for each API request.
        self.client_token = client_token
        # The deployment set information for the capacity reservation.
        self.deployment_sets = deployment_sets
        # The reserved capacity for each zone in the capacity reservation.
        self.minimum_transit_router_capacities = minimum_transit_router_capacities
        # Cancels capacity reservations.
        self.reset_capacity_reservations = reset_capacity_reservations
        # The ID of the transit router instance for forward routing.
        # 
        # This parameter is required.
        self.transit_router_id = transit_router_id
        self.version = version

    def validate(self):
        if self.deployment_sets:
            for v1 in self.deployment_sets:
                 if v1:
                    v1.validate()
        if self.minimum_transit_router_capacities:
            for v1 in self.minimum_transit_router_capacities:
                 if v1:
                    v1.validate()
        if self.reset_capacity_reservations:
            for v1 in self.reset_capacity_reservations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['DeploymentSets'] = []
        if self.deployment_sets is not None:
            for k1 in self.deployment_sets:
                result['DeploymentSets'].append(k1.to_map() if k1 else None)

        result['MinimumTransitRouterCapacities'] = []
        if self.minimum_transit_router_capacities is not None:
            for k1 in self.minimum_transit_router_capacities:
                result['MinimumTransitRouterCapacities'].append(k1.to_map() if k1 else None)

        result['ResetCapacityReservations'] = []
        if self.reset_capacity_reservations is not None:
            for k1 in self.reset_capacity_reservations:
                result['ResetCapacityReservations'].append(k1.to_map() if k1 else None)

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.deployment_sets = []
        if m.get('DeploymentSets') is not None:
            for k1 in m.get('DeploymentSets'):
                temp_model = main_models.ModifyTransitRouterCapacityReservationsRequestDeploymentSets()
                self.deployment_sets.append(temp_model.from_map(k1))

        self.minimum_transit_router_capacities = []
        if m.get('MinimumTransitRouterCapacities') is not None:
            for k1 in m.get('MinimumTransitRouterCapacities'):
                temp_model = main_models.ModifyTransitRouterCapacityReservationsRequestMinimumTransitRouterCapacities()
                self.minimum_transit_router_capacities.append(temp_model.from_map(k1))

        self.reset_capacity_reservations = []
        if m.get('ResetCapacityReservations') is not None:
            for k1 in m.get('ResetCapacityReservations'):
                temp_model = main_models.ModifyTransitRouterCapacityReservationsRequestResetCapacityReservations()
                self.reset_capacity_reservations.append(temp_model.from_map(k1))

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ModifyTransitRouterCapacityReservationsRequestResetCapacityReservations(DaraModel):
    def __init__(
        self,
        zone_id: str = None,
    ):
        # The ID of the zone for which to cancel the capacity reservation.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ModifyTransitRouterCapacityReservationsRequestMinimumTransitRouterCapacities(DaraModel):
    def __init__(
        self,
        data_process_gbps: main_models.ModifyTransitRouterCapacityReservationsRequestMinimumTransitRouterCapacitiesDataProcessGbps = None,
        zone_id: str = None,
    ):
        # The reserved capacity for the specified zone.
        self.data_process_gbps = data_process_gbps
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        if self.data_process_gbps:
            self.data_process_gbps.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_process_gbps is not None:
            result['DataProcessGbps'] = self.data_process_gbps.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataProcessGbps') is not None:
            temp_model = main_models.ModifyTransitRouterCapacityReservationsRequestMinimumTransitRouterCapacitiesDataProcessGbps()
            self.data_process_gbps = temp_model.from_map(m.get('DataProcessGbps'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class ModifyTransitRouterCapacityReservationsRequestMinimumTransitRouterCapacitiesDataProcessGbps(DaraModel):
    def __init__(
        self,
        target: int = None,
    ):
        # The target reserved capacity for the specified zone.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self

class ModifyTransitRouterCapacityReservationsRequestDeploymentSets(DaraModel):
    def __init__(
        self,
        deployment_set_id: str = None,
        zone_id: str = None,
    ):
        # The ID of the deployment set instance used.
        self.deployment_set_id = deployment_set_id
        # The zone for which to modify the deployment set of the capacity reservation.
        # 
        # - To cancel the deployment set, specify the zone and leave the deployment set ID empty.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_set_id is not None:
            result['DeploymentSetID'] = self.deployment_set_id

        if self.zone_id is not None:
            result['ZoneID'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentSetID') is not None:
            self.deployment_set_id = m.get('DeploymentSetID')

        if m.get('ZoneID') is not None:
            self.zone_id = m.get('ZoneID')

        return self

