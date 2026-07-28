# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListJobsRequest(DaraModel):
    def __init__(
        self,
        job_type: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        task_type: str = None,
    ):
        # The job type.
        self.job_type = job_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of results per page. Default value: 20. Minimum value: 1. Maximum value: 100.
        self.page_size = page_size
        # The job status. Valid values:
        # 
        # - Pending: The initial status after the job is created.
        # - PlanQueued: After the job is created, if no workflow is available, the job is queued.
        # - Planning: The resource job is in the Plan execution phase.
        # - ConfigProactiveInProgress: Compliance pre-check is in progress. The compliance pre-check feature must be enabled for the account.
        # - ConfigProactiveSuccess: Compliance pre-check succeeded. The compliance pre-check feature must be enabled for the account.
        # - Planned: The resource job has completed the Plan execution.
        # - PlannedAndFinished: After the Plan execution is complete, no diff is found. This is a final status.
        # - Confirmed: The resource job is waiting for confirmation after the Plan execution is complete.
        # - ApplyQueued: During job execution, if no workflow is available, the job is queued.
        # - Applying: The resource job is in the Apply execution phase.
        # - Applied: The resource job has completed the Apply execution. This is a final status.
        # - Errored: The job execution encountered an error. This is a final status.
        # - Canceled: The job execution was canceled. This is a final status.
        # - Discarded: The plan of the resource job was discarded. This is a final status.
        # - ConfigProactiveFailure: Compliance pre-check failed. The compliance pre-check feature must be enabled for the account.
        self.status = status
        # The task type. Valid values:
        # 
        # - Task: regular task. This is the default value.
        # - SceneTestingTask: scenario-based testing task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_type is not None:
            result['jobType'] = self.job_type

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        if self.task_type is not None:
            result['taskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobType') is not None:
            self.job_type = m.get('jobType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')

        return self

