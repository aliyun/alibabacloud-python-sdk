# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchUpdateSystemRunningPlanRequest(DaraModel):
    def __init__(
        self,
        control_type: int = None,
        date_type: int = None,
        earliest_startup_time: str = None,
        end_time: str = None,
        factory_id: str = None,
        latest_shutdown_time: str = None,
        max_carbon_dioxide: float = None,
        max_tem: float = None,
        min_tem: float = None,
        season_mode: int = None,
        start_time: str = None,
        system_id: str = None,
        working_end_time: str = None,
        working_start_time: str = None,
    ):
        self.control_type = control_type
        self.date_type = date_type
        self.earliest_startup_time = earliest_startup_time
        # This parameter is required.
        self.end_time = end_time
        # This parameter is required.
        self.factory_id = factory_id
        self.latest_shutdown_time = latest_shutdown_time
        self.max_carbon_dioxide = max_carbon_dioxide
        self.max_tem = max_tem
        self.min_tem = min_tem
        self.season_mode = season_mode
        # This parameter is required.
        self.start_time = start_time
        # This parameter is required.
        self.system_id = system_id
        self.working_end_time = working_end_time
        self.working_start_time = working_start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_type is not None:
            result['controlType'] = self.control_type

        if self.date_type is not None:
            result['dateType'] = self.date_type

        if self.earliest_startup_time is not None:
            result['earliestStartupTime'] = self.earliest_startup_time

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.factory_id is not None:
            result['factoryId'] = self.factory_id

        if self.latest_shutdown_time is not None:
            result['latestShutdownTime'] = self.latest_shutdown_time

        if self.max_carbon_dioxide is not None:
            result['maxCarbonDioxide'] = self.max_carbon_dioxide

        if self.max_tem is not None:
            result['maxTem'] = self.max_tem

        if self.min_tem is not None:
            result['minTem'] = self.min_tem

        if self.season_mode is not None:
            result['seasonMode'] = self.season_mode

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.system_id is not None:
            result['systemId'] = self.system_id

        if self.working_end_time is not None:
            result['workingEndTime'] = self.working_end_time

        if self.working_start_time is not None:
            result['workingStartTime'] = self.working_start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('controlType') is not None:
            self.control_type = m.get('controlType')

        if m.get('dateType') is not None:
            self.date_type = m.get('dateType')

        if m.get('earliestStartupTime') is not None:
            self.earliest_startup_time = m.get('earliestStartupTime')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('factoryId') is not None:
            self.factory_id = m.get('factoryId')

        if m.get('latestShutdownTime') is not None:
            self.latest_shutdown_time = m.get('latestShutdownTime')

        if m.get('maxCarbonDioxide') is not None:
            self.max_carbon_dioxide = m.get('maxCarbonDioxide')

        if m.get('maxTem') is not None:
            self.max_tem = m.get('maxTem')

        if m.get('minTem') is not None:
            self.min_tem = m.get('minTem')

        if m.get('seasonMode') is not None:
            self.season_mode = m.get('seasonMode')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('systemId') is not None:
            self.system_id = m.get('systemId')

        if m.get('workingEndTime') is not None:
            self.working_end_time = m.get('workingEndTime')

        if m.get('workingStartTime') is not None:
            self.working_start_time = m.get('workingStartTime')

        return self

