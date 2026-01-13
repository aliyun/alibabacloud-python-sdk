# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeJobMetricDataShrinkRequest(DaraModel):
    def __init__(
        self,
        array_index_shrink: str = None,
        job_id: str = None,
        metric_name: str = None,
        task_name: str = None,
    ):
        # The list of array job indexes.
        self.array_index_shrink = array_index_shrink
        # The job ID.
        self.job_id = job_id
        # The metrics of the job.
        self.metric_name = metric_name
        # The name of the task.
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array_index_shrink is not None:
            result['ArrayIndex'] = self.array_index_shrink

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.metric_name is not None:
            result['MetricName'] = self.metric_name

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index_shrink = m.get('ArrayIndex')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('MetricName') is not None:
            self.metric_name = m.get('MetricName')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

