# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetElecTrendResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetElecTrendResponseBodyData = None,
        request_id: str = None,
    ):
        # The code returned for the request. A value of Success indicates that the request was successful. Other values indicate that the request failed. You can troubleshoot the error by viewing the error message returned.
        self.code = code
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetElecTrendResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetElecTrendResponseBodyData(DaraModel):
    def __init__(
        self,
        light: List[main_models.GetElecTrendResponseBodyDataLight] = None,
        nuclear: List[main_models.GetElecTrendResponseBodyDataNuclear] = None,
        renewing: List[main_models.GetElecTrendResponseBodyDataRenewing] = None,
        urban: List[main_models.GetElecTrendResponseBodyDataUrban] = None,
        water: List[main_models.GetElecTrendResponseBodyDataWater] = None,
        wind: List[main_models.GetElecTrendResponseBodyDataWind] = None,
        zero: List[main_models.GetElecTrendResponseBodyDataZero] = None,
    ):
        # Photoelectricity monthly electricity consumption and carbon emissions and other data.
        self.light = light
        # Monthly electricity consumption and carbon emissions data for nuclear power
        self.nuclear = nuclear
        # Monthly data on renewable electricity consumption and carbon emissions
        self.renewing = renewing
        # Data such as monthly electricity consumption and carbon emissions from the mains.
        self.urban = urban
        # Monthly data on electricity consumption and carbon emissions for hydropower.
        self.water = water
        # Monthly wind power consumption and carbon emission data
        self.wind = wind
        # Zero electricity monthly electricity consumption and carbon emissions and other data.
        self.zero = zero

    def validate(self):
        if self.light:
            for v1 in self.light:
                 if v1:
                    v1.validate()
        if self.nuclear:
            for v1 in self.nuclear:
                 if v1:
                    v1.validate()
        if self.renewing:
            for v1 in self.renewing:
                 if v1:
                    v1.validate()
        if self.urban:
            for v1 in self.urban:
                 if v1:
                    v1.validate()
        if self.water:
            for v1 in self.water:
                 if v1:
                    v1.validate()
        if self.wind:
            for v1 in self.wind:
                 if v1:
                    v1.validate()
        if self.zero:
            for v1 in self.zero:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['light'] = []
        if self.light is not None:
            for k1 in self.light:
                result['light'].append(k1.to_map() if k1 else None)

        result['nuclear'] = []
        if self.nuclear is not None:
            for k1 in self.nuclear:
                result['nuclear'].append(k1.to_map() if k1 else None)

        result['renewing'] = []
        if self.renewing is not None:
            for k1 in self.renewing:
                result['renewing'].append(k1.to_map() if k1 else None)

        result['urban'] = []
        if self.urban is not None:
            for k1 in self.urban:
                result['urban'].append(k1.to_map() if k1 else None)

        result['water'] = []
        if self.water is not None:
            for k1 in self.water:
                result['water'].append(k1.to_map() if k1 else None)

        result['wind'] = []
        if self.wind is not None:
            for k1 in self.wind:
                result['wind'].append(k1.to_map() if k1 else None)

        result['zero'] = []
        if self.zero is not None:
            for k1 in self.zero:
                result['zero'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.light = []
        if m.get('light') is not None:
            for k1 in m.get('light'):
                temp_model = main_models.GetElecTrendResponseBodyDataLight()
                self.light.append(temp_model.from_map(k1))

        self.nuclear = []
        if m.get('nuclear') is not None:
            for k1 in m.get('nuclear'):
                temp_model = main_models.GetElecTrendResponseBodyDataNuclear()
                self.nuclear.append(temp_model.from_map(k1))

        self.renewing = []
        if m.get('renewing') is not None:
            for k1 in m.get('renewing'):
                temp_model = main_models.GetElecTrendResponseBodyDataRenewing()
                self.renewing.append(temp_model.from_map(k1))

        self.urban = []
        if m.get('urban') is not None:
            for k1 in m.get('urban'):
                temp_model = main_models.GetElecTrendResponseBodyDataUrban()
                self.urban.append(temp_model.from_map(k1))

        self.water = []
        if m.get('water') is not None:
            for k1 in m.get('water'):
                temp_model = main_models.GetElecTrendResponseBodyDataWater()
                self.water.append(temp_model.from_map(k1))

        self.wind = []
        if m.get('wind') is not None:
            for k1 in m.get('wind'):
                temp_model = main_models.GetElecTrendResponseBodyDataWind()
                self.wind.append(temp_model.from_map(k1))

        self.zero = []
        if m.get('zero') is not None:
            for k1 in m.get('zero'):
                temp_model = main_models.GetElecTrendResponseBodyDataZero()
                self.zero.append(temp_model.from_map(k1))

        return self

class GetElecTrendResponseBodyDataZero(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit

        if self.month is not None:
            result['month'] = self.month

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class GetElecTrendResponseBodyDataWind(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit

        if self.month is not None:
            result['month'] = self.month

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class GetElecTrendResponseBodyDataWater(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e. 50%).
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit

        if self.month is not None:
            result['month'] = self.month

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class GetElecTrendResponseBodyDataUrban(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e. 50%).
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit

        if self.month is not None:
            result['month'] = self.month

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class GetElecTrendResponseBodyDataRenewing(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit

        if self.month is not None:
            result['month'] = self.month

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class GetElecTrendResponseBodyDataNuclear(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The price unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power Type Name
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit

        if self.month is not None:
            result['month'] = self.month

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class GetElecTrendResponseBodyDataLight(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        month: int = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        year: str = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # Month
        self.month = month
        # Power type name.
        self.name = name
        # Power Type Code
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e. 50%).
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data
        # Year
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit

        if self.month is not None:
            result['month'] = self.month

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

