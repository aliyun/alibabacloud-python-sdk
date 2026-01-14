# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetElecConstituteResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetElecConstituteResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # Id of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetElecConstituteResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetElecConstituteResponseBodyData(DaraModel):
    def __init__(
        self,
        light: main_models.GetElecConstituteResponseBodyDataLight = None,
        nuclear: main_models.GetElecConstituteResponseBodyDataNuclear = None,
        renewing: main_models.GetElecConstituteResponseBodyDataRenewing = None,
        urban: main_models.GetElecConstituteResponseBodyDataUrban = None,
        water: main_models.GetElecConstituteResponseBodyDataWater = None,
        wind: main_models.GetElecConstituteResponseBodyDataWind = None,
        zero: main_models.GetElecConstituteResponseBodyDataZero = None,
    ):
        # Photoelectric power consumption and carbon emission data of each enterprise.
        self.light = light
        # Data on nuclear power consumption and carbon emissions at each enterprise.
        self.nuclear = nuclear
        # Data on renewable electricity consumption and carbon emissions at each enterprise.
        self.renewing = renewing
        # Data on mains power electricity consumption and carbon emission of each enterprise.
        self.urban = urban
        # Hydropower consumption and carbon emission data of each enterprise.
        self.water = water
        # Wind power consumption and carbon emission data of each enterprise.
        self.wind = wind
        # Data of zero electricity consumption and carbon emission of each enterprise.
        self.zero = zero

    def validate(self):
        if self.light:
            self.light.validate()
        if self.nuclear:
            self.nuclear.validate()
        if self.renewing:
            self.renewing.validate()
        if self.urban:
            self.urban.validate()
        if self.water:
            self.water.validate()
        if self.wind:
            self.wind.validate()
        if self.zero:
            self.zero.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.light is not None:
            result['light'] = self.light.to_map()

        if self.nuclear is not None:
            result['nuclear'] = self.nuclear.to_map()

        if self.renewing is not None:
            result['renewing'] = self.renewing.to_map()

        if self.urban is not None:
            result['urban'] = self.urban.to_map()

        if self.water is not None:
            result['water'] = self.water.to_map()

        if self.wind is not None:
            result['wind'] = self.wind.to_map()

        if self.zero is not None:
            result['zero'] = self.zero.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('light') is not None:
            temp_model = main_models.GetElecConstituteResponseBodyDataLight()
            self.light = temp_model.from_map(m.get('light'))

        if m.get('nuclear') is not None:
            temp_model = main_models.GetElecConstituteResponseBodyDataNuclear()
            self.nuclear = temp_model.from_map(m.get('nuclear'))

        if m.get('renewing') is not None:
            temp_model = main_models.GetElecConstituteResponseBodyDataRenewing()
            self.renewing = temp_model.from_map(m.get('renewing'))

        if m.get('urban') is not None:
            temp_model = main_models.GetElecConstituteResponseBodyDataUrban()
            self.urban = temp_model.from_map(m.get('urban'))

        if m.get('water') is not None:
            temp_model = main_models.GetElecConstituteResponseBodyDataWater()
            self.water = temp_model.from_map(m.get('water'))

        if m.get('wind') is not None:
            temp_model = main_models.GetElecConstituteResponseBodyDataWind()
            self.wind = temp_model.from_map(m.get('wind'))

        if m.get('zero') is not None:
            temp_model = main_models.GetElecConstituteResponseBodyDataZero()
            self.zero = temp_model.from_map(m.get('zero'))

        return self

class GetElecConstituteResponseBodyDataZero(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

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

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        return self

class GetElecConstituteResponseBodyDataWind(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

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

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        return self

class GetElecConstituteResponseBodyDataWater(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

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

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        return self

class GetElecConstituteResponseBodyDataUrban(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

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

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        return self

class GetElecConstituteResponseBodyDataRenewing(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

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

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        return self

class GetElecConstituteResponseBodyDataNuclear(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

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

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        return self

class GetElecConstituteResponseBodyDataLight(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        # Carbon emission.
        self.carbon_emission_data = carbon_emission_data
        # The unit.
        self.data_unit = data_unit
        # The name.
        self.name = name
        # The unique identifier of name.
        self.name_key = name_key
        # Proportion of electricity consumption to all electricity consumption in the month: example value: 0.5 (i. e., 50%)
        self.ratio = ratio
        # Electricity consumption
        self.raw_data = raw_data

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

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        return self

