# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetricsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data_points: str = None,
        message: str = None,
        next_token: str = None,
        period: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code. A value of 200 indicates success.
        self.code = code
        # The monitoring metrics data.
        self.data_points = data_points
        # The detailed information about the detection result.
        self.message = message
        # Id of the request
        self.next_token = next_token
        # The statistical period of the monitoring data. Valid values: 15, 60, 900, and 3600. Unit: seconds. If you do not set the statistical period, monitoring data is queried based on the reporting period that was specified when the monitoring metric was registered. The statistical period varies for each monitoring metric (MetricName) of each cloud service. For more information, see cloud service monitoring items.
        self.period = period
        # The request ID.
        self.request_id = request_id
        # Indicates whether the operation was successful. Valid values:
        # - true: The operation was successful.
        # - false: The operation failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data_points is not None:
            result['DataPoints'] = self.data_points

        if self.message is not None:
            result['Message'] = self.message

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.period is not None:
            result['Period'] = self.period

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DataPoints') is not None:
            self.data_points = m.get('DataPoints')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

