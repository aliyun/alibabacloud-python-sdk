# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_nlb20220430 import models as main_models
from darabonba.model import DaraModel

class UpdateServerGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
        dry_run: bool = None,
        health_check_config: main_models.UpdateServerGroupAttributeRequestHealthCheckConfig = None,
        preserve_client_ip_enabled: bool = None,
        region_id: str = None,
        scheduler: str = None,
        server_group_id: str = None,
        server_group_name: str = None,
    ):
        # The client token used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token. Ensure that the token is unique among different requests. Only ASCII characters are allowed.
        # 
        # >  If you do not specify this parameter, the value of **RequestId** is used.**** The value of **RequestId** is different for each request.
        self.client_token = client_token
        # Specifies whether to enable connection draining. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.connection_drain_enabled = connection_drain_enabled
        # Specify a timeout period for connection draining. Unit: seconds. Valid values: **0** to **900**.
        self.connection_drain_timeout = connection_drain_timeout
        # Specifies whether to perform a dry run. Valid values:
        # 
        # *   **true**: validates the request without performing the operation. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the validation, the corresponding error message is returned. If the request passes the validation, the `DryRunOperation` error code is returned.
        # *   **false** (default): validates the request and performs the operation. If the request passes the validation, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # Health check configurations.
        self.health_check_config = health_check_config
        # Specifies whether to enable client IP preservation. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  You cannot set this parameter to **true** if **PreserveClientIpEnabled** is set to **false** and the server group is associated with a listener that uses **SSL over TCP**.
        self.preserve_client_ip_enabled = preserve_client_ip_enabled
        # The ID of the region where the NLB instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/443657.html) operation to query the most recent region list.
        self.region_id = region_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **Wrr**: weighted round-robin. Backend servers with higher weights receive more requests.
        # *   **Wlc**: weighted least connections. Requests are distributed based on the weight and load of each backend server. The load refers to the number of connections on a backend server. If multiple backend servers have the same weight, requests are forwarded to the backend server with the least connections.
        # *   **rr**: Requests are forwarded to backend servers in sequence.
        # *   **sch**: source IP hash. Requests from the same source IP address are forwarded to the same backend server.
        # *   **tch**: consistent hashing based on four factors: source IP address, destination IP address, source port, and destination port. Requests that contain the same four factors are forwarded to the same backend server.
        # *   **qch**: QUIC ID hash. Requests that contain the same QUIC ID are forwarded to the same backend server.
        # 
        # >  QUIC ID hash is supported only when the backend protocol is set to UDP.
        self.scheduler = scheduler
        # The server group ID.
        # 
        # This parameter is required.
        self.server_group_id = server_group_id
        # The new name of the server group.
        # 
        # The name must be 2 to 128 characters in length, can contain digits, periods (.), underscores (_), and hyphens (-), and must start with a letter.
        self.server_group_name = server_group_name

    def validate(self):
        if self.health_check_config:
            self.health_check_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        # The backend port that is used for health checks. Valid values: **0** to **65535**. If you set this parameter to **0**, the port that the backend server uses to provide services is also used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period for a health check response. Unit: seconds. Valid values: **1 to 300**. Default value: **5**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name used for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the internal IP address of a backend server.
        # *   **domain**: the specified domain name. The domain name must be 1 to 80 characters in length, and can contain lowercase letters, digits, hyphens (-), and periods (.).
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.health_check_domain = health_check_domain
        # Specifies whether to enable health checks. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.health_check_enabled = health_check_enabled
        # The response string of UDP health checks. The string must be 1 to 512 characters in length, and can contain letters and digits.
        self.health_check_exp = health_check_exp
        # The HTTP status codes to return for health checks. Separate multiple HTTP status codes with commas (,). Valid values: **http_2xx** (default), **http_3xx**, **http_4xx**, and **http_5xx**.
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.health_check_http_code = health_check_http_code
        # The version of the HTTP protocol. Valid values: **HTTP1.0** and **HTTP1.1**.
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.health_check_http_version = health_check_http_version
        # The interval at which health checks are performed. Unit: seconds. Default value: **5**.
        # 
        # *   If you set **HealthCheckType** to **TCP** or **HTTP**, valid values are **1 to 50**.
        # *   If you set **HealthCheckType** to **UDP**, valid values are **1 to 300**. Set the health check interval equal to or larger than the response timeout period to ensure that UDP response timeouts are not determined as no responses.
        self.health_check_interval = health_check_interval
        # The request string of UDP health checks. The string must be 1 to 512 characters in length, and can contain letters and digits.
        self.health_check_req = health_check_req
        # The protocol that is used for health checks. Valid values:
        # 
        # *   **TCP**
        # *   **HTTP**
        # *   **UDP**
        self.health_check_type = health_check_type
        # The path to which health check probes are sent.
        # 
        # The path must be 1 to 80 characters in length and can contain only letters, digits, and the following special characters: `- / . % ? # & =`. It can also contain the following extended characters: `_ ; ~ ! ( ) * [ ] @ $ ^ : \\" , +`. It must start with a forward slash (/).
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.health_check_url = health_check_url
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status changes from **fail** to **success**. Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The HTTP method used for health checks. Valid values: **GET** and **HEAD**.
        # 
        # >  This parameter takes effect only if you set **HealthCheckType** to **HTTP**.
        self.http_check_method = http_check_method
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status changes from **success** to **fail**. Valid values: **2** to **10**.
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

