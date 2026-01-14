# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class OrgEmission(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        module_emission_list: List[main_models.OrgEmissionModuleEmissionList] = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
        sub_emission_items: List[main_models.OrgEmission] = None,
        weighting_carbon_emission_data: float = None,
        weighting_proportion: float = None,
        weighting_ratio: float = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.module_emission_list = module_emission_list
        self.name = name
        self.name_key = name_key
        self.ratio = ratio
        self.sub_emission_items = sub_emission_items
        self.weighting_carbon_emission_data = weighting_carbon_emission_data
        self.weighting_proportion = weighting_proportion
        self.weighting_ratio = weighting_ratio

    def validate(self):
        if self.module_emission_list:
            for v1 in self.module_emission_list:
                 if v1:
                    v1.validate()
        if self.sub_emission_items:
            for v1 in self.sub_emission_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        result['moduleEmissionList'] = []
        if self.module_emission_list is not None:
            for k1 in self.module_emission_list:
                result['moduleEmissionList'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        result['subEmissionItems'] = []
        if self.sub_emission_items is not None:
            for k1 in self.sub_emission_items:
                result['subEmissionItems'].append(k1.to_map() if k1 else None)

        if self.weighting_carbon_emission_data is not None:
            result['weightingCarbonEmissionData'] = self.weighting_carbon_emission_data

        if self.weighting_proportion is not None:
            result['weightingProportion'] = self.weighting_proportion

        if self.weighting_ratio is not None:
            result['weightingRatio'] = self.weighting_ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        self.module_emission_list = []
        if m.get('moduleEmissionList') is not None:
            for k1 in m.get('moduleEmissionList'):
                temp_model = main_models.OrgEmissionModuleEmissionList()
                self.module_emission_list.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        self.sub_emission_items = []
        if m.get('subEmissionItems') is not None:
            for k1 in m.get('subEmissionItems'):
                temp_model = main_models.OrgEmission()
                self.sub_emission_items.append(temp_model.from_map(k1))

        if m.get('weightingCarbonEmissionData') is not None:
            self.weighting_carbon_emission_data = m.get('weightingCarbonEmissionData')

        if m.get('weightingProportion') is not None:
            self.weighting_proportion = m.get('weightingProportion')

        if m.get('weightingRatio') is not None:
            self.weighting_ratio = m.get('weightingRatio')

        return self

class OrgEmissionModuleEmissionList(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        name: str = None,
        name_key: str = None,
        ratio: float = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.name = name
        self.name_key = name_key
        self.ratio = ratio

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.carbon_emission_data is not None:
            result['carbonEmissionData'] = self.carbon_emission_data

        if self.name is not None:
            result['name'] = self.name

        if self.name_key is not None:
            result['nameKey'] = self.name_key

        if self.ratio is not None:
            result['ratio'] = self.ratio

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nameKey') is not None:
            self.name_key = m.get('nameKey')

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        return self

