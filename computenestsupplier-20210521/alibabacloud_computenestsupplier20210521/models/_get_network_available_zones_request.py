# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNetworkAvailableZonesRequest(DaraModel):
    def __init__(
        self,
        is_poc: bool = None,
        network_region_id: str = None,
        private_vpc_connection_mode: str = None,
        service_id: str = None,
        service_instance_endpoint_service_type: str = None,
        service_region_id: str = None,
        service_version: str = None,
        zone_id: str = None,
    ):
        self.is_poc = is_poc
        self.network_region_id = network_region_id
        self.private_vpc_connection_mode = private_vpc_connection_mode
        self.service_id = service_id
        self.service_instance_endpoint_service_type = service_instance_endpoint_service_type
        self.service_region_id = service_region_id
        self.service_version = service_version
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_poc is not None:
            result['IsPoc'] = self.is_poc

        if self.network_region_id is not None:
            result['NetworkRegionId'] = self.network_region_id

        if self.private_vpc_connection_mode is not None:
            result['PrivateVpcConnectionMode'] = self.private_vpc_connection_mode

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_instance_endpoint_service_type is not None:
            result['ServiceInstanceEndpointServiceType'] = self.service_instance_endpoint_service_type

        if self.service_region_id is not None:
            result['ServiceRegionId'] = self.service_region_id

        if self.service_version is not None:
            result['ServiceVersion'] = self.service_version

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPoc') is not None:
            self.is_poc = m.get('IsPoc')

        if m.get('NetworkRegionId') is not None:
            self.network_region_id = m.get('NetworkRegionId')

        if m.get('PrivateVpcConnectionMode') is not None:
            self.private_vpc_connection_mode = m.get('PrivateVpcConnectionMode')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceInstanceEndpointServiceType') is not None:
            self.service_instance_endpoint_service_type = m.get('ServiceInstanceEndpointServiceType')

        if m.get('ServiceRegionId') is not None:
            self.service_region_id = m.get('ServiceRegionId')

        if m.get('ServiceVersion') is not None:
            self.service_version = m.get('ServiceVersion')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

