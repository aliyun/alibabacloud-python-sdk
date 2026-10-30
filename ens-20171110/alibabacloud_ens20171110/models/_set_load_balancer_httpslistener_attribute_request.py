# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoadBalancerHTTPSListenerAttributeRequest(DaraModel):
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
        server_certificate_id: str = None,
        unhealthy_threshold: int = None,
    ):
        # The name of the listener. The name must be **1** to **80** characters in length.
        # 
        # > It cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable the health check. Valid values:
        # - **on**: enables the health check.
        # - **off**: disables the health check.
        self.health_check = health_check
        # The port used for health checks. Valid values: **1** to **65535**. If the Settings for this parameter are not specified, the backend service port (BackendServerPort) is used.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_connect_port = health_check_connect_port
        # The domain name used for health checks.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_domain = health_check_domain
        # The HTTP status codes that indicate a successful health check. Valid values:
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
        # The HTTP method used for health checks. Valid values:
        # 
        # - **head** (default): requests only the header of the page.
        # - **get**: requests the specified page information and returns the entity body.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_method = health_check_method
        # The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the health check fails.
        # - Default value: 5.
        # - Valid values: **1** to **300**.
        # - Unit: seconds.
        # > - This parameter takes effect only when HealthCheck is set to on.
        # > - If the value of HealthCheckTimeout is less than the value of HealthCheckInterval, HealthCheckTimeout is invalid and the timeout period is the value of HealthCheckInterval.
        self.health_check_timeout = health_check_timeout
        # The URI used for health checks. The URI must be **1** to **80** characters in length.
        # > - The URI cannot be only `/`, but must start with `/`.
        # > - This parameter takes effect only when HealthCheck is set to on.
        self.health_check_uri = health_check_uri
        # The number of consecutive successful health checks that must occur before the health check status of a backend server changes from fail (unreachable) to success (reachable). Valid values: **2** to **10**.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.healthy_threshold = healthy_threshold
        # The idle connection timeout period. Default value: 15. Valid values: **1** to **60**. Unit: seconds.
        # > If there is no access request within the timeout period, load balancing temporarily breaks the current connection until a new connection is established when the next request arrives.
        self.idle_timeout = idle_timeout
        # The frontend port of the listener whose attributes you want to modify. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the load balancing instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The request timeout period. Default value: 60. Valid values: **1** to **180**. Unit: seconds.
        # > If a backend server does not send a response within the timeout period, load balancing stops waiting and returns an HTTP 504 error code to the client.
        self.request_timeout = request_timeout
        # The scheduling algorithm. Valid values:
        # - **wrr**: Backend servers with higher weights receive more requests.
        # - **wlc**: Requests are distributed based on the weights and actual loads (connections) of backend servers. If the weights are the same, backend servers with fewer connections receive more requests.
        # - **rr**: Requests are evenly distributed to backend servers in sequence.
        # - **sch**: Consistent hashing based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # - **qch**: Consistent hashing based on QUIC Connection IDs. Requests with the same QUIC Connection ID are distributed to the same backend server.
        # - **iqch**: Consistent hashing based on specific three bytes of the iQUIC CID. Requests with the same 2nd to 4th bytes are distributed to the same backend server.
        self.scheduler = scheduler
        # The ID of the server certificate.
        self.server_certificate_id = server_certificate_id
        # The number of consecutive failed health checks that must occur before the health check status of a backend server changes from success (reachable) to fail (unreachable). Valid values: **2** to **10**.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.unhealthy_threshold = unhealthy_threshold

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

        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

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

        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

