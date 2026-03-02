# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_neuron20211115 import models as main_models
from darabonba.model import DaraModel

class LibraryDeveloperRepoMetricResult(DaraModel):
    def __init__(
        self,
        developer_repo_metrics: List[main_models.ReposDeveloperGroupMetric] = None,
    ):
        self.developer_repo_metrics = developer_repo_metrics

    def validate(self):
        if self.developer_repo_metrics:
            for v1 in self.developer_repo_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['developerRepoMetrics'] = []
        if self.developer_repo_metrics is not None:
            for k1 in self.developer_repo_metrics:
                result['developerRepoMetrics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.developer_repo_metrics = []
        if m.get('developerRepoMetrics') is not None:
            for k1 in m.get('developerRepoMetrics'):
                temp_model = main_models.ReposDeveloperGroupMetric()
                self.developer_repo_metrics.append(temp_model.from_map(k1))

        return self

