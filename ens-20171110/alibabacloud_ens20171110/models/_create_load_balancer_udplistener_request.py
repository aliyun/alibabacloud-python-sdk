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
        # The port used by the backend ELB server of the ELB instance. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The name of the listener. The value must be **1** to **80** characters in length.
        # 
        # >  The value cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to enable Elastic IP address (EIP) pass-through. Valid values:
        # 
        # *   **on**
        # *   **off** (default)
        self.eip_transmit = eip_transmit
        # The timeout period of a connection. Valid values: **10** to **900**. Default value: **900**. Unit: seconds.
        self.established_timeout = established_timeout
        # The port that is used for health checks. Valid values: **1** to **65535**. If you leave this parameter empty, the port specified by BackendServerPort is used for health checks.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period for a health check response. If a backend server does not respond within the specified timeout period, the server fails the health check.
        # 
        # *   Default value: 5.
        # *   Valid values: **1** to **300**.
        # *   Unit: seconds.
        # 
        # >  If the value of the HealthCheckConnectTimeout parameter is smaller than that of the HealthCheckInterval parameter, the timeout period specified by the HealthCheckConnectTimeout parameter becomes invalid and the value of the HealthCheckInterval parameter is used as the timeout period.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The response string for UDP listener health checks. The string can be up to 64 characters in length and can contain only letters and digits.
        self.health_check_exp = health_check_exp
        # The interval at which health checks are performed. Valid values: **1** to **50**. Default value: **2**. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The request string for UDP listener health checks. The string can be up to 64 characters in length and can contain only letters and digits.
        self.health_check_req = health_check_req
        # The number of consecutive successful health checks that must occur before an unhealthy and inaccessible backend server is declared healthy and accessible. Valid values: **2** to **10**. Default value: **3**.
        self.healthy_threshold = healthy_threshold
        # The listener port that is used by Edge Load Balancer (ELB) to receive requests and forward the requests to backend servers. Valid values: **1** to **65535**.
        # 
        # >  You cannot specify ports 250, 4789, or 4790 for UDP listeners. They are system reserved ports.
        # 
        # This parameter is required.
        self.listener_port = listener_port
        # The ID of the Edge Load Balancer (ELB) instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The scheduling algorithm. Valid values:
        # 
        # *   **wrr**: Backend servers with higher weights receive more requests than backend servers with lower weights. This is the default value.
        # *   **wlc**: Requests are distributed based on the weight and load of each backend server. The load refers to the number of connections on a backend server. If two backend servers have the same weight, the backend server that has fewer connections receives more requests.
        # *   **rr**: Requests are distributed to backend servers in sequence.
        # *   **sch**: Consistent hashing that is based on source IP addresses. Requests from the same source IP address are distributed to the same backend server.
        # *   **qch**: Consistent hashing based on Quick UDP Internet Connection (QUIC) IDs. Requests that contain the same QUIC ID are scheduled to the same backend server.
        # *   **iqch**: Consistent hashing based on three specific bytes of iQUIC CID. Requests with the same second, third, and forth bytes are scheduled to the same backend server.
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

