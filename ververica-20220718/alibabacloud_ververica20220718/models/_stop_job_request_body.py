# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopJobRequestBody(DaraModel):
    def __init__(
        self,
        stop_strategy: str = None,
    ):
        # The strategy that is used to stop a job. Valid values:
        # 
        # *   `NONE`: Directly stop the job.
        # *   `STOP_WITH_SAVEPOINT`: Stop the job after a savepoint is generated.
        # *   `STOP_WITH_DRAIN`: Stop the job and drain the pipeline. Use this strategy only if you want to permanently terminate the job.
        # 
        # This parameter is required.
        self.stop_strategy = stop_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.stop_strategy is not None:
            result['stopStrategy'] = self.stop_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stopStrategy') is not None:
            self.stop_strategy = m.get('stopStrategy')

        return self

