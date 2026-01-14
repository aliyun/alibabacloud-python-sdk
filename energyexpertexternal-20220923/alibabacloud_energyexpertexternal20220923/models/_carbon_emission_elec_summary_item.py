# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CarbonEmissionElecSummaryItem(DaraModel):
    def __init__(
        self,
        carbon_emission_data: float = None,
        data_unit: str = None,
        name: str = None,
        ratio: float = None,
        raw_data: float = None,
    ):
        self.carbon_emission_data = carbon_emission_data
        self.data_unit = data_unit
        self.name = name
        self.ratio = ratio
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

        if m.get('ratio') is not None:
            self.ratio = m.get('ratio')

        if m.get('rawData') is not None:
            self.raw_data = m.get('rawData')

        return self

