# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDiagnosticMetricSetResponseBody(DaraModel):
    def __init__(
        self,
        metric_set_id: str = None,
        request_id: str = None,
    ):
        # The ID of the diagnostic metric set, which is the unique identifier of the set.
        self.metric_set_id = metric_set_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metric_set_id is not None:
            result['MetricSetId'] = self.metric_set_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MetricSetId') is not None:
            self.metric_set_id = m.get('MetricSetId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

