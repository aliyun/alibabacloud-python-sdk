# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribePlaybookNumberMetricsResponseBody(DaraModel):
    def __init__(
        self,
        metrics: main_models.DescribePlaybookNumberMetricsResponseBodyMetrics = None,
        request_id: str = None,
    ):
        # The statistics.
        self.metrics = metrics
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.metrics:
            self.metrics.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metrics is not None:
            result['Metrics'] = self.metrics.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metrics') is not None:
            temp_model = main_models.DescribePlaybookNumberMetricsResponseBodyMetrics()
            self.metrics = temp_model.from_map(m.get('Metrics'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePlaybookNumberMetricsResponseBodyMetrics(DaraModel):
    def __init__(
        self,
        start_up_num: int = None,
        total_num: int = None,
    ):
        # The number of enabled playbooks.
        self.start_up_num = start_up_num
        # The total number of playbooks.
        self.total_num = total_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.start_up_num is not None:
            result['StartUpNum'] = self.start_up_num

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StartUpNum') is not None:
            self.start_up_num = m.get('StartUpNum')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

