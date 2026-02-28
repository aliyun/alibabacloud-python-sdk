# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateErRouteMapRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        destination_cidr_block: str = None,
        er_id: str = None,
        reception_instance_id: str = None,
        reception_instance_owner: str = None,
        reception_instance_type: str = None,
        region_id: str = None,
        route_map_action: str = None,
        route_map_num: int = None,
        transmission_instance_id: str = None,
        transmission_instance_owner: str = None,
        transmission_instance_type: str = None,
    ):
        # Policy description
        self.description = description
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Lingjun HUB ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # The ID of the destination instance.
        # 
        # This parameter is required.
        self.reception_instance_id = reception_instance_id
        # The tenant to which the route receiving instance belongs.
        self.reception_instance_owner = reception_instance_owner
        # The type of the destination instance. Valid values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        # 
        # This parameter is required.
        self.reception_instance_type = reception_instance_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Policy behavior; optional values:
        # 
        # *   **permit**: Allow
        # *   **deny**: Rejected
        # 
        # This parameter is required.
        self.route_map_action = route_map_action
        # The ID of the policy.
        # 
        # A smaller sequence number indicates a lower priority. When a route is matched, a policy with a higher priority is preferentially matched.
        # 
        # **Valid values: 1001 to 2000**
        # 
        # This parameter is required.
        self.route_map_num = route_map_num
        # The ID of the source instance.
        # 
        # This parameter is required.
        self.transmission_instance_id = transmission_instance_id
        # The tenant to which the route publish instance belongs
        self.transmission_instance_owner = transmission_instance_owner
        # The type of the source instance. Valid values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        # 
        # This parameter is required.
        self.transmission_instance_type = transmission_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.reception_instance_id is not None:
            result['ReceptionInstanceId'] = self.reception_instance_id

        if self.reception_instance_owner is not None:
            result['ReceptionInstanceOwner'] = self.reception_instance_owner

        if self.reception_instance_type is not None:
            result['ReceptionInstanceType'] = self.reception_instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.route_map_action is not None:
            result['RouteMapAction'] = self.route_map_action

        if self.route_map_num is not None:
            result['RouteMapNum'] = self.route_map_num

        if self.transmission_instance_id is not None:
            result['TransmissionInstanceId'] = self.transmission_instance_id

        if self.transmission_instance_owner is not None:
            result['TransmissionInstanceOwner'] = self.transmission_instance_owner

        if self.transmission_instance_type is not None:
            result['TransmissionInstanceType'] = self.transmission_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ReceptionInstanceId') is not None:
            self.reception_instance_id = m.get('ReceptionInstanceId')

        if m.get('ReceptionInstanceOwner') is not None:
            self.reception_instance_owner = m.get('ReceptionInstanceOwner')

        if m.get('ReceptionInstanceType') is not None:
            self.reception_instance_type = m.get('ReceptionInstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RouteMapAction') is not None:
            self.route_map_action = m.get('RouteMapAction')

        if m.get('RouteMapNum') is not None:
            self.route_map_num = m.get('RouteMapNum')

        if m.get('TransmissionInstanceId') is not None:
            self.transmission_instance_id = m.get('TransmissionInstanceId')

        if m.get('TransmissionInstanceOwner') is not None:
            self.transmission_instance_owner = m.get('TransmissionInstanceOwner')

        if m.get('TransmissionInstanceType') is not None:
            self.transmission_instance_type = m.get('TransmissionInstanceType')

        return self

