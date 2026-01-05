# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alb20200616 import models as main_models
from darabonba.model import DaraModel

class ListServerGroupsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        server_groups: List[main_models.ListServerGroupsResponseBodyServerGroups] = None,
        total_count: int = None,
    ):
        # The number of entries returned per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. Valid values:
        # 
        # *   If **NextToken** is empty, no next page exists.
        # *   If **NextToken** is not empty, the value of NextToken can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The server groups.
        self.server_groups = server_groups
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.server_groups:
            for v1 in self.server_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ServerGroups'] = []
        if self.server_groups is not None:
            for k1 in self.server_groups:
                result['ServerGroups'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.server_groups = []
        if m.get('ServerGroups') is not None:
            for k1 in m.get('ServerGroups'):
                temp_model = main_models.ListServerGroupsResponseBodyServerGroups()
                self.server_groups.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServerGroupsResponseBodyServerGroups(DaraModel):
    def __init__(
        self,
        config_managed_enabled: bool = None,
        connection_drain_config: main_models.ListServerGroupsResponseBodyServerGroupsConnectionDrainConfig = None,
        create_time: str = None,
        cross_zone_enabled: bool = None,
        health_check_config: main_models.ListServerGroupsResponseBodyServerGroupsHealthCheckConfig = None,
        ipv_6enabled: bool = None,
        protocol: str = None,
        related_load_balancer_ids: List[str] = None,
        resource_group_id: str = None,
        scheduler: str = None,
        server_count: int = None,
        server_group_id: str = None,
        server_group_name: str = None,
        server_group_status: str = None,
        server_group_type: str = None,
        service_name: str = None,
        slow_start_config: main_models.ListServerGroupsResponseBodyServerGroupsSlowStartConfig = None,
        sticky_session_config: main_models.ListServerGroupsResponseBodyServerGroupsStickySessionConfig = None,
        tags: List[main_models.ListServerGroupsResponseBodyServerGroupsTags] = None,
        uch_config: main_models.ListServerGroupsResponseBodyServerGroupsUchConfig = None,
        upstream_keepalive_enabled: bool = None,
        vpc_id: str = None,
    ):
        # Indicates whether configuration management is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.config_managed_enabled = config_managed_enabled
        # The configurations of connection draining.
        # 
        # After connection draining is enabled, ALB maintains data transmission for a period of time after the backend server is removed or declared unhealthy.
        # > 
        # > - Basic ALB instances do not support connection draining. Standard and WAF-enabled ALB instances support connection draining. 
        # > -  Server groups of the instance and IP types support connection draining. Server groups of the Function Compute type do not support connection draining.
        self.connection_drain_config = connection_drain_config
        # The time when the resource was created.
        self.create_time = create_time
        # Indicates whether cross-zone load balancing is enabled. Valid values:
        # 
        # *   **true** (default)
        # *   **false**
        self.cross_zone_enabled = cross_zone_enabled
        # The health check configurations.
        self.health_check_config = health_check_config
        # Indicates whether IPv6 is supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.ipv_6enabled = ipv_6enabled
        # The backend protocol. Valid values:
        # 
        # *   **HTTP**: allows you to associate HTTPS, HTTP, or QUIC listeners with backend servers.
        # *   **HTTPS**: allows you to associate HTTPS listeners with backend servers.
        # *   **GRPC**: allows you to associate HTTPS and QUIC listeners with backend servers.
        self.protocol = protocol
        # The ID of the ALB instance associated with the server group.
        self.related_load_balancer_ids = related_load_balancer_ids
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **Wrr**: weighted round-robin. Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **Wlc**: weighted least connections. Requests are distributed based on the weight and load of each backend server. The load refers to the number of connections on a backend server. If multiple backend servers have the same weight, requests are forwarded to the backend server with the least number of connections.
        # *   **Sch**: consistent hashing. Requests that have the same hash factors are distributed to the same backend server. If you do not specify the UchConfig parameter, the source IP address is used as the hash factor by default. Requests that are from the same IP address are distributed to the same backend server. If you specify the UchConfig parameter, the URL string is used as the hash factor. Requests that have the same URL string are distributed to the same backend server.
        self.scheduler = scheduler
        # The number of backend servers in the server group.
        self.server_count = server_count
        # The server group ID.
        self.server_group_id = server_group_id
        # The server group name.
        self.server_group_name = server_group_name
        # The status of the server group. Valid values:
        # 
        # *   **Creating**.
        # *   **Available**
        # *   **Configuring**
        self.server_group_status = server_group_status
        # The server group type. Valid values:
        # 
        # *   **Instance**: instances, including ECS instances, ENIs, and elastic container instances.
        # *   **Ip**: IP addresses.
        # *   **Fc**: Function Compute
        self.server_group_type = server_group_type
        # The name of the server group.
        self.service_name = service_name
        # The configurations of slow starts.
        # 
        # After slow starts are enabled, ALB prefetches data to newly added backend servers. Requests distributed to the backend servers gradually increase.
        # 
        # > 
        # > - Basic ALB instances do not support slow starts. Standard and WAF-enabled ALB instances support slow starts.
        # > - Server groups of the instance and IP types support slow starts. Server groups of the Function Compute type do not support slow starts.
        # > - Slow start is supported only by the weighted round-robin scheduling algorithm.
        self.slow_start_config = slow_start_config
        # The configuration of session persistence.
        self.sticky_session_config = sticky_session_config
        # The tags that are added to the server group.
        self.tags = tags
        # The configuration of consistent hashing based on URLs.
        self.uch_config = uch_config
        # Indicates whether persistent TCP connections are enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.upstream_keepalive_enabled = upstream_keepalive_enabled
        # The ID of the VPC to which the ALB instance belongs.
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
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.uch_config:
            self.uch_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_managed_enabled is not None:
            result['ConfigManagedEnabled'] = self.config_managed_enabled

        if self.connection_drain_config is not None:
            result['ConnectionDrainConfig'] = self.connection_drain_config.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.cross_zone_enabled is not None:
            result['CrossZoneEnabled'] = self.cross_zone_enabled

        if self.health_check_config is not None:
            result['HealthCheckConfig'] = self.health_check_config.to_map()

        if self.ipv_6enabled is not None:
            result['Ipv6Enabled'] = self.ipv_6enabled

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.related_load_balancer_ids is not None:
            result['RelatedLoadBalancerIds'] = self.related_load_balancer_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_count is not None:
            result['ServerCount'] = self.server_count

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.server_group_name is not None:
            result['ServerGroupName'] = self.server_group_name

        if self.server_group_status is not None:
            result['ServerGroupStatus'] = self.server_group_status

        if self.server_group_type is not None:
            result['ServerGroupType'] = self.server_group_type

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.slow_start_config is not None:
            result['SlowStartConfig'] = self.slow_start_config.to_map()

        if self.sticky_session_config is not None:
            result['StickySessionConfig'] = self.sticky_session_config.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.uch_config is not None:
            result['UchConfig'] = self.uch_config.to_map()

        if self.upstream_keepalive_enabled is not None:
            result['UpstreamKeepaliveEnabled'] = self.upstream_keepalive_enabled

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigManagedEnabled') is not None:
            self.config_managed_enabled = m.get('ConfigManagedEnabled')

        if m.get('ConnectionDrainConfig') is not None:
            temp_model = main_models.ListServerGroupsResponseBodyServerGroupsConnectionDrainConfig()
            self.connection_drain_config = temp_model.from_map(m.get('ConnectionDrainConfig'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CrossZoneEnabled') is not None:
            self.cross_zone_enabled = m.get('CrossZoneEnabled')

        if m.get('HealthCheckConfig') is not None:
            temp_model = main_models.ListServerGroupsResponseBodyServerGroupsHealthCheckConfig()
            self.health_check_config = temp_model.from_map(m.get('HealthCheckConfig'))

        if m.get('Ipv6Enabled') is not None:
            self.ipv_6enabled = m.get('Ipv6Enabled')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RelatedLoadBalancerIds') is not None:
            self.related_load_balancer_ids = m.get('RelatedLoadBalancerIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerCount') is not None:
            self.server_count = m.get('ServerCount')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('ServerGroupName') is not None:
            self.server_group_name = m.get('ServerGroupName')

        if m.get('ServerGroupStatus') is not None:
            self.server_group_status = m.get('ServerGroupStatus')

        if m.get('ServerGroupType') is not None:
            self.server_group_type = m.get('ServerGroupType')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('SlowStartConfig') is not None:
            temp_model = main_models.ListServerGroupsResponseBodyServerGroupsSlowStartConfig()
            self.slow_start_config = temp_model.from_map(m.get('SlowStartConfig'))

        if m.get('StickySessionConfig') is not None:
            temp_model = main_models.ListServerGroupsResponseBodyServerGroupsStickySessionConfig()
            self.sticky_session_config = temp_model.from_map(m.get('StickySessionConfig'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListServerGroupsResponseBodyServerGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('UchConfig') is not None:
            temp_model = main_models.ListServerGroupsResponseBodyServerGroupsUchConfig()
            self.uch_config = temp_model.from_map(m.get('UchConfig'))

        if m.get('UpstreamKeepaliveEnabled') is not None:
            self.upstream_keepalive_enabled = m.get('UpstreamKeepaliveEnabled')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class ListServerGroupsResponseBodyServerGroupsUchConfig(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The parameter type. Valid value: QueryString.
        self.type = type
        # The hash value.
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

class ListServerGroupsResponseBodyServerGroupsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class ListServerGroupsResponseBodyServerGroupsStickySessionConfig(DaraModel):
    def __init__(
        self,
        cookie: str = None,
        cookie_timeout: int = None,
        sticky_session_enabled: bool = None,
        sticky_session_type: str = None,
    ):
        # The cookie configured for the server.
        self.cookie = cookie
        # The timeout period of the cookie. Unit: seconds. Valid values: **1** to **86400**.
        # 
        # >  This parameter takes effect only when **StickySessionEnabled** is set to **true** and **StickySessionType** is set to **Insert**.
        self.cookie_timeout = cookie_timeout
        # Indicates whether session persistence is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.sticky_session_enabled = sticky_session_enabled
        # The method that is used to handle the cookie. Valid values:
        # 
        # *   **insert**: inserts the cookie. The first time a client accesses ALB, ALB inserts the SERVERID cookie into the HTTP or HTTPS response packet. Subsequent requests from the client that carry this cookie are forwarded to the same backend server as the first request.
        # *   **Server**: rewrites the cookie. ALB rewrites the custom cookies in requests from a client. Subsequent requests from the client that carry the new cookie are forwarded to the same backend server as the first request.
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

class ListServerGroupsResponseBodyServerGroupsSlowStartConfig(DaraModel):
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

class ListServerGroupsResponseBodyServerGroupsHealthCheckConfig(DaraModel):
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
        # The backend port that is used for health checks. Valid values: **0** to **65535**.
        # 
        # A value of **0** indicates that the port of a backend server is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # Indicates whether the health check feature is enabled. Valid values:
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
        #     *   The domain name is 1 to 80 characters in length.
        #     *   The domain name contains lowercase letters, digits, hyphens (-), and periods (.).
        #     *   The domain name contains at least one period (.) but does not start or end with a period (.).
        #     *   The rightmost domain label of the domain name contains only letters, and does not contain digits or hyphens (-).
        #     *   The domain name does not start or end with a hyphen (-).
        # 
        # >  This parameter takes effect only if HealthCheckProtocol is set to HTTP, HTTPS, or gRPC.
        self.health_check_host = health_check_host
        # The HTTP version that is used for health checks.
        # 
        # Valid values: **HTTP1.0** and **HTTP1.1**.
        # 
        # >  This parameter takes effect only if **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        self.health_check_http_version = health_check_http_version
        # The interval at which health checks are performed. Unit: seconds. Valid values: **1** to **50**.
        self.health_check_interval = health_check_interval
        # The HTTP method that is used for health checks. Valid values:
        # 
        # *   **GET**: If the length of a response exceeds 8 KB, the response is truncated. However, the health check result is not affected.
        # *   **POST**: gRPC health checks use the POST method by default.
        # *   **HEAD**: HTTP and HTTPS health checks use the HEAD method by default.
        # 
        # >  This parameter takes effect only if **HealthCheckProtocol** is set to **HTTP**, **HTTPS**, or **gRPC**.
        self.health_check_method = health_check_method
        # The URL that is used for health checks.
        # 
        # >  This parameter takes effect only if **HealthCheckProtocol** is set to **HTTP** or **HTTPS**.
        self.health_check_path = health_check_path
        # The protocol that is used for health checks. Valid values:
        # 
        # *   **HTTP**: HTTP health checks simulate browser behaviors by sending HEAD or GET requests to probe the availability of backend servers.
        # *   **HTTPS**: HTTPS health checks simulate browser behaviors by sending HEAD or GET requests to probe the availability of backend servers. HTTPS supports encryption and provides higher security than HTTP.
        # *   **TCP**: TCP health checks send TCP SYN packets to a backend server to check whether the port of the backend server is reachable.
        # *   **gRPC**: gRPC health checks send POST or GET requests to a backend server to check whether the backend server is healthy.
        self.health_check_protocol = health_check_protocol
        # The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the backend server is declared unhealthy. Unit: seconds.
        self.health_check_timeout = health_check_timeout
        # The number of times that an unhealthy backend server must consecutively pass health checks before it is declared healthy. In this case, the health status is changed from **fail** to **success**.
        self.healthy_threshold = healthy_threshold
        # The number of times that a healthy backend server must consecutively fail health checks before it is declared unhealthy. In this case, the health status is changed from **success** to **fail**.
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

class ListServerGroupsResponseBodyServerGroupsConnectionDrainConfig(DaraModel):
    def __init__(
        self,
        connection_drain_enabled: bool = None,
        connection_drain_timeout: int = None,
    ):
        # Indicates whether connection draining is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.connection_drain_enabled = connection_drain_enabled
        # The timeout period of connection draining.
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

