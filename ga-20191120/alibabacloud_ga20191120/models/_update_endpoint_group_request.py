# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class UpdateEndpointGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        endpoint_configurations: List[main_models.UpdateEndpointGroupRequestEndpointConfigurations] = None,
        endpoint_group_id: str = None,
        endpoint_group_region: str = None,
        endpoint_ip_version: str = None,
        endpoint_protocol_version: str = None,
        endpoint_request_protocol: str = None,
        health_check_enabled: bool = None,
        health_check_host: str = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        name: str = None,
        port_overrides: List[main_models.UpdateEndpointGroupRequestPortOverrides] = None,
        region_id: str = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        # A client-generated token to ensure the idempotence of the request.
        # 
        # The token must be unique across requests and can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** is unique for each API request.
        self.client_token = client_token
        # The description of the endpoint group.
        # 
        # The description can be up to 200 characters long and cannot start with `http://` or `https://`.
        self.description = description
        # The configurations of the endpoints.
        self.endpoint_configurations = endpoint_configurations
        # The ID of the endpoint group.
        # 
        # This parameter is required.
        self.endpoint_group_id = endpoint_group_id
        # The ID of the region where the endpoint group is deployed.
        # 
        # This parameter is required.
        self.endpoint_group_region = endpoint_group_region
        # Specifies the IP protocol that GA uses to communicate with endpoints. Valid values: ● **IPv4** (default): Use IPv4. ● **IPv6**: Use IPv6. ● **ProtocolAffinity**: Use the same IP protocol as the client request.
        self.endpoint_ip_version = endpoint_ip_version
        # The version of the backend service protocol. Valid values:
        # 
        # - **HTTP1.1**
        # 
        # - **HTTP2**
        # 
        # > You can configure this parameter only when `EndpointRequestProtocol` is set to HTTPS.
        self.endpoint_protocol_version = endpoint_protocol_version
        # The backend service protocol. Valid values:
        # 
        # - **HTTP**
        # 
        # - **HTTPS**
        # 
        # > * You can configure this parameter only for endpoint groups of HTTP or HTTPS listeners.
        # >
        # > * For an HTTP listener, the backend service protocol must be HTTP.
        self.endpoint_request_protocol = endpoint_request_protocol
        # Specifies whether to enable health checks. Valid values:
        # 
        # - **true**: Enables health checks.
        # 
        # - **false** (default): Disables health checks.
        self.health_check_enabled = health_check_enabled
        # The domain name for the health check.
        self.health_check_host = health_check_host
        # The interval between health checks, in seconds. Valid values: **1** to **50**.
        self.health_check_interval_seconds = health_check_interval_seconds
        # The path for health checks.
        self.health_check_path = health_check_path
        # The port used for health checks. Valid values: **1** to **65535**.
        self.health_check_port = health_check_port
        # The protocol for health checks. Valid values:
        # 
        # - **tcp** or **TCP**
        # 
        # - **http** or **HTTP**
        # 
        # - **https** or **HTTPS**
        self.health_check_protocol = health_check_protocol
        # The name of the endpoint group.
        # 
        # The name must be 1 to 128 characters long, start with a letter or a Chinese character, and can contain digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The port override settings.
        self.port_overrides = port_overrides
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The number of consecutive successful or failed health checks required to change an endpoint\\"s health status.
        # 
        # Valid values: **2** to **10**.
        self.threshold_count = threshold_count
        # The weight of the endpoint group when the listener is associated with multiple endpoint groups.
        self.traffic_percentage = traffic_percentage

    def validate(self):
        if self.endpoint_configurations:
            for v1 in self.endpoint_configurations:
                 if v1:
                    v1.validate()
        if self.port_overrides:
            for v1 in self.port_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k1 in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k1.to_map() if k1 else None)

        if self.endpoint_group_id is not None:
            result['EndpointGroupId'] = self.endpoint_group_id

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.endpoint_ip_version is not None:
            result['EndpointIpVersion'] = self.endpoint_ip_version

        if self.endpoint_protocol_version is not None:
            result['EndpointProtocolVersion'] = self.endpoint_protocol_version

        if self.endpoint_request_protocol is not None:
            result['EndpointRequestProtocol'] = self.endpoint_request_protocol

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

        if self.name is not None:
            result['Name'] = self.name

        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k1 in self.port_overrides:
                result['PortOverrides'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count

        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k1 in m.get('EndpointConfigurations'):
                temp_model = main_models.UpdateEndpointGroupRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k1))

        if m.get('EndpointGroupId') is not None:
            self.endpoint_group_id = m.get('EndpointGroupId')

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('EndpointIpVersion') is not None:
            self.endpoint_ip_version = m.get('EndpointIpVersion')

        if m.get('EndpointProtocolVersion') is not None:
            self.endpoint_protocol_version = m.get('EndpointProtocolVersion')

        if m.get('EndpointRequestProtocol') is not None:
            self.endpoint_request_protocol = m.get('EndpointRequestProtocol')

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

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k1 in m.get('PortOverrides'):
                temp_model = main_models.UpdateEndpointGroupRequestPortOverrides()
                self.port_overrides.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')

        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')

        return self

class UpdateEndpointGroupRequestPortOverrides(DaraModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        # The endpoint port in the port override settings.
        self.endpoint_port = endpoint_port
        # The listener port in the port override settings.
        # 
        # > - For TCP listeners, virtual endpoint groups do not support port overrides. If a listener is already associated with a virtual endpoint group, you cannot configure port overrides for the default endpoint group. If the default endpoint group has port overrides configured, you cannot add a virtual endpoint group.
        # >
        # > - After you configure port overrides, you can change the listener protocol only between HTTP and HTTPS.
        # >
        # > - The updated listener port range must include all listener ports in the configured port overrides. For example, if the listener port range is 80-82 and port overrides are configured to map the ports to endpoint ports 100-102, you cannot update the listener port range to 80-81.
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

class UpdateEndpointGroupRequestEndpointConfigurations(DaraModel):
    def __init__(
        self,
        api_keys: List[str] = None,
        enable_client_ippreservation: bool = None,
        enable_proxy_protocol: bool = None,
        endpoint: str = None,
        provider: str = None,
        sub_address: str = None,
        type: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        weight: int = None,
    ):
        self.api_keys = api_keys
        # Specifies whether to preserve client source IP addresses. Valid values:
        # 
        # - **true**: Preserves client source IP addresses.
        # 
        # - **false** (default): Does not preserve client source IP addresses.
        # 
        # > * For endpoint groups of TCP or UDP listeners, this feature is disabled by default but can be enabled if needed.
        # >
        # > * For endpoint groups of HTTP or HTTPS listeners, client source IP addresses are preserved by default. The client IP addresses are retrieved from the X-Forwarded-For header. You cannot disable this feature.
        # >
        # > * You cannot set both `EnableClientIPPreservation` and `EnableProxyProtocol` to `true`.
        # >
        # > * For more information, see [preserve client source IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_client_ippreservation = enable_client_ippreservation
        # Specifies whether to use the Proxy Protocol to preserve client source IP addresses. Valid values:
        # 
        # - **true**: Preserves client source IP addresses.
        # 
        # - **false** (default): Does not preserve client source IP addresses.
        # 
        # > * You can configure this parameter only for endpoint groups of TCP listeners.
        # >
        # > * You cannot set both `EnableClientIPPreservation` and `EnableProxyProtocol` to `true`.
        # >
        # > * For more information, see [preserve client source IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_proxy_protocol = enable_proxy_protocol
        # Enter an IP address, a domain name, or an instance ID based on the value of the `Type` parameter.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        self.provider = provider
        # The private IP address of the elastic network interface.
        # 
        # > If the endpoint type is **ENI**, you can specify this parameter. If you omit this parameter, the primary private IP address of the ENI is used.
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
        # - **ECS**: an ECS instance.
        # 
        # - **SLB**: an SLB instance.
        # 
        # - **ALB**: an ALB instance.
        # 
        # - **OSS**: an OSS instance.
        # 
        # - **ENI**: an elastic network interface.
        # 
        # - **NLB**: an NLB instance.
        # 
        # > * If the endpoint type is **ECS**, **ENI**, **SLB**, or **IpTarget**, and the service-linked role does not exist, the system automatically creates a service-linked role named AliyunServiceRoleForGaVpcEndpoint.
        # >
        # > * If the endpoint type is **ALB**, and the service-linked role does not exist, the system automatically creates a service-linked role named AliyunServiceRoleForGaAlb.
        # >
        # > * If the endpoint type is **OSS**, and the service-linked role does not exist, the system automatically creates a service-linked role named AliyunServiceRoleForGaOss.
        # >
        # > * If the endpoint type is **NLB**, and the service-linked role does not exist, the system automatically creates a service-linked role named AliyunServiceRoleForGaNlb.
        # >
        # > > For more information, see [service-linked roles](https://help.aliyun.com/document_detail/178360.html).
        # 
        # This parameter is required.
        self.type = type
        # A list of vSwitches in the VPC.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC.
        # 
        # You can specify at most one VPC ID for an endpoint group that is associated with an intelligent routing listener.
        # 
        # > This parameter is required only when the endpoint type is **IpTarget**.
        self.vpc_id = vpc_id
        # The weight of the endpoint.
        # 
        # Valid values: **0** to **255**.
        # 
        # > If you set the weight of an endpoint to 0, Global Accelerator stops distributing traffic to the endpoint. Proceed with caution.
        # 
        # This parameter is required.
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

