# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoadBalancerTCPListenerRequest(DaraModel):
    def __init__(
        self,
        backend_server_port: int = None,
        description: str = None,
        eip_transmit: str = None,
        established_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        persistence_timeout: int = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
    ):
        # The port used by the backend ELB server of the ELB instance. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The name of the listener. The value must be **1** to **80** characters in length.
        # 
        # >  The value cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable elastic IP address (EIP) pass-through. Valid values:
        # 
        # *   **on**
        # *   **off** (default)
        self.eip_transmit = eip_transmit
        # The timeout period of a connection. Valid values: **10** to **900**. Default value: **900**. Unit: seconds.
        self.established_timeout = established_timeout
        # The port that is used for health checks. Valid values: **1** to **65535**. If you leave this parameter empty, the port specified for BackendServerPort is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period of a health check response. If a backend server does not respond within the specified timeout period, the server fails the health check.
        # 
        # *   Default value: 5.
        # *   Valid values: **1** to **300**.
        # *   Unit: seconds.
        # 
        # >  If the value of the HealthCheckConnectTimeout parameter is smaller than that of the HealthCheckInterval parameter, the timeout period specified by the HealthCheckConnectTimeout parameter is ignored and the period of time specified by the HealthCheckInterval parameter is used as the timeout period.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name that you want to use for health checks.
        self.health_check_domain = health_check_domain
        # The HTTP status codes for a successful health check. Valid values:
        # 
        # *   **http_2xx** (default)
        # *   **http_3xx**.
        # *   **http_4xx**
        # *   **http_5xx**
        self.health_check_http_code = health_check_http_code
        # The interval at which health checks are performed. Valid values: **1** to **50**. Default value: **2**. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The type of health checks. Valid values:
        # 
        # *   **tcp** (default)
        # *   **http**
        self.health_check_type = health_check_type
        # The Uniform Resource Identifier (URI) that you want to use for health checks. The URI must be **1** to **80** characters in length.
        # 
        # >  The URL must start with `/` and contain characters other than `/`.
        self.health_check_uri = health_check_uri
        # The number of consecutive successful health checks that must occur before an unhealthy and inaccessible backend server is declared healthy and accessible. Valid values: **2** to **10**. Default value: **3**.
        self.healthy_threshold = healthy_threshold
        # The listener port that is used by Edge Load Balancer (ELB) to receive requests and forward the requests to backend servers. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the Edge Load Balancer (ELB) instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The timeout period of session persistence.
        # 
        # *   Default value: 0. If the default value is used, the system disables session persistence.
        # *   Valid values: **0** to **3600**.
        # *   Unit: seconds.
        self.persistence_timeout = persistence_timeout
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr** (default): Backend servers with higher weights receive more requests than backend servers with lower weights.
        # *   **wlc**: Requests are distributed based on the weights and number of connections to backend servers. If two backend servers have the same weight, the backend server that has fewer connections receives more requests.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # *   **sch**: consistent hashing based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # *   **qch**: consistent hashing based on QUIC connection IDs (CIDs). Requests that contain the same QUIC CID are distributed to the same backend server.
        # *   **iqch**: consistent hashing based on three specific bytes of iQUIC CIDs. Requests with the same second, third, and fourth bytes are distributed to the same backend server.
        self.scheduler = scheduler
        # The number of consecutive failed health checks that must occur before a healthy and accessible backend server is declared unhealthy and inaccessible. Valid values: **2** to **10**. Default value: **3**.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.eip_transmit is not None:
            result['EipTransmit'] = self.eip_transmit

        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout

        if self.health_check_connect_port is not None:
            result['HealthCheckConnectPort'] = self.health_check_connect_port

        if self.health_check_connect_timeout is not None:
            result['HealthCheckConnectTimeout'] = self.health_check_connect_timeout

        if self.health_check_domain is not None:
            result['HealthCheckDomain'] = self.health_check_domain

        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

        if self.unhealthy_threshold is not None:
            result['UnhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackendServerPort') is not None:
            self.backend_server_port = m.get('BackendServerPort')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EipTransmit') is not None:
            self.eip_transmit = m.get('EipTransmit')

        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')

        if m.get('HealthCheckConnectPort') is not None:
            self.health_check_connect_port = m.get('HealthCheckConnectPort')

        if m.get('HealthCheckConnectTimeout') is not None:
            self.health_check_connect_timeout = m.get('HealthCheckConnectTimeout')

        if m.get('HealthCheckDomain') is not None:
            self.health_check_domain = m.get('HealthCheckDomain')

        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

