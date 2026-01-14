# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListCustomRoutingEndpointsResponseBody(DaraModel):
    def __init__(
        self,
        endpoints: List[main_models.ListCustomRoutingEndpointsResponseBodyEndpoints] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the endpoints.
        self.endpoints = endpoints
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.endpoints:
            for v1 in self.endpoints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k1 in self.endpoints:
                result['Endpoints'].append(k1.to_map() if k1 else None)

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
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k1 in m.get('Endpoints'):
                temp_model = main_models.ListCustomRoutingEndpointsResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomRoutingEndpointsResponseBodyEndpoints(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        endpoint: str = None,
        endpoint_group_id: str = None,
        endpoint_id: str = None,
        listener_id: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.ListCustomRoutingEndpointsResponseBodyEndpointsServiceManagedInfos] = None,
        traffic_to_endpoint_policy: str = None,
        type: str = None,
    ):
        # The ID of the GA instance with which the endpoint is associated.
        self.accelerator_id = accelerator_id
        # The name of the vSwitch that is specified as an endpoint.
        self.endpoint = endpoint
        # The ID of the endpoint group to which the endpoint belongs.
        self.endpoint_group_id = endpoint_group_id
        # The endpoint ID.
        self.endpoint_id = endpoint_id
        # The ID of the listener to which the endpoint belongs.
        self.listener_id = listener_id
        # The ID of the service that manages the GA instance.
        # 
        # >  This parameter is valid only if **ServiceManaged** is set to **True**.
        self.service_id = service_id
        # Indicates whether the GA instance is managed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.service_managed = service_managed
        # The actions that users can perform on the managed instance.
        # 
        # >  This parameter is valid only if **ServiceManaged** is set to **True**.
        # 
        # *   Users can perform only specific actions on a managed instance.
        self.service_managed_infos = service_managed_infos
        # The access policy of traffic that is destined for the endpoint. Valid values:
        # 
        # *   **AllowAll**: allows all traffic to the endpoint.
        # *   **DenyAll**: denies all traffic to the endpoint.
        # *   **AllowCustom**: allows traffic only to specified destinations.
        self.traffic_to_endpoint_policy = traffic_to_endpoint_policy
        # The backend service type of the endpoint.
        # 
        # Only **PrivateSubNet** may be returned, which indicates a private CIDR block.
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

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_managed is not None:
            result['ServiceManaged'] = self.service_managed

        result['ServiceManagedInfos'] = []
        if self.service_managed_infos is not None:
            for k1 in self.service_managed_infos:
                result['ServiceManagedInfos'].append(k1.to_map() if k1 else None)

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

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.ListCustomRoutingEndpointsResponseBodyEndpointsServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('TrafficToEndpointPolicy') is not None:
            self.traffic_to_endpoint_policy = m.get('TrafficToEndpointPolicy')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListCustomRoutingEndpointsResponseBodyEndpointsServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the action performed on the managed instance. Valid values:
        # 
        # *   **Create**
        # *   **Update**
        # *   **Delete**
        # *   **Associate**
        # *   **UserUnmanaged**
        # *   **CreateChild**
        self.action = action
        # The type of the child resource. Valid values:
        # 
        # *   **Listener**: listener
        # *   **IpSet**: acceleration region
        # *   **EndpointGroup**: endpoint group
        # *   **ForwardingRule**: forwarding rule
        # *   **Endpoint**: endpoint
        # *   **EndpointGroupDestination**: protocol mapping of an endpoint group associated with a custom routing listener
        # *   **EndpointPolicy**: traffic policy of an endpoint associated with a custom routing listener
        # 
        # >  This parameter is valid only if **Action** is set to **CreateChild**.
        self.child_type = child_type
        # Indicates whether the specified actions are managed. Valid values:
        # 
        # *   **true**: The specified actions are managed, and users cannot perform the specified actions on the managed resource.
        # *   **false**: The specified actions are not managed, and users can perform the specified actions on the managed resource.
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

