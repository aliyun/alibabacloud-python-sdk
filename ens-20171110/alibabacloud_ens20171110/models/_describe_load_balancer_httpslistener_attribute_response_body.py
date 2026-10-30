# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLoadBalancerHTTPSListenerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        backend_server_port: int = None,
        bandwidth: int = None,
        description: str = None,
        forward_port: int = None,
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
        listener_forward: str = None,
        listener_port: int = None,
        request_id: str = None,
        request_timeout: int = None,
        scheduler: str = None,
        server_certificate_id: str = None,
        status: str = None,
        unhealthy_threshold: int = None,
    ):
        # The port used by the backend server of the load balancer instance. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The peak bandwidth of the load balancer. Default value: -1, which indicates that bandwidth is not limited.
        self.bandwidth = bandwidth
        # The description of the listener. The description must be **1** to **80** characters in length.
        self.description = description
        # The HTTP-to-HTTPS forwarding port for the listener.
        self.forward_port = forward_port
        # Specifies whether to enable the health check. Valid values:
        # - **on**: Enables the health check.
        # - **off**: Disables the health check.
        self.health_check = health_check
        # The port used for health checks. Valid values: **1** to **65535**. If this parameter is not specified, the backend server port (BackendServerPort) is used.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_connect_port = health_check_connect_port
        # The domain name used for health checks.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_domain = health_check_domain
        # The HTTP status codes that indicate a successful health check. Valid values:
        # 
        # - **http_2xx** (default)
        # - **http_3xx**
        # - **http_4xx**
        # - **http_5xx**
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Valid values: **1** to **50**. Unit: seconds.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_interval = health_check_interval
        # The HTTP method used for health checks. Valid values:
        # 
        # - **head**: Requests only the header of the page.
        # - **get**: Requests the specified page information and returns the entity body.
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_method = health_check_method
        # The timeout period for receiving a response from a health check. If the backend ENS instance does not respond within the specified timeout period, the health check fails.
        # - Default value: 5.
        # - Valid values: **1** to **300**.
        # - Unit: seconds.
        # > - This parameter takes effect only when HealthCheck is set to on.
        # > - If the value of HealthCheckTimeout is less than the value of HealthCheckInterval, HealthCheckTimeout is invalid and the timeout period is the value of HealthCheckInterval.
        self.health_check_timeout = health_check_timeout
        # The URI used for health checks. The URI must be **1** to **80** characters in length.
        # - The URI cannot be only a forward slash (`/`), but must start with a forward slash.
        # - This parameter takes effect only when HealthCheck is set to on.
        self.health_check_uri = health_check_uri
        # The number of consecutive successful health checks required to change the health check status of a backend server from fail (unreachable) to success (reachable). Valid values: **2** to **10**.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.healthy_threshold = healthy_threshold
        # The idle connection timeout period. Default value: 15. Valid values: **1** to **60**. Unit: seconds.
        # > If no access request is received within the timeout period, the load balancer temporarily interrupts the current connection and establishes a new connection when the next request arrives.
        self.idle_timeout = idle_timeout
        # Specifies whether to enable HTTP-to-HTTPS forwarding. Valid values:
        # 
        # - **on**: Enables HTTP-to-HTTPS forwarding.
        # - **off**: Disables HTTP-to-HTTPS forwarding.
        self.listener_forward = listener_forward
        # The frontend port used by the load balancer instance. Valid values: **1** to **65535**.
        self.listener_port = listener_port
        # The request ID.
        self.request_id = request_id
        # The request timeout period. Default value: 60. Valid values: **1** to **180**. Unit: seconds.
        # > If no response is received from the backend server within the timeout period, the load balancer stops waiting and returns an HTTP 504 error code to the client.
        self.request_timeout = request_timeout
        # The scheduling algorithm. Valid values:
        # - **wrr**: Backend servers with higher weights are polled more frequently.
        # - **wlc**: In addition to the weight of each backend server, the actual load (number of connections) of the backend server is also considered. If the weights are the same, backend servers with fewer current connections are polled more frequently.
        # - **rr**: External requests are distributed to backend servers in sequence.
        # - **sch**: Consistent hashing based on source IP addresses. Requests from the same source IP address are scheduled to the same backend server.
        # - **qch**: Consistent hashing based on QUIC Connection IDs. Requests with the same QUIC Connection ID are scheduled to the same backend server.
        # - **iqch**: Consistent hashing based on three specific bytes of the iQUIC CID. Requests with the same 2nd to 4th bytes are scheduled to the same backend server.
        self.scheduler = scheduler
        # The ID of the server certificate.
        self.server_certificate_id = server_certificate_id
        # The current status of the listener. Valid values:
        # 
        # - **Running**: The listener is running normally.
        # - **Stopped**: The listener is stopped.
        # - **Starting**: The listener is starting.
        # - **Configuring**: The listener is being configured.
        # - **Stopping**: The listener is being stopped.
        self.status = status
        # The number of consecutive failed health checks required to change the health check status of a backend server from success (reachable) to fail (unreachable). Valid values: **2** to **10**.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backend_server_port is not None:
            result['BackendServerPort'] = self.backend_server_port

        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.description is not None:
            result['Description'] = self.description

        if self.forward_port is not None:
            result['ForwardPort'] = self.forward_port

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

        if self.listener_forward is not None:
            result['ListenerForward'] = self.listener_forward

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id

        if self.status is not None:
            result['Status'] = self.status

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')

        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ForwardPort') is not None:
            self.forward_port = m.get('ForwardPort')

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

        if m.get('ListenerForward') is not None:
            self.listener_forward = m.get('ListenerForward')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

