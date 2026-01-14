# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class CreateServerGroupRequest(DaraModel):
    def __init__(
        self,
        address_ipversion: str = None,
        any_port_enabled: bool = None,
        client_token: str = None,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
        dry_run: bool = None,
        health_check_config: main_models.CreateServerGroupRequestHealthCheckConfig = None,
        ip_version_affinity_mode: str = None,
        preserve_client_ip_enabled: bool = None,
        protocol: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        scheduler: str = None,
        server_group_name: str = None,
        server_group_type: str = None,
        tag: List[main_models.CreateServerGroupRequestTag] = None,
        vpc_id: str = None,
    ):
        # The IP version. Valid values:
        # 
        # *   **ipv4** (default): IPv4
        # *   **DualStack**: dual-stack
        self.address_ipversion = address_ipversion
        # Specifies whether to enable multi-port forwarding. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.any_port_enabled = any_port_enabled
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token. Ensure that the token is unique among different requests. Only ASCII characters are allowed.
        # 
        # >  If you do not set this parameter, the value of **RequestId** is used.**** The value of **RequestId** is different for each request.
        self.client_token = client_token
        # Specifies whether to enable connection draining. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.connection_drain_enabled = connection_drain_enabled
        # Specifies a timeout period for connection draining. Unit: seconds. Valid values: **0** to **900**.
        self.connection_drain_timeout = connection_drain_timeout
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true:**: validates the request without performing the operation. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the validation, the corresponding error message is returned. If the request passes the validation, the `DryRunOperation` error code is returned.
        # *   **false** (default): validates the request and performs the operation. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The configurations of health checks.
        self.health_check_config = health_check_config
        self.ip_version_affinity_mode = ip_version_affinity_mode
        # Specifies whether to enable client IP preservation. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        # 
        # >  If you set this parameter to **true** and **Protocol** to **TCP**, the server group cannot be associated with **TCPSSL** listeners.
        self.preserve_client_ip_enabled = preserve_client_ip_enabled
        # The protocol between the NLB instance and backend servers. Valid values:
        # 
        # *   **TCP** (default)
        # *   **UDP**
        # *   **TCP_UDP**
        # 
        # > *   If you set this parameter to **UDP**, you can associate the server group only with **UDP** listeners.
        # > *   If you set this parameter to **TCP** and **PreserveClientIpEnabled** to **true**, you can associate the server group only with **TCP** listeners.
        # > *   If you set this parameter to **TCP** and **PreserveClientIpEnabled** to **false**, you can associate the server group with **TCPSSL** and **TCP** listeners.
        # > *   If you set this parameter to **TCP_UDP**, you can associate the server group with **TCP** and **UDP** listeners.
        self.protocol = protocol
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **Wrr** (default): weighted round-robin. Backend servers with higher weights receive more requests.
        # *   **Wlc**: weighted least connections. Requests are distributed based on the weights and the number of connections to backend servers. If multiple backend servers have the same weight, requests are forwarded to the backend server with the least connections.
        # *   **rr**: Requests are forwarded to backend servers in sequence.
        # *   **sch**: source IP hash. Requests from the same source IP address are forwarded to the same backend server.
        # *   **tch**: consistent hashing based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same four factors are forwarded to the same backend server.
        # *   **qch**: QUIC ID hash. Requests that contain the same QUIC ID are forwarded to the same backend server.
        # 
        # >  QUIC ID hash is supported only when the backend protocol is set to UDP.
        self.scheduler = scheduler
        # The server group name.
        # 
        # The name must be 2 to 128 characters in length, can contain digits, periods (.), underscores (_), and hyphens (-), and must start with a letter.
        # 
        # This parameter is required.
        self.server_group_name = server_group_name
        # The type of the server group. Valid values:
        # 
        # *   **Instance** (default): allows you to specify servers of the **Ecs**, **Eni**, or **Eci** type.
        # *   **Ip**: allows you to specify IP addresses.
        self.server_group_type = server_group_type
        # The tags.
        self.tag = tag
        # The ID of the virtual private cloud (VPC) where the server group is deployed.
        # 
        # >  If **ServerGroupType** is set to **Instance**, only servers in the specified VPC can be added to the server group.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.any_port_enabled is not None:
            result['AnyPortEnabled'] = self.any_port_enabled

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_drain_enabled is not None:
            result['ConnectionDrainEnabled'] = self.connection_drain_enabled

        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()

        if self.ip_version_affinity_mode is not None:
            result['IpVersionAffinityMode'] = self.ip_version_affinity_mode

        if self.preserve_client_ip_enabled is not None:
            result['PreserveClientIpEnabled'] = self.preserve_client_ip_enabled

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name

        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('AnyPortEnabled') is not None:
            self.any_port_enabled = m.get('AnyPortEnabled')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')

        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('HealthCheckConfig') is not None:
            temp_model = main_models.CreateServerGroupRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('HealthCheckConfig'))

        if m.get('IpVersionAffinityMode') is not None:
            self.ip_version_affinity_mode = m.get('IpVersionAffinityMode')

        if m.get('PreserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('PreserveClientIpEnabled')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')

        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateServerGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateServerGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. The tag key can be up to 64 characters in length, cannot start with `aliyun` or `acs:`, and cannot contain `http://` or `https://`. The tag key can contain letters, digits, and the following special characters: _ . : / = + - @
        # 
        # You can specify up to 20 tags in each call.
        self.key = key
        # The value of the tag. The tag value can be up to 128 characters in length, cannot start with `acs:` or `aliyun`, and cannot contain `http://` or `https://`. The tag value can contain letters, digits, and the following special characters: _ . : / = + - @
        # 
        # You can specify up to 20 tags in each call.
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

class CreateServerGroupRequestHealthCheckConfig(DaraModel):
    def __init__(
        self,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_enabled: bool = None,
        health_check_exp: str = None,
        health_check_http_code: List[str] = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        health_check_type: str = None,
        health_check_url: str = None,
        healthy_threshold: int = None,
        http_check_method: str = None,
        unhealthy_threshold: int = None,
    ):
        # The port that you want to use for health checks on backend servers.
        # 
        # Valid values: **0** to **65535**.
        # 
        # Default value: **0**. If you set this parameter to 0, the port that the backend server uses to provide services is also used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period for a health check response. Unit: seconds. Valid values: **1** to **300**. Default value: **5**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name that is used for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the internal IP address of a backend server.
        # *   **domain**: a domain name. The domain name must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), and periods (.).
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.health_check_domain = health_check_domain
        # Specifies whether to enable health checks. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.health_check_enabled = health_check_enabled
        # The response string that backend servers return to UDP listeners for health checks. The string must be 1 to 512 characters in length and can contain only letters and digits.
        self.health_check_exp = health_check_exp
        # The HTTP status codes to return for health checks. Separate multiple HTTP status codes with commas (,). Valid values: **http_2xx** (default), **http_3xx**, **http_4xx**, and **http_5xx**.
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.health_check_http_code = health_check_http_code
        # The HTTP version used for health checks. Valid values: **HTTP1.0** (default) and **HTTP1.1**.
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.health_check_http_version = health_check_http_version
        # The interval at which health checks are performed. Unit: seconds. Default value: **5**.
        # 
        # *   If you set **HealthCheckType** to **TCP** or **HTTP**, valid values are **1** to **50**.
        # *   If you set **HealthCheckType** to **UDP**, valid values are **1** to **300**. Set the health check interval equal to or larger than the response timeout period to ensure that UDP response timeouts are not determined as no responses.
        self.health_check_interval = health_check_interval
        # The request string that UDP listeners send to backend servers for health checks. The string must be 1 to 512 characters in length and can contain only letters and digits.
        self.health_check_req = health_check_req
        # The protocol that you want to use for health checks. Valid values:
        # 
        # *   **TCP**
        # *   **HTTP**
        # *   **UDP**
        self.health_check_type = health_check_type
        # The URL path to which health check probes are sent.
        # 
        # The URL path must be 1 to 80 characters in length, and can contain letters, digits, and the following special characters: ` - / . % ? # &  `. It must start with a forward slash (/).
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.health_check_url = health_check_url
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        # 
        # Default value: **2**.
        self.healthy_threshold = healthy_threshold
        # The HTTP method that is used for health checks. Valid values: **GET** (default) and **HEAD**.
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.http_check_method = http_check_method
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
        # 
        # Default value: **2**.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout

        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain

        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled

        if self.health_check_exp is not None:
            result['HealthCheckExp'] = self.health_check_exp

        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code

        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_url is not None:
            result['HealthCheckUrl'] = self.health_check_url

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.http_check_method is not None:
            result['HttpCheckMethod'] = self.http_check_method

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')

        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')

        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')

        if m.get('HealthCheckExp') is not None:
            self.health_check_exp = m.get('HealthCheckExp')

        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')

        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckUrl') is not None:
            self.health_check_url = m.get('HealthCheckUrl')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('HttpCheckMethod') is not None:
            self.http_check_method = m.get('HttpCheckMethod')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

