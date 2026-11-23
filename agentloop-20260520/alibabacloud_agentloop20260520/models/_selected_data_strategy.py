# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SelectedDataStrategy(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        eval_ids: List[str] = None,
        start_time: int = None,
    ):
        # The end time of the statistical window in UNIX seconds.
        self.end_time = end_time
        # The list of evaluation IDs.
        self.eval_ids = eval_ids
        # The estimated start time in milliseconds.
        # 
        # > You can modify this parameter only when the course is in the preview state.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.eval_ids is not None:
            result['evalIds'] = self.eval_ids

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('evalIds') is not None:
            self.eval_ids = m.get('evalIds')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

