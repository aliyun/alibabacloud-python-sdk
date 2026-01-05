# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class CreateServerGroupRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        connection_drain_config: main_models.CreateServerGroupRequestConnectionDrainConfig = None,
        cross_zone_enabled: bool = None,
        dry_run: bool = None,
        health_check_config: main_models.CreateServerGroupRequestHealthCheckConfig = None,
        ipv_6enabled: bool = None,
        protocol: str = None,
        resource_group_id: str = None,
        scheduler: str = None,
        server_group_name: str = None,
        server_group_type: str = None,
        service_name: str = None,
        slow_start_config: main_models.CreateServerGroupRequestSlowStartConfig = None,
        sticky_session_config: main_models.CreateServerGroupRequestStickySessionConfig = None,
        tag: List[main_models.CreateServerGroupRequestTag] = None,
        uch_config: main_models.CreateServerGroupRequestUchConfig = None,
        upstream_keepalive_enabled: bool = None,
        vpc_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The configurations of connection draining.
        # 
        # After connection draining is enabled, ALB maintains data transmission for a period of time after the backend server is removed or declared unhealthy.
        # 
        # 
        # >*   Basic ALB instances do not support connection draining. Standard and WAF-enabled ALB instances support connection draining.
        # >*   Server groups of the instance and IP types support connection draining. Server groups of the Function Compute type do not support connection draining.
        self.connection_drain_config = connection_drain_config
        # Specifies whether to enable cross-zone load balancing. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        # 
        # > *   Basic ALB instances do not support server groups that have cross-zone load balancing disabled. Only Standard and WAF-enabled ALB instances support server groups that have cross-zone load balancing.
        # > *   Cross-zone load balancing can be disabled for server groups of the server and IP type, but not for server groups of the Function Compute type.
        # > *   When cross-zone load balancing is disabled, session persistence cannot be enabled.
        self.cross_zone_enabled = cross_zone_enabled
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, and service limits. If the request fails the dry run, an error code is returned. If the request passes the dry run, the `DryRunOperation` error code is returned.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, a 2xx HTTP status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The configuration of the health check feature.
        # 
        # This parameter is required.
        self.health_check_config = health_check_config
        # Specifies whether to enable Ipv6.
        self.ipv_6enabled = ipv_6enabled
        # The backend protocol. Valid values:
        # 
        # *   **HTTP**: allows you to associate an HTTPS, HTTP, or QUIC listener with the server group. This is the default value.
        # *   **HTTPS**: allows you to associate HTTPS listeners with backend servers.
        # *   **gRPC**: allows you to associate an HTTPS or QUIC listener with the server group.
        # 
        # >  You do not need to specify a backend protocol if you set **ServerGroupType** to **Fc**.
        self.protocol = protocol
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **Wrr** (default): The weighted round-robin algorithm is used. Backend servers that have higher weights receive more requests than those that have lower weights.
        # *   **Wlc**: The weighted least connections algorithm is used. Requests are distributed based on the weights and the number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections is expected to receive more requests.
        # *   **Sch**: The consistent hashing algorithm is used. Requests from the same source IP address are distributed to the same backend server.
        # 
        # > This parameter takes effect when the **ServerGroupType** parameter is set to **Instance** or **Ip**.
        self.scheduler = scheduler
        # The name of the server group. The name must be 2 to 128 characters in length, and can contain letters, digits, periods (.), underscores (_), and hyphens (-). The name must start with a letter.
        # 
        # This parameter is required.
        self.server_group_name = server_group_name
        # The type of server group. Valid values:
        # 
        # *   **Instance** (default): allows you to add servers by specifying **Ecs**, **Eni**, or **Eci**.
        # *   **Ip**: allows you to add servers by specifying IP addresses.
        # *   **Fc**: allows you to add servers by specifying functions of Function Compute.
        self.server_group_type = server_group_type
        # This parameter is available only if the ALB Ingress controller is used. In this case, set this parameter to the name of the `Kubernetes Service` that is associated with the server group.
        self.service_name = service_name
        # The configurations of slow starts.
        # After slow starts are enabled, SLB prefetches data to newly added backend servers. Requests distributed to the backend servers gradually increase.
        # 
        # > - Basic SLB instances do not support slow starts. Standard and WAF-enabled SLB instances support slow starts. 
        # >* Server groups of the server and IP types support slow starts. Server groups of the Function Compute type do not support slow starts.
        # >* Slow start is supported only by the weighted round-robin scheduling algorithm.
        self.slow_start_config = slow_start_config
        # The configuration of session persistence.
        # 
        # >  This parameter takes effect when the **ServerGroupType** parameter is set to **Instance** or **Ip**.
        self.sticky_session_config = sticky_session_config
        # The tag.
        self.tag = tag
        # The configuration of consistent hashing based on URLs.
        self.uch_config = uch_config
        # Specifies whether to enable persistent TCP connections.
        self.upstream_keepalive_enabled = upstream_keepalive_enabled
        # The ID of the virtual private cloud (VPC). You can add only servers that are deployed in the specified VPC to the server group.
        # 
        # >  This parameter takes effect when the **ServerGroupType** parameter is set to **Instance** or **Ip**.
        self.vpc_id = vpc_id

    def validate(self):
        if self.connection_drain_config:
            self.connection_drain_config.validate()
        if self.health_check_config:
            self.health_check_config.validate()
        if self.slow_start_config:
            self.slow_start_config.validate()
        if self.sticky_session_config:
            self.sticky_session_config.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
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

        if self.ipv_6enabled is not None:
            result['Ipv6Enabled'] = self.ipv_6enabled

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name

        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.slow_start_config is not None:
            result['SlowStartConfig'] = self.slow_start_config.to_map()

        if self.sticky_session_config is not None:
            result['StickySessionConfig'] = self.sticky_session_config.to_map()

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.uch_config is not None:
            result['UchConfig'] = self.uch_config.to_map()

        if self.upstream_keepalive_enabled is not None:
            result['UpstreamKeepaliveEnabled'] = self.upstream_keepalive_enabled

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConnectionDrainConfig') is not None:
            temp_model = main_models.CreateServerGroupRequestConnectionDrainConfig()
            self.connection_drain_config = temp_model.from_map(m.get('ConnectionDrainConfig'))

        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('HealthCheckConfig') is not None:
            temp_model = main_models.CreateServerGroupRequestHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('HealthCheckConfig'))

        if m.get('Ipv6Enabled') is not None:
            self.ipv_6enabled = m.get('Ipv6Enabled')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')

        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SlowStartConfig') is not None:
            temp_model = main_models.CreateServerGroupRequestSlowStartConfig()
            self.slow_start_config = temp_model.from_map(m.get('SlowStartConfig'))

        if m.get('StickySessionConfig') is not None:
            temp_model = main_models.CreateServerGroupRequestStickySessionConfig()
            self.sticky_session_config = temp_model.from_map(m.get('StickySessionConfig'))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateServerGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UchConfig') is not None:
            temp_model = main_models.CreateServerGroupRequestUchConfig()
            self.uch_config = temp_model.from_map(m.get('UchConfig'))

        if m.get('UpstreamKeepaliveEnabled') is not None:
            self.upstream_keepalive_enabled = m.get('UpstreamKeepaliveEnabled')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateServerGroupRequestUchConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the parameter.
        # 
        # This parameter is required.
        self.type = type
        # The parameter value for consistent hashing.
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

class CreateServerGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. The tag key can be up to 128 characters in length, and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
        self.key = key
        # The tag value. The tag value can be up to 128 characters in length, and cannot start with `acs:` or `aliyun`. It cannot contain `http://` or `https://`.
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

class CreateServerGroupRequestStickySessionConfig(DaraModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        sticky_session_enabled: bool = None,
        sticky_session_type: str = None,
    ):
        # The cookie that you want to configure for the server.
        # 
        # The cookie must be 1 to 200 characters in length, and can contain only ASCII letters and digits. It cannot contain commas (,), semicolons (;), or space characters. It cannot start with a dollar sign ($).
        # 
        # >  This parameter takes effect only when **StickySessionEnabled** is set to **true** and **StickySessionType** is set to **server**.
        self.cookie = cookie
        # The maximum amount of time to wait before the session cookie expires. Unit: seconds
        # 
        # Valid values: **1** to **86400**
        # 
        # Default value: **1000**
        # 
        # >  This parameter takes effect only when **StickySessionEnabled** is set to **true** and **StickySessionType** is set to **Insert**.
        self.cookie_timeout = cookie_timeout
        # Specifies whether to enable session persistence. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  This parameter takes effect when the **ServerGroupType** parameter is set to **Instance** or **Ip**.
        self.sticky_session_enabled = sticky_session_enabled
        # The method that is used to handle cookies. Valid values:
        # 
        # *   **Insert** (default value): inserts a cookie. The first time a client accesses ALB, ALB inserts the SERVERID cookie into the HTTP or HTTPS response packet. Subsequent requests from the client that carry this cookie are forwarded to the same backend server as the first request.
        # *   **Server**: rewrites a cookie. ALB rewrites the custom cookies in requests from a client. Subsequent requests from the client that carry the new cookie are forwarded to the same backend server as the first request.
        # 
        # >  This parameter takes effect when the **StickySessionEnabled** parameter is set to **true**.
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

class CreateServerGroupRequestSlowStartConfig(DaraModel):
    def __init__(
        self,
        slow_start_duration: int = None,
        slow_start_enabled: bool = None,
    ):
        # The duration of a slow start.
        # Valid values: 30 to 900.
        # Default value: 30.
        self.slow_start_duration = slow_start_duration
        # Specifies whether to enable slow starts. Valid values:
        # 
        # - true
        # 
        # - false(default)
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

class CreateServerGroupRequestHealthCheckConfig(DaraModel):
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
        # The HTTP status code that indicates healthy backend servers.
        self.health_check_codes = health_check_codes
        # The backend port that is used for health checks.
        # 
        # Valid values: **0** to **65535**
        # 
        # The default value is **0**, which specifies that the port of a backend server is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # >  If the **ServerGroupType** parameter is set to **Instance** or **Ip**, the health check feature is enabled by default. If the **ServerGroupType** parameter is set to **Fc**, the health check feature is disabled by default.
        # 
        # This parameter is required.
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
        # The version of the HTTP protocol. Valid values: **HTTP1.0** and **HTTP1.1**. Default value: HTTP1.1.
        # 
        # >  This parameter takes effect only if **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        self.health_check_http_version = health_check_http_version
        # The interval at which health checks are performed. Unit: seconds
        # 
        # Valid values: **1** to **50**
        # 
        # Default value: **2**.
        self.health_check_interval = health_check_interval
        # The HTTP method that is used for health checks. Valid values:
        # 
        # *   **GET**: If the length of a response exceeds 8 KB, the response is truncated. However, the health check result is not affected.
        # *   **POST**: By default, gRPC health checks use the POST method.
        # *   **HEAD** (default): By default, HTTP and HTTPS use the HEAD method.
        # 
        # >  This parameter takes effect only if **HealthCheckProtocol** is set to **HTTP**, **HTTPS**, or **gRPC**.
        self.health_check_method = health_check_method
        # The URL that is used for health checks.
        # 
        # The URL must be 1 to 80 characters in length, and can contain letters, digits, and the following special characters: `- / . % ? # & =`. It can also contain the following extended characters: `_ ; ~ ! ( ) * [ ] @ $ ^ : \\" , +`. The URL must start with a forward slash (/).
        # 
        # >  This parameter takes effect only if **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        self.health_check_path = health_check_path
        # The protocol that is used for health checks. Valid values:
        # 
        # *   **HTTP**: HTTP health checks simulate browser behaviors by sending HEAD or GET requests to probe the availability of backend servers.
        # *   **HTTPS**: HTTPS health checks simulate browser behaviors by sending HEAD or GET requests to probe the availability of backend servers. HTTPS provides higher security than HTTP because HTTPS supports data encryption.
        # *   **TCP**: TCP health checks send TCP SYN packets to a backend server to probe the availability of backend servers.
        # *   **gRPC**: gRPC health checks send POST or GET requests to a backend server to check whether the backend server is healthy.
        self.health_check_protocol = health_check_protocol
        # The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Unit: seconds
        # 
        # Valid values: **1** to **300**
        # 
        # Default value: **5**
        self.health_check_timeout = health_check_timeout
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health check status of the backend server changes from **fail** to **success**.
        # 
        # Valid values: **2** to **10**
        # 
        # Default value: **3**.
        self.healthy_threshold = healthy_threshold
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health check status of the backend server changes from **success** to **fail**.
        # 
        # Valid values: **2** to **10**
        # 
        # Default value: **3**
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

class CreateServerGroupRequestConnectionDrainConfig(DaraModel):
    def __init__(
        self,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
    ):
        # Specifies whether to enable connection draining. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period of connection draining.
        # 
        # Valid values: **0** to **900**.
        # 
        # Default value: **300**.
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

