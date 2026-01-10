# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HealthCheckConfiguration(DaraModel):
    def __init__(
        self,
        failure_threshold: int = None,
        http_get_url: str = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        timeout_seconds: int = None,
    ):
        # 在将容器视为不健康之前，连续失败的健康检查次数
        self.failure_threshold = failure_threshold
        # 用于健康检查的HTTP GET请求的URL地址
        self.http_get_url = http_get_url
        # 在容器启动后，首次执行健康检查前的延迟时间（秒）
        self.initial_delay_seconds = initial_delay_seconds
        # 执行健康检查的时间间隔（秒）
        self.period_seconds = period_seconds
        # 在将容器视为健康之前，连续成功的健康检查次数
        self.success_threshold = success_threshold
        # 健康检查的超时时间（秒）
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

