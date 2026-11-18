# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyNatGatewayCapacityReservationShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: str = None,
        nat_gateway_capacity_shrink: str = None,
        nat_gateway_id: str = None,
        region_id: str = None,
        reset_capacity_reservation: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must make sure that it is unique among different requests. The client token can contain only ASCII characters. Note: If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run on the request. Valid values:
        # - true: Performs a dry run without upgrading the Internet NAT gateway. The system checks whether your AccessKey pair is valid, the authorization of the Resource Access Management (RAM) user, and whether the required parameters are specified. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # - false (default): Sends a Normal request. If the request passes the dry run, a 2xx HTTP status code is returned and the Internet NAT gateway is upgraded.
        self.dry_run = dry_run
        # The number of capacity units (CUs) for the NAT resource reservation.
        self.nat_gateway_capacity_shrink = nat_gateway_capacity_shrink
        # The instance ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The region ID of the NAT gateway.
        self.region_id = region_id
        # Specifies whether to cancel the resource reservation. Valid values:
        # - **true**: Cancels the resource reservation.
        # - **false** (default): Does not cancel the resource reservation. You do not need to specify this parameter when you create or modify a resource reservation.
        self.reset_capacity_reservation = reset_capacity_reservation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.nat_gateway_capacity_shrink is not None:
            result['NatGatewayCapacity'] = self.nat_gateway_capacity_shrink

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reset_capacity_reservation is not None:
            result['ResetCapacityReservation'] = self.reset_capacity_reservation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NatGatewayCapacity') is not None:
            self.nat_gateway_capacity_shrink = m.get('NatGatewayCapacity')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResetCapacityReservation') is not None:
            self.reset_capacity_reservation = m.get('ResetCapacityReservation')

        return self

