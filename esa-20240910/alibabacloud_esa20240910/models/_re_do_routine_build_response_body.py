# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReDoRoutineBuildResponseBody(DaraModel):
    def __init__(
        self,
        pipe_line_run_id: int = None,
        request_id: str = None,
        routine_build_id: int = None,
    ):
        # The workflow execution ID.
        self.pipe_line_run_id = pipe_line_run_id
        # The request ID.
        self.request_id = request_id
        # The ID of the ER build task.
        self.routine_build_id = routine_build_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pipe_line_run_id is not None:
            result['PipeLineRunId'] = self.pipe_line_run_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.routine_build_id is not None:
            result['RoutineBuildId'] = self.routine_build_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PipeLineRunId') is not None:
            self.pipe_line_run_id = m.get('PipeLineRunId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoutineBuildId') is not None:
            self.routine_build_id = m.get('RoutineBuildId')

        return self

