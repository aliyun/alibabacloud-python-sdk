# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetryLifecycleRetrieveJobRequest(DaraModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # The data retrieval task ID.
        # 
        # **Scenarios**
        # 
        # Call this operation to retry a data retrieval task that has entered the `failed` state. Common causes for a task to enter the `failed` state include:
        # - A backend error occurred during data retrieval from the InfrequentAccess or Archive storage tier.
        # - The data retrieval request timed out.
        # - A temporary storage tier failure or network exception occurred.
        # 
        # **Before you begin**
        # 
        # Before calling this operation, call [ListLifecycleRetrieveJobs](https://www.alibabacloud.com/help/en/nas/developer-reference/api-nas-2017-06-26-listlifecycleretrievejobs) to query the task list, confirm that the target task is in the `failed` state, and obtain the JobId of the task you want to retry.
        # 
        # This parameter is required.
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

