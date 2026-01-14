# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class ConstituteItem(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        emission_source: str = None,
        emission_source_key: str = None,
        enterprise_name: str = None,
        env_gas_emissions: List[main_models.ConstituteItemEnvGasEmissions] = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        raw_data: float = None,
        sub_constitute_items: List[main_models.ConstituteItem] = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.data_unit = data_unit
        self.emission_source = emission_source
        self.emission_source_key = emission_source_key
        self.enterprise_name = enterprise_name
        self.env_gas_emissions = env_gas_emissions
        self.name = name
        self.name_key = name_key
        self.ratio = ratio
        self.raw_data = raw_data
        self.sub_constitute_items = sub_constitute_items

    def validate(self):
        if self.env_gas_emissions:
            for v1 in self.env_gas_emissions:
                 if v1:
                    v1.validate()
        if self.sub_constitute_items:
            for v1 in self.sub_constitute_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.data_unit is not None:
            result['dataUnit'] = self.data_unit

        if self.emission_source is not None:
            result['emissionSource'] = self.emission_source

        if self.emission_source_key is not None:
            result['emissionSourceKey'] = self.emission_source_key

        if self.enterprise_name is not None:
            result['enterpriseName'] = self.enterprise_name

        result['envGasEmissions'] = []
        if self.env_gas_emissions is not None:
            for k1 in self.env_gas_emissions:
                result['envGasEmissions'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        if self.raw_data is not None:
            result['rawData'] = self.raw_data

        result['subConstituteItems'] = []
        if self.sub_constitute_items is not None:
            for k1 in self.sub_constitute_items:
                result['subConstituteItems'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('dataUnit') is not None:
            self.data_unit = m.get('dataUnit')

        if m.get('emissionSource') is not None:
            self.emission_source = m.get('emissionSource')

        if m.get('emissionSourceKey') is not None:
            self.emission_source_key = m.get('emissionSourceKey')

        if m.get('enterpriseName') is not None:
            self.enterprise_name = m.get('enterpriseName')

        self.env_gas_emissions = []
        if m.get('envGasEmissions') is not None:
            for k1 in m.get('envGasEmissions'):
                temp_model = main_models.ConstituteItemEnvGasEmissions()
                self.env_gas_emissions.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        self.sub_constitute_items = []
        if m.get('subConstituteItems') is not None:
            for k1 in m.get('subConstituteItems'):
                temp_model = main_models.ConstituteItem()
                self.sub_constitute_items.append(temp_model.from_map(k1))

        return self



class ConstituteItemEnvGasEmissions(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        gas_emission_data: float = None,
        name: str = None,
        type: str = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.gas_emission_data = gas_emission_data
        self.name = name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.gas_emission_data is not None:
            result['gasEmissionData'] = self.gas_emission_data

        if self.name is not None:
            result['name'] = self.name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('gasEmissionData') is not None:
            self.gas_emission_data = m.get('gasEmissionData')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

