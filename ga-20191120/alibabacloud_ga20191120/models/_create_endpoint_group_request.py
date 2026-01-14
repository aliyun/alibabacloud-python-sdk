# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateEndpointGroupRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        description: str = None,
        dry_run: bool = None,
        endpoint_configurations: List[main_models.CreateEndpointGroupRequestEndpointConfigurations] = None,
        endpoint_group_region: str = None,
        endpoint_group_type: str = None,
        endpoint_ip_version: str = None,
        endpoint_protocol_version: str = None,
        endpoint_request_protocol: str = None,
        health_check_enabled: bool = None,
        health_check_host: str = None,
        health_check_interval_seconds: int = None,
        health_check_path: str = None,
        health_check_port: int = None,
        health_check_protocol: str = None,
        listener_id: str = None,
        name: str = None,
        port_overrides: List[main_models.CreateEndpointGroupRequestPortOverrides] = None,
        region_id: str = None,
        tag: List[main_models.CreateEndpointGroupRequestTag] = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        # The ID of the GA instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The description of the endpoint group.
        # 
        # The description can be up to 200 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to perform a dry run, without sending the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, a 2xx HTTP status code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The configurations of the endpoints in the endpoint group.
        self.endpoint_configurations = endpoint_configurations
        # The ID of the region in which to create the endpoint group.
        # 
        # This parameter is required.
        self.endpoint_group_region = endpoint_group_region
        # The type of the endpoint group. Valid values:
        # 
        # *   **default** (default): a default endpoint group.
        # *   **virtual**: a virtual endpoint group.
        # 
        # >  When you call this operation to create a virtual endpoint group for a Layer 4 listener, make sure that a default endpoint group is created.
        self.endpoint_group_type = endpoint_group_type
        self.endpoint_ip_version = endpoint_ip_version
        # The backend service protocol. Valid values:
        # 
        # *   **HTTP1.1** (default)
        # *   **HTTP2**
        # 
        # >  This parameter is required only when you set the EndpointRequestProtocol parameter to HTTPS.
        self.endpoint_protocol_version = endpoint_protocol_version
        # The protocol that is used by the backend service. Default value: HTTP. Valid values:
        # 
        # *   **HTTP**
        # *   **HTTPS**
        # 
        # > *   You can set this parameter only when the listener that is associated with the endpoint group uses **HTTP** or **HTTPS**.
        # >*   For an **HTTP** listener, the backend service protocol must be **HTTP**.
        self.endpoint_request_protocol = endpoint_request_protocol
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.health_check_enabled = health_check_enabled
        self.health_check_host = health_check_host
        # The interval at which health checks are performed. Unit: seconds.
        self.health_check_interval_seconds = health_check_interval_seconds
        # The path to which to send health check requests.
        self.health_check_path = health_check_path
        # The port that is used for health checks.
        self.health_check_port = health_check_port
        # The protocol over which to send health check requests. Valid values:
        # 
        # *   **tcp** or **TCP**
        # *   **http** or **HTTP**
        # *   **https** or **HTTPS**
        self.health_check_protocol = health_check_protocol
        # The ID of the listener.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The name of the endpoint group.
        # 
        # The name must be 1 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.name = name
        # The port mappings.
        self.port_overrides = port_overrides
        # The ID of the region where the GA instance is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Tags of GA instances.
        self.tag = tag
        # The number of consecutive health check failures that must occur before a healthy endpoint group is considered unhealthy, or the number of consecutive health check successes that must occur before an unhealthy endpoint group is considered healthy.
        # 
        # Valid values: **2** to **10**. Default value: **3**.
        self.threshold_count = threshold_count
        # The traffic ratio for the endpoint group when the specified listener is associated with multiple endpoint groups.
        # 
        # Valid values: **1** to **100**.
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
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k1 in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k1.to_map() if k1 else None)

        if self.endpoint_group_region is not None:
            result['EndpointGroupRegion'] = self.endpoint_group_region

        if self.endpoint_group_type is not None:
            result['EndpointGroupType'] = self.endpoint_group_type

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

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.name is not None:
            result['Name'] = self.name

        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k1 in self.port_overrides:
                result['PortOverrides'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.threshold_count is not None:
            result['ThresholdCount'] = self.threshold_count

        if self.traffic_percentage is not None:
            result['TrafficPercentage'] = self.traffic_percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k1 in m.get('EndpointConfigurations'):
                temp_model = main_models.CreateEndpointGroupRequestEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k1))

        if m.get('EndpointGroupRegion') is not None:
            self.endpoint_group_region = m.get('EndpointGroupRegion')

        if m.get('EndpointGroupType') is not None:
            self.endpoint_group_type = m.get('EndpointGroupType')

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

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k1 in m.get('PortOverrides'):
                temp_model = main_models.CreateEndpointGroupRequestPortOverrides()
                self.port_overrides.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateEndpointGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')

        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')

        return self

class CreateEndpointGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the GA instance. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        # 
        # You can specify up to 20 tag keys.
        self.key = key
        # The tag value of the GA instance. The tag value cannot be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot contain `http://` or `https://`. It cannot start with `aliyun` or `acs:`.
        # 
        # You can specify up to 20 tag values.
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

class CreateEndpointGroupRequestPortOverrides(DaraModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        # The endpoint port that is mapped to the listener port.
        self.endpoint_port = endpoint_port
        # The listener port that is mapped to the endpoint port.
        # 
        # > *   You cannot configure port mappings for virtual endpoint groups of TCP listeners. If a virtual endpoint group already exists on the listener, you cannot configure port mappings for the default endpoint group. If port mappings are configured for the default endpoint group, you cannot add a virtual endpoint group.
        # > *   If you configure port mappings for a listener, you cannot modify the listener protocol. You can only switch between HTTP and HTTPS.
        # > *   Listener port: When you modify the listener port range, make sure that the port range includes the ports configured in port mappings. For example, if you set the listener port range to 80 to 82 and map the listener ports to endpoint ports 100 to 102, you cannot change the listener port range to 80 to 81.
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

class CreateEndpointGroupRequestEndpointConfigurations(DaraModel):
    def __init__(
        self,
        enable_client_ippreservation: bool = None,
        enable_proxy_protocol: bool = None,
        endpoint: str = None,
        sub_address: str = None,
        type: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
        weight: int = None,
    ):
        # Specifies whether to automatically preserve client IP addresses. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # > *   By default, client IP address preservation is disabled for an endpoint group of a UDP or TCP listener. You can configure this parameter based on your business requirements.
        # > *   By default, client IP address preservation is enabled for an endpoint group of an HTTP or HTTP listener. You can obtain client IP addresses by using the X-Forwarded-For header. You cannot disable the feature.
        # > *   EnableClientIPPreservation and EnableProxyProtocol cannot be set to true at the same time.
        # > > For more information, see [Preserve client IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_client_ippreservation = enable_client_ippreservation
        # Specifies whether to use the proxy protocol to preserve client IP addresses. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        # 
        # > *   This parameter is available only to endpoint groups of TCP listeners.
        # > *   EnableClientIPPreservation and EnableProxyProtocol cannot be set to true at the same time.
        # > >  For more information, see [Preserve client IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_proxy_protocol = enable_proxy_protocol
        # The IP address, domain name, or instance ID based on the value of Type.
        # 
        # This parameter is required.
        self.endpoint = endpoint
        # The private IP address of the ENI.
        # 
        # >  This parameter is available only when you set the endpoint type to **ENI**. If you leave this parameter empty, the primary private IP address of the ENI is used.
        self.sub_address = sub_address
        # The type of the endpoint. Valid values:
        # 
        # *   **Domain**: a custom domain name.
        # *   **Ip**: a custom IP address.
        # *   **IpTarget**: a custom private IP address.
        # *   **PublicIp**: a public IP address provided by Alibaba Cloud.
        # *   **ECS**: an Elastic Compute Service (ECS) instance.
        # *   **SLB**: a Server Load Balancer (SLB) instance.
        # *   **ALB**: an Application Load Balancer (ALB) instance.
        # *   **OSS**: an Object Storage Service (OSS) bucket.
        # *   **ENI**: an elastic network interface (ENI).
        # *   **NLB**: a Network Load Balancer (NLB) instance.
        # 
        # > *   If you set this parameter to **ECS**, **ENI**, **SLB**, **ALB**, **NLB**, or **IpTarget** and the AliyunServiceRoleForGaVpcEndpoint service-linked role does not exist, the system automatically creates the role.
        # > *   If you set this parameter to **ALB** and the AliyunServiceRoleForGaAlb service-linked role does not exist, the system automatically creates the role.
        # > *   If you set this parameter to **OSS** and the AliyunServiceRoleForGaOss service-linked role does not exist, the system automatically creates the role.
        # > *   If you set this parameter to **NLB** and the AliyunServiceRoleForGaNlb service-linked role does not exist, the system automatically creates the role.
        # > > For more information, see [Service-linked roles](https://help.aliyun.com/document_detail/178360.html).
        # 
        # This parameter is required.
        self.type = type
        # The IDs of vSwitches that are deployed in the VPC.
        self.v_switch_ids = v_switch_ids
        # The virtual private cloud (VPC) ID.
        # 
        # You can specify one VPC ID for an endpoint group of an intelligent routing listener.
        # 
        # >  This parameter is valid and required only if Type is set to **IpTarget**.
        self.vpc_id = vpc_id
        # The weight of the endpoint.
        # 
        # Valid values: **0** to **255**.
        # 
        # >  If you set the weight of an endpoint to 0, GA stops distributing traffic to the endpoint. Proceed with caution.
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
        if self.enable_client_ippreservation is not None:
            result['EnableClientIPPreservation'] = self.enable_client_ippreservation

        if self.enable_proxy_protocol is not None:
            result['EnableProxyProtocol'] = self.enable_proxy_protocol

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

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
        if m.get('EnableClientIPPreservation') is not None:
            self.enable_client_ippreservation = m.get('EnableClientIPPreservation')

        if m.get('EnableProxyProtocol') is not None:
            self.enable_proxy_protocol = m.get('EnableProxyProtocol')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

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

