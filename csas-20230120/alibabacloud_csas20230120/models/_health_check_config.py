# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HealthCheckConfig(DaraModel):
    def __init__(
        self,
        check_interval: int = None,
        failure_count: int = None,
        port: int = None,
        protocol: str = None,
        timeout_seconds: int = None,
    ):
        # The check interval in seconds. Default value: 30 seconds.
        self.check_interval = check_interval
        # The failure count. Default value: 3.
        self.failure_count = failure_count
        # The port number. This parameter is optional.
        self.port = port
        # The protocol type. Valid values: TCP and UDP. This parameter is required only in Continuous mode.
        self.protocol = protocol
        # The timeout period for a single check in seconds. Default value: 5 seconds.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_interval is not None:
            result['CheckInterval'] = self.check_interval

        if self.failure_count is not None:
            result['FailureCount'] = self.failure_count

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckInterval') is not None:
            self.check_interval = m.get('CheckInterval')

        if m.get('FailureCount') is not None:
            self.failure_count = m.get('FailureCount')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

