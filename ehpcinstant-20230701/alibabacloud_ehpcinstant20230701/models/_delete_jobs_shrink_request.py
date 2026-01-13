# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteJobsShrinkRequest(DaraModel):
    def __init__(
        self,
        executor_ids_shrink: str = None,
        job_scheduler: str = None,
        job_spec_shrink: str = None,
    ):
        # The list of executor IDs. A maximum of 100 IDs are supported.
        self.executor_ids_shrink = executor_ids_shrink
        # The type of the job scheduler.
        # 
        # *   HPC
        # *   K8S
        # 
        # Default value: HPC
        self.job_scheduler = job_scheduler
        # The information about the job to be deleted.
        self.job_spec_shrink = job_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_ids_shrink is not None:
            result['ExecutorIds'] = self.executor_ids_shrink

        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler

        if self.job_spec_shrink is not None:
            result['JobSpec'] = self.job_spec_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorIds') is not None:
            self.executor_ids_shrink = m.get('ExecutorIds')

        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')

        if m.get('JobSpec') is not None:
            self.job_spec_shrink = m.get('JobSpec')

        return self

