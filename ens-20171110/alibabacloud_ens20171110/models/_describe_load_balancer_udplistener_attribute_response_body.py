# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLoadBalancerUDPListenerAttributeResponseBody(DaraModel):
    def __init__(
        self,
        backend_server_port: int = None,
        bandwidth: int = None,
        description: str = None,
        eip_transmit: str = None,
        established_timeout: int = None,
        health_check: str = None,
        health_check_connect_port: int = None,
        health_check_connect_timeout: int = None,
        health_check_exp: str = None,
        health_check_interval: int = None,
        health_check_req: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        request_id: str = None,
        scheduler: str = None,
        status: str = None,
        unhealthy_threshold: int = None,
    ):
        # The port used by the backend servers. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The peak bandwidth of the load balancer. A value of -1 indicates that no rate limit is applied.
        self.bandwidth = bandwidth
        # The listener name.
        self.description = description
        # Specifies whether to enable EIP passthrough. Valid values:
        # 
        # - **on**: Enabled.
        # 
        # - **off** (default): Disabled.
        self.eip_transmit = eip_transmit
        # The connection timeout period. Valid values: **10** to **900**. Unit: seconds.
        self.established_timeout = established_timeout
        # Specifies whether to enable health checks. Valid values:
        # 
        # - **on**: Enabled.
        # 
        # - **off**: Disabled.
        self.health_check = health_check
        # The port used for health checks. Valid values: **1** to **65535**. If you do not specify this parameter, the value of `BackendServerPort` is used.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period for a health check response. If a backend ENS instance does not respond within the specified timeout period, the health check fails.
        # 
        # - Default value: 5.
        # 
        # - Valid values: **1** to **300**.
        # 
        # - Unit: seconds.
        # 
        # > * This parameter takes effect only when `HealthCheck` is set to `on`.
        # >
        # > * If the value of `HealthCheckConnectTimeout` is less than the value of `HealthCheckInterval`, the value of `HealthCheckInterval` is used as the timeout period.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The response string for UDP health checks. The string can contain only letters and digits and can be up to 64 characters in length.
        self.health_check_exp = health_check_exp
        # The interval between health checks. Valid values: **1** to **50**. Unit: seconds.
        # 
        # > This parameter takes effect only when `HealthCheck` is set to `on`.
        self.health_check_interval = health_check_interval
        # The request string for UDP health checks. The string can contain only letters and digits and can be up to 64 characters in length.
        self.health_check_req = health_check_req
        # The number of consecutive successful health checks that must occur before a backend server can be declared healthy. Valid values: **2** to **10**.
        # 
        # > This parameter takes effect only when `HealthCheck` is set to `on`.
        self.healthy_threshold = healthy_threshold
        # The listener port.
        self.listener_port = listener_port
        # The request ID.
        self.request_id = request_id
        # The scheduling algorithm. Valid values:
        # 
        # - **wrr** (Weighted Round Robin): Backend servers with higher weights receive a larger proportion of requests.
        # 
        # - **wlc** (Weighted Least Connections): Requests are distributed based on both the weight and the current connection count of each backend server. If backend servers have the same weight, the server with the fewest connections receives more new requests.
        # 
        # - **rr** (Round Robin): Requests are distributed to backend servers sequentially.
        # 
        # - **sch** (Source IP Hash): Routes requests from the same source IP address to the same backend server by using a consistent hash of the source IP address.
        # 
        # - **tch** (4-tuple Hash): Routes packets from the same flow to the same backend server by using a consistent hash of the 4-tuple (source IP address, destination IP address, source port, and destination port).
        # 
        # - **qch** (QUIC Connection ID Hash): Uses a consistent hashing algorithm on the QUIC Connection ID to ensure that requests with the same connection ID are always routed to the same backend server.
        # 
        # - **iqch** (iQUIC CID Hash): Uses a consistent hashing algorithm on bytes 2, 3, and 4 of the iQUIC CID. Requests where these three bytes are the same are routed to the same backend server.
        self.scheduler = scheduler
        # The status of the listener. Valid values:
        # 
        # - **Running**: The listener is running.
        # 
        # - **Stopped**: The listener is stopped.
        # 
        # - **Starting**: The listener is starting.
        # 
        # - **Configuring**: The listener is being configured.
        # 
        # - **Stopping**: The listener is being stopped.
        self.status = status
        # The number of consecutive failed health checks that must occur before a backend server can be declared unhealthy. Valid values: **2** to **10**.
        # 
        # > This parameter takes effect only when `HealthCheck` is set to `on`.
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

        if self.eip_transmit is not None:
            result['EipTransmit'] = self.eip_transmit

        if self.established_timeout is not None:
            result['EstablishedTimeout'] = self.established_timeout

        if self.health_check is not None:
            result['HealthCheck'] = self.health_check

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scheduler is not None:
            result['Scheduler'] = self.scheduler

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

        if m.get('EipTransmit') is not None:
            self.eip_transmit = m.get('EipTransmit')

        if m.get('EstablishedTimeout') is not None:
            self.established_timeout = m.get('EstablishedTimeout')

        if m.get('HealthCheck') is not None:
            self.health_check = m.get('HealthCheck')

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

