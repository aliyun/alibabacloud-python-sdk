# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class UpdateGatewayMaintenancePeriodRequest(DaraModel):
    def __init__(
        self,
        maintenance_period: main_models.UpdateGatewayMaintenancePeriodRequestMaintenancePeriod = None,
    ):
        self.maintenance_period = maintenance_period

    def validate(self):
        if self.maintenance_period:
            self.maintenance_period.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.maintenance_period is not None:
            result['maintenancePeriod'] = self.maintenance_period.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maintenancePeriod') is not None:
            temp_model = main_models.UpdateGatewayMaintenancePeriodRequestMaintenancePeriod()
            self.maintenance_period = temp_model.from_map(m.get('maintenancePeriod'))

        return self

class UpdateGatewayMaintenancePeriodRequestMaintenancePeriod(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
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

        if self.start_time is not None:
            result['startTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        return self

