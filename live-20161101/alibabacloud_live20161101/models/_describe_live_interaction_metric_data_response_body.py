# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLiveInteractionMetricDataResponseBody(DaraModel):
    def __init__(
        self,
        nodes: List[main_models.DescribeLiveInteractionMetricDataResponseBodyNodes] = None,
        request_id: str = None,
        summary_data: str = None,
    ):
        # The node data.
        self.nodes = nodes
        # The ID of the request.
        self.request_id = request_id
        # The summary data.
        self.summary_data = summary_data

    def validate(self):
        if self.nodes:
            for v1 in self.nodes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Nodes'] = []
        if self.nodes is not None:
            for k1 in self.nodes:
                result['Nodes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.summary_data is not None:
            result['SummaryData'] = self.summary_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('Nodes') is not None:
            for k1 in m.get('Nodes'):
                temp_model = main_models.DescribeLiveInteractionMetricDataResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SummaryData') is not None:
            self.summary_data = m.get('SummaryData')

        return self

class DescribeLiveInteractionMetricDataResponseBodyNodes(DaraModel):
    def __init__(
        self,
        timestamp: str = None,
        value: str = None,
    ):
        # The time when the metric was queried. The value is a UNIX timestamp. Unit: milliseconds.
        self.timestamp = timestamp
        # The value of the metric.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

