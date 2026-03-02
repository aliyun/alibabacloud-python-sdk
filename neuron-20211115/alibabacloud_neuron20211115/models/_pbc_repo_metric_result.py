# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class PbcRepoMetricResult(DaraModel):
    def __init__(
        self,
        repo_metrics: List[main_models.RepoMetric] = None,
        request_id: str = None,
    ):
        self.repo_metrics = repo_metrics
        self.request_id = request_id

    def validate(self):
        if self.repo_metrics:
            for v1 in self.repo_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['repoMetrics'] = []
        if self.repo_metrics is not None:
            for k1 in self.repo_metrics:
                result['repoMetrics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.repo_metrics = []
        if m.get('repoMetrics') is not None:
            for k1 in m.get('repoMetrics'):
                temp_model = main_models.RepoMetric()
                self.repo_metrics.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

