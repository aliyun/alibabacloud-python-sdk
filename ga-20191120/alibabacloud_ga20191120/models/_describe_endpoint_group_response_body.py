# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class DescribeEndpointGroupResponseBody(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        access_log_record_customized_header_list: List[str] = None,
        access_log_record_customized_headers_enabled: bool = None,
        access_log_switch: str = None,
        description: str = None,
        enable_access_log: bool = None,
        endpoint_configurations: List[main_models.DescribeEndpointGroupResponseBodyEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        endpoint_group_ip_list: List[str] = None,
        endpoint_group_region: str = None,
        endpoint_group_type: str = None,
        endpoint_group_unconfirmed_ip_list: List[str] = None,
        endpoint_ip_version: str = None,
        endpoint_private_ip_list: List[main_models.DescribeEndpointGroupResponseBodyEndpointPrivateIpList] = None,
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
        port_overrides: List[main_models.DescribeEndpointGroupResponseBodyPortOverrides] = None,
        request_id: str = None,
        service_id: str = None,
        service_managed: bool = None,
        service_managed_infos: List[main_models.DescribeEndpointGroupResponseBodyServiceManagedInfos] = None,
        sls_log_store_name: str = None,
        sls_project_name: str = None,
        sls_region: str = None,
        state: str = None,
        tags: List[main_models.DescribeEndpointGroupResponseBodyTags] = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        # The Global Accelerator instance ID.
        self.accelerator_id = accelerator_id
        # The custom header fields to record in access logs.
        self.access_log_record_customized_header_list = access_log_record_customized_header_list
        # Specifies whether to record custom header fields in access logs. Valid values:
        # 
        # - **true**: Yes.
        # 
        # - **false** (default): No.
        # 
        # > You can set this parameter to **true** only when **EnableAccessLog** is set to **true**.
        self.access_log_record_customized_headers_enabled = access_log_record_customized_headers_enabled
        # The status of the access log configuration. Valid values:
        # 
        # - **on**: The access log is configured.
        # 
        # - **off**: The access log is not configured.
        # 
        # - **binding**: The access log is being configured.
        # 
        # - **unbinding**: The access log configuration is being removed.
        self.access_log_switch = access_log_switch
        # The description of the endpoint group.
        self.description = description
        # Indicates whether access logging is enabled.
        # 
        # - **true**: Access logging is enabled.
        # 
        # - **false**: Access logging is disabled.
        self.enable_access_log = enable_access_log
        # The endpoint configurations.
        self.endpoint_configurations = endpoint_configurations
        # The endpoint group ID.
        self.endpoint_group_id = endpoint_group_id
        # The list of active IP addresses of the endpoints in the endpoint group.
        # >Notice: For an endpoint group configured for back-to-source from a private network, the console displays only the private back-to-source IP addresses and not the public IP addresses. If the network connection type for the backend service of the endpoint group changes (for example, from a private network to a public network, or to a mix of private and public networks), you must monitor the changes in the back-to-source IP addresses and update the access control list (ACL) of the backend service accordingly.
        self.endpoint_group_ip_list = endpoint_group_ip_list
        # The region ID where the endpoint group is deployed.
        self.endpoint_group_region = endpoint_group_region
        # The type of the endpoint group. Valid values:
        # 
        # - **default**: A default endpoint group.
        # 
        # - **virtual**: A virtual endpoint group.
        self.endpoint_group_type = endpoint_group_type
        # A list of endpoint IP addresses pending confirmation after a Global Accelerator instance upgrade.
        self.endpoint_group_unconfirmed_ip_list = endpoint_group_unconfirmed_ip_list
        # The IP version used to connect to the backend service. Valid values:
        # 
        # - **IPv4** (default): Global Accelerator connects to the backend service using IPv4.
        # 
        # - **IPv6**: Global Accelerator connects to the backend service using IPv6.
        # 
        # - **ProtocolAffinity**: Global Accelerator connects to the backend service using the same IP version as the client request.
        self.endpoint_ip_version = endpoint_ip_version
        # The private IP addresses of the endpoints.
        self.endpoint_private_ip_list = endpoint_private_ip_list
        # The version of the backend service protocol. Valid values:
        # 
        # - **HTTP1.1**
        # 
        # - **HTTP2**
        self.endpoint_protocol_version = endpoint_protocol_version
        # The protocol used by the backend service. Valid values:
        # 
        # - **HTTP**
        # 
        # - **HTTPS**
        self.endpoint_request_protocol = endpoint_request_protocol
        # The IDs of the associated forwarding rules.
        self.forwarding_rule_ids = forwarding_rule_ids
        # Indicates whether health checks are enabled.
        # 
        # - **true**: Health checks are enabled.
        # 
        # - **false**: Health checks are disabled.
        self.health_check_enabled = health_check_enabled
        # The domain name used for health checks.
        self.health_check_host = health_check_host
        # The health check interval, in seconds.
        self.health_check_interval_seconds = health_check_interval_seconds
        # The path for health check probes.
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
        # The listener ID.
        self.listener_id = listener_id
        # The name of the endpoint group.
        self.name = name
        # The port mapping configuration.
        self.port_overrides = port_overrides
        # The request ID.
        self.request_id = request_id
        # The ID of the service that manages the instance.
        # 
        # > This parameter is returned only if **ServiceManaged** is set to **True**.
        self.service_id = service_id
        # Indicates whether the instance is a managed instance. Valid values:
        # 
        # - **true**: The instance is a managed instance.
        # 
        # - **false**: The instance is not a managed instance.
        self.service_managed = service_managed
        # A list of management states for actions that can be performed on the instance.
        # 
        # > - This parameter is returned only if **ServiceManaged** is set to **True**.
        # >
        # > - When an instance is managed, some operations may be restricted.
        self.service_managed_infos = service_managed_infos
        # The name of the Logstore.
        self.sls_log_store_name = sls_log_store_name
        # The name of the Log Service project.
        self.sls_project_name = sls_project_name
        # The region of the Log Service project.
        self.sls_region = sls_region
        # The status of the endpoint group.
        # 
        # - **init**: The endpoint group is being initialized.
        # 
        # - **active**: The endpoint group is active.
        # 
        # - **updating**: The endpoint group is being updated.
        # 
        # - **deleting**: The endpoint group is being deleted.
        self.state = state
        # A list of tags attached to the endpoint group.
        self.tags = tags
        # The number of consecutive failed health checks before an endpoint is marked as unhealthy.
        self.threshold_count = threshold_count
        # The percentage of traffic that is distributed to the endpoint group. This parameter is returned only when a listener is associated with multiple endpoint groups.
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

        if self.access_log_record_customized_header_list is not None:
            result['AccessLogRecordCustomizedHeaderList'] = self.access_log_record_customized_header_list

        if self.access_log_record_customized_headers_enabled is not None:
            result['AccessLogRecordCustomizedHeadersEnabled'] = self.access_log_record_customized_headers_enabled

        if self.access_log_switch is not None:
            result['AccessLogSwitch'] = self.access_log_switch

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_access_log is not None:
            result['EnableAccessLog'] = self.enable_access_log

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

        if m.get('AccessLogRecordCustomizedHeaderList') is not None:
            self.access_log_record_customized_header_list = m.get('AccessLogRecordCustomizedHeaderList')

        if m.get('AccessLogRecordCustomizedHeadersEnabled') is not None:
            self.access_log_record_customized_headers_enabled = m.get('AccessLogRecordCustomizedHeadersEnabled')

        if m.get('AccessLogSwitch') is not None:
            self.access_log_switch = m.get('AccessLogSwitch')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableAccessLog') is not None:
            self.enable_access_log = m.get('EnableAccessLog')

        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k1 in m.get('EndpointConfigurations'):
                temp_model = main_models.DescribeEndpointGroupResponseBodyEndpointConfigurations()
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
                temp_model = main_models.DescribeEndpointGroupResponseBodyEndpointPrivateIpList()
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
                temp_model = main_models.DescribeEndpointGroupResponseBodyPortOverrides()
                self.port_overrides.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceManaged') is not None:
            self.service_managed = m.get('ServiceManaged')

        self.service_managed_infos = []
        if m.get('ServiceManagedInfos') is not None:
            for k1 in m.get('ServiceManagedInfos'):
                temp_model = main_models.DescribeEndpointGroupResponseBodyServiceManagedInfos()
                self.service_managed_infos.append(temp_model.from_map(k1))

        if m.get('SlsLogStoreName') is not None:
            self.sls_log_store_name = m.get('SlsLogStoreName')

        if m.get('SlsProjectName') is not None:
            self.sls_project_name = m.get('SlsProjectName')

        if m.get('SlsRegion') is not None:
            self.sls_region = m.get('SlsRegion')

        if m.get('State') is not None:
            self.state = m.get('State')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeEndpointGroupResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')

        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')

        return self

class DescribeEndpointGroupResponseBodyTags(DaraModel):
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

class DescribeEndpointGroupResponseBodyServiceManagedInfos(DaraModel):
    def __init__(
        self,
        action: str = None,
        child_type: str = None,
        is_managed: bool = None,
    ):
        # The name of the action on the managed instance. Valid values:
        # 
        # - **Create**: Create an instance.
        # 
        # - **Update**: Update the instance.
        # 
        # - **Delete**: Delete the instance.
        # 
        # - **Associate**: Associate the instance.
        # 
        # - **UserUnmanaged**: Releases the instance from service management.
        # 
        # - **CreateChild**: Create a child resource.
        self.action = action
        # The type of the child resource. Valid values:
        # 
        # - **Listener**: A listener.
        # 
        # - **IpSet**: An acceleration region.
        # 
        # - **EndpointGroup**: An endpoint group.
        # 
        # - **ForwardingRule**: A forwarding rule.
        # 
        # - **Endpoint**: An endpoint.
        # 
        # - **EndpointGroupDestination**: A protocol mapping for an endpoint group of a custom routing listener.
        # 
        # - **EndpointPolicy**: A traffic policy for an endpoint of a custom routing listener.
        # 
        # > This parameter is valid only when **Action** is set to **CreateChild**.
        self.child_type = child_type
        # Indicates whether the action is managed. Valid values:
        # 
        # - **true**: The action is managed. You cannot perform this action on the instance.
        # 
        # - **false**: The action is not managed. You can perform this action on the instance.
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

class DescribeEndpointGroupResponseBodyPortOverrides(DaraModel):
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

class DescribeEndpointGroupResponseBodyEndpointPrivateIpList(DaraModel):
    def __init__(
        self,
        cidr: str = None,
        private_ip: str = None,
        v_switch_id: str = None,
    ):
        self.cidr = cidr
        # The private IP address.
        self.private_ip = private_ip
        # The VSwitch ID in the VPC.
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

class DescribeEndpointGroupResponseBodyEndpointConfigurations(DaraModel):
    def __init__(
        self,
        api_keys: List[str] = None,
        enable_client_ippreservation: bool = None,
        enable_proxy_protocol: bool = None,
        endpoint: str = None,
        probe_port: int = None,
        probe_protocol: str = None,
        provider: str = None,
        sub_address: str = None,
        type: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        weight: int = None,
    ):
        # The API keys for the endpoint configuration.
        self.api_keys = api_keys
        # Indicates whether client IP preservation is enabled by using the automatic method.
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.enable_client_ippreservation = enable_client_ippreservation
        # Indicates whether client IP preservation is enabled using the Proxy Protocol.
        # 
        # - **true**: Enabled.
        # 
        # - **false**: Disabled.
        self.enable_proxy_protocol = enable_proxy_protocol
        # The IP address, domain name, or instance ID of the endpoint.
        self.endpoint = endpoint
        # The port used for latency probing.
        self.probe_port = probe_port
        # The protocol for latency probing. Valid values:
        # 
        # - **tcp**: TCP
        # 
        # - **icmp**: ICMP
        self.probe_protocol = probe_protocol
        # The provider of the endpoint configuration.
        self.provider = provider
        # The private IP address of the elastic network interface.
        self.sub_address = sub_address
        # The type of the endpoint. Valid values:
        # 
        # - **Domain**: A custom domain name.
        # 
        # - **Ip**: A custom IP address.
        # 
        # - **IpTarget**: A custom private IP address.
        # 
        # - **PublicIp**: An Alibaba Cloud public IP address.
        # 
        # - **ECS**: An ECS instance.
        # 
        # - **SLB**: An SLB instance.
        # 
        # - **ALB**: An ALB instance.
        # 
        # - **OSS**: An OSS instance.
        # 
        # - **ENI**: An elastic network interface.
        # 
        # - **NLB**: An NLB instance.
        self.type = type
        # A list of VSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The VPC ID.
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

