# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class GetEmonMonitorDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[main_models.GetEmonMonitorDataResponseBodyResult] = None,
        success: bool = None,
    ):
        # The status code of the request.
        self.code = code
        # The request result.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The returned result.
        self.result = result
        # Specifies whether the request is successful. Valid values:
        # - true: Successful.
        # - false: Unsuccessful.
        self.success = success

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.GetEmonMonitorDataResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetEmonMonitorDataResponseBodyResult(DaraModel):
    def __init__(
        self,
        dps: Dict[str, Any] = None,
        integrity: float = None,
        message_watermark: int = None,
        metric: str = None,
        summary: float = None,
        tags: Dict[str, Any] = None,
    ):
        # The real-time metric monitoring data. The format is `{timestamp:data}`.
        self.dps = dps
        # The completeness of the time series curve data points in the result returned by the metric query. A value of 1.0 indicates 100% completeness.
        self.integrity = integrity
        # The timestamp when the request reaches the server. This parameter is used for troubleshooting.
        self.message_watermark = message_watermark
        # The metric name.
        self.metric = metric
        # If the queries contain wildcards, the result includes multiple matched time series data records. The summary is the aggregation of the value sets of these time series at each time point based on the aggregator type provided in the query. Currently, only the avg aggregation method is supported.
        self.summary = summary
        # The query tags.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dps is not None:
            result['dps'] = self.dps

        if self.integrity is not None:
            result['integrity'] = self.integrity

        if self.message_watermark is not None:
            result['messageWatermark'] = self.message_watermark

        if self.metric is not None:
            result['metric'] = self.metric

        if self.summary is not None:
            result['summary'] = self.summary

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dps') is not None:
            self.dps = m.get('dps')

        if m.get('integrity') is not None:
            self.integrity = m.get('integrity')

        if m.get('messageWatermark') is not None:
            self.message_watermark = m.get('messageWatermark')

        if m.get('metric') is not None:
            self.metric = m.get('metric')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

