# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyActiveOperationTasksRequest(DaraModel):
    def __init__(
        self,
        ids: str = None,
        immediate_start: int = None,
        region_id: str = None,
        switch_time: str = None,
    ):
        # The O&M event ID.
        # 
        # This parameter is required.
        self.ids = ids
        # Specifies whether to immediately execute the event. Valid values:
        # 
        # - 1: immediately execute
        # - 0: execute at the specified time.
        self.immediate_start = immediate_start
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The switchover start time in the YYYY-MM-DDThh:mm:ssZ format.
        self.switch_time = switch_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ids is not None:
            result['Ids'] = self.ids

        if self.immediate_start is not None:
            result['ImmediateStart'] = self.immediate_start

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.switch_time is not None:
            result['SwitchTime'] = self.switch_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')

        if m.get('ImmediateStart') is not None:
            self.immediate_start = m.get('ImmediateStart')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SwitchTime') is not None:
            self.switch_time = m.get('SwitchTime')

        return self

