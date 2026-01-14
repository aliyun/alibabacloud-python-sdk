# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListCustomRoutingPortMappingsByDestinationResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        port_mappings: List[main_models.ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # Details about the port mapping table.
        self.port_mappings = port_mappings
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.port_mappings:
            for v1 in self.port_mappings:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PortMappings'] = []
        if self.port_mappings is not None:
            for k1 in self.port_mappings:
                result['PortMappings'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.port_mappings = []
        if m.get('PortMappings') is not None:
            for k1 in m.get('PortMappings'):
                temp_model = main_models.ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings()
                self.port_mappings.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappings(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        accelerator_port: int = None,
        destination_socket_address: main_models.ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress = None,
        destination_traffic_state: str = None,
        endpoint_group_id: str = None,
        endpoint_group_region: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        protocols: List[str] = None,
        vswitch: str = None,
    ):
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        # The acceleration port.
        self.accelerator_port = accelerator_port
        # The service IP address and port of the backend instance.
        self.destination_socket_address = destination_socket_address
        # The access policy of traffic for the backend instance.
        # 
        # *   **allow**: allows traffic to the backend instance.
        # *   **deny**: denies all traffic to the backend instance.
        self.destination_traffic_state = destination_traffic_state
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The ID of the region in which the endpoint group resides.
        self.endpoint_group_region = endpoint_group_region
        # The ID of the endpoint.
        self.endpoint_id = endpoint_id
        # The ID of the listener.
        self.listener_id = listener_id
        # The protocol of the backend service.
        # 
        # *   **tcp**: TCP
        # *   **udp**: UDP
        self.protocols = protocols
        # The name of the endpoint (vSwitch).
        self.vswitch = vswitch

    def validate(self):
        if self.destination_socket_address:
            self.destination_socket_address.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.accelerator_port is not None:
            result['AcceleratorPort'] = self.accelerator_port

        if self.destination_socket_address is not None:
            result['DestinationSocketAddress'] = self.destination_socket_address.to_map()

        if self.destination_traffic_state is not None:
            result['DestinationTrafficState'] = self.destination_traffic_state

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AcceleratorPort') is not None:
            self.accelerator_port = m.get('AcceleratorPort')

        if m.get('DestinationSocketAddress') is not None:
            temp_model = main_models.ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress()
            self.destination_socket_address = temp_model.from_map(m.get('DestinationSocketAddress'))

        if m.get('DestinationTrafficState') is not None:
            self.destination_traffic_state = m.get('DestinationTrafficState')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')

        return self

class ListCustomRoutingPortMappingsByDestinationResponseBodyPortMappingsDestinationSocketAddress(DaraModel):
    def __init__(
        self,
        ip_address: str = None,
        port: int = None,
    ):
        # The service IP address of the backend instance.
        self.ip_address = ip_address
        # The service port of the backend instance.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

