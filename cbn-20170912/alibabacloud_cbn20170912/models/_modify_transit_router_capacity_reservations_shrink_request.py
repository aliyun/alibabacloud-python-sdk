# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyTransitRouterCapacityReservationsShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        deployment_sets_shrink: str = None,
        minimum_transit_router_capacities_shrink: str = None,
        reset_capacity_reservations_shrink: str = None,
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
        self.deployment_sets_shrink = deployment_sets_shrink
        # The reserved capacity for each zone in the capacity reservation.
        self.minimum_transit_router_capacities_shrink = minimum_transit_router_capacities_shrink
        # Cancels capacity reservations.
        self.reset_capacity_reservations_shrink = reset_capacity_reservations_shrink
        # The ID of the transit router instance for forward routing.
        # 
        # This parameter is required.
        self.transit_router_id = transit_router_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.deployment_sets_shrink is not None:
            result['DeploymentSets'] = self.deployment_sets_shrink

        if self.minimum_transit_router_capacities_shrink is not None:
            result['MinimumTransitRouterCapacities'] = self.minimum_transit_router_capacities_shrink

        if self.reset_capacity_reservations_shrink is not None:
            result['ResetCapacityReservations'] = self.reset_capacity_reservations_shrink

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeploymentSets') is not None:
            self.deployment_sets_shrink = m.get('DeploymentSets')

        if m.get('MinimumTransitRouterCapacities') is not None:
            self.minimum_transit_router_capacities_shrink = m.get('MinimumTransitRouterCapacities')

        if m.get('ResetCapacityReservations') is not None:
            self.reset_capacity_reservations_shrink = m.get('ResetCapacityReservations')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

