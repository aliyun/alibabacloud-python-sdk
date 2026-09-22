# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_green20220926 import models as main_models
from darabonba.model import DaraModel

class GetQpsStatsResponseBody(DaraModel):
    def __init__(
        self,
        charts: Dict[str, main_models.ChartsValue] = None,
        request_id: str = None,
    ):
        # The chart configurations.
        self.charts = charts
        # The ID assigned by the backend to uniquely identify a request. It can be used to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.charts:
            for v1 in self.charts.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Charts'] = {}
        if self.charts is not None:
            for k1, v1 in self.charts.items():
                result['Charts'][k1] = v1.to_map() if v1 else None

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.charts = {}
        if m.get('Charts') is not None:
            for k1, v1 in m.get('Charts').items():
                temp_model = main_models.ChartsValue()
                self.charts[k1] = temp_model.from_map(v1)

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

