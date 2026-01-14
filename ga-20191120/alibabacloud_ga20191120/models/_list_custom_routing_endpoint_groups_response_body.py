# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListCustomRoutingEndpointGroupsResponseBody(DaraModel):
    def __init__(
        self,
        endpoint_groups: List[main_models.ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The configuration information about the endpoint group.
        self.endpoint_groups = endpoint_groups
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.endpoint_groups:
            for v1 in self.endpoint_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EndpointGroups'] = []
        if self.endpoint_groups is not None:
            for k1 in self.endpoint_groups:
                result['EndpointGroups'].append(k1.to_map() if k1 else None)

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
        self.endpoint_groups = []
        if m.get('EndpointGroups') is not None:
            for k1 in m.get('EndpointGroups'):
                temp_model = main_models.ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups()
                self.endpoint_groups.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCustomRoutingEndpointGroupsResponseBodyEndpointGroups(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        description: str = None,
        endpoint_group_id: str = None,
        endpoint_group_ip_list: List[str] = None,
        endpoint_group_region: str = None,
        endpoint_group_unconfirmed_ip_list: List[str] = None,
        listener_id: str = None,
        name: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.ListCustomRoutingEndpointGroupsResponseBodyEndpointGroupsServiceManagedInfos] = None,
        state: str = None,
    ):
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        # The description of the endpoint group.
        self.description = description
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # The endpoint group IP addresses.
        self.endpoint_group_ip_list = endpoint_group_ip_list
        # The ID of the region where the endpoint group is created.
        self.endpoint_group_region = endpoint_group_region
        # The endpoint group IP addresses to be confirmed after the GA instance is upgraded.
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list
        # The ID of the custom routing listener.
        self.listener_id = listener_id
        # The name of the endpoint group.
        self.name = name
        # The ID of the service that manages the instance.
        # 
        # >  This parameter takes effect only if **ServiceManaged** is set to **True**.
        self.service_id = service_id
        # Indicates whether the GA instance is managed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.service_managed = service_managed
        # The actions that users can perform on the managed instance.
        # 
        # > 
        # 
        # *   This parameter takes effect only if **ServiceManaged** is set to **True**.
        # 
        # *   Users can perform only specific actions on a managed instance.
        self.service_managed_infos = service_managed_infos
        # The status of the endpoint group. Valid values:
        # 
        # *   **init**
        # *   **active**
        # *   **updating**
        # *   **deleting**
        self.state = state

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

        if self.description is not None:
            result['Description'] = self.description

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.name is not None:
            result['Name'] = self.name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.ListCustomRoutingEndpointGroupsResponseBodyEndpointGroupsServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class ListCustomRoutingEndpointGroupsResponseBodyEndpointGroupsServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the action on the managed instance. Valid values:
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
        # >  This parameter takes effect only if **Action** is set to **CreateChild**.
        self.child_type = child_type
        # Indicates whether the specified actions are managed.
        # 
        # *   **true**: Users cannot perform the specified actions on the managed instance.
        # *   **false**: Users can perform the specified actions on the managed instance.
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

