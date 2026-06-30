# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class CreateEndpointGroupsRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        endpoint_group_configurations: List[main_models.CreateEndpointGroupsRequestEndpointGroupConfigurations] = None,
        listener_id: str = None,
        region_id: str = None,
    ):
        # The ID of the accelerator.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token used to ensure request idempotence.
        # 
        # You can generate the token on your client. Ensure that it is unique across different requests. The value of `ClientToken` can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the request as the **ClientToken**. The **RequestId** is unique for each API request.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run but does not create the resource. The system checks the required parameters, request format, and service limits. If the request fails the dry run, the system returns an error message. If the request passes the dry run, the system returns a 2xx HTTP status code.
        # 
        # - **false** (default): sends a normal request and creates the resource if the request passes.
        self.dry_run = dry_run
        # The configurations of the endpoint groups.
        # 
        # You can configure up to 10 endpoint groups.
        # 
        # This parameter is required.
        self.endpoint_group_configurations = endpoint_group_configurations
        # The ID of the listener.
        # 
        # > If the listener protocol is **HTTP** or **HTTPS**, you can create only one endpoint group in each **CreateEndpointGroups** call.
        # 
        # This parameter is required.
        self.listener_id = listener_id
        # The ID of the region where the accelerator is deployed. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.endpoint_group_configurations:
            for v1 in self.endpoint_group_configurations:
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

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        result['EndpointGroupConfigurations'] = []
        if self.endpoint_group_configurations is not None:
            for k1 in self.endpoint_group_configurations:
                result['EndpointGroupConfigurations'].append(k1.to_map() if k1 else None)

        if self.listener_id is not None:
            result['ListenerId'] = self.listener_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        self.endpoint_group_configurations = []
        if m.get('EndpointGroupConfigurations') is not None:
            for k1 in m.get('EndpointGroupConfigurations'):
                temp_model = main_models.CreateEndpointGroupsRequestEndpointGroupConfigurations()
                self.endpoint_group_configurations.append(temp_model.from_map(k1))

        if m.get('ListenerId') is not None:
            self.listener_id = m.get('ListenerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class CreateEndpointGroupsRequestEndpointGroupConfigurations(DaraModel):
    def __init__(
        self,
        endpoint_configurations: List[main_models.CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations] = None,
        endpoint_group_description: str = None,
        endpoint_group_name: str = None,
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
        port_overrides: List[main_models.CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides] = None,
        system_tag: List[main_models.CreateEndpointGroupsRequestEndpointGroupConfigurationsSystemTag] = None,
        tag: List[main_models.CreateEndpointGroupsRequestEndpointGroupConfigurationsTag] = None,
        threshold_count: int = None,
        traffic_percentage: int = None,
    ):
        # The configurations of the endpoints in the endpoint group.
        self.endpoint_configurations = endpoint_configurations
        # The description of the endpoint group.
        # 
        # The description can be up to 200 characters in length and cannot start with `http://` or `https://`.
        self.endpoint_group_description = endpoint_group_description
        # The name of the endpoint group.
        # 
        # The name must be 1 to 128 characters long, start with a letter or a Chinese character, and contain digits, periods (.), underscores (_), and hyphens (-).
        self.endpoint_group_name = endpoint_group_name
        # The ID of the region where the endpoint group is deployed.
        # 
        # You can enter up to 10 endpoint group region IDs.
        # 
        # This parameter is required.
        self.endpoint_group_region = endpoint_group_region
        # The type of the endpoint group in an intelligent routing listener. Valid values:
        # 
        # - **default** (default): a default endpoint group.
        # 
        # - **virtual**: a virtual endpoint group.
        # 
        # You can enter up to 10 endpoint group types.
        self.endpoint_group_type = endpoint_group_type
        # The IP version of the backend service. Valid values:
        # 
        # - **IPv4** (default): Global Accelerator uses only IPv4 addresses to communicate with the backend service.
        # 
        # - **IPv6**: Global Accelerator uses only IPv6 addresses to communicate with the backend service.
        # 
        # - **ProtocolAffinity**: Global Accelerator communicates with the backend service using the same IP version as the client request.
        self.endpoint_ip_version = endpoint_ip_version
        # The protocol version of the backend service. Valid values:
        # 
        # - **HTTP1.1** (default): HTTP 1.1.
        # 
        # - **HTTP2**: HTTP 2.
        # 
        # > You can set this parameter only when `EndpointRequestProtocol` is set to **HTTPS**.
        self.endpoint_protocol_version = endpoint_protocol_version
        # The protocol of the backend service. Valid values:
        # 
        # - **HTTP**
        # 
        # - **HTTPS**
        # 
        # > * You can set this parameter only when you create an endpoint group for an HTTP or HTTPS listener.
        # >
        # > * For an HTTP listener, you can set this parameter only to HTTP.
        self.endpoint_request_protocol = endpoint_request_protocol
        # Specifies whether to enable health checks for the endpoint group. Valid values:
        # 
        # - **true**: enables health checks.
        # 
        # - **false** (default): disables health checks.
        # 
        # You can enable health checks for up to 10 endpoint groups.
        self.health_check_enabled = health_check_enabled
        # The domain name to which health check requests are sent.
        self.health_check_host = health_check_host
        # The interval between health checks, in seconds.
        # 
        # You can enter up to 10 health check intervals.
        self.health_check_interval_seconds = health_check_interval_seconds
        # The path used for health checks.
        # 
        # You can enter up to 10 health check paths.
        self.health_check_path = health_check_path
        # The port used for health checks. Valid values: **1** to **65535**.
        # 
        # You can enter up to 10 ports for health checks.
        self.health_check_port = health_check_port
        # The protocol used for health checks. Valid values:
        # 
        # - **tcp** or **TCP**: TCP protocol.
        # 
        # - **http** or **HTTP**: HTTP protocol.
        # 
        # - **https** or **HTTPS**: HTTPS protocol.
        # 
        # You can enter up to 10 health check protocols.
        self.health_check_protocol = health_check_protocol
        # The port override settings.
        self.port_overrides = port_overrides
        # This parameter is reserved.
        self.system_tag = system_tag
        # The tags to add to the endpoint group. You can specify up to 20 tags.
        self.tag = tag
        # The number of consecutive health checks that must succeed for an endpoint to be considered healthy, or fail for it to be considered unhealthy. Valid values: **2** to **10**. Default value: **3**.
        # 
        # You can enter up to 10 values for the number of consecutive health checks required for a health status change.
        self.threshold_count = threshold_count
        # The traffic distribution percentage for the endpoint group. If an intelligent routing listener is associated with multiple endpoint groups, this parameter specifies the percentage of traffic that is routed to this endpoint group.
        # 
        # Valid values: **1** to **100**. Default value: **100**.
        # 
        # You can enter traffic dial values for up to 10 endpoint groups.
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
        if self.system_tag:
            for v1 in self.system_tag:
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
        result['EndpointConfigurations'] = []
        if self.endpoint_configurations is not None:
            for k1 in self.endpoint_configurations:
                result['EndpointConfigurations'].append(k1.to_map() if k1 else None)

        if self.endpoint_group_description is not None:
            result['EndpointGroupDescription'] = self.endpoint_group_description

        if self.endpoint_group_name is not None:
            result['EndpointGroupName'] = self.endpoint_group_name

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

        result['PortOverrides'] = []
        if self.port_overrides is not None:
            for k1 in self.port_overrides:
                result['PortOverrides'].append(k1.to_map() if k1 else None)

        result['SystemTag'] = []
        if self.system_tag is not None:
            for k1 in self.system_tag:
                result['SystemTag'].append(k1.to_map() if k1 else None)

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
        self.endpoint_configurations = []
        if m.get('EndpointConfigurations') is not None:
            for k1 in m.get('EndpointConfigurations'):
                temp_model = main_models.CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations()
                self.endpoint_configurations.append(temp_model.from_map(k1))

        if m.get('EndpointGroupDescription') is not None:
            self.endpoint_group_description = m.get('EndpointGroupDescription')

        if m.get('EndpointGroupName') is not None:
            self.endpoint_group_name = m.get('EndpointGroupName')

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

        self.port_overrides = []
        if m.get('PortOverrides') is not None:
            for k1 in m.get('PortOverrides'):
                temp_model = main_models.CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides()
                self.port_overrides.append(temp_model.from_map(k1))

        self.system_tag = []
        if m.get('SystemTag') is not None:
            for k1 in m.get('SystemTag'):
                temp_model = main_models.CreateEndpointGroupsRequestEndpointGroupConfigurationsSystemTag()
                self.system_tag.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateEndpointGroupsRequestEndpointGroupConfigurationsTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('ThresholdCount') is not None:
            self.threshold_count = m.get('ThresholdCount')

        if m.get('TrafficPercentage') is not None:
            self.traffic_percentage = m.get('TrafficPercentage')

        return self

class CreateEndpointGroupsRequestEndpointGroupConfigurationsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The tag key cannot be an empty string.
        # 
        # The tag key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can enter up to 20 tag keys.
        self.key = key
        # The value of the tag. The tag value can be an empty string.
        # 
        # The tag value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`.
        # 
        # You can enter up to 20 tag values.
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

class CreateEndpointGroupsRequestEndpointGroupConfigurationsSystemTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        scope: str = None,
        value: str = None,
    ):
        # This parameter is reserved.
        self.key = key
        # This parameter is reserved.
        self.scope = scope
        # This parameter is reserved.
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

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateEndpointGroupsRequestEndpointGroupConfigurationsPortOverrides(DaraModel):
    def __init__(
        self,
        endpoint_port: int = None,
        listener_port: int = None,
    ):
        # The endpoint port used for the port override.
        self.endpoint_port = endpoint_port
        # The listener port.
        # 
        # Valid values: **1** to **65499**.
        # 
        # > - For TCP listeners, you cannot configure port overrides for a virtual endpoint group. If a virtual endpoint group already exists for the listener, you cannot configure port overrides for the default endpoint group. If port overrides are configured for the default endpoint group, you cannot add a virtual endpoint group.
        # >
        # > - After you configure a port override, you cannot change the listener protocol, except for switching between HTTP and HTTPS.
        # >
        # > - When you modify the listener port range, the new range must include all listener ports that are used in the port overrides. For example, if the listener port range is 80-82 and a port override is configured to map listener ports to endpoint ports 100-102, you cannot change the listener port range to 80-81.
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

class CreateEndpointGroupsRequestEndpointGroupConfigurationsEndpointConfigurations(DaraModel):
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
        # Specifies whether to preserve client IP addresses. Valid values:
        # 
        # - **true**: preserves client IP addresses.
        # 
        # - **false** (default): does not preserve client IP addresses.
        # 
        # > * For endpoint groups of UDP and TCP listeners, the preserve client IP feature is disabled by default. You can enable this feature based on your business requirements.
        # >
        # > * For endpoint groups of HTTP and HTTPS listeners, the preserve client IP feature is enabled by default. Client IP addresses are preserved in the X-Forwarded-For header. You cannot disable this feature.
        # >
        # > * `EnableClientIPPreservation` and `EnableProxyProtocol` cannot be set to `true` at the same time.
        # >
        # > * For more information, see [preserve client IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_client_ippreservation = enable_client_ippreservation
        # Specifies whether to use the Proxy Protocol to preserve client IP addresses. Valid values:
        # 
        # - **true**: uses the Proxy Protocol to preserve client IP addresses.
        # 
        # - **false** (default): does not use the Proxy Protocol to preserve client IP addresses.
        # 
        # > * This parameter is available only for endpoint groups that are associated with TCP listeners.
        # >
        # > * `EnableClientIPPreservation` and `EnableProxyProtocol` cannot be set to `true` at the same time.
        # >
        # > * For more information, see [preserve client IP addresses](https://help.aliyun.com/document_detail/158080.html).
        self.enable_proxy_protocol = enable_proxy_protocol
        # The IP address or domain name of the endpoint.
        # 
        # In an endpoint group of an intelligent routing listener, you can enter a maximum of 100 endpoint IP addresses or domain names.
        self.endpoint = endpoint
        self.provider = provider
        # The private IP address of the elastic network interface (ENI).
        # 
        # > This parameter is available only when the endpoint type is **ENI**. If you do not specify this parameter, the system uses the primary private IP address of the ENI.
        self.sub_address = sub_address
        # The type of endpoint in an intelligent routing listener. Valid values:
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
        # - **OSS**: an OSS bucket.
        # 
        # - **ENI**: an elastic network interface.
        # 
        # - **NLB**: an NLB instance.
        # 
        # In an endpoint group of an intelligent routing listener, you can specify up to 100 endpoints.
        # 
        # > - If the routing type of the listener is **Standard** (intelligent routing), you must configure the endpoint group and endpoint information for the listener. This parameter is required.
        # >
        # > - If you set Type to **ECS**, **ENI**, **SLB**, or **IpTarget** and a service-linked role does not exist, the system automatically creates a service-linked role named AliyunServiceRoleForGaVpcEndpoint.
        # >
        # > - If you set Type to **ALB** and a service-linked role does not exist, the system automatically creates a service-linked role named AliyunServiceRoleForGaAlb.
        # >
        # > - If you set Type to **OSS** and a service-linked role does not exist, the system automatically creates a service-linked role named AliyunServiceRoleForGaOss.
        # >
        # > - If you set Type to **NLB** and a service-linked role does not exist, the system automatically creates a service-linked role named AliyunServiceRoleForGaNlb.
        # >
        # > > For more information, see [service-linked roles](https://help.aliyun.com/document_detail/178360.html).
        self.type = type
        # A list of VSwitch IDs.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC.
        # 
        # In an endpoint group of an intelligent routing listener, you can specify only one VPC ID.
        # 
        # > This parameter is required only when you set Type to **IpTarget**.
        self.vpc_id = vpc_id
        # The weight of the endpoint.
        # 
        # Valid values: **0** to **255**.
        # 
        # > If you set the weight of an endpoint to 0, Global Accelerator stops distributing traffic to the endpoint. Proceed with caution.
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

