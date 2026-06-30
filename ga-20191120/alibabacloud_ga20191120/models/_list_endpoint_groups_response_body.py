# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListEndpointGroupsResponseBody(DaraModel):
    def __init__(
        self,
        endpoint_groups: List[main_models.ListEndpointGroupsResponseBodyEndpointGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of endpoint groups.
        self.endpoint_groups = endpoint_groups
        # The page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
                temp_model = main_models.ListEndpointGroupsResponseBodyEndpointGroups()
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

class ListEndpointGroupsResponseBodyEndpointGroups(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        description: str = None,
        endpoint_configurations: List[main_models.ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        endpoint_group_ip_list: List[str] = None,
        endpoint_group_region: str = None,
        endpoint_group_type: str = None,
        endpoint_group_unconfirmed_ip_list: List[str] = None,
        endpoint_ip_version: str = None,
        endpoint_private_ip_list: List[main_models.ListEndpointGroupsResponseBodyEndpointGroupsEndpointPrivateIpList] = None,
        endpoint_protocol_version: str = None,
        endpoint_request_protocol: str = None,
        forwarding_rule_ids: List[str] = None,
        health_check_enabled: bool = None,
        health_check_host: str = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        listener_id: str = None,
        name: str = None,
        port_overrides: List[main_models.ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides] = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.ListEndpointGroupsResponseBodyEndpointGroupsServiceManagedInfos] = None,
        state: str = None,
        tags: List[main_models.ListEndpointGroupsResponseBodyEndpointGroupsTags] = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        # The ID of the Global Accelerator instance.
        self.accelerator_id = accelerator_id
        # The description of the endpoint group.
        self.description = description
        # A list of endpoint configurations.
        self.endpoint_configurations = endpoint_configurations
        # The ID of the endpoint group.
        self.endpoint_group_id = endpoint_group_id
        # A list of public egress IP addresses of the endpoint group.
        # 
        # >Notice: 
        # 
        # For endpoint groups connected to private backend services, the console shows only the private source IP addresses, not the public ones. If the network connection type of a backend service changes (for example, from private to public), monitor the source IP addresses and update the backend service\\"s access control list (ACL).
        self.endpoint_group_ip_list = endpoint_group_ip_list
        # The ID of the region where the endpoint group is deployed.
        self.endpoint_group_region = endpoint_group_region
        # The type of the endpoint group. Valid values:
        # 
        # - **default**: a default endpoint group.
        # 
        # - **virtual**: a virtual endpoint group.
        self.endpoint_group_type = endpoint_group_type
        # The list of new IP addresses in the endpoint group that require confirmation after a Global Accelerator instance is upgraded.
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list
        # The IP protocol of the backend service. Valid values:
        # 
        # - **IPv4** (default): Connections to the backend service use IPv4.
        # 
        # - **IPv6**: Connections to the backend service use IPv6.
        # 
        # - **ProtocolAffinity**: The connection to the backend service uses the same IP protocol as the client request.
        self.endpoint_ip_version = endpoint_ip_version
        # A list of private IP addresses of the endpoints.
        self.endpoint_private_ip_list = endpoint_private_ip_list
        # The version of the backend service protocol. Valid values:
        # 
        # - **HTTP1.1**: HTTP/1.1
        # 
        # - **HTTP2**: HTTP/2
        self.endpoint_protocol_version = endpoint_protocol_version
        # The protocol of the backend service. Valid values:
        # 
        # - **HTTP**: HTTP
        # 
        # - **HTTPS**: HTTPS
        self.endpoint_request_protocol = endpoint_request_protocol
        # The IDs of forwarding rules associated with the endpoint group.
        self.forwarding_rule_ids = forwarding_rule_ids
        # Specifies whether to enable health checks.
        # 
        # - **true**: Health checks are enabled.
        # 
        # - **false**: Health checks are disabled.
        self.health_check_enabled = health_check_enabled
        # The domain name used for health checks.
        self.health_check_host = health_check_host
        # The health check interval, in seconds.
        self.health_check_interval_seconds = health_check_interval_seconds
        # The health check path.
        self.health_check_path = health_check_path
        # The port used for health checks.
        self.health_check_port = health_check_port
        # The protocol used for health checks.
        # 
        # - **tcp** or **TCP**: TCP
        # 
        # - **http** or **HTTP**: HTTP
        # 
        # - **https** or **HTTPS**: HTTPS
        self.health_check_protocol = health_check_protocol
        # The ID of the listener.
        self.listener_id = listener_id
        # The name of the endpoint group.
        self.name = name
        # The port mappings.
        self.port_overrides = port_overrides
        # The ID of the service that manages the instance.
        # 
        # > This parameter is returned only if **ServiceManaged** is **true**.
        self.service_id = service_id
        # Specifies whether the instance is managed. Valid values:
        # 
        # - **true**: The instance is a managed instance.
        # 
        # - **false**: The instance is not a managed instance.
        self.service_managed = service_managed
        # The actions that you can perform on the managed instance.
        # 
        # > - This parameter is returned only if **ServiceManaged** is **true**.
        # >
        # > - Your permissions to operate on a managed instance are restricted.
        self.service_managed_infos = service_managed_infos
        # The state of the endpoint group.
        # 
        # - **init**: The endpoint group is initializing.
        # 
        # - **active**: The endpoint group is stable.
        # 
        # - **updating**: The endpoint group is updating.
        # 
        # - **deleting**: The endpoint group is deleting.
        self.state = state
        # The tags attached to the endpoint group.
        self.tags = tags
        # The number of consecutive failed health checks required to mark an endpoint as unhealthy.
        self.threshold_count = threshold_count
        # The percentage of traffic routed to the endpoint group. This parameter applies only if a listener is associated with multiple endpoint groups.
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for v1 in self.endpoint_configurations:
                 if v1:
                    v1.validate()
        if self.endpoint_private_ip_list:
            for v1 in self.endpoint_private_ip_list:
                 if v1:
                    v1.validate()
        if self.port_overrides:
            for v1 in self.port_overrides:
                 if v1:
                    v1.validate()
        if self.service_managed_infos:
            for v1 in self.service_managed_infos:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
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

        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k1 in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k1.to_map() if k1 else None)

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_group_ip_list is not None:
            result['EndpointGroupIpList'] = self.endpoint_group_ip_list

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type

        if self.endpoint_group_unconfirmed_ip_list is not None:
            result['EndpointGroupUnconfirmedIpList'] = self.endpoint_group_unconfirmed_ip_list

        if self.endpoint_ip_version is not None:
            result['EndpointIpVersion'] = self.endpoint_ip_version

        result['EndpointPrivateIpList'] = []
        if self.endpoint_private_ip_list is not None:
            for k1 in self.endpoint_private_ip_list:
                result['EndpointPrivateIpList'].append(k1.to_map() if k1 else None)

        if self.endpoint_protocol_version is not None:
            result['EndpointProtocolVersion'] = self.endpoint_protocol_version

        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol

        if self.forwarding_rule_ids is not None:
            result['ForwardingRuleIds'] = self.forwarding_rule_ids

        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled

        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host

        if self.health_check_interval_seconds is not None:
            result['HealthCheckIntervalSeconds'] = self.health_check_interval_seconds

        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path

        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port

        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.name is not None:
            result['Name'] = self.name

        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k1 in self.port_overrides:
                result['PortOverrides'].append(k1.to_map() if k1 else None)

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

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count

        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k1 in m.get('EndpointConfigurations'):
                temp_model = main_models.ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k1))

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointGroupIpList') is not None:
            self.endpoint_group_ip_list = m.get('EndpointGroupIpList')

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')

        if m.get('EndpointGroupUnconfirmedIpList') is not None:
            self.endpoint_group_unconfirmed_ip_list = m.get('EndpointGroupUnconfirmedIpList')

        if m.get('EndpointIpVersion') is not None:
            self.endpoint_ip_version = m.get('EndpointIpVersion')

        self.endpoint_private_ip_list = []
        if m.get('EndpointPrivateIpList') is not None:
            for k1 in m.get('EndpointPrivateIpList'):
                temp_model = main_models.ListEndpointGroupsResponseBodyEndpointGroupsEndpointPrivateIpList()
                self.endpoint_private_ip_list.append(temp_model.from_map(k1))

        if m.get('EndpointProtocolVersion') is not None:
            self.endpoint_protocol_version = m.get('EndpointProtocolVersion')

        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')

        if m.get('ForwardingRuleIds') is not None:
            self.forwarding_rule_ids = m.get('ForwardingRuleIds')

        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')

        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')

        if m.get('HealthCheckIntervalSeconds') is not None:
            self.health_check_interval_seconds = m.get('HealthCheckIntervalSeconds')

        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')

        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')

        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k1 in m.get('PortOverrides'):
                temp_model = main_models.ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k1))

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.ListEndpointGroupsResponseBodyEndpointGroupsServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('State') is not None:
            self.state = m.get('State')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListEndpointGroupsResponseBodyEndpointGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')

        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')

        return self

class ListEndpointGroupsResponseBodyEndpointGroupsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListEndpointGroupsResponseBodyEndpointGroupsServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the action on the managed instance. Valid values:
        # 
        # - **Create**: creates an instance.
        # 
        # - **Update**: updates the instance.
        # 
        # - **Delete**: deletes the instance.
        # 
        # - **Associate**: associates the instance with other resources.
        # 
        # - **UserUnmanaged**: Reverts the instance to an unmanaged state.
        # 
        # - **CreateChild**: creates a child resource for the instance.
        self.action = action
        # The type of the child resource. Valid values:
        # 
        # - **Listener**: a listener.
        # 
        # - **IpSet**: an acceleration region.
        # 
        # - **EndpointGroup**: an endpoint group.
        # 
        # - **ForwardingRule**: a forwarding rule.
        # 
        # - **Endpoint**: an endpoint.
        # 
        # - **EndpointGroupDestination**: a protocol mapping for an endpoint group of a custom routing listener.
        # 
        # - **EndpointPolicy**: a traffic policy for an endpoint of a custom routing listener.
        # 
        # > This parameter is returned only if **Action** is set to **CreateChild**.
        self.child_type = child_type
        # Specifies whether the action is managed. Valid values:
        # 
        # - **true**: The action is managed. You cannot perform the specified action on the managed instance.
        # 
        # - **false**: The action is not managed. You can perform the specified action on the managed instance.
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

class ListEndpointGroupsResponseBodyEndpointGroupsPortOverrides(DaraModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        # The endpoint port.
        self.endpoint_port = endpoint_port
        # The listener port.
        self.listener_port = listener_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint_port is not None:
            result['EndpointPort'] = self.endpoint_port

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointPort') is not None:
            self.endpoint_port = m.get('EndpointPort')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        return self

class ListEndpointGroupsResponseBodyEndpointGroupsEndpointPrivateIpList(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        private_ip: str = None,
        v_switch_id: str = None,
    ):
        self.cidr = cidr
        # The private IP address.
        self.private_ip = private_ip
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr is not None:
            result['CIDR'] = self.cidr

        if self.private_ip is not None:
            result['PrivateIp'] = self.private_ip

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CIDR') is not None:
            self.cidr = m.get('CIDR')

        if m.get('PrivateIp') is not None:
            self.private_ip = m.get('PrivateIp')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

class ListEndpointGroupsResponseBodyEndpointGroupsEndpointConfigurations(DaraModel):
    def __init__(
        self,
        api_keys: List[str] = None,
        enable_client_ippreservation: bool = None,
        enable_proxy_protocol: bool = None,
        endpoint: str = None,
        endpoint_id: str = None,
        probe_port: int = None,
        probe_protocol: str = None,
        provider: str = None,
        sub_address: str = None,
        type: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        weight: int = None,
    ):
        # The API keys in the endpoint configuration.
        self.api_keys = api_keys
        # Specifies whether to preserve client IP addresses.
        # 
        # - **true**: Client IP preservation is enabled.
        # 
        # - **false**: Client IP preservation is disabled.
        self.enable_client_ippreservation = enable_client_ippreservation
        # Specifies whether to use Proxy Protocol to preserve client IP addresses.
        # 
        # - **true**: Proxy Protocol is enabled.
        # 
        # - **false**: Proxy Protocol is disabled.
        self.enable_proxy_protocol = enable_proxy_protocol
        # The endpoint\\"s IP address, domain name, or instance ID.
        self.endpoint = endpoint
        # The ID of the endpoint.
        self.endpoint_id = endpoint_id
        # The port used for latency monitoring probes.
        self.probe_port = probe_port
        # The protocol that is used for latency monitoring probes.
        # 
        # - **icmp**: ICMP
        # 
        # - **tcp**: TCP
        self.probe_protocol = probe_protocol
        # The service provider.
        self.provider = provider
        # The private IP address of the elastic network interface.
        self.sub_address = sub_address
        # The type of endpoint. Valid values:
        # 
        # - **Domain**: a custom domain name.
        # 
        # - **Ip**: a custom IP address.
        # 
        # - **IpTarget**: a custom private IP address.
        # 
        # - **PublicIp**: an Alibaba Cloud public IP address.
        # 
        # - **ECS**: an Alibaba Cloud ECS instance.
        # 
        # - **SLB**: an Alibaba Cloud SLB instance.
        # 
        # - **ALB**: an Alibaba Cloud ALB instance.
        # 
        # - **OSS**: an Alibaba Cloud OSS bucket.
        # 
        # - **ENI**: an Alibaba Cloud elastic network interface.
        # 
        # - **NLB**: an Alibaba Cloud NLB instance.
        self.type = type
        # A list of vSwitches in the VPC.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC.
        self.vpc_id = vpc_id
        # The weight of the endpoint.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_keys is not None:
            result['ApiKeys'] = self.api_keys

        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation

        if self.enable_proxy_protocol is not None:
            result['EnableProxyProtocol'] = self.enable_proxy_protocol

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.endpoint_id is not None:
            result['EndpointId'] = self.endpoint_id

        if self.probe_port is not None:
            result['ProbePort'] = self.probe_port

        if self.probe_protocol is not None:
            result['ProbeProtocol'] = self.probe_protocol

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.sub_address is not None:
            result['SubAddress'] = self.sub_address

        if self.type is not None:
            result['Type'] = self.type

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKeys') is not None:
            self.api_keys = m.get('ApiKeys')

        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')

        if m.get('EnableProxyProtocol') is not None:
            self.enable_proxy_protocol = m.get('EnableProxyProtocol')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EndpointId') is not None:
            self.endpoint_id = m.get('EndpointId')

        if m.get('ProbePort') is not None:
            self.probe_port = m.get('ProbePort')

        if m.get('ProbeProtocol') is not None:
            self.probe_protocol = m.get('ProbeProtocol')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('SubAddress') is not None:
            self.sub_address = m.get('SubAddress')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

