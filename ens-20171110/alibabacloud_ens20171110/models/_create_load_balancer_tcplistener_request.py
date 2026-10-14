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
        # The port used by backend servers. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The description of the listener. The description must be **1** to **80** characters in length.
        # 
        # > The description cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable EIP passthrough. Valid values:
        # 
        # - **on**: Enables EIP passthrough.
        # 
        # - **off** (default): Disables EIP passthrough.
        self.eip_transmit = eip_transmit
        # The timeout period for established connections, in seconds. Valid values: **10** to **900**. Default value: **900**.
        self.established_timeout = established_timeout
        # The port used for health checks. Valid values: **1** to **65535**. If you do not specify this parameter, the port specified by `BackendServerPort` is used by default.
        self.health_check_connect_port = health_check_connect_port
        # The maximum time to wait for a health check response. If a backend ENS instance does not respond within this timeout period, the health check fails.
        # 
        # - Default value: 5.
        # 
        # - Valid values: **1** to **300**.
        # 
        # - Unit: seconds.
        # 
        # > If the value of this parameter is less than the value of `HealthCheckInterval`, this parameter is ignored and the value of `HealthCheckInterval` is used as the timeout period.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name used for health checks.
        self.health_check_domain = health_check_domain
        # The HTTP status codes that indicate a successful health check. Valid values:
        # 
        # - **http_2xx** (default)
        # 
        # - **http_3xx**
        # 
        # - **http_4xx**
        # 
        # - **http_5xx**
        self.health_check_http_code = health_check_http_code
        # The interval between health checks, in seconds. Valid values: **1** to **50**. Default value: **2**.
        self.health_check_interval = health_check_interval
        # The health check type. Valid values:
        # 
        # - **tcp** (default)
        # 
        # - **http**
        self.health_check_type = health_check_type
        # The URI for health checks. The URI must be **1** to **80** characters in length.
        # 
        # > The URI must start with a forward slash (/) but cannot be only a forward slash (/).
        self.health_check_uri = health_check_uri
        # The number of consecutive successful health checks required for a backend server to be considered healthy (from a `fail` to `success` state). Valid values: **2** to **10**. Default value: **3**.
        self.healthy_threshold = healthy_threshold
        # The listener port that receives and forwards requests to backend servers. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the load balancer instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The timeout period for session persistence.
        # 
        # - Default value: **0**, which indicates that session persistence is disabled.
        # 
        # - Valid values: **0** to **3600**.
        # 
        # - Unit: seconds.
        self.persistence_timeout = persistence_timeout
        # The scheduling algorithm. Valid values:
        # 
        # - **wrr** (default): Weighted Round Robin. Requests are distributed to backend servers based on their weights. Backend servers with higher weights receive more requests.
        # 
        # - **wlc**: Weighted Least Connections. Requests are distributed to backend servers based on both their weights and the number of connections. If multiple backend servers have the same weight, the one with the fewest connections receives more requests.
        # 
        # - **rr**: Round Robin. Requests are distributed to backend servers in sequential order.
        # 
        # - **sch**: Source IP Hash. Requests are routed based on a consistent hash of the source IP address, ensuring that requests from the same source IP address are sent to the same backend server.
        # 
        # - **tch**: Four-tuple Hash. Requests are routed based on a consistent hash of a four-tuple (source IP address, destination IP address, source port, and destination port), ensuring that requests from the same flow are sent to the same backend server.
        self.scheduler = scheduler
        # The number of consecutive failed health checks required for a backend server to be considered unhealthy (from a `success` to `fail` state). Valid values: **2** to **10**. Default value: **3**.
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

