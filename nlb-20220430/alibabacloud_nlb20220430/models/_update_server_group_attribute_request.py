# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class UpdateServerGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        address_ipversion: str = None,
        client_token: str = None,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
        dry_run: bool = None,
        health_check_config: main_models.UpdateServerGroupAttributeRequestHealthCheckConfig = None,
        ip_version_affinity_mode: str = None,
        preserve_client_ip_enabled: bool = None,
        region_id: str = None,
        scheduler: str = None,
        server_group_id: str = None,
        server_group_name: str = None,
    ):
        # The IP version. Valid values: **ipv4** and **dualStack**.
        self.address_ipversion = address_ipversion
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is unique.
        self.client_token = client_token
        # Specifies whether to enable connection draining. Valid values:
        # 
        # - **true**: Enables connection draining.
        # 
        # - **false**: Disables connection draining.
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period for connection draining. Unit: seconds. Valid values: **0** to **900**.
        self.connection_drain_timeout = connection_drain_timeout
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without updating the server group. The system checks whether required parameters are specified, the request format is valid, and the service limits are met. If the request fails the dry run, an error message is returned. If the request passes the dry run, the DryRunOperation error code is returned.
        # - **false** (default): performs a dry run and sends the actual request. If the request passes the dry run, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The health check configuration.
        self.health_check_config = health_check_config
        # The traffic scheduling policy in dual-stack mode. Valid values:
        # 
        # - **NonAffinity**: non-affinity mode. Requests are forwarded to healthy backend servers based on the scheduling algorithm regardless of the IP version of the source address. This is the default value.
        # - **Affinity**: affinity mode. Requests are forwarded to backend servers based on the IP version of the source address. IPv4 requests are forwarded only to IPv4 backend servers, and IPv6 requests are forwarded only to IPv6 backend servers.
        # > This parameter takes effect only when **AddressIPVersion** is set to **DualStack**.
        self.ip_version_affinity_mode = ip_version_affinity_mode
        # Specifies whether to enable client IP preservation. Valid values:
        # 
        # - **true**: Enables client IP preservation.
        # 
        # - **false**: Disables client IP preservation.
        # 
        # > If **PreserveClientIpEnabled** is set to **false** and the server group is associated with a **TCPSSL** listener, you cannot change the value of this parameter to **true**.
        self.preserve_client_ip_enabled = preserve_client_ip_enabled
        # The region ID of the network load balancing instance.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to obtain the region ID.
        self.region_id = region_id
        # The scheduling algorithm. Valid values:
        # 
        # - **Wrr**: weighted round-robin. Backend servers with higher weights receive more requests.
        # 
        # - **Wlc**: weighted least connections. Requests are distributed based on the weights and actual loads (number of connections) of backend servers. If weights are the same, backend servers with fewer connections receive more requests.
        # 
        # - **rr**: round-robin. Requests are distributed to backend servers in sequence.
        # 
        # - **sch**: source IP hash. Requests from the same source IP address are distributed to the same backend server.
        # 
        # - **tch**: 4-tuple hash. Consistent hashing based on the 4-tuple (source IP address, destination IP address, source port, and destination port). Requests from the same flow are distributed to the same backend server.
        # 
        # - **qch**: QUIC ID hash. Requests with the same QUIC ID are distributed to the same backend server.
        # 
        # > QUIC ID hash is supported only when the backend protocol is UDP.
        self.scheduler = scheduler
        # The ID of the server group.
        # 
        # This parameter is required.
        self.server_group_id = server_group_id
        # The new name of the server group.
        # 
        # The name must be 2 to 128 characters in length, and must start with a letter or Chinese character. It can contain digits, periods (.), underscores (_), and hyphens (-).
        self.server_group_name = server_group_name

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')

        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('HealthCheckConfig') is not None:
            temp_model = main_models.UpdateServerGroupAttributeRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('HealthCheckConfig'))

        if m.get('IpVersionAffinityMode') is not None:
            self.ip_version_affinity_mode = m.get('IpVersionAffinityMode')

        if m.get('PreserveClientIpEnabled') is not None:
            self.preserve_client_ip_enabled = m.get('PreserveClientIpEnabled')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')

        return self

class UpdateServerGroupAttributeRequestHealthCheckConfig(DaraModel):
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
        # The port used for health checks on backend servers. Valid values: **0** to **65535**. A value of **0** indicates that the port of the backend server is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The maximum timeout period for a health check response. Unit: seconds. Valid values: **1** to **300**. Default value: **5**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name used for health checks. Valid values:
        # - **$SERVER_IP**: the internal IP address of the backend server.
        # - **domain**: a custom domain name. The domain name must be 1 to 80 characters in length, and can contain only lowercase letters, digits, hyphens (-), and periods (.).
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_domain = health_check_domain
        # Specifies whether to enable health checks. Valid values:
        # 
        # - **true**: Enables health checks.
        # 
        # - **false**: Disables health checks.
        self.health_check_enabled = health_check_enabled
        # The response string used for UDP health checks. The string can contain only letters and digits, and can be up to 512 characters in length.
        self.health_check_exp = health_check_exp
        # The HTTP status codes that indicate a successful health check. Separate multiple HTTP status codes with commas (,). Valid values: **http_2xx** (default), **http_3xx**, **http_4xx**, and **http_5xx**.
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_http_code = health_check_http_code
        # The HTTP version used for health checks. Valid values: **HTTP1.0** and **HTTP1.1**.
        # 
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_http_version = health_check_http_version
        # The interval between two consecutive health checks. Unit: seconds. Default value: **5**.
        # 
        # - If **HealthCheckType** is set to **TCP** or **HTTP**, valid values are **1** to **50**.
        # 
        # - If **HealthCheckType** is set to **UDP**, valid values are **1** to **300**. You must set the interval to a value greater than or equal to the response timeout period to ensure that UDP probe responses are not mistakenly identified as timeouts.
        self.health_check_interval = health_check_interval
        # The request string used for UDP health checks. The string can contain only letters and digits, and can be up to 512 characters in length.
        self.health_check_req = health_check_req
        # The health check protocol. Valid values:
        # 
        # - **TCP**
        # - **HTTP**
        # - **UDP**
        self.health_check_type = health_check_type
        # The health check path.
        # 
        # The path must be 1 to 80 characters in length. It can contain only letters, digits, the characters `-/.%?#&=`, and extension characters `_;~!()*[]@$^:\\",+`. It must start with a forward slash (/).
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.health_check_url = health_check_url
        # The number of consecutive successful health checks required to change the health status of a backend server from **Failed** to **Success**. Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The HTTP method used for health checks. Valid values: **GET** and **HEAD**.
        # > This parameter takes effect only when **HealthCheckType** is set to **HTTP**.
        self.http_check_method = http_check_method
        # The number of consecutive failed health checks required to change the health status of a backend server from **Success** to **Failed**. Valid values: **2** to **10**.
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

