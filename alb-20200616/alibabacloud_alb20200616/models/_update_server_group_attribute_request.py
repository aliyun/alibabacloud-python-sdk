# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class UpdateServerGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connection_drain_config: main_models.UpdateServerGroupAttributeRequestConnectionDrainConfig = None,
        cross_zone_enabled: bool = None,
        dry_run: bool = None,
        health_check_config: main_models.UpdateServerGroupAttributeRequestHealthCheckConfig = None,
        scheduler: str = None,
        server_group_id: str = None,
        server_group_name: str = None,
        service_name: str = None,
        slow_start_config: main_models.UpdateServerGroupAttributeRequestSlowStartConfig = None,
        sticky_session_config: main_models.UpdateServerGroupAttributeRequestStickySessionConfig = None,
        uch_config: main_models.UpdateServerGroupAttributeRequestUchConfig = None,
        upstream_keepalive_enabled: bool = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The configurations of connection draining.
        # 
        # After connection draining is enabled, SLB remains data transmission for a period of time after a backend server is removed or declared unhealthy.
        # 
        # > *   Basic SLB instances do not support connection draining. Standard and WAF-enabled SLB instances support connection draining.
        # > *   Server groups of the server and IP types support connection draining. Server groups of the Function Compute type do not support connection draining.
        self.connection_drain_config = connection_drain_config
        # Indicates whether cross-zone load balancing is enabled for the server group. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        # 
        # > *   Basic ALB instances do not support server groups that have cross-zone load balancing disabled. Only Standard and WAF-enabled ALB instances support server groups that have cross-zone load balancing.
        # >*   Cross-zone load balancing can be disabled for server groups of the server and IP type, but not for server groups of the Function Compute type.
        # >*   When cross-zone load balancing is disabled, session persistence cannot be enabled.
        self.cross_zone_enabled = cross_zone_enabled
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: checks the request without performing the operation. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a `2xx` HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The configuration of health checks.
        self.health_check_config = health_check_config
        # The scheduling algorithm. Valid values:
        # 
        # *   **Wrr**: the weighted round robin algorithm. Backend servers that have higher weights receive more requests than those that have lower weights.
        # *   **Wlc**: the weighted least connections algorithm. Requests are distributed based on the weights and the number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests.
        # *   **Sch**: the consistent hashing algorithm. Requests from the same source IP address are distributed to the same backend server.
        self.scheduler = scheduler
        # The server group ID.
        # 
        # This parameter is required.
        self.server_group_id = server_group_id
        # The server group name.
        # 
        # The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        self.server_group_name = server_group_name
        # This parameter is available only if the ALB Ingress controller is used. In this case, set this parameter to the name of the `Kubernetes Service` that is associated with the server group.
        self.service_name = service_name
        # The configurations of slow starts.
        # 
        # After slow starts are enabled, ALB prefetches data to newly added backend servers. Requests distributed to the backend servers gradually increase.
        # 
        # > *   Basic ALB instances do not support slow starts. Standard and WAF-enabled ALB instances support slow starts.
        # >*   Server groups of the instance and IP types support slow starts. Server groups of the Function Compute type do not support slow starts.
        # >*   Slow start is supported only by the weighted round-robin scheduling algorithm.
        self.slow_start_config = slow_start_config
        # The configuration of session persistence.
        self.sticky_session_config = sticky_session_config
        # The configurations of consistent hashing based on URLs.
        self.uch_config = uch_config
        # Specifies whether to enable persistent TCP connections.
        self.upstream_keepalive_enabled = upstream_keepalive_enabled

    def validate(self):
        if self.connection_drain_config:
            self.connection_drain_config.validate()
        if self.health_check_config:
            self.health_check_config.validate()
        if self.slow_start_config:
            self.slow_start_config.validate()
        if self.sticky_session_config:
            self.sticky_session_config.validate()
        if self.uch_config:
            self.uch_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.connection_drain_config is not None:
            result['ConnectionDrainConfig'] = self.connection_drain_config.to_map()

        if self.cross_zone_enabled is not None:
            result['CrossZoneEnabled'] = self.cross_zone_enabled

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.slow_start_config is not None:
            result['SlowStartConfig'] = self.slow_start_config.to_map()

        if self.sticky_session_config is not None:
            result['StickySessionConfig'] = self.sticky_session_config.to_map()

        if self.uch_config is not None:
            result['UchConfig'] = self.uch_config.to_map()

        if self.upstream_keepalive_enabled is not None:
            result['UpstreamKeepaliveEnabled'] = self.upstream_keepalive_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionDrainConfig') is not None:
            temp_model = main_models.UpdateServerGroupAttributeRequestConnectionDrainConfig()
            self.connection_drain_config = temp_model.from_map(m.get('ConnectionDrainConfig'))

        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('HealthCheckConfig') is not None:
            temp_model = main_models.UpdateServerGroupAttributeRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('HealthCheckConfig'))

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SlowStartConfig') is not None:
            temp_model = main_models.UpdateServerGroupAttributeRequestSlowStartConfig()
            self.slow_start_config = temp_model.from_map(m.get('SlowStartConfig'))

        if m.get('StickySessionConfig') is not None:
            temp_model = main_models.UpdateServerGroupAttributeRequestStickySessionConfig()
            self.sticky_session_config = temp_model.from_map(m.get('StickySessionConfig'))

        if m.get('UchConfig') is not None:
            temp_model = main_models.UpdateServerGroupAttributeRequestUchConfig()
            self.uch_config = temp_model.from_map(m.get('UchConfig'))

        if m.get('UpstreamKeepaliveEnabled') is not None:
            self.upstream_keepalive_enabled = m.get('UpstreamKeepaliveEnabled')

        return self

class UpdateServerGroupAttributeRequestUchConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the parameter. Only query strings are supported.
        # 
        # This parameter is required.
        self.type = type
        # The value of the parameter used for consistent hashing.
        # 
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class UpdateServerGroupAttributeRequestStickySessionConfig(DaraModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        sticky_session_enabled: bool = None,
        sticky_session_type: str = None,
    ):
        # The cookie to be configured on the server.
        # 
        # The cookie must be 1 to 200 characters in length and can contain only ASCII characters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($).
        # 
        # > This parameter takes effect when the **StickySessionEnabled** parameter is set to **true** and the **StickySessionType** parameter is set to **Server**.
        self.cookie = cookie
        # The timeout period of a cookie. Unit: seconds.
        # 
        # Valid values: **1** to **86400**.
        # 
        # > This parameter takes effect when the **StickySessionEnabled** parameter is set to **true** and the **StickySessionType** parameter is set to **Insert**.
        self.cookie_timeout = cookie_timeout
        # Specifies whether to enable session persistence. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.sticky_session_enabled = sticky_session_enabled
        # The method that is used to handle a cookie. Valid values:
        # 
        # *   **Insert**: inserts a cookie.
        # 
        # ALB inserts a cookie (SERVERID) into the first HTTP or HTTPS response packet that is sent to a client. The next request from the client contains this cookie and the listener forwards this request to the recorded backend server.
        # 
        # *   **Server**: rewrites a cookie.
        # 
        # When ALB detects a user-defined cookie, it overwrites the original cookie with the user-defined cookie. Subsequent requests to ALB carry this user-defined cookie, and ALB determines the destination servers of the requests based on the cookies.
        # 
        # > This parameter takes effect when the **StickySessionEnabled** parameter is set to **true** for the server group.
        self.sticky_session_type = sticky_session_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cookie is not None:
            result['Cookie'] = self.cookie

        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout

        if self.sticky_session_enabled is not None:
            result['StickySessionEnabled'] = self.sticky_session_enabled

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

        if m.get('StickySessionEnabled') is not None:
            self.sticky_session_enabled = m.get('StickySessionEnabled')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        return self

class UpdateServerGroupAttributeRequestSlowStartConfig(DaraModel):
    def __init__(
        self,
        slow_start_duration: int = None,
        slow_start_enabled: bool = None,
    ):
        # The duration of a slow start.
        self.slow_start_duration = slow_start_duration
        # Indicates whether slow starts are enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.slow_start_enabled = slow_start_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.slow_start_duration is not None:
            result['SlowStartDuration'] = self.slow_start_duration

        if self.slow_start_enabled is not None:
            result['SlowStartEnabled'] = self.slow_start_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlowStartDuration') is not None:
            self.slow_start_duration = m.get('SlowStartDuration')

        if m.get('SlowStartEnabled') is not None:
            self.slow_start_enabled = m.get('SlowStartEnabled')

        return self

class UpdateServerGroupAttributeRequestHealthCheckConfig(DaraModel):
    def __init__(
        self,
        health_check_codes: List[str] = None,
        health_check_connect_port: int = None,
        health_check_enabled: bool = None,
        health_check_host: str = None,
        health_check_http_version: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_path: str = None,
        health_check_protocol: str = None,
        health_check_timeout: int = None,
        healthy_threshold: int = None,
        unhealthy_threshold: int = None,
    ):
        # The HTTP status codes that indicate healthy backend servers.
        self.health_check_codes = health_check_codes
        # The backend port that is used for health checks.
        # 
        # Valid values: **0** to **65535**.
        # 
        # If you set the value to **0**, the backend port is used for health checks.
        # 
        # >  This parameter takes effect only if you set **HealthCheckEnabled** to **true**.
        self.health_check_connect_port = health_check_connect_port
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.health_check_enabled = health_check_enabled
        # The domain name that is used for health checks.
        # 
        # *   **Backend Server Internal IP** (default): Use the internal IP address of backend servers as the health check domain name.
        # 
        # *   **Custom Domain Name**: Enter a domain name.
        # 
        #     *   The domain name must be 1 to 80 characters in length.
        #     *   The domain name can contain lowercase letters, digits, hyphens (-), and periods (.).
        #     *   The domain name must contain at least one period (.) but cannot start or end with a period (.).
        #     *   The rightmost domain label of the domain name can contain only letters, and cannot contain digits or hyphens (-).
        #     *   The domain name cannot start or end with a hyphen (-).
        # 
        # >  This parameter takes effect only if **HealthCheckProtocol** is set to **HTTP**, **HTTPS**, or **gRPC**.
        self.health_check_host = health_check_host
        # The HTTP version that is used for health checks. Valid values:
        # 
        # *   **HTTP1.0**
        # *   **HTTP1.1**
        # 
        # >  This parameter takes effect only if you set **HealthCheckEnabled** to true and **HealthCheckProtocol** to **HTTP** or **HTTPS**.
        self.health_check_http_version = health_check_http_version
        # The interval at which health checks are performed. Unit: seconds.
        # 
        # Valid values: **1** to **50**.
        # 
        # >  This parameter takes effect only if you set **HealthCheckEnabled** to **true**.
        self.health_check_interval = health_check_interval
        # The HTTP method that is used for health checks. Valid values:
        # 
        # *   **GET**: If the length of a response exceeds 8 KB, the response is truncated. However, the health check result is not affected.
        # *   **POST**: gRPC health checks use the POST method by default.
        # *   **HEAD**: HTTP and HTTPS health checks use the HEAD method by default.
        # 
        # >  This parameter takes effect only if you set **HealthCheckEnabled** to true and **HealthCheckProtocol** to **HTTP**, **HTTPS**, or **gRPC**.
        self.health_check_method = health_check_method
        # The URL that is used for health checks.
        # 
        # The URL must be 1 to 80 characters in length, and can contain letters, digits, and the following special characters: `- / . % ? # & =`. It can also contain the following extended characters: `_ ; ~ ! ( ) * [ ] @ $ ^ : \\" , +`. The URL must start with a forward slash (`/`).
        # 
        # >  This parameter takes effect only if you set **HealthCheckEnabled** to **true** and **HealthCheckProtocol** to **HTTP** or **HTTPS**.
        self.health_check_path = health_check_path
        # The protocol that you want to use for health checks. Valid values:
        # 
        # *   **HTTP**: HTTP health checks simulate browser behaviors by sending HEAD or GET requests to probe the availability of backend servers.
        # *   **HTTPS**: HTTPS health checks simulate browser behaviors by sending HEAD or GET requests to probe the availability of backend servers. HTTPS supports encryption and provides higher security than HTTP.
        # *   **TCP**: TCP health checks send TCP SYN packets to a backend server to probe the availability of backend servers.
        # *   **gRPC**: gRPC health checks send POST or GET requests to a backend server to check whether the backend server is healthy.
        self.health_check_protocol = health_check_protocol
        # The timeout period of a health check response. If a backend ECS instance does not respond within the specified timeout period, the ECS instance fails the health check. Unit: seconds.
        # 
        # Valid values: **1** to **300**.
        # 
        # >  This parameter takes effect only if you set **HealthCheckEnabled** to **true**.
        self.health_check_timeout = health_check_timeout
        # The number of times that an unhealthy backend server must consecutively pass health checks before it can be declared healthy. In this case, the health check status of the backend server changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The number of times that a healthy backend server must consecutively fail health checks before it can be declared unhealthy. In this case, the health check status of the backend server changes from **success** to **fail**.
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
        if self.health_check_codes is not None:
            result['HealthCheckCodes'] = self.health_check_codes

        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_enabled is not None:
            result['HealthCheckEnabled'] = self.health_check_enabled

        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host

        if self.health_check_http_version is not None:
            result['HealthCheckHttpVersion'] = self.health_check_http_version

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method

        if self.health_check_path is not None:
            result['HealthCheckPath'] = self.health_check_path

        if self.health_check_protocol is not None:
            result['HealthCheckProtocol'] = self.health_check_protocol

        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckCodes') is not None:
            self.health_check_codes = m.get('HealthCheckCodes')

        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckEnabled') is not None:
            self.health_check_enabled = m.get('HealthCheckEnabled')

        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')

        if m.get('HealthCheckHttpVersion') is not None:
            self.health_check_http_version = m.get('HealthCheckHttpVersion')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')

        if m.get('HealthCheckPath') is not None:
            self.health_check_path = m.get('HealthCheckPath')

        if m.get('HealthCheckProtocol') is not None:
            self.health_check_protocol = m.get('HealthCheckProtocol')

        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')

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
        # Valid values: **0** to **900**.
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

