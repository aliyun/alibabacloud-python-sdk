# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartDIJobShrinkRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        force_to_rerun: bool = None,
        realtime_start_settings_shrink: str = None,
    ):
        # The task ID.
        # 
        # This parameter is required.
        self.dijob_id = dijob_id
        # Specifies whether to forcefully rerun all synchronization steps. If you do not configure this parameter, the system does not forcefully rerun the task.
        self.force_to_rerun = force_to_rerun
        # The settings for the start.
        self.realtime_start_settings_shrink = realtime_start_settings_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dijob_id is not None:
            result['DIJobId'] = self.dijob_id

        if self.force_to_rerun is not None:
            result['ForceToRerun'] = self.force_to_rerun

        if self.realtime_start_settings_shrink is not None:
            result['RealtimeStartSettings'] = self.realtime_start_settings_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('ForceToRerun') is not None:
            self.force_to_rerun = m.get('ForceToRerun')

        if m.get('RealtimeStartSettings') is not None:
            self.realtime_start_settings_shrink = m.get('RealtimeStartSettings')

        return self

