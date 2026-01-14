# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomRoutingEndpointGroupDestinationsResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        destination_id: str = None,
        endpoint_group_id: str = None,
        from_port: int = None,
        listener_id: str = None,
        protocols: List[str] = None,
        request_id: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.DescribeCustomRoutingEndpointGroupDestinationsResponseBodyServiceManagedInfos] = None,
        state: str = None,
        to_port: int = None,
    ):
        # The ID of the Global Accelerator (GA) instance.
        self.accelerator_id = accelerator_id
        # The ID of the endpoint group mapping configuration.
        self.destination_id = destination_id
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The start port of the backend service port range of the endpoint group.
        self.from_port = from_port
        # The ID of the listener.
        self.listener_id = listener_id
        # The backend service protocol of the endpoint group.
        # 
        # *   **TCP**: TCP
        # *   **UDP**: UDP
        # *   **TCP,UDP**: TCP and UDP
        self.protocols = protocols
        # The ID of the request.
        self.request_id = request_id
        # The service ID to which the managed instance belongs.
        # 
        # >  Valid only when the ServiceManaged parameter is True.
        self.service_id = service_id
        # Is it a managed instance. Valid values:
        # 
        # - true
        # - false
        self.service_managed = service_managed
        # A list of action policies that users can execute on this managed instance.
        self.service_managed_infos = service_managed_infos
        # The status of the endpoint group mapping configuration.
        # 
        # *   **init**: being initialized.
        # *   **active**: normal.
        # *   **updating**: being updated.
        # *   **deleting**: being deleted.
        self.state = state
        # The end port of the backend service port range of the endpoint group.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        result['ServiceManagedInfos'] = []
        if self.service_managed_infos is not None:
            for k1 in self.service_managed_infos:
                result['ServiceManagedInfos'].append(k1.to_map() if k1 else None)

        if self.state is not None:
            result['State'] = self.state

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.DescribeCustomRoutingEndpointGroupDestinationsResponseBodyServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

class DescribeCustomRoutingEndpointGroupDestinationsResponseBodyServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # Managed policy action name, Valid values:
        # 
        # - Create
        # - Update
        # - Delete
        # - Associate
        # - UserUnmanaged
        # - CreateChild
        self.action = action
        # Sub resource type, Valid values:
        # 
        # - Listener
        # - IpSet
        # - EndpointGroup
        # - ForwardingRule
        # - Endpoint
        # - EndpointGroupDestination
        # - EndpointPolicy
        # 
        # >Only valid when the Action parameter is CreateChild.
        self.child_type = child_type
        # Is the managed policy action managed, Valid values:
        # 
        # - true: The managed policy action is managed, and users do not have permission to perform the operation specified in the Action on the managed instance.
        # 
        # - false: The managed policy action is not managed, and users have permission to perform the operation specified in the Action on the managed instance.
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

