# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRayDashboardResponseBody(DaraModel):
    def __init__(
        self,
        metrics_enabled: str = None,
        url: str = None,
    ):
        # Indicates whether the dashboard has been integrated with CloudMonitor and supports ray metrics
        self.metrics_enabled = metrics_enabled
        # The Ray Dashboard URL
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metrics_enabled is not None:
            result['metricsEnabled'] = self.metrics_enabled

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metricsEnabled') is not None:
            self.metrics_enabled = m.get('metricsEnabled')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

