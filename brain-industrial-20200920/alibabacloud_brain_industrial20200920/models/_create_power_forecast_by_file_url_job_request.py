# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_brain_industrial20200920 import models as main_models
from darabonba.model import DaraModel

class CreatePowerForecastByFileUrlJobRequest(DaraModel):
    def __init__(
        self,
        business_key: str = None,
        data_mode: str = None,
        device_type: str = None,
        duration: int = None,
        forecast_horizon: str = None,
        freq: str = None,
        history_url: str = None,
        location: main_models.CreatePowerForecastByFileUrlJobRequestLocation = None,
        model_version: str = None,
        run_date: str = None,
        system_type: str = None,
        time_column: str = None,
        time_zone: str = None,
        value_column: str = None,
    ):
        self.business_key = business_key
        self.data_mode = data_mode
        self.device_type = device_type
        self.duration = duration
        self.forecast_horizon = forecast_horizon
        self.freq = freq
        self.history_url = history_url
        self.location = location
        self.model_version = model_version
        self.run_date = run_date
        self.system_type = system_type
        self.time_column = time_column
        self.time_zone = time_zone
        self.value_column = value_column

    def validate(self):
        if self.location:
            self.location.validate()

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

        if self.history_url is not None:
            result['HistoryUrl'] = self.history_url

        if self.location is not None:
            result['Location'] = self.location.to_map()

        if self.model_version is not None:
            result['ModelVersion'] = self.model_version

        if self.run_date is not None:
            result['RunDate'] = self.run_date

        if self.system_type is not None:
            result['SystemType'] = self.system_type

        if self.time_column is not None:
            result['TimeColumn'] = self.time_column

        if self.time_zone is not None:
            result['TimeZone'] = self.time_zone

        if self.value_column is not None:
            result['ValueColumn'] = self.value_column

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

        if m.get('HistoryUrl') is not None:
            self.history_url = m.get('HistoryUrl')

        if m.get('Location') is not None:
            temp_model = main_models.CreatePowerForecastByFileUrlJobRequestLocation()
            self.location = temp_model.from_map(m.get('Location'))

        if m.get('ModelVersion') is not None:
            self.model_version = m.get('ModelVersion')

        if m.get('RunDate') is not None:
            self.run_date = m.get('RunDate')

        if m.get('SystemType') is not None:
            self.system_type = m.get('SystemType')

        if m.get('TimeColumn') is not None:
            self.time_column = m.get('TimeColumn')

        if m.get('TimeZone') is not None:
            self.time_zone = m.get('TimeZone')

        if m.get('ValueColumn') is not None:
            self.value_column = m.get('ValueColumn')

        return self

class CreatePowerForecastByFileUrlJobRequestLocation(DaraModel):
    def __init__(
        self,
        altitude: float = None,
        latitude: float = None,
        longitude: float = None,
    ):
        self.altitude = altitude
        self.latitude = latitude
        self.longitude = longitude

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.altitude is not None:
            result['Altitude'] = self.altitude

        if self.latitude is not None:
            result['Latitude'] = self.latitude

        if self.longitude is not None:
            result['Longitude'] = self.longitude

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Altitude') is not None:
            self.altitude = m.get('Altitude')

        if m.get('Latitude') is not None:
            self.latitude = m.get('Latitude')

        if m.get('Longitude') is not None:
            self.longitude = m.get('Longitude')

        return self

