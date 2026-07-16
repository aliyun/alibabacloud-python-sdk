# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StopScheduledPreloadExecutionRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The preload plan ID, obtained from the SuccessExecutions[].Id field returned by CreateScheduledPreloadExecutions. Before calling this API, you must first create a preload task by calling CreateScheduledPreloadJob, and then create an execution plan by calling CreateScheduledPreloadExecutions.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

