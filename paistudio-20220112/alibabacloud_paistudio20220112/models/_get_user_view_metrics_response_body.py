# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class GetUserViewMetricsResponseBody(DaraModel):
    def __init__(
        self,
        resource_group_id: str = None,
        summary: main_models.UserViewMetric = None,
        total: int = None,
        user_metrics: List[main_models.UserViewMetric] = None,
    ):
        self.resource_group_id = resource_group_id
        self.summary = summary
        self.total = total
        self.user_metrics = user_metrics

    def validate(self):
        if self.summary:
            self.summary.validate()
        if self.user_metrics:
            for v1 in self.user_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.summary is not None:
            result['Summary'] = self.summary.to_map()

        if self.total is not None:
            result['Total'] = self.total

        result['UserMetrics'] = []
        if self.user_metrics is not None:
            for k1 in self.user_metrics:
                result['UserMetrics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Summary') is not None:
            temp_model = main_models.UserViewMetric()
            self.summary = temp_model.from_map(m.get('Summary'))

        if m.get('Total') is not None:
            self.total = m.get('Total')

        self.user_metrics = []
        if m.get('UserMetrics') is not None:
            for k1 in m.get('UserMetrics'):
                temp_model = main_models.UserViewMetric()
                self.user_metrics.append(temp_model.from_map(k1))

        return self

