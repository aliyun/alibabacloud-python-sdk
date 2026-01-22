# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeJobResultsRequest(DaraModel):
    def __init__(
        self,
        array_index: int = None,
        content_encoding: str = None,
        job_id: str = None,
        limit_bytes: str = None,
        start_time: str = None,
        task_name: str = None,
    ):
        self.array_index = array_index
        self.content_encoding = content_encoding
        self.job_id = job_id
        self.limit_bytes = limit_bytes
        self.start_time = start_time
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

        if self.content_encoding is not None:
            result['ContentEncoding'] = self.content_encoding

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.limit_bytes is not None:
            result['LimitBytes'] = self.limit_bytes

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayIndex') is not None:
            self.array_index = m.get('ArrayIndex')

        if m.get('ContentEncoding') is not None:
            self.content_encoding = m.get('ContentEncoding')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('LimitBytes') is not None:
            self.limit_bytes = m.get('LimitBytes')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        return self

