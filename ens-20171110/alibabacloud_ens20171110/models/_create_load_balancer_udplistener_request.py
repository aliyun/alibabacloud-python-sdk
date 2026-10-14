# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoadBalancerUDPListenerRequest(DaraModel):
    def __init__(
        self,
        backend_server_port: int = None,
        description: str = None,
        eip_transmit: str = None,
        established_timeout: int = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_exp: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        load_balancer_id: str = None,
        scheduler: str = None,
        unhealthy_threshold: int = None,
    ):
        # The port used by the backend servers. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The name of the listener. The name must be **1** to **80** characters long.
        # 
        # > The name cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether EIP pass-through is enabled. Valid values:
        # 
        # - **on**: Enables EIP pass-through.
        # 
        # - **off** (default): Disables EIP pass-through.
        self.eip_transmit = eip_transmit
        # The timeout for established connections. Valid values: **10** to **900**. Default value: **900**. Unit: seconds.
        self.established_timeout = established_timeout
        # The port used for health checks. Valid values: **1** to **65535**. If you do not specify this parameter, the port specified by `BackendServerPort` is used.
        self.health_check_connect_port = health_check_connect_port
        # The maximum time to wait for a response to a health check. A health check fails if a backend ENS instance does not respond within this time.
        # 
        # - Default value: 5.
        # 
        # - Valid values: **1** to **300**.
        # 
        # - Unit: seconds.
        # 
        # > If this timeout is shorter than the health check interval (`HealthCheckInterval`), the interval value is used for the timeout instead.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The expected response string for UDP health checks. The string must be up to 64 characters long and contain only letters and digits.
        self.health_check_exp = health_check_exp
        # The interval between health checks, in seconds. Valid values: **1** to **50**. Default value: **2**.
        self.health_check_interval = health_check_interval
        # The request string for UDP health checks. The string must be up to 64 characters long and contain only letters and digits.
        self.health_check_req = health_check_req
        # The number of consecutive successful health checks required for a backend server to be considered healthy. Valid values: **2** to **10**. Default value: **3**.
        self.healthy_threshold = healthy_threshold
        # The listener port used to receive requests and forward them to backend servers. Valid values: **1** to **65535**.
        # 
        # > For UDP listeners, ports 250, 4789, and 4790 are system-reserved and not available for use.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the load balancer instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The scheduling algorithm. Valid values:
        # 
        # - **wrr** (default): Weighted Round Robin. Backend servers with a higher weight receive more requests.
        # 
        # - **wlc**: Weighted Least Connections. Requests are distributed based on both the weight and the number of current connections of each backend server. If multiple backend servers have the same weight, the one with the fewest active connections receives the next request.
        # 
        # - **rr**: Round Robin. Requests are distributed to backend servers sequentially.
        # 
        # - **sch**: Source IP Hash. Requests from the same source IP address are routed to the same backend server.
        # 
        # - **tch**: Four-tuple Hash. Requests are routed to backend servers based on a hash of four values: source IP address, destination IP address, source port, and destination port. Flows with the same four values are routed to the same backend server.
        # 
        # - **qch**: QUIC Connection ID Hash. Requests with the same QUIC Connection ID are routed to the same backend server.
        # 
        # - **iqch**: A consistent hash algorithm for iQUIC Connection IDs. Flows with the same second, third, and fourth bytes in the iQUIC CID are routed to the same backend server.
        self.scheduler = scheduler
        # The number of consecutive failed health checks required for a backend server to be considered unhealthy. Valid values: **2** to **10**. Default value: **3**.
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

        if self.health_check_exp is not None:
            result['HealthCheckExp'] = self.health_check_exp

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_req is not None:
            result['HealthCheckReq'] = self.health_check_req

        if self.healthy_threshold is not None:
            result['HealthyThreshold'] = self.healthy_threshold

        if self.listener_port is not None:
            result['ListenerPort'] = self.listener_port

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

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

        if m.get('HealthCheckExp') is not None:
            self.health_check_exp = m.get('HealthCheckExp')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckReq') is not None:
            self.health_check_req = m.get('HealthCheckReq')

        if m.get('HealthyThreshold') is not None:
            self.healthy_threshold = m.get('HealthyThreshold')

        if m.get('ListenerPort') is not None:
            self.listener_port = m.get('ListenerPort')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

