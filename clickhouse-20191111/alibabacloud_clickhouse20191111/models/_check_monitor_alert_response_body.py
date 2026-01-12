# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckMonitorAlertResponseBody(DaraModel):
    def __init__(
        self,
        parameter: str = None,
        request_id: str = None,
        state: str = None,
    ):
        # The parameters that are used to configure the monitoring and alerting feature.
        self.parameter = parameter
        # The request ID.
        self.request_id = request_id
        # Indicates whether the monitoring and alerting feature is enabled. Valid values:
        # 
        # *   **enable**: The monitoring and alerting feature is enabled.
        # *   **disable**: The monitoring and alerting feature is disabled.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter is not None:
            result['Parameter'] = self.parameter

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameter') is not None:
            self.parameter = m.get('Parameter')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

