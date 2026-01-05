# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StartDIJobShrinkRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        force_to_rerun: bool = None,
        id: int = None,
        realtime_start_settings_shrink: str = None,
    ):
        # This parameter is deprecated. Use the Id parameter instead.
        self.dijob_id = dijob_id
        # Specifies whether to forcefully rerun all synchronization steps. If you do not configure this parameter, the system does not perform the forcible rerun operation.
        # 
        # *   If the system does not perform the forcible rerun operation, only the steps that are not run start to run.
        # *   If the system performs the forcible rerun operation, all steps start to rerun.
        self.force_to_rerun = force_to_rerun
        # The ID of the synchronization task.
        self.id = id
        # The settings for starting real-time synchronization.
        # 
        #     {
        #       "StartTime":1663765058
        #     }
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

        if self.id is not None:
            result['Id'] = self.id

        if self.realtime_start_settings_shrink is not None:
            result['RealtimeStartSettings'] = self.realtime_start_settings_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DIJobId') is not None:
            self.dijob_id = m.get('DIJobId')

        if m.get('ForceToRerun') is not None:
            self.force_to_rerun = m.get('ForceToRerun')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('RealtimeStartSettings') is not None:
            self.realtime_start_settings_shrink = m.get('RealtimeStartSettings')

        return self

