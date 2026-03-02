# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobStatusRunning(DaraModel):
    def __init__(
        self,
        observed_flink_job_restarts: int = None,
        observed_flink_job_status: str = None,
    ):
        # The number of times the job is restarted.
        self.observed_flink_job_restarts = observed_flink_job_restarts
        # The status of the Flink job.
        self.observed_flink_job_status = observed_flink_job_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.observed_flink_job_restarts is not None:
            result['observedFlinkJobRestarts'] = self.observed_flink_job_restarts

        if self.observed_flink_job_status is not None:
            result['observedFlinkJobStatus'] = self.observed_flink_job_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('observedFlinkJobRestarts') is not None:
            self.observed_flink_job_restarts = m.get('observedFlinkJobRestarts')

        if m.get('observedFlinkJobStatus') is not None:
            self.observed_flink_job_status = m.get('observedFlinkJobStatus')

        return self

