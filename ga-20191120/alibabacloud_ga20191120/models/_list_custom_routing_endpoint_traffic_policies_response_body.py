# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListCustomRoutingEndpointTrafficPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        policies: List[main_models.ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the list.
        self.page_number = page_number
        # The number of entries per page in a paging query.
        self.page_size = page_size
        # The list of traffic policies.
        self.policies = policies
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.policies:
            for v1 in self.policies:
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

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

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

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomRoutingEndpointTrafficPoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        address: str = None,
        endpoint_group_id: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        policy_id: str = None,
        port_ranges: List[main_models.ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges] = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesServiceManagedInfos] = None,
    ):
        # The instance ID of the Alibaba Cloud Global Accelerator (GA) instance to which the endpoint belongs.
        self.accelerator_id = accelerator_id
        # The IP address of the traffic policy destination.
        self.address = address
        # The ID of the endpoint group to which the endpoint belongs.
        self.endpoint_group_id = endpoint_group_id
        # The ID of the endpoint to which the traffic policy belongs.
        self.endpoint_id = endpoint_id
        # The ID of the custom routing type listener to which the endpoint belongs.
        self.listener_id = listener_id
        # The traffic policy ID.
        self.policy_id = policy_id
        # The port range of the traffic policy destination.
        self.port_ranges = port_ranges
        # The ID of the service to which the managed instance belongs.
        # > This parameter is valid only when **ServiceManaged** is set to **True**.
        self.service_id = service_id
        # Indicates whether the instance is managed. Valid values:
        # - **true**: The instance is managed.
        # - **false**: The instance is not managed.
        self.service_managed = service_managed
        # The list of action policies that the user can perform on the managed instance.
        # 
        # > - This parameter is valid only when **ServiceManaged** is set to **True**.
        # > - When the instance is in the managed state, user operations on the instance are restricted, and certain operations are prohibited.
        self.service_managed_infos = service_managed_infos

    def validate(self):
        if self.port_ranges:
            for v1 in self.port_ranges:
                 if v1:
                    v1.validate()
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

        if self.address is not None:
            result['Address'] = self.address

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        result['PortRanges'] = []
        if self.port_ranges is not None:
            for k1 in self.port_ranges:
                result['PortRanges'].append(k1.to_map() if k1 else None)

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        result['ServiceManagedInfos'] = []
        if self.service_managed_infos is not None:
            for k1 in self.service_managed_infos:
                result['ServiceManagedInfos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        self.port_ranges = []
        if m.get('PortRanges') is not None:
            for k1 in m.get('PortRanges'):
                temp_model = main_models.ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges()
                self.port_ranges.append(temp_model.from_map(k1))

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        return self

class ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the managed policy action. Valid values:
        # - **Create**: Create an instance.
        # - **Update**: Update the current instance.
        # - **Delete**: Delete the current instance.
        # - **Associate**: Reference or be referenced by the current instance.
        # - **UserUnmanaged**: Unmanage the instance.
        # - **CreateChild**: Create a child resource under the current instance.
        self.action = action
        # The type of the child resource. Valid values:
        # 
        # - **Listener**: listener resource.
        # 
        # - **IpSet**: acceleration region resource.
        # 
        # - **EndpointGroup**: endpoint group resource.
        # 
        # - **ForwardingRule**: forwarding rule resource.
        # 
        # - **Endpoint**: endpoint resource.
        # 
        # - **EndpointGroupDestination**: protocol mapping resource of the endpoint group under the custom routing listener.
        # 
        # - **EndpointPolicy**: traffic policy resource of the endpoint under the custom routing listener.
        # 
        # > This parameter is valid only when **Action** is set to **CreateChild**.
        self.child_type = child_type
        # Indicates whether the managed policy action is managed. Valid values:
        # 
        # - **true**: The managed policy action is managed. The user cannot perform the action specified by Action on the managed instance.
        # 
        # - **false**: The managed policy action is not managed. The user can perform the action specified by Action on the managed instance.
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

class ListCustomRoutingEndpointTrafficPoliciesResponseBodyPoliciesPortRanges(DaraModel):
    def __init__(
        self,
        from_port: int = None,
        to_port: int = None,
    ):
        # The start port of the traffic policy destination for processing requests.
        self.from_port = from_port
        # The end port of the traffic policy destination for processing requests.
        self.to_port = to_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_port is not None:
            result['FromPort'] = self.from_port

        if self.to_port is not None:
            result['ToPort'] = self.to_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromPort') is not None:
            self.from_port = m.get('FromPort')

        if m.get('ToPort') is not None:
            self.to_port = m.get('ToPort')

        return self

