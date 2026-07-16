# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ServiceHealthCheck(DaraModel):
    def __init__(
        self,
        enable: bool = None,
        healthy_threshold: int = None,
        http_host: str = None,
        http_path: str = None,
        interval: int = None,
        protocol: str = None,
        timeout: int = None,
        unhealthy_threshold: int = None,
    ):
        # Specifies whether to enable the health check.
        self.enable = enable
        # The healthy threshold for the health check.
        self.healthy_threshold = healthy_threshold
        # The health check domain name. This parameter is optional when the health check protocol is HTTP.
        self.http_host = http_host
        # The health check path. This parameter is required when the health check protocol is HTTP.
        self.http_path = http_path
        # The health check interval.
        self.interval = interval
        # The health check protocol. Valid values: TCP, HTTP, and GRPC.
        self.protocol = protocol
        # The health check response timeout period.
        self.timeout = timeout
        # The unhealthy threshold for the health check.
        self.unhealthy_threshold = unhealthy_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        if self.healthy_threshold is not None:
            result['healthyThreshold'] = self.healthy_threshold

        if self.http_host is not None:
            result['httpHost'] = self.http_host

        if self.http_path is not None:
            result['httpPath'] = self.http_path

        if self.interval is not None:
            result['interval'] = self.interval

        if self.protocol is not None:
            result['protocol'] = self.protocol

        if self.timeout is not None:
            result['timeout'] = self.timeout

        if self.unhealthy_threshold is not None:
            result['unhealthyThreshold'] = self.unhealthy_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('healthyThreshold') is not None:
            self.healthy_threshold = m.get('healthyThreshold')

        if m.get('httpHost') is not None:
            self.http_host = m.get('httpHost')

        if m.get('httpPath') is not None:
            self.http_path = m.get('httpPath')

        if m.get('interval') is not None:
            self.interval = m.get('interval')

        if m.get('protocol') is not None:
            self.protocol = m.get('protocol')

        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')

        if m.get('unhealthyThreshold') is not None:
            self.unhealthy_threshold = m.get('unhealthyThreshold')

        return self

