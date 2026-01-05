# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class StartDIJobRequest(DaraModel):
    def __init__(
        self,
        dijob_id: int = None,
        force_to_rerun: bool = None,
        id: int = None,
        realtime_start_settings: main_models.StartDIJobRequestRealtimeStartSettings = None,
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
        self.realtime_start_settings = realtime_start_settings

    def validate(self):
        if self.realtime_start_settings:
            self.realtime_start_settings.validate()

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

        if self.realtime_start_settings is not None:
            result['RealtimeStartSettings'] = self.realtime_start_settings.to_map()

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
            temp_model = main_models.StartDIJobRequestRealtimeStartSettings()
            self.realtime_start_settings = temp_model.from_map(m.get('RealtimeStartSettings'))

        return self

class StartDIJobRequestRealtimeStartSettings(DaraModel):
    def __init__(
        self,
        failover_settings: main_models.StartDIJobRequestRealtimeStartSettingsFailoverSettings = None,
        start_time: int = None,
    ):
        # This parameter is deprecated. Use advanced parameters for failover settings when you create a task.
        self.failover_settings = failover_settings
        # The start time.
        self.start_time = start_time

    def validate(self):
        if self.failover_settings:
            self.failover_settings.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failover_settings is not None:
            result['FailoverSettings'] = self.failover_settings.to_map()

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailoverSettings') is not None:
            temp_model = main_models.StartDIJobRequestRealtimeStartSettingsFailoverSettings()
            self.failover_settings = temp_model.from_map(m.get('FailoverSettings'))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class StartDIJobRequestRealtimeStartSettingsFailoverSettings(DaraModel):
    def __init__(
        self,
        interval: int = None,
        upper_limit: int = None,
    ):
        # This parameter is deprecated. Use advanced parameters for failover settings when you create a task.
        self.interval = interval
        # This parameter is deprecated. Use advanced parameters for failover settings when you create a task.
        self.upper_limit = upper_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.interval is not None:
            result['Interval'] = self.interval

        if self.upper_limit is not None:
            result['UpperLimit'] = self.upper_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('UpperLimit') is not None:
            self.upper_limit = m.get('UpperLimit')

        return self

