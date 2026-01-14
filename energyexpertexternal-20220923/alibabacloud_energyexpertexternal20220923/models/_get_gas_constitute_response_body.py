# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetGasConstituteResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.GetGasConstituteResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.GetGasConstituteResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGasConstituteResponseBodyData(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        gas_emission_data: float = None,
        name: str = None,
        ratio: float = None,
        type: int = None,
    ):
        # Carbon emissions
        self.carbon_emission_data = carbon_emission_data
        # Gas emissions
        self.gas_emission_data = gas_emission_data
        # Name of gas
        self.name = name
        # Proportion of carbon emissions. Example value: 0.5 (50%)
        self.ratio = ratio
        # Gas Type
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

        if self.ratio is not None:
            result['ratio'] = self.ratio

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

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

