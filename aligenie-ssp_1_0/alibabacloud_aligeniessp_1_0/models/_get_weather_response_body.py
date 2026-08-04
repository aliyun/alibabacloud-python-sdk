# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligeniessp_1_0 import models as main_models
from darabonba.model import DaraModel

class GetWeatherResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: main_models.GetWeatherResponseBodyResult = None,
    ):
        # HttpCode
        self.code = code
        # error message
        self.message = message
        # Request ID
        self.request_id = request_id
        # model data
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            temp_model = main_models.GetWeatherResponseBodyResult()
            self.result = temp_model.from_map(m.get('Result'))

        return self

class GetWeatherResponseBodyResult(DaraModel):
    def __init__(
        self,
        current_meteorology: main_models.GetWeatherResponseBodyResultCurrentMeteorology = None,
    ):
        # Current weather
        self.current_meteorology = current_meteorology

    def validate(self):
        if self.current_meteorology:
            self.current_meteorology.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_meteorology is not None:
            result['CurrentMeteorology'] = self.current_meteorology.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentMeteorology') is not None:
            temp_model = main_models.GetWeatherResponseBodyResultCurrentMeteorology()
            self.current_meteorology = temp_model.from_map(m.get('CurrentMeteorology'))

        return self

class GetWeatherResponseBodyResultCurrentMeteorology(DaraModel):
    def __init__(
        self,
        temperature: main_models.GetWeatherResponseBodyResultCurrentMeteorologyTemperature = None,
        weather: main_models.GetWeatherResponseBodyResultCurrentMeteorologyWeather = None,
    ):
        # Temperature
        self.temperature = temperature
        # Daytime weather
        self.weather = weather

    def validate(self):
        if self.temperature:
            self.temperature.validate()
        if self.weather:
            self.weather.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.temperature is not None:
            result['Temperature'] = self.temperature.to_map()

        if self.weather is not None:
            result['Weather'] = self.weather.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Temperature') is not None:
            temp_model = main_models.GetWeatherResponseBodyResultCurrentMeteorologyTemperature()
            self.temperature = temp_model.from_map(m.get('Temperature'))

        if m.get('Weather') is not None:
            temp_model = main_models.GetWeatherResponseBodyResultCurrentMeteorologyWeather()
            self.weather = temp_model.from_map(m.get('Weather'))

        return self

class GetWeatherResponseBodyResultCurrentMeteorologyWeather(DaraModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        # Weather code: for example, "000,100"
        self.code = code
        # Weather name description: "Sunny (000), Multicloud (100), Overcast (101), Rain (200), Light rain (201), Light to moderate rain (202), Moderate rain (203), Moderate to heavy rain (204), Heavy rain (205), Heavy to storm rain (206), Storm rain (207), Heavy storm rain (209), Severe storm rain (211), Showers (212), Thunderstorms (213), Freezing rain (214), Snow (300), Sleet (301), Snow showers (302), Light snow (303), Light to moderate snow (304), Moderate snow (305), Heavy snow (307), Blizzard (309), Fog (400), Dust (501), Sand blowing (502), Sandstorm (503), Severe sandstorm (504), Mostly sunny (000), Partly cloudy (100), Light showers (212), Lightning (213), Ice pellets (214), Thunderstorms with hail (215), Light snow showers (302), Freezing fog (400), Haze (500), Dust whirls (502), Localized showers (212), Thunderstorm (213), Ice needles (214), Hail (215), Intense showers (212)"
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetWeatherResponseBodyResultCurrentMeteorologyTemperature(DaraModel):
    def __init__(
        self,
        current: str = None,
        current_desc: str = None,
        high: str = None,
        high_desc: str = None,
        logical: str = None,
        low: str = None,
        low_desc: str = None,
    ):
        # Current temperature value
        self.current = current
        # Description of the current temperature value
        self.current_desc = current_desc
        # Maximum temperature value
        self.high = high
        # Description of the maximum temperature value
        self.high_desc = high_desc
        # Temperature with logic, as follows:
        self.logical = logical
        # Lowest temperature
        self.low = low
        # Description of the lowest temperature
        self.low_desc = low_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['Current'] = self.current

        if self.current_desc is not None:
            result['CurrentDesc'] = self.current_desc

        if self.high is not None:
            result['High'] = self.high

        if self.high_desc is not None:
            result['HighDesc'] = self.high_desc

        if self.logical is not None:
            result['Logical'] = self.logical

        if self.low is not None:
            result['Low'] = self.low

        if self.low_desc is not None:
            result['LowDesc'] = self.low_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('CurrentDesc') is not None:
            self.current_desc = m.get('CurrentDesc')

        if m.get('High') is not None:
            self.high = m.get('High')

        if m.get('HighDesc') is not None:
            self.high_desc = m.get('HighDesc')

        if m.get('Logical') is not None:
            self.logical = m.get('Logical')

        if m.get('Low') is not None:
            self.low = m.get('Low')

        if m.get('LowDesc') is not None:
            self.low_desc = m.get('LowDesc')

        return self

