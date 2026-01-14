# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListDomainsResponseBody(DaraModel):
    def __init__(
        self,
        domains: List[main_models.ListDomainsResponseBodyDomains] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # A list of accelerated domain names.
        self.domains = domains
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.domains:
            for v1 in self.domains:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Domains'] = []
        if self.domains is not None:
            for k1 in self.domains:
                result['Domains'].append(k1.to_map() if k1 else None)

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
        self.domains = []
        if m.get('Domains') is not None:
            for k1 in m.get('Domains'):
                temp_model = main_models.ListDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDomainsResponseBodyDomains(DaraModel):
    def __init__(
        self,
        accelerators: List[main_models.ListDomainsResponseBodyDomainsAccelerators] = None,
        domain: str = None,
        state: str = None,
    ):
        # A list of GA instances.
        self.accelerators = accelerators
        # The accelerated domain name.
        self.domain = domain
        # The ICP filing status of the accelerated domain name. Valid values:
        # 
        # *   **illegal:** The domain name is illegal.
        # *   **inactive:** The domain name has not completed ICP filing.
        # *   **active:** The domain name has a valid ICP number.
        # *   **unknown:** The ICP filing status is unknown.
        self.state = state

    def validate(self):
        if self.accelerators:
            for v1 in self.accelerators:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Accelerators'] = []
        if self.accelerators is not None:
            for k1 in self.accelerators:
                result['Accelerators'].append(k1.to_map() if k1 else None)

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.accelerators = []
        if m.get('Accelerators') is not None:
            for k1 in m.get('Accelerators'):
                temp_model = main_models.ListDomainsResponseBodyDomainsAccelerators()
                self.accelerators.append(temp_model.from_map(k1))

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class ListDomainsResponseBodyDomainsAccelerators(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        name: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.ListDomainsResponseBodyDomainsAcceleratorsServiceManagedInfos] = None,
    ):
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        # The name of the GA instance.
        self.name = name
        # The ID of the service that manages the GA instance.
        # 
        # >  This parameter takes effect only if **ServiceManaged** is set to **True**.
        self.service_id = service_id
        # Indicates whether the GA instance is managed. Valid values:
        # 
        # *   **true**: The GA instance is managed.
        # *   **false**: The GA instance is not managed.
        self.service_managed = service_managed
        # The actions that you can perform on the managed instance.
        # 
        # >  This parameter takes effect only if **ServiceManaged** is set to **True**.
        # 
        # *   You can perform only specific actions on a managed instance.
        self.service_managed_infos = service_managed_infos

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.ListDomainsResponseBodyDomainsAcceleratorsServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        return self

class ListDomainsResponseBodyDomainsAcceleratorsServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the action on the managed instance. Valid values:
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

