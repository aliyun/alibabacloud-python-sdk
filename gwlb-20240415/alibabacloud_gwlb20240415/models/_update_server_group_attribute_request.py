# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gwlb20240415 import models as main_models
from darabonba.model import DaraModel

class UpdateServerGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connection_drain_config: main_models.UpdateServerGroupAttributeRequestConnectionDrainConfig = None,
        dry_run: bool = None,
        health_check_config: main_models.UpdateServerGroupAttributeRequestHealthCheckConfig = None,
        scheduler: str = None,
        server_failover_mode: str = None,
        server_group_id: str = None,
        server_group_name: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The configurations of connection draining.
        self.connection_drain_config = connection_drain_config
        # Specifies whether to perform only a dry run without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The health check configuration.
        self.health_check_config = health_check_config
        # The scheduling algorithm. Valid values:
        # 
        # *   **5TCH**: specifies consistent hashing that is based on the following factors: source IP address, destination IP address, source port, protocol, and destination port. Requests that contain the same information based on the preceding factors are forwarded to the same backend server.
        # *   **3TCH**: indicates consistent hashing that is based on the following factors: source IP address, destination IP address, and protocol. Requests that contain the same information based on the preceding factors are forwarded to the same backend server.
        # *   **2TCH**: specifies consistent hashing that is based on the following factors: source IP address and destination IP address. Requests that contain the same information based on the preceding factors are forwarded to the same backend server.
        self.scheduler = scheduler
        # Specifies how GWLB processes requests over existing connections when a backend server is not running as expected. Valid values:
        # 
        # *   **NoRebalance**: GWLB continues to forward requests over existing connections to the unavailable backend server.
        # *   **Rebalance**: GWLB forwards requests over existing connections to the remaining healthy backend servers.
        self.server_failover_mode = server_failover_mode
        # The server group ID.
        # 
        # This parameter is required.
        self.server_group_id = server_group_id
        # The server group name.
        # 
        # The name must be 2 to 128 characters in length, and can contain digits, periods (.), underscores (_), and hyphens (-). It must start with a letter.
        self.server_group_name = server_group_name

    def validate(self):
        if self.connection_drain_config:
            self.connection_drain_config.validate()
        if self.health_check_config:
            self.health_check_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_drain_config is not None:
            result['ConnectionDrainConfig'] = self.connection_drain_config.to_map()

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_failover_mode is not None:
            result['ServerFailoverMode'] = self.server_failover_mode

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionDrainConfig') is not None:
            temp_model = main_models.UpdateServerGroupAttributeRequestConnectionDrainConfig()
            self.connection_drain_config = temp_model.from_map(m.get('ConnectionDrainConfig'))

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('HealthCheckConfig') is not None:
            temp_model = main_models.UpdateServerGroupAttributeRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('HealthCheckConfig'))

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerFailoverMode') is not None:
            self.server_failover_mode = m.get('ServerFailoverMode')

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
        health_check_interval: int = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_req: str = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # The backend server port that is used for health checks.
        # 
        # Valid values: **1** to **65535**.
        self.health_check_connect_port = health_check_connect_port
        # The maximum timeout period for a health check response.
        # 
        # Unit: seconds.
        # 
        # Valid values: **1** to **300**.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name used for health checks. Valid values:
        # 
        # *   **$SERVER_IP**: the internal IP address of a backend server.
        # *   **domain**: a domain name. The domain name must be 1 to 80 characters in length, and can contain letters, digits, hyphens (-), and periods (.).
        # 
        # >  This parameter takes effect only if you set **HealthCheckProtocol** to **HTTP**.
        self.health_check_domain = health_check_domain
        # Specifies whether to enable health checks. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.health_check_enabled = health_check_enabled
        self.health_check_exp = health_check_exp
        # The HTTP status codes that the system returns for health checks.
        self.health_check_http_code = health_check_http_code
        # The interval at which health checks are performed.
        # 
        # Unit: seconds.
        # 
        # Valid values: **1** to **50**.
        self.health_check_interval = health_check_interval
        # The URL used for health checks.
        # 
        # The URL must be 1 to 80 characters in length, and can contain letters, digits, and the following special characters: ` - / . % ? # &  `It must start with a forward slash (/).
        # 
        # >  This parameter takes effect only if you set **HealthCheckProtocol** to **HTTP**.
        self.health_check_path = health_check_path
        # The protocol that is used for health checks. Valid values:
        # 
        # *   **TCP**: TCP health checks send TCP SYN packets to a backend server to check whether the port of the backend server is reachable.
        # *   **HTTP**: HTTP health checks simulate a process that uses a web browser to access resources by sending GET requests to an instance. These requests are used to check whether the instance is healthy.
        self.health_check_protocol = health_check_protocol
        self.health_check_req = health_check_req
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health check status of the backend server changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health check status of the backend server changes from **success** to **fail**.
        # 
        # Valid values: **2** to **10**.
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

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path

        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol

        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

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

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')

        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')

        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

class UpdateServerGroupAttributeRequestConnectionDrainConfig(DaraModel):
    def __init__(
        self,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
    ):
        # Specifies whether to enable connection draining. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period of connection draining.
        # 
        # Unit: seconds
        # 
        # Valid values: 1 to 3600.
        self.connection_drain_timeout = connection_drain_timeout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_drain_enabled is not None:
            result['ConnectionDrainEnabled'] = self.connection_drain_enabled

        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDrainEnabled') is not None:
            self.connection_drain_enabled = m.get('ConnectionDrainEnabled')

        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

        return self

