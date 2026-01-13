# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeJobMetricLastRequest(DaraModel):
    def __init__(
        self,
        array_index: List[int] = None,
        job_id: str = None,
        task_name: str = None,
    ):
        # The list of array job indexes.
        self.array_index = array_index
        # The job ID.
        self.job_id = job_id
        # The name of the task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array_index is not None:
            result['ArrayIndex'] = self.array_index

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

