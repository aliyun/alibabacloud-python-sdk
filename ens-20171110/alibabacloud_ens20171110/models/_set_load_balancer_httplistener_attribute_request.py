# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoadBalancerHTTPListenerAttributeRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_timeout: int = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        idle_timeout: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        request_timeout: int = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
        xforwarded_for: str = None,
    ):
        # The listener name. The name must be **1** to **80** characters in length.
        # 
        # > The name cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable health checks. Valid values:
        # - **on**: enabled.
        # - **off**: disabled.
        self.health_check = health_check
        # The port used for health checks. Valid values: **1** to **65535**. If this parameter is not configured in Settings, the backend service port (BackendServerPort) is used.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_connect_port = health_check_connect_port
        # The domain name used for health checks.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_domain = health_check_domain
        # The HTTP status code that indicates a successful health check. Valid values:
        # 
        # - **http_2xx** (default).
        # - **http_3xx**.
        # - **http_4xx**.
        # - **http_5xx**.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Valid values: **1** to **50**. Unit: seconds.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_interval = health_check_interval
        # The health check method for the HTTP listener. Valid values:
        # 
        # - **head**.
        # - **get**.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_method = health_check_method
        # The amount of time to wait for a response from a health check. If the backend ECS instance does not respond within the specified time, the health check fails.
        # - Default value: 5 seconds.
        # - Valid values: **1** to **300**.
        # - Unit: seconds.
        # > - This parameter takes effect only when HealthCheck is set to on.
        # >- If the value of HealthCheckTimeout is less than the value of HealthCheckInterval, HealthCheckTimeout becomes ineffective and the timeout period equals the value of HealthCheckInterval.
        self.health_check_timeout = health_check_timeout
        # The URI used for health checks. The URI must be **1** to **80** characters in length.
        # 
        # > - The URI cannot be only `/` but must start with `/`.
        # >- This parameter takes effect only when HealthCheck is set to on.
        self.health_check_uri = health_check_uri
        # The number of consecutive successful health checks required before a backend server is declared healthy (changing the status from fail to success). Valid values: **2** to **10**.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.healthy_threshold = healthy_threshold
        # The idle connection timeout period. Default value: 15 seconds. Valid values: **1** to **60**. Unit: seconds.
        # 
        # > If no access request is received within the timeout period, the load balancing instance temporarily breaks the current connection and re-establishes a new connection when the next request arrives.
        self.idle_timeout = idle_timeout
        # The listener port whose attributes you want to modify. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the load balancing instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The request timeout period. Default value: 60 seconds. Valid values: **1** to **180**. Unit: seconds.
        # 
        # > If no response is received from the backend server within the timeout period, the load balancing instance stops waiting and returns an HTTP 504 error code to the client.
        self.request_timeout = request_timeout
        # The scheduling algorithm. Valid values:
        # - **wrr**: Backend servers with higher weights are polled more frequently.
        # - **wlc**: Requests are distributed based on the weight and actual load (number of connections) of each backend server. When the weights are the same, backend servers with fewer connections are polled more frequently.
        # - **rr**: Requests are distributed to backend servers in sequence.
        # - **sch**: Consistent hashing based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # - **qch**: Consistent hashing based on QUIC Connection IDs. Requests with the same QUIC Connection ID are distributed to the same backend server.
        # - **iqch**: Consistent hashing based on specific three bytes of the iQUIC CID. Requests with the same 2nd to 4th bytes are distributed to the same backend server.
        self.scheduler = scheduler
        # The number of consecutive failed health checks required before a backend server is declared unhealthy (changing the status from success to fail). Valid values: **2** to **10**.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.unhealthy_threshold = unhealthy_threshold
        # Specifies whether to use the X-Forwarded-For header to retrieve the originating IP address of the client. Valid values:
        # - **on** (default): enabled.
        # - **off**: disabled.
        self.xforwarded_for = xforwarded_for

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain

        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method

        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout

        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.idle_timeout is not None:
            result['IdleTimeout'] = self.idle_timeout

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        if self.xforwarded_for is not None:
            result['XForwardedFor'] = self.xforwarded_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')

        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')

        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')

        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('IdleTimeout') is not None:
            self.idle_timeout = m.get('IdleTimeout')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        if m.get('XForwardedFor') is not None:
            self.xforwarded_for = m.get('XForwardedFor')

        return self

