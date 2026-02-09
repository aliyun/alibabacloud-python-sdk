# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoadForecastJobShrinkRequest(DaraModel):
    def __init__(
        self,
        business_key: str = None,
        data_mode: str = None,
        device_type: str = None,
        duration: int = None,
        forecast_horizon: str = None,
        freq: str = None,
        history_data_shrink: str = None,
        model_version: str = None,
        run_date: str = None,
        system_type: str = None,
        time_zone: str = None,
    ):
        self.business_key = business_key
        self.data_mode = data_mode
        self.device_type = device_type
        self.duration = duration
        self.forecast_horizon = forecast_horizon
        self.freq = freq
        self.history_data_shrink = history_data_shrink
        self.model_version = model_version
        self.run_date = run_date
        self.system_type = system_type
        self.time_zone = time_zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_key is not None:
            result['BusinessKey'] = self.business_key

        if self.data_mode is not None:
            result['DataMode'] = self.data_mode

        if self.device_type is not None:
            result['DeviceType'] = self.device_type

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.forecast_horizon is not None:
            result['ForecastHorizon'] = self.forecast_horizon

        if self.freq is not None:
            result['Freq'] = self.freq

        if self.history_data_shrink is not None:
            result['HistoryData'] = self.history_data_shrink

        if self.model_version is not None:
            result['ModelVersion'] = self.model_version

        if self.run_date is not None:
            result['RunDate'] = self.run_date

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessKey') is not None:
            self.business_key = m.get('BusinessKey')

        if m.get('DataMode') is not None:
            self.data_mode = m.get('DataMode')

        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ForecastHorizon') is not None:
            self.forecast_horizon = m.get('ForecastHorizon')

        if m.get('Freq') is not None:
            self.freq = m.get('Freq')

        if m.get('HistoryData') is not None:
            self.history_data_shrink = m.get('HistoryData')

        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')

        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        return self

