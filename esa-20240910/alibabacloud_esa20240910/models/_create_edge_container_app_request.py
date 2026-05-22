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
        self.health_check_fail_times = health_check_fail_times
        self.health_check_host = health_check_host
        self.health_check_http_code = health_check_http_code
        self.health_check_interval = health_check_interval
        self.health_check_method = health_check_method
        self.health_check_port = health_check_port
        self.health_check_succ_times = health_check_succ_times
        self.health_check_timeout = health_check_timeout
        self.health_check_type = health_check_type
        self.health_check_uri = health_check_uri
        # This parameter is required.
        self.name = name
        self.remarks = remarks
        # This parameter is required.
        self.service_port = service_port
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

