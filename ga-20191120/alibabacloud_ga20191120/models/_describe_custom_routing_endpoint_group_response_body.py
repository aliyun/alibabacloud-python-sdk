# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeCustomRoutingEndpointGroupResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_log_switch: str = None,
        description: str = None,
        enable_access_log: bool = None,
        endpoint_group_id: str = None,
        endpoint_group_ip_list: List[str] = None,
        endpoint_group_region: str = None,
        endpoint_group_unconfirmed_ip_list: List[str] = None,
        listener_id: str = None,
        name: str = None,
        request_id: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.DescribeCustomRoutingEndpointGroupResponseBodyServiceManagedInfos] = None,
        sls_log_store_name: str = None,
        sls_project_name: str = None,
        sls_region: str = None,
        state: str = None,
    ):
        # The GA instance ID.
        self.accelerator_id = accelerator_id
        # Indicates the status of the binding between the Log Service project and the endpoint group. Valid values:
        # 
        # *   **on:** The endpoint group is bound to the Log Service project.
        # *   **off:** The endpoint group is not bound to the Log Service project.
        # *   **binding:** The endpoint group is being bound to the Log Service project.
        # *   **unbinding:** The endpoint group is being unbound from the Log Service project.
        self.access_log_switch = access_log_switch
        # The description of the endpoint group.
        self.description = description
        # Indicates whether the access log feature is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_access_log = enable_access_log
        # The endpoint group ID.
        self.endpoint_group_id = endpoint_group_id
        # The endpoint group IP addresses.
        self.endpoint_group_ip_list = endpoint_group_ip_list
        # The region ID of the endpoint group.
        self.endpoint_group_region = endpoint_group_region
        # The endpoint group IP addresses that need to be confirmed after the GA instance is upgraded.
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list
        # The custom routing listener ID.
        self.listener_id = listener_id
        # The name of the endpoint group.
        self.name = name
        # The request ID.
        self.request_id = request_id
        # The ID of the service that manages the GA instance.
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
        # >  This parameter takes effect only if **ServiceManaged** is set to **True**.
        # 
        # *   Users can perform only specific actions on a managed instance.
        self.service_managed_infos = service_managed_infos
        # The name of the Logstore.
        self.sls_log_store_name = sls_log_store_name
        # The name of the Log Service project.
        self.sls_project_name = sls_project_name
        # The region of the logs that are created in Log Service.
        self.sls_region = sls_region
        # The status of the endpoint group. Valid values:
        # 
        # *   **init:** The endpoint group is being initialized.
        # *   **active:** The endpoint group is running normally.
        # *   **updating:** The endpoint group is being updated.
        # *   **deleting:** The ACL is being deleted.
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

        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_access_log is not None:
            result['EnableAccessLog'] = self.enable_access_log

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

        if self.sls_log_store_name is not None:
            result['SlsLogStoreName'] = self.sls_log_store_name

        if self.sls_project_name is not None:
            result['SlsProjectName'] = self.sls_project_name

        if self.sls_region is not None:
            result['SlsRegion'] = self.sls_region

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableAccessLog') is not None:
            self.enable_access_log = m.get('EnableAccessLog')

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.DescribeCustomRoutingEndpointGroupResponseBodyServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')

        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')

        if m.get('SlsRegion') is not None:
            self.sls_region = m.get('SlsRegion')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

class DescribeCustomRoutingEndpointGroupResponseBodyServiceManagedInfos(DaraModel):
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
        # Indicates whether the specified actions are managed. Valid values:
        # 
        # *   **true**: The specified actions are managed, and users cannot perform the specified actions on the managed instance.
        # *   **false**: The specified actions are not managed, and users can perform the specified actions on the managed instance.
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

