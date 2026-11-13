# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sandbox20260820 import models as main_models
from darabonba.model import DaraModel

class GetMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        metric_data: main_models.MetricData = None,
        request_id: str = None,
    ):
        # 成功时为 200。失败时为对应的错误码。
        self.code = code
        # 本次请求的结果说明。
        self.message = message
        # 各指标的查询结果及对应的时间和分组。
        self.metric_data = metric_data
        # 本次请求的唯一标识。
        self.request_id = request_id

    def validate(self):
        if self.metric_data:
            self.metric_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.metric_data is not None:
            result['metricData'] = self.metric_data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('metricData') is not None:
            temp_model = main_models.MetricData()
            self.metric_data = temp_model.from_map(m.get('metricData'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

