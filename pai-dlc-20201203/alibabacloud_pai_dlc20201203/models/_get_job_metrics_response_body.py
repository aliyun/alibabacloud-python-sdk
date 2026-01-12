# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class GetJobMetricsResponseBody(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        pod_metrics: List[main_models.PodMetric] = None,
        request_id: str = None,
    ):
        # The job ID.
        self.job_id = job_id
        # The monitoring metrics of the job.
        self.pod_metrics = pod_metrics
        # The request ID. You can troubleshoot issues based on the request ID.
        self.request_id = request_id

    def validate(self):
        if self.pod_metrics:
            for v1 in self.pod_metrics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        result['PodMetrics'] = []
        if self.pod_metrics is not None:
            for k1 in self.pod_metrics:
                result['PodMetrics'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        self.pod_metrics = []
        if m.get('PodMetrics') is not None:
            for k1 in m.get('PodMetrics'):
                temp_model = main_models.PodMetric()
                self.pod_metrics.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

