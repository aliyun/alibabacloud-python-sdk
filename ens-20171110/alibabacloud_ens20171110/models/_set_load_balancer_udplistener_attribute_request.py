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
        # The name of the listener. The name must be **1** to **80** characters in length.
        # > The name cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable EIP pass-through. Valid values:
        # 
        # - **on**: Enables EIP pass-through.
        # - **off**: Disables EIP pass-through. This is the default value.
        self.eip_transmit = eip_transmit
        # The connection timeout period. Valid values: **10** to **900**. Default value: **900**. Unit: seconds.
        self.established_timeout = established_timeout
        # The port used for health checks. Valid values: **1** to **65535**. If no Settings are specified for this parameter, the backend service port (BackendServerPort) is used.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period for a health check response. If a backend ENS instance does not respond within the specified timeout period, the health check fails.
        # - Default value: 5.
        # - Valid values: **1** to **300**.
        # - Unit: seconds.
        # 
        # > If the value of HealthCheckConnectTimeout is less than the value of HealthCheckInterval, HealthCheckConnectTimeout is invalid and the timeout period is the value of HealthCheckInterval.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The response string for UDP health checks. The string can contain only letters and digits and can be up to 64 characters in length.
        self.health_check_exp = health_check_exp
        # The interval between two consecutive health checks. Valid values: **1** to **50**. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The request string for UDP health checks. The string can contain only letters and digits and can be up to 64 characters in length.
        self.health_check_req = health_check_req
        # The number of consecutive successful health checks that must occur before a backend server is declared healthy (from fail to success). Valid values: **2** to **10**.
        self.healthy_threshold = healthy_threshold
        # The frontend port of the listener whose attributes you want to modify. Valid values: **1** to **65535**.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the load balancing instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The scheduling algorithm. Valid values:
        # - **wrr**: Backend servers with higher weights receive more requests.
        # - **wlc**: Requests are distributed based on the weights and actual loads (connections) of backend servers. If two backend servers have the same weight, the backend server with fewer connections receives more requests.
        # - **rr**: Requests are evenly and sequentially distributed to backend servers.
        # - **sch**: Consistent hashing based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # - **tch**: Consistent hashing based on quadruples (source IP address, destination IP address, source port, and destination port). Requests from the same stream are distributed to the same backend server.
        # - **qch**: Consistent hashing based on QUIC connection IDs. Requests with the same QUIC connection ID are distributed to the same backend server.
        # - **iqch**: Consistent hashing based on specific three bytes of the iQUIC CID. Requests with the same second to fourth bytes are distributed to the same backend server.
        self.scheduler = scheduler
        # The number of consecutive failed health checks that must occur before a backend server is declared unhealthy (from success to fail). Valid values: **2** to **10**.
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

