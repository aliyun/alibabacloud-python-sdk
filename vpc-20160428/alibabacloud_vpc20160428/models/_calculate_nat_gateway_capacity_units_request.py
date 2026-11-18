# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class CalculateNatGatewayCapacityUnitsRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: str = None,
        nat_gateway_capacity: main_models.CalculateNatGatewayCapacityUnitsRequestNatGatewayCapacity = None,
        nat_gateway_id: str = None,
        nat_gateway_performance_values: main_models.CalculateNatGatewayCapacityUnitsRequestNatGatewayPerformanceValues = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. Note: If you do not specify this parameter, the system automatically uses the RequestId of the API request as the ClientToken. The RequestId of each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # - true: sends the request without upgrading the Internet NAT gateway. The system checks whether your AccessKey pair is valid, the authorization of the Resource Access Management (RAM) user, and whether the required parameters are specified. If the request fails the check, an error message is returned. If the request passes the check, the DryRunOperation error code is returned.
        # - false (default value): sends a normal request. If the request passes the check, a 2xx HTTP status code is returned and the Internet NAT gateway is directly upgraded.
        self.dry_run = dry_run
        # The details of the reserved capacity units (CUs) to be calculated.
        self.nat_gateway_capacity = nat_gateway_capacity
        # The instance ID of the NAT gateway.
        self.nat_gateway_id = nat_gateway_id
        # The details of the resource reservation metrics to be calculated.
        self.nat_gateway_performance_values = nat_gateway_performance_values
        # The region ID of the NAT gateway.
        self.region_id = region_id

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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.nat_gateway_capacity is not None:
            result['NatGatewayCapacity'] = self.nat_gateway_capacity.to_map()

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_performance_values is not None:
            result['NatGatewayPerformanceValues'] = self.nat_gateway_performance_values.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('NatGatewayCapacity') is not None:
            temp_model = main_models.CalculateNatGatewayCapacityUnitsRequestNatGatewayCapacity()
            self.nat_gateway_capacity = temp_model.from_map(m.get('NatGatewayCapacity'))

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayPerformanceValues') is not None:
            temp_model = main_models.CalculateNatGatewayCapacityUnitsRequestNatGatewayPerformanceValues()
            self.nat_gateway_performance_values = temp_model.from_map(m.get('NatGatewayPerformanceValues'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CalculateNatGatewayCapacityUnitsRequestNatGatewayPerformanceValues(DaraModel):
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

class CalculateNatGatewayCapacityUnitsRequestNatGatewayCapacity(DaraModel):
    def __init__(
        self,
        capacity_units: int = None,
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

