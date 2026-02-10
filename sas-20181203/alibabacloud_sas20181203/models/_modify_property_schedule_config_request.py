# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPropertyScheduleConfigRequest(DaraModel):
    def __init__(
        self,
        schedule_time: str = None,
        type: str = None,
    ):
        # The new collection frequency of asset fingerprints. Valid values:
        # 
        # *   **0**: disabled, which indicates that the asset fingerprints are not automatically or periodically collected.
        # *   **1**: collects asset fingerprints once an hour.
        # *   **3**: collects asset fingerprints once every 3 hours.
        # *   **12**: collects asset fingerprints once every 12 hours.
        # *   **24**: collects asset fingerprints once a day.
        # *   **168**: collects asset fingerprints once every 7 days.
        # 
        # This parameter is required.
        self.schedule_time = schedule_time
        # The type of the asset fingerprints for which you want to modify the collection frequency. Valid values:
        # 
        # *   **scheduler_port_period**: listening port
        # *   **scheduler_process_period**: running process
        # *   **scheduler_account_period**: account
        # *   **scheduler_software_period**: software
        # *   **scheduler_cron_period**: scheduled task
        # *   **scheduler_sca_period**: middleware, database, or web service
        # *   **scheduler_autorun_period**: startup item
        # *   **scheduler_lkm_period**: kernel module
        # *   **scheduler_sca_proxy_period**: website
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

