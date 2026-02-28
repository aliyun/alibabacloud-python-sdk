# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListErRouteMapsRequest(DaraModel):
    def __init__(
        self,
        destination_cidr_block: str = None,
        enable_page: bool = None,
        er_id: str = None,
        er_route_map_id: str = None,
        er_route_map_num: int = None,
        page_number: int = None,
        page_size: int = None,
        reception_instance_id: str = None,
        reception_instance_name: str = None,
        reception_instance_type: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        route_map_action: str = None,
        transmission_instance_id: str = None,
        transmission_instance_name: str = None,
        transmission_instance_type: str = None,
    ):
        # Destination CIDR Block
        self.destination_cidr_block = destination_cidr_block
        # Specifies whether to enable paged query.
        self.enable_page = enable_page
        # Elastic Router ID
        # 
        # This parameter is required.
        self.er_id = er_id
        # routing policy ID
        self.er_route_map_id = er_route_map_id
        # Policy number (default for automatic creation is 3000; The value range of the policy number manually created by the user is 1001-2000)
        self.er_route_map_num = er_route_map_num
        # The page number of the page to return. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10.
        self.page_size = page_size
        # Receive Instance ID
        self.reception_instance_id = reception_instance_id
        # Receive Instance Name
        self.reception_instance_name = reception_instance_name
        # The type of the received instance. Optional values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.reception_instance_type = reception_instance_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Resource group instance ID
        self.resource_group_id = resource_group_id
        # Policy behavior; optional values:
        # 
        # *   **permit**: Allow
        # *   **deny**: Rejected
        self.route_map_action = route_map_action
        # Release Instance ID
        self.transmission_instance_id = transmission_instance_id
        # Release Instance Name
        self.transmission_instance_name = transmission_instance_name
        # The type of the published instance. Optional values:
        # 
        # *   **VPD**: Lingjun network segment.
        # *   **VCC**: Lingjun Connection.
        self.transmission_instance_type = transmission_instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.destination_cidr_block is not None:
            result['DestinationCidrBlock'] = self.destination_cidr_block

        if self.enable_page is not None:
            result['EnablePage'] = self.enable_page

        if self.er_id is not None:
            result['ErId'] = self.er_id

        if self.er_route_map_id is not None:
            result['ErRouteMapId'] = self.er_route_map_id

        if self.er_route_map_num is not None:
            result['ErRouteMapNum'] = self.er_route_map_num

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.reception_instance_id is not None:
            result['ReceptionInstanceId'] = self.reception_instance_id

        if self.reception_instance_name is not None:
            result['ReceptionInstanceName'] = self.reception_instance_name

        if self.reception_instance_type is not None:
            result['ReceptionInstanceType'] = self.reception_instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.route_map_action is not None:
            result['RouteMapAction'] = self.route_map_action

        if self.transmission_instance_id is not None:
            result['TransmissionInstanceId'] = self.transmission_instance_id

        if self.transmission_instance_name is not None:
            result['TransmissionInstanceName'] = self.transmission_instance_name

        if self.transmission_instance_type is not None:
            result['TransmissionInstanceType'] = self.transmission_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DestinationCidrBlock') is not None:
            self.destination_cidr_block = m.get('DestinationCidrBlock')

        if m.get('EnablePage') is not None:
            self.enable_page = m.get('EnablePage')

        if m.get('ErId') is not None:
            self.er_id = m.get('ErId')

        if m.get('ErRouteMapId') is not None:
            self.er_route_map_id = m.get('ErRouteMapId')

        if m.get('ErRouteMapNum') is not None:
            self.er_route_map_num = m.get('ErRouteMapNum')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ReceptionInstanceId') is not None:
            self.reception_instance_id = m.get('ReceptionInstanceId')

        if m.get('ReceptionInstanceName') is not None:
            self.reception_instance_name = m.get('ReceptionInstanceName')

        if m.get('ReceptionInstanceType') is not None:
            self.reception_instance_type = m.get('ReceptionInstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RouteMapAction') is not None:
            self.route_map_action = m.get('RouteMapAction')

        if m.get('TransmissionInstanceId') is not None:
            self.transmission_instance_id = m.get('TransmissionInstanceId')

        if m.get('TransmissionInstanceName') is not None:
            self.transmission_instance_name = m.get('TransmissionInstanceName')

        if m.get('TransmissionInstanceType') is not None:
            self.transmission_instance_type = m.get('TransmissionInstanceType')

        return self

