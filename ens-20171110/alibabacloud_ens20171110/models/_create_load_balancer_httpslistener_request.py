# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoadBalancerHTTPSListenerRequest(DaraModel):
    def __init__(
        self,
        backend_server_port: int = None,
        cookie: str = None,
        cookie_timeout: int = None,
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
        load_balancer_id: str = None,
        request_timeout: int = None,
        scheduler: str = None,
        server_certificate_id: str = None,
        sticky_session_type: str = None,
        unhealthy_threshold: int = None,
    ):
        # The backend port that is used by the ELB instance. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The cookie that is configured on the server. The cookie must be **1** to **200** characters in length and contain only ASCII characters and digits.
        # 
        # >  This parameter is required if you set StickySession to on and StickySessionType to server.
        self.cookie = cookie
        # The timeout period of a cookie. Valid values: **1** to **86400**. Unit: seconds.
        # 
        # >  This parameter is required if you set StickySession to on and StickySessionType to insert.
        self.cookie_timeout = cookie_timeout
        # The description of the listener. The description must be **1** to **80** characters in length.
        # 
        # >  The value cannot start with `http://` or `https://`.
        self.description = description
        # The listener port that is used to redirect HTTP requests to HTTPS.
        self.forward_port = forward_port
        # Indicates whether the health check feature is enabled. Valid values:
        # 
        # *   **on**
        # *   **off**
        # 
        # This parameter is required.
        self.health_check = health_check
        # The port that is used for health checks. Valid values: **1** to **65535**. If you leave this parameter empty, the port specified by BackendServerPort is used for health checks.
        # 
        # >  This parameter takes effect only if you set HealthCheck to on.
        self.health_check_connect_port = health_check_connect_port
        # The domain name that you want to use for health checks.
        # 
        # >  This parameter takes effect only if you set HealthCheck to on.
        self.health_check_domain = health_check_domain
        # The HTTP status code for a successful health check. Valid values:
        # 
        # *   **http_2xx** (default)
        # *   **http_3xx**
        # *   **http_4xx**
        # *   **http_5xx**
        # 
        # >  This parameter takes effect only if you set HealthCheck to on.
        self.health_check_http_code = health_check_http_code
        # The interval at which health checks are performed. Valid values: **1** to **50**. Default value: **2**. Unit: seconds.
        # 
        # >  This parameter takes effect only if you set HealthCheck to on.
        self.health_check_interval = health_check_interval
        # The HTTP request method for health checks. Valid values:
        # 
        # *   **head** (default): requests the head of the page.
        # *   **get**: requests the specified part of the page and returns the entity body.
        # 
        # >  This parameter takes effect only if the HealthCheck parameter is set to on.
        self.health_check_method = health_check_method
        # The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the server fails to pass the health check.
        # 
        # *   Default value: 5.
        # *   Valid values: **1** to **300**.
        # *   Unit: seconds.
        # 
        # > 
        # 
        # *   This parameter takes effect only if the HealthCheck parameter is set to on.
        # 
        # *   If the value of HealthCheckTimeout is smaller than the value of HealthCheckInterval, the timeout period specified by HealthCheckTimeout becomes invalid, and the value of HealthCheckInterval is used as the timeout period.
        self.health_check_timeout = health_check_timeout
        # The URI used for health checks. The URI must be **1** to **80** characters in length.
        # 
        # >  A URL must start with a forward slash (`/`) but cannot contain only forward slashes (`/`).
        self.health_check_uri = health_check_uri
        # The number of consecutive successful health checks that must occur before an unhealthy and inaccessible backend server is declared healthy and accessible. Valid values: **2** to **10**. Default value: **3**.
        # 
        # >  This parameter takes effect only if you set HealthCheck to on.
        self.healthy_threshold = healthy_threshold
        # The timeout period for idle connections. Default value: 15. Valid values: **1** to **60**. Unit: seconds.
        # 
        # >  If no request is received within the specified timeout period, ELB closes the connection. When another request is received, ELB establishes a new connection.
        self.idle_timeout = idle_timeout
        # Specifies whether to enable redirection from HTTP to HTTPS. Valid values:
        # 
        # *   **on**
        # *   **off** (default)
        self.listener_forward = listener_forward
        # The listening port that is used by Edge Load Balancer (ELB) to receive requests and forward the requests to backend servers. Valid values: **1** to **65535**.
        # 
        # >  We recommend that you use port 443 for HTTPS.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the Edge Load Balancer (ELB) instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The timeout period of requests. Default value: 60. Valid values: **1** to **180**. Unit: seconds.
        # 
        # >  If no response is received from the backend server within the specified timeout period, ELB returns an HTTP 504 error code to the client.
        self.request_timeout = request_timeout
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr** (default): Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **wlc**: Requests are distributed based on the weight and load of each backend server. The load refers to the number of connections on a backend server. If two backend servers have the same weight, the backend server that has fewer connections receives more requests.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # *   **sch**: consistent hashing based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # *   **qch**: consistent hashing based on QUIC connection IDs (CIDs). Requests that contain the same QUIC CID are distributed to the same backend server.
        # *   **iqch**: consistent hashing based on three specific bytes of iQUIC CIDs. Requests with the same second, third, and fourth bytes are distributed to the same backend server.
        self.scheduler = scheduler
        # The ID of the server certificate.
        # 
        # This parameter is required.
        self.server_certificate_id = server_certificate_id
        # The method that is used to handle cookies. Valid values:
        # 
        # *   **insert**: inserts a cookie. ELB inserts a session cookie (SERVERID) into the first HTTP or HTTPS response that is sent to a client. Subsequent requests to ELB carry this cookie, and ELB determines the destination servers of the requests based on the cookies.
        # *   **server**: rewrites the original cookie. SLB rewrites the custom cookies in requests from a client. Subsequent requests from the client that carry the new cookie are forwarded to the same backend server as the first request.
        # 
        # >  This parameter is required when the StickySession parameter is set to on.
        self.sticky_session_type = sticky_session_type
        # The number of consecutive failed health checks that must occur before a healthy and accessible backend server is declared unhealthy and inaccessible. Valid values: **2** to **10**. Default value: **3**.
        # 
        # >  This parameter takes effect only if you set HealthCheck to on.
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

        if self.cookie is not None:
            result['Cookie'] = self.cookie

        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout

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

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.request_timeout is not None:
            result['RequestTimeout'] = self.request_timeout

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.server_certificate_id is not None:
            result['ServerCertificateId'] = self.server_certificate_id

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')

        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

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

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('RequestTimeout') is not None:
            self.request_timeout = m.get('RequestTimeout')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('ServerCertificateId') is not None:
            self.server_certificate_id = m.get('ServerCertificateId')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

