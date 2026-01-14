# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetCarbonEmissionTrendResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetCarbonEmissionTrendResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
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
            temp_model = main_models.GetCarbonEmissionTrendResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetCarbonEmissionTrendResponseBodyData(DaraModel):
    def __init__(
        self,
        actual_emission_list: List[main_models.GetCarbonEmissionTrendResponseBodyDataActualEmissionList] = None,
        target_emission_list: List[main_models.GetCarbonEmissionTrendResponseBodyDataTargetEmissionList] = None,
    ):
        # Actual emission list.
        self.actual_emission_list = actual_emission_list
        # Target Emission List.
        self.target_emission_list = target_emission_list

    def validate(self):
        if self.actual_emission_list:
            for v1 in self.actual_emission_list:
                 if v1:
                    v1.validate()
        if self.target_emission_list:
            for v1 in self.target_emission_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['actualEmissionList'] = []
        if self.actual_emission_list is not None:
            for k1 in self.actual_emission_list:
                result['actualEmissionList'].append(k1.to_map() if k1 else None)

        result['targetEmissionList'] = []
        if self.target_emission_list is not None:
            for k1 in self.target_emission_list:
                result['targetEmissionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actual_emission_list = []
        if m.get('actualEmissionList') is not None:
            for k1 in m.get('actualEmissionList'):
                temp_model = main_models.GetCarbonEmissionTrendResponseBodyDataActualEmissionList()
                self.actual_emission_list.append(temp_model.from_map(k1))

        self.target_emission_list = []
        if m.get('targetEmissionList') is not None:
            for k1 in m.get('targetEmissionList'):
                temp_model = main_models.GetCarbonEmissionTrendResponseBodyDataTargetEmissionList()
                self.target_emission_list.append(temp_model.from_map(k1))

        return self

class GetCarbonEmissionTrendResponseBodyDataTargetEmissionList(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems] = None,
        year: str = None,
    ):
        # Data item list.
        self.items = items
        # The year.
        self.year = year

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class GetCarbonEmissionTrendResponseBodyDataTargetEmissionListItems(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        month: int = None,
        year: str = None,
    ):
        # Carbon emissions.
        self.carbon_emission_data = carbon_emission_data
        # The month.
        self.month = month
        # The year.
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

        if self.month is not None:
            result['month'] = self.month

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class GetCarbonEmissionTrendResponseBodyDataActualEmissionList(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems] = None,
        year: str = None,
    ):
        # Data item list.
        self.items = items
        # The year.
        self.year = year

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

class GetCarbonEmissionTrendResponseBodyDataActualEmissionListItems(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        month: int = None,
        year: str = None,
    ):
        # Carbon emissions.
        self.carbon_emission_data = carbon_emission_data
        # The month.
        self.month = month
        # The year.
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

        if self.month is not None:
            result['month'] = self.month

        if self.year is not None:
            result['year'] = self.year

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('carbonEmissionData') is not None:
            self.carbon_emission_data = m.get('carbonEmissionData')

        if m.get('month') is not None:
            self.month = m.get('month')

        if m.get('year') is not None:
            self.year = m.get('year')

        return self

