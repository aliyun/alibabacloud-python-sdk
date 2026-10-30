# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLoadBalancerTCPListenerAttributeResponseBody(DaraModel):
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
        health_check_domain: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        healthy_threshold: int = None,
        listener_port: int = None,
        persistence_timeout: int = None,
        request_id: str = None,
        scheduler: str = None,
        status: str = None,
        unhealthy_threshold: int = None,
    ):
        # The port used by the backend server of the load balancing instance. Valid values: **1** to **65535**.
        self.backend_server_port = backend_server_port
        # The peak bandwidth of the load balancing instance. Default value: -1, which indicates that no bandwidth throttling is applied.
        self.bandwidth = bandwidth
        # The name of the listener.
        self.description = description
        # Specifies whether to enable EIP pass-through. Valid values:
        # 
        # - **on**: enabled
        # - **off** (default): disabled
        self.eip_transmit = eip_transmit
        # The connection timeout period. Valid values: **10** to **900**. Unit: seconds.
        self.established_timeout = established_timeout
        # Specifies whether to enable the health check feature. Valid values:
        # 
        # - **on**: enabled
        # - **off**: disabled
        self.health_check = health_check
        # The port used for health checks. Valid values: **1** to **65535**. If the Settings for this parameter are not specified, the backend service port (BackendServerPort) is used.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_connect_port = health_check_connect_port
        # The timeout period for receiving a health check response. If a backend ENS instance does not respond within the specified timeout period, the health check fails.
        # - Default value: 5.
        # - Valid values: **1** to **300**.
        # - Unit: seconds.
        # > - This parameter takes effect only when HealthCheck is set to on.
        # > - If the value of HealthCheckConnectTimeout is less than the value of HealthCheckInterval, HealthCheckConnectTimeout becomes invalid and the timeout period is the value of HealthCheckInterval.
        self.health_check_connect_timeout = health_check_connect_timeout
        # The domain name used for health checks.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_domain = health_check_domain
        # The HTTP status code that indicates a successful health check. Valid values:
        # 
        # - **http_2xx** (default)
        # - **http_3xx**
        # - **http_4xx**
        # - **http_5xx**
        # 
        # > This parameter takes effect only when HealthCheck is set to on.
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Valid values: **1** to **50**. Unit: seconds.
        self.health_check_interval = health_check_interval
        # The health check type. Valid values:
        # - **tcp** (default)
        # - **http**
        self.health_check_type = health_check_type
        # The URI used for health checks. The URI must be **1** to **80** characters in length.
        # > - The URI cannot contain only a forward slash (`/`), but it must start with a forward slash.
        # > - This parameter takes effect only when HealthCheck is set to on.
        self.health_check_uri = health_check_uri
        # The number of consecutive successful health checks required to change the health check status of a backend server from fail (unreachable) to success (reachable). Valid values: **2** to **10**.
        # > This parameter takes effect only when HealthCheck is set to on.
        self.healthy_threshold = healthy_threshold
        # The frontend port used by the load balancing instance.
        self.listener_port = listener_port
        # The timeout period for session persistence.
        # 
        # - Default value: 0, which indicates that session persistence is disabled.
        # - Valid values: **0** to **3600**.
        # - Unit: seconds.
        self.persistence_timeout = persistence_timeout
        # The request ID.
        self.request_id = request_id
        # The scheduling algorithm. Valid values:
        # - **wrr**: Backend servers with higher weights are polled more frequently.
        # - **wlc**: Backend servers are polled based on their weights and actual loads (number of connections). If weights are the same, backend servers with fewer current connections are polled more frequently.
        # - **rr**: External requests are distributed to backend servers in sequence.
        # - **sch**: Consistent hashing is based on source IP addresses. Requests from the same source IP address are scheduled to the same backend server.
        # - **tch**: Consistent hashing is based on quadruples (source IP address, destination IP address, source port, and destination port). Requests from the same stream are scheduled to the same backend server.
        self.scheduler = scheduler
        # The status of the listener. Valid values:
        # 
        # - **Running**: running normally
        # - **Stopped**: stopped
        # - **Starting**: starting
        # - **Configuring**: configuring
        # - **Stopping**: stopping
        self.status = status
        # The number of consecutive failed health checks required to change the health check status of a backend server from success (reachable) to fail (unreachable). Valid values: **2** to **10**.
        # 
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

        if self.persistence_timeout is not None:
            result['PersistenceTimeout'] = self.persistence_timeout

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

        if m.get('PersistenceTimeout') is not None:
            self.persistence_timeout = m.get('PersistenceTimeout')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Scheduler') is not None:
            self.scheduler = m.get('Scheduler')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UnhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('UnhealthyThreshold')

        return self

