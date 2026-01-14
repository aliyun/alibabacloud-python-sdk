# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetAreaElecConstituteResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetAreaElecConstituteResponseBodyData = None,
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
            temp_model = main_models.GetAreaElecConstituteResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetAreaElecConstituteResponseBodyData(DaraModel):
    def __init__(
        self,
        light: List[main_models.CarbonEmissionElecSummaryItem] = None,
        nuclear: List[main_models.CarbonEmissionElecSummaryItem] = None,
        renewing: List[main_models.CarbonEmissionElecSummaryItem] = None,
        urban: List[main_models.CarbonEmissionElecSummaryItem] = None,
        water: List[main_models.CarbonEmissionElecSummaryItem] = None,
        wind: List[main_models.CarbonEmissionElecSummaryItem] = None,
        zero: List[main_models.CarbonEmissionElecSummaryItem] = None,
    ):
        # Photoelectric power consumption and carbon emission data of each enterprise.
        self.light = light
        # Data on nuclear power consumption and carbon emissions at each enterprise.
        self.nuclear = nuclear
        # Data on renewable electricity consumption and carbon emissions at each enterprise.
        self.renewing = renewing
        # Data on mains electricity consumption and carbon emission of each enterprise.
        self.urban = urban
        # Hydropower consumption and carbon emission data of each enterprise.
        self.water = water
        # Wind power consumption and carbon emission data of each enterprise.
        self.wind = wind
        # Data of zero electricity consumption and carbon emission of each enterprise.
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
                temp_model = main_models.CarbonEmissionElecSummaryItem()
                self.light.append(temp_model.from_map(k1))

        self.nuclear = []
        if m.get('nuclear') is not None:
            for k1 in m.get('nuclear'):
                temp_model = main_models.CarbonEmissionElecSummaryItem()
                self.nuclear.append(temp_model.from_map(k1))

        self.renewing = []
        if m.get('renewing') is not None:
            for k1 in m.get('renewing'):
                temp_model = main_models.CarbonEmissionElecSummaryItem()
                self.renewing.append(temp_model.from_map(k1))

        self.urban = []
        if m.get('urban') is not None:
            for k1 in m.get('urban'):
                temp_model = main_models.CarbonEmissionElecSummaryItem()
                self.urban.append(temp_model.from_map(k1))

        self.water = []
        if m.get('water') is not None:
            for k1 in m.get('water'):
                temp_model = main_models.CarbonEmissionElecSummaryItem()
                self.water.append(temp_model.from_map(k1))

        self.wind = []
        if m.get('wind') is not None:
            for k1 in m.get('wind'):
                temp_model = main_models.CarbonEmissionElecSummaryItem()
                self.wind.append(temp_model.from_map(k1))

        self.zero = []
        if m.get('zero') is not None:
            for k1 in m.get('zero'):
                temp_model = main_models.CarbonEmissionElecSummaryItem()
                self.zero.append(temp_model.from_map(k1))

        return self

