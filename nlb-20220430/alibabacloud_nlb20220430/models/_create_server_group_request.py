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
        # The protocol version. Valid values:
        # 
        # - **ipv4** (default): IPv4.
        # 
        # - **DualStack**: dual-stack.
        self.address_ipversion = address_ipversion
        # Specifies whether to enable all-port forwarding. Valid values:
        # 
        # - **true**: enables all-port forwarding.
        # 
        # - **false** (default): disables all-port forwarding.
        self.any_port_enabled = any_port_enabled
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether to enable connection draining. Valid values:
        # 
        # - **true**: enables connection draining.
        # 
        # - **false** (default): disables connection draining.
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period for connection draining. Unit: seconds.
        # Valid values: **0** to **900**.
        self.connection_drain_timeout = connection_drain_timeout
        # Specifies whether to only precheck the request. Valid values:
        # - **true**: prechecks the request without creating the server group. The system checks whether required parameters are specified, the request format, and service limits. If the request fails the precheck, the corresponding error is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        # - **false** (default): sends the request. If the request passes the precheck, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The health check configuration.
        self.health_check_config = health_check_config
        # The traffic scheduling policy in dual-stack mode. Valid values:
        # 
        # - NonAffinity (default): non-affinity mode. Traffic is forwarded to healthy backend servers based on the scheduling algorithm regardless of the IP protocol version of the source.
        # - Affinity: affinity mode. Traffic is forwarded based on the IP protocol version of the request source. IPv4 requests are forwarded only to IPv4 backend servers, and IPv6 requests are forwarded only to IPv6 backend servers.
        # > This parameter takes effect only when **AddressIPVersion** is set to **DualStack**.
        self.ip_version_affinity_mode = ip_version_affinity_mode
        # Specifies whether to enable client IP address preservation. Valid values:
        # 
        # - **true** (default): enables client IP address preservation.
        # - **false**: disables client IP address preservation.
        # 
        # 
        # > 
        # > If **Protocol** is set to **TCP** and this parameter is set to **true**, the server group cannot be associated with **TCPSSL** listeners.
        self.preserve_client_ip_enabled = preserve_client_ip_enabled
        # The communication protocol used to forward traffic to backend servers. Valid values:
        # 
        # - **TCP** (default)
        # - **UDP**
        # - **TCP_UDP**
        # > 
        # > - If this parameter is set to **UDP**, the server group can be associated only with **UDP** listeners.
        # > - If this parameter is set to **TCP** and **PreserveClientIpEnabled** is set to **true**, the server group can be associated only with **TCP** listeners.
        # > - If this parameter is set to **TCP** and **PreserveClientIpEnabled** is set to **false**, the server group can be associated with **TCPSSL** and **TCP** listeners.
        # > - If this parameter is set to **TCP_UDP**, the server group can be associated with **TCP** and **UDP** listeners.
        self.protocol = protocol
        # The region ID of the Network Load Balancer (NLB) instance. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # The ID of the resource group to which the server group belongs.
        self.resource_group_id = resource_group_id
        # The scheduling algorithm. Valid values:
        # 
        # - **Wrr** (default): weighted round-robin. Backend servers with higher weights are more likely to be polled.
        # 
        # - **Wlc**: weighted least connections. In addition to the weight of each backend server, the actual load (number of connections) of the backend server is also considered. If the weights are the same, backend servers with fewer current connections are more likely to be polled.
        # 
        # - **rr**: round-robin. External requests are distributed to backend servers in sequence.
        # 
        # - **sch**: source IP hash. Requests from the same source IP address are scheduled to the same backend server.
        # 
        # - **tch**: 4-tuple hash. Consistent hashing based on the 4-tuple (source IP address, destination IP address, source port, and destination port). Requests from the same flow are scheduled to the same backend server.
        # 
        # - **qch**: QUIC ID hash. Requests with the same QUIC ID are scheduled to the same backend server.
        # 
        # > QUIC ID hash is supported only when the backend protocol is UDP.
        self.scheduler = scheduler
        # The name of the server group.
        # 
        # The name must be 2 to 128 characters in length, and must start with a letter or Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.server_group_name = server_group_name
        # The server group type. Valid values:
        # 
        # - **Instance** (default): server type. This type of server group supports adding **Ecs**, **Eni**, and **Eci** instances.
        # 
        # - **Ip**: IP address type. This type of server group supports directly adding backend servers by IP address.
        self.server_group_type = server_group_type
        # The list of tags.
        self.tag = tag
        # The ID of the VPC where the server group is deployed.
        # 
        # > If **ServerGroupType** is set to **Instance**, only servers in this VPC can be added to the server group.
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
        # The tag key. The tag key can be up to 64 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`. It can contain letters, digits, underscores (_), periods (.), colons (:), forward slashes (/), equal signs (=), plus signs (+), hyphens (-), and at signs (@).
        # 
        # You can add up to 20 tags in a single call.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length, and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`. It can contain letters, digits, underscores (_), periods (.), colons (:), forward slashes (/), equal signs (=), plus signs (+), hyphens (-), and at signs (@).
        # 
        # You can add up to 20 tags in a single call.
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
        # The port of the backend server used for health checks.
        # 
        # Valid values: **0** to **65535**.
        # 
        # Default value: **0**. This value indicates that the port of the backend server is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The maximum timeout period for a health check response. Unit: seconds.
        # Valid values: **1** to **300**.
        # Default value: **5**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name used for health checks. Valid values:
        # 
        # - **$SERVER_IP**: the internal IP address of the backend server.
        # 
        # - **domain**: a specified domain name. The domain name must be 1 to 80 characters in length, and can contain only letters, digits, hyphens (-), and periods (.).
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_domain = health_check_domain
        # Specifies whether to enable health checks. Valid values:
        # 
        # - **true** (default): enables health checks.
        # 
        # - **false**: disables health checks.
        self.health_check_enabled = health_check_enabled
        # The query string in the request for UDP listener health checks. The string can contain only letters and digits, and can be up to 512 characters in length.
        self.health_check_exp = health_check_exp
        # The HTTP status codes for healthy responses. Separate multiple status codes with commas (,).
        # Valid values: **http_2xx** (default), **http_3xx**, **http_4xx**, and **http_5xx**.
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_http_code = health_check_http_code
        # The HTTP protocol version for health checks. Valid values: **HTTP1.0** (default) and **HTTP1.1**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_http_version = health_check_http_version
        # The interval between two consecutive health checks. Unit: seconds. Default value: **5**.
        # 
        # - If **HealthCheckType** is set to **TCP** or **HTTP**, valid values are **1** to **50**.
        # - If **HealthCheckType** is set to **UDP**, valid values are **1** to **300**. You must set the interval to be greater than or equal to the response timeout period to ensure that UDP probe responses are not misjudged as unresponsive due to a timeout.
        self.health_check_interval = health_check_interval
        # The query string in the request for UDP listener health checks. The string can contain only letters and digits, and can be up to 512 characters in length.
        self.health_check_req = health_check_req
        # The protocol used for health checks. Valid values:
        # 
        # - **TCP**
        # - **HTTP**
        # - **UDP**
        self.health_check_type = health_check_type
        # The health check path.
        # 
        # The path must be 1 to 80 characters in length, and can contain only letters, digits, and the following special characters: `-/.%?#&`. It must start with a forward slash (/).
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_url = health_check_url
        # The number of consecutive successful health checks that must occur before the health check status of a backend server is changed from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        # 
        # Default value: **2**.
        self.healthy_threshold = healthy_threshold
        # The HTTP method used for health checks. Valid values: **GET** (default) and **HEAD**.
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.http_check_method = http_check_method
        # The number of consecutive failed health checks that must occur before the health check status of a backend server is changed from **success** to **fail**.
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

