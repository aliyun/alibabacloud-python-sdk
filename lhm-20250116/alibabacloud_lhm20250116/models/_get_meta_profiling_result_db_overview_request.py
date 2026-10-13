# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMetaProfilingResultDbOverviewRequest(DaraModel):
    def __init__(
        self,
        is_summary: str = None,
        task_id: str = None,
    ):
        # Specifies whether to return only summary data.
        self.is_summary = is_summary
        # The ID of the metadata profiling task. It is used to locate the profiling task for which you want to query the overview.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_summary is not None:
            result['isSummary'] = self.is_summary

        if self.task_id is not None:
            result['taskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isSummary') is not None:
            self.is_summary = m.get('isSummary')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        return self

