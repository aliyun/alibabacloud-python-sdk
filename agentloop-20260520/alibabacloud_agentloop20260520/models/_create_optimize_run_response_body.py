# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateOptimizeRunResponseBody(DaraModel):
    def __init__(
        self,
        optimize_run: Dict[str, Any] = None,
        optimize_run_id: str = None,
        request_id: str = None,
    ):
        # The details of the created run. You can call the GetOptimizeRun operation to query the subsequent status.
        self.optimize_run = optimize_run
        # The run ID.
        self.optimize_run_id = optimize_run_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.optimize_run is not None:
            result['optimizeRun'] = self.optimize_run

        if self.optimize_run_id is not None:
            result['optimizeRunId'] = self.optimize_run_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('optimizeRun') is not None:
            self.optimize_run = m.get('optimizeRun')

        if m.get('optimizeRunId') is not None:
            self.optimize_run_id = m.get('optimizeRunId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

