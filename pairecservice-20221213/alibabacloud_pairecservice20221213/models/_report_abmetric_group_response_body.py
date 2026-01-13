# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class ReportABMetricGroupResponseBody(DaraModel):
    def __init__(
        self,
        experiment_report: Dict[str, main_models.ExperimentReportValue] = None,
        group_dimension: List[str] = None,
        request_id: str = None,
    ):
        self.experiment_report = experiment_report
        self.group_dimension = group_dimension
        self.request_id = request_id

    def validate(self):
        if self.experiment_report:
            for v1 in self.experiment_report.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExperimentReport'] = {}
        if self.experiment_report is not None:
            for k1, v1 in self.experiment_report.items():
                result['ExperimentReport'][k1] = v1.to_map() if v1 else None

        if self.group_dimension is not None:
            result['GroupDimension'] = self.group_dimension

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.experiment_report = {}
        if m.get('ExperimentReport') is not None:
            for k1, v1 in m.get('ExperimentReport').items():
                temp_model = main_models.ExperimentReportValue()
                self.experiment_report[k1] = temp_model.from_map(v1)

        if m.get('GroupDimension') is not None:
            self.group_dimension = m.get('GroupDimension')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

