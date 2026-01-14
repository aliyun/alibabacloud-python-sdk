# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeIpSetResponseBody(DaraModel):
    def __init__(
        self,
        accelerate_region_id: str = None,
        accelerator_id: str = None,
        bandwidth: int = None,
        ip_address_list: List[str] = None,
        ip_set_id: str = None,
        ip_version: str = None,
        isp_type: str = None,
        request_id: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.DescribeIpSetResponseBodyServiceManagedInfos] = None,
        state: str = None,
    ):
        # The ID of the acceleration region.
        self.accelerate_region_id = accelerate_region_id
        # The ID of the GA instance.
        self.accelerator_id = accelerator_id
        # The bandwidth that is allocated to the acceleration region. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The list of accelerated IP addresses in the acceleration region.
        self.ip_address_list = ip_address_list
        # The ID of the acceleration region.
        self.ip_set_id = ip_set_id
        # The IP version. Valid values:
        # 
        # *   **IPv4**
        # *   **IPv6**
        # *   **DUAL_STACK**
        self.ip_version = ip_version
        # The line type of the elastic IP address (EIP) in the acceleration region. Valid values:
        # 
        # *   **BGP**: BGP (Multi-ISP) lines. This is the default value.
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro lines.
        self.isp_type = isp_type
        # The ID of the request.
        self.request_id = request_id
        # The ID of the service that manages the instance.
        # 
        # >  This parameter is returned only if the value of **ServiceManaged** is **true**.
        self.service_id = service_id
        # Indicates whether the GA instance is managed. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.service_managed = service_managed
        # The actions that users can perform on the managed instance.
        # 
        # > *   This parameter is returned only if the value of **ServiceManaged** is **true**.
        # >*   Users can perform only specific actions on a managed instance.
        self.service_managed_infos = service_managed_infos
        # The status of the acceleration region. Valid values:
        # 
        # *   **init**: The acceleration region is being initialized.
        # *   **active**: The acceleration region is in the running state.
        # *   **updating**: The acceleration region is being configured.
        # *   **deleting**: The GA instance is being deleted.
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
        if self.accelerate_region_id is not None:
            result['AccelerateRegionId'] = self.accelerate_region_id

        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.ip_address_list is not None:
            result['IpAddressList'] = self.ip_address_list

        if self.ip_set_id is not None:
            result['IpSetId'] = self.ip_set_id

        if self.ip_version is not None:
            result['IpVersion'] = self.ip_version

        if self.isp_type is not None:
            result['IspType'] = self.isp_type

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerateRegionId') is not None:
            self.accelerate_region_id = m.get('AccelerateRegionId')

        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('IpAddressList') is not None:
            self.ip_address_list = m.get('IpAddressList')

        if m.get('IpSetId') is not None:
            self.ip_set_id = m.get('IpSetId')

        if m.get('IpVersion') is not None:
            self.ip_version = m.get('IpVersion')

        if m.get('IspType') is not None:
            self.isp_type = m.get('IspType')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.DescribeIpSetResponseBodyServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeIpSetResponseBodyServiceManagedInfos(DaraModel):
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
        # Indicates whether the specified actions are managed.
        # 
        # *   **true**: The specified actions are managed, and users cannot perform the actions on the managed instance.
        # *   **false**: The specified actions are not managed, and users can perform the actions on the managed instance.
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

