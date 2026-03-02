# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class JobStatus(DaraModel):
    def __init__(
        self,
        current_job_status: str = None,
        failure: main_models.JobFailure = None,
        health_score: int = None,
        risk_level: str = None,
        running: main_models.JobStatusRunning = None,
    ):
        # The status of the current job. Valid values:
        # 
        # *   STARTING
        # *   RUNNING
        # *   CANCELLING
        # *   FAILED
        # *   CANCELLED
        # *   FINISHED
        self.current_job_status = current_job_status
        # The information about the job failure. This parameter is valid when the value of the currentJobStatus parameter is FAILED.
        self.failure = failure
        self.health_score = health_score
        self.risk_level = risk_level
        # The details of the job. This parameter is valid when the value of the currentJobStatus parameter is RUNNING.
        self.running = running

    def validate(self):
        if self.failure:
            self.failure.validate()
        if self.running:
            self.running.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status

        if self.failure is not None:
            result['failure'] = self.failure.to_map()

        if self.health_score is not None:
            result['healthScore'] = self.health_score

        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.running is not None:
            result['running'] = self.running.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')

        if m.get('failure') is not None:
            temp_model = main_models.JobFailure()
            self.failure = temp_model.from_map(m.get('failure'))

        if m.get('healthScore') is not None:
            self.health_score = m.get('healthScore')

        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('running') is not None:
            temp_model = main_models.JobStatusRunning()
            self.running = temp_model.from_map(m.get('running'))

        return self

