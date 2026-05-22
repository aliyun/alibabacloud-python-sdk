# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEdgeContainerAppRequest(DaraModel):
    def __init__(
        self,
        health_check_fail_times: int = None,
        health_check_host: str = None,
        health_check_http_code: str = None,
        health_check_interval: int = None,
        health_check_method: str = None,
        health_check_port: int = None,
        health_check_succ_times: int = None,
        health_check_timeout: int = None,
        health_check_type: str = None,
        health_check_uri: str = None,
        name: str = None,
        remarks: str = None,
        service_port: int = None,
        target_port: int = None,
    ):
        # The number of consecutive failed health checks required for an application to be considered as unhealthy. Valid values: 1 to 10. Default value: 5.
        self.health_check_fail_times = health_check_fail_times
        # The domain name that is used for health checks. This parameter is empty by default.
        self.health_check_host = health_check_host
        # The HTTP status code returned for a successful health check. Valid values:
        # 
        # *   **http_2xx** (default)
        # *   **http_3xx**
        self.health_check_http_code = health_check_http_code
        # The interval between two consecutive health checks. Unit: seconds. Valid values: **1** to **50**. Default value: **5**.
        self.health_check_interval = health_check_interval
        # The HTTP request method for health checks. Valid values:
        # 
        # *   **HEAD** (default): requests the headers of the resource.
        # *   **GET**: requests the specified resource and returns both the headers and entity body.
        self.health_check_method = health_check_method
        # The port used for health checks. Valid values: 1 to 65535. Default value: 80.
        self.health_check_port = health_check_port
        # The number of consecutive successful health checks required for an application to be considered as healthy. Valid values: 1 to 10. Default value: 2.
        self.health_check_succ_times = health_check_succ_times
        # The timeout period of a health check response. If a backend ECS instance does not respond within the specified timeout period, the ECS instance fails the health check. Unit: seconds.\\
        # Valid values: **1** to **100**.\\
        # Default value: **3**.
        self.health_check_timeout = health_check_timeout
        # The health check type. By default, this parameter is left empty.
        # 
        # Valid values:
        # 
        # *   **l4**: Layer 4 health check.
        # *   **l7**: Layer 7 health check.
        self.health_check_type = health_check_type
        # The URI used for health checks. The URI must be **1** to **80** characters in length. Default value: "/".
        self.health_check_uri = health_check_uri
        # The name of the application. The name must start with a lowercase letter and can contain lowercase letters, digits, and hyphens (-). The name must be 6 to 128 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The remarks. This parameter is empty by default.
        self.remarks = remarks
        # The server port. Valid values: 1 to 65535.
        # 
        # This parameter is required.
        self.service_port = service_port
        # The backend port, which is also the service port of the application. Valid values: 1 to 65535.
        # 
        # This parameter is required.
        self.target_port = target_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.health_check_fail_times is not None:
            result['HealthCheckFailTimes'] = self.health_check_fail_times

        if self.health_check_host is not None:
            result['HealthCheckHost'] = self.health_check_host

        if self.health_check_http_code is not None:
            result['HealthCheckHttpCode'] = self.health_check_http_code

        if self.health_check_interval is not None:
            result['HealthCheckInterval'] = self.health_check_interval

        if self.health_check_method is not None:
            result['HealthCheckMethod'] = self.health_check_method

        if self.health_check_port is not None:
            result['HealthCheckPort'] = self.health_check_port

        if self.health_check_succ_times is not None:
            result['HealthCheckSuccTimes'] = self.health_check_succ_times

        if self.health_check_timeout is not None:
            result['HealthCheckTimeout'] = self.health_check_timeout

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_uri is not None:
            result['HealthCheckURI'] = self.health_check_uri

        if self.name is not None:
            result['Name'] = self.name

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        if self.service_port is not None:
            result['ServicePort'] = self.service_port

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HealthCheckFailTimes') is not None:
            self.health_check_fail_times = m.get('HealthCheckFailTimes')

        if m.get('HealthCheckHost') is not None:
            self.health_check_host = m.get('HealthCheckHost')

        if m.get('HealthCheckHttpCode') is not None:
            self.health_check_http_code = m.get('HealthCheckHttpCode')

        if m.get('HealthCheckInterval') is not None:
            self.health_check_interval = m.get('HealthCheckInterval')

        if m.get('HealthCheckMethod') is not None:
            self.health_check_method = m.get('HealthCheckMethod')

        if m.get('HealthCheckPort') is not None:
            self.health_check_port = m.get('HealthCheckPort')

        if m.get('HealthCheckSuccTimes') is not None:
            self.health_check_succ_times = m.get('HealthCheckSuccTimes')

        if m.get('HealthCheckTimeout') is not None:
            self.health_check_timeout = m.get('HealthCheckTimeout')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckURI') is not None:
            self.health_check_uri = m.get('HealthCheckURI')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        if m.get('ServicePort') is not None:
            self.service_port = m.get('ServicePort')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        return self

