# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeMetricTopResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        datapoints: str = None,
        message: str = None,
        period: str = None,
        request_id: str = None,
    ):
        # The HTTP status code.
        # 
        # >  The status code 200 indicates that the request was successful.
        self.code = code
        # The monitoring data.
        self.datapoints = datapoints
        # The error message.
        self.message = message
        # The statistical period of the monitoring data. Unit: seconds. Valid values: 15, 60, 900, and 3600.
        self.period = period
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.datapoints is not None:
            result['Datapoints'] = self.datapoints

        if self.message is not None:
            result['Message'] = self.message

        if self.period is not None:
            result['Period'] = self.period

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Datapoints') is not None:
            self.datapoints = m.get('Datapoints')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

