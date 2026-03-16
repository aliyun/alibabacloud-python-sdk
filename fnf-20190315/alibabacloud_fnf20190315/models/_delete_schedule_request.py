# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteScheduleRequest(DaraModel):
    def __init__(
        self,
        flow_name: str = None,
        schedule_name: str = None,
    ):
        # The name of the workflow with which the scheduling task that you want to delete is associated.
        # 
        # This parameter is required.
        self.flow_name = flow_name
        # The name of the scheduling task that you want to delete.
        # 
        # This parameter is required.
        self.schedule_name = schedule_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.schedule_name is not None:
            result['ScheduleName'] = self.schedule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('ScheduleName') is not None:
            self.schedule_name = m.get('ScheduleName')

        return self

