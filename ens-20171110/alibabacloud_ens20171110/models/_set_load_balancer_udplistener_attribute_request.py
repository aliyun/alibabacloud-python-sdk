# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoadBalancerUDPListenerAttributeRequest(DaraModel):
    def __init__(
        self,
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
        # The name of the listener. The name must be **1** to **80** characters long.
        # 
        # > The name cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable EIP passthrough. Valid values:
        # 
        # - **on**: Enables EIP passthrough.
        # 
        # - **off** (default): Disables EIP passthrough.
        self.eip_transmit = eip_transmit
        # The timeout for established connections, in seconds. The value must be an integer from **10** to **900**. The default value is **900**.
        self.established_timeout = established_timeout
        # The port used for health checks. Valid values: **1** to **65535**. Defaults to the backend server port (`BackendServerPort`) if not specified.
        self.health_check_connect_port = health_check_connect_port
        # The timeout for a health check response. If a backend ENS instance does not respond within this timeout period, the health check fails.
        # 
        # - Default value: 5
        # 
        # - Valid values: **1** to **300**
        # 
        # - Unit: seconds
        # 
        # > If the value of `HealthCheckConnectTimeout` is less than the value of `HealthCheckInterval`, the system ignores `HealthCheckConnectTimeout` and uses the value of `HealthCheckInterval` as the timeout period.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The expected response string for a UDP listener health check. The string can contain only letters and digits and must be at most 64 characters long.
        self.health_check_exp = health_check_exp
        # The interval, in seconds, between consecutive health checks. Valid values: **1** to **50**.
        self.health_check_interval = health_check_interval
        # The request string for a UDP listener health check. The string can contain only letters and digits and must be at most 64 characters long.
        self.health_check_req = health_check_req
        # The number of consecutive successful health checks required to mark an unhealthy backend server as healthy. Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The listener port to modify. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the load balancer instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The scheduling algorithm. Valid values:
        # 
        # - **wrr**: Weighted Round Robin. Backend servers with higher weights receive a larger proportion of requests.
        # 
        # - **wlc**: Weighted Least Connections. Requests are distributed based on both the weights and the number of active connections of backend servers. If servers have the same weight, the server with the fewest active connections receives more requests.
        # 
        # - **rr**: Round Robin. Requests are distributed to backend servers in sequence.
        # 
        # - **sch**: Source IP Hash. A consistent hash based on the source IP address. Requests from the same source IP address are routed to the same backend server.
        # 
        # - **tch**: 4-Tuple Hash. A consistent hash based on the 4-tuple (source IP, destination IP, source port, and destination port). Flows with the same 4-tuple are routed to the same backend server.
        # 
        # - **qch**: QUIC Connection ID Hash. A consistent hash based on the QUIC Connection ID. Requests with the same QUIC Connection ID are routed to the same backend server.
        # 
        # - **iqch**: iQUIC CID Hash. A consistent hash based on three specific bytes (from the second to the fourth byte) of the iQUIC CID. Requests with identical values in these three bytes are routed to the same backend server.
        self.scheduler = scheduler
        # The number of consecutive failed health checks required to mark a healthy backend server as unhealthy. Valid values: **2** to **10**.
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

