# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListCustomRoutingEndpointGroupDestinationsResponseBody(DaraModel):
    def __init__(
        self,
        destinations: List[main_models.ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The details about the endpoint group mappings.
        self.destinations = destinations
        # The number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.destinations:
            for v1 in self.destinations:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Destinations'] = []
        if self.destinations is not None:
            for k1 in self.destinations:
                result['Destinations'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.destinations = []
        if m.get('Destinations') is not None:
            for k1 in m.get('Destinations'):
                temp_model = main_models.ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations()
                self.destinations.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinations(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        destination_id: str = None,
        endpoint_group_id: str = None,
        from_port: int = None,
        listener_id: str = None,
        protocols: List[str] = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinationsServiceManagedInfos] = None,
        to_port: int = None,
    ):
        # The GA instance ID.
        self.accelerator_id = accelerator_id
        # The ID of the endpoint group mapping.
        self.destination_id = destination_id
        # The endpoint group ID.
        self.endpoint_group_id = endpoint_group_id
        # The first port of the backend service port range.
        self.from_port = from_port
        # The listener ID.
        self.listener_id = listener_id
        # The backend service protocols of the endpoint group. Valid values:
        # 
        # *   **TCP**
        # *   **UDP**
        # *   **TCP,UDP**
        self.protocols = protocols
        # The ID of the service that manages the GA instance.
        # 
        # >  This parameter takes effect only if **ServiceManaged** is set to **True**.
        self.service_id = service_id
        # Indicates whether the GA instance is managed. Valid values:
        # 
        # *   true
        # *   false
        self.service_managed = service_managed
        # The actions that you can perform on the managed instance.
        # 
        # >  - This parameter takes effect only if **ServiceManaged** is set to **True**.
        # >  - You can perform only specific actions on the managed instance.
        self.service_managed_infos = service_managed_infos
        # The last port of the backend service port range.
        self.to_port = to_port

    def validate(self):
        if self.service_managed_infos:
            for v1 in self.service_managed_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.destination_id is not None:
            result['DestinationId'] = self.destination_id

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.from_port is not None:
            result['FromPort'] = self.from_port

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.protocols is not None:
            result['Protocols'] = self.protocols

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        result['ServiceManagedInfos'] = []
        if self.service_managed_infos is not None:
            for k1 in self.service_managed_infos:
                result['ServiceManagedInfos'].append(k1.to_map() if k1 else None)

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('DestinationId') is not None:
            self.destination_id = m.get('DestinationId')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('Protocols') is not None:
            self.protocols = m.get('Protocols')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinationsServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

class ListCustomRoutingEndpointGroupDestinationsResponseBodyDestinationsServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the action that you can perform on the managed instance. Valid values:
        # 
        # *   **Create**: Create an instance.
        # *   **Update**: Update the current instance.
        # *   **Delete**: Delete the current instance.
        # *   **Associate**: Reference the current instance.
        # *   **UserUnmanaged**: Unmanage the instance.
        # *   **CreateChild**: Create a child resource in the current instance.
        self.action = action
        # The type of the child resource. Valid values:
        # 
        # *   **Listener**: listener.
        # *   **IpSet**: acceleration region.
        # *   **EndpointGroup**: endpoint group.
        # *   **ForwardingRule**: forwarding rule.
        # *   **Endpoint**: endpoint.
        # *   **EndpointGroupDestination**: protocol mapping of an endpoint group associated with a custom routing listener.
        # *   **EndpointPolicy**: traffic policy of an endpoint associated with a custom routing listener.
        # 
        # >  This parameter takes effect only if **Action** is set to **CreateChild**.
        self.child_type = child_type
        # Indicates whether the specified actions are managed. Valid values:
        # 
        # *   **true**: The specified actions are managed, and you cannot perform the specified actions on the managed instance.
        # *   **false**: The specified actions are not managed, and you can perform the specified actions on the managed instance.
        self.is_managed = is_managed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.child_type is not None:
            result['ChildType'] = self.child_type

        if self.is_managed is not None:
            result['IsManaged'] = self.is_managed

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ChildType') is not None:
            self.child_type = m.get('ChildType')

        if m.get('IsManaged') is not None:
            self.is_managed = m.get('IsManaged')

        return self

