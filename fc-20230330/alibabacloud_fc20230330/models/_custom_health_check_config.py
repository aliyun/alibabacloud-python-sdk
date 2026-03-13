# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CustomHealthCheckConfig(DaraModel):
    def __init__(
        self,
        failure_threshold: int = None,
        http_get_url: str = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        timeout_seconds: int = None,
    ):
        # The threshold for health check failures. When this value is reached, the system considers the health check failed. Valid values: 1 to 120. Default value: 3.
        self.failure_threshold = failure_threshold
        # The health check URL of the custom container. The URL can be up to 2,048 characters in length.
        self.http_get_url = http_get_url
        # The delay between the container startup and the health check. Valid values: 0 to 120. Default value: 0.
        self.initial_delay_seconds = initial_delay_seconds
        # The health check period. Valid values: 1 to 120. Default value: 3.
        self.period_seconds = period_seconds
        # The threshold for health check successes. When this value is reached, the system considers the health check successful. Valid values: 1 to 120. Default value: 1.
        self.success_threshold = success_threshold
        # The timeout period of the health check. Unit: seconds. Valid values: 1 to 3. Default value: 1.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failure_threshold is not None:
            result['failureThreshold'] = self.failure_threshold

        if self.http_get_url is not None:
            result['httpGetUrl'] = self.http_get_url

        if self.initial_delay_seconds is not None:
            result['initialDelaySeconds'] = self.initial_delay_seconds

        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds

        if self.success_threshold is not None:
            result['successThreshold'] = self.success_threshold

        if self.timeout_seconds is not None:
            result['timeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failureThreshold') is not None:
            self.failure_threshold = m.get('failureThreshold')

        if m.get('httpGetUrl') is not None:
            self.http_get_url = m.get('httpGetUrl')

        if m.get('initialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('initialDelaySeconds')

        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')

        if m.get('successThreshold') is not None:
            self.success_threshold = m.get('successThreshold')

        if m.get('timeoutSeconds') is not None:
            self.timeout_seconds = m.get('timeoutSeconds')

        return self

