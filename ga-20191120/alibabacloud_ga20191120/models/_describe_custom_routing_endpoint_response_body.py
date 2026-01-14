# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomRoutingEndpointResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        endpoint: str = None,
        endpoint_group_id: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        request_id: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.DescribeCustomRoutingEndpointResponseBodyServiceManagedInfos] = None,
        state: str = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        # The ID of the GA instance with which the endpoint is associated.
        self.accelerator_id = accelerator_id
        # The name of the endpoint (vSwitch).
        self.endpoint = endpoint
        # The ID of the endpoint group to which the endpoint belongs.
        self.endpoint_group_id = endpoint_group_id
        # The ID of the endpoint.
        self.endpoint_id = endpoint_id
        # The ID of the listener with which the endpoint is associated.
        self.listener_id = listener_id
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
        # The status of the endpoint.
        self.state = state
        # The access policy of traffic for the specified endpoint. Valid values:
        # 
        # *   **AllowAll**: allows all traffic to the endpoint.
        # *   **DenyAll**: denies all traffic to the endpoint.
        # *   **AllowCustom**: allows traffic only to specified destinations.
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        # The backend service type of the endpoint.
        # 
        # Set the value to **PrivateSubNet**, which indicates private CIDR blocks.
        self.type = type

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

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

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

        if self.traffic_to_endpoint_policy is not None:
            result['TrafficToEndpointPolicy'] = self.traffic_to_endpoint_policy

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.DescribeCustomRoutingEndpointResponseBodyServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeCustomRoutingEndpointResponseBodyServiceManagedInfos(DaraModel):
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

