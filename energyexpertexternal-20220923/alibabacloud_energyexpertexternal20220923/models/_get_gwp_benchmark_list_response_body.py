# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_energyexpertexternal20220923 import models as main_models
from darabonba.model import DaraModel

class GetGwpBenchmarkListResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetGwpBenchmarkListResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request. The value is unique for each request. This facilitates subsequent troubleshooting.
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
            temp_model = main_models.GetGwpBenchmarkListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetGwpBenchmarkListResponseBodyData(DaraModel):
    def __init__(
        self,
        items: List[main_models.GetGwpBenchmarkListResponseBodyDataItems] = None,
        unit: str = None,
    ):
        # Active carbon reduction ranking list.
        self.items = items
        # unit of emissions. The default value is `kgCO₂e/productUnit`. 
        # The `productUnit` is the unit selected for the product. The unit value is changed to `tCO₂e/productUnit` or `gCO₂e/productUnit`. For more information, see the remarks in the quantity column.
        self.unit = unit

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

        if self.unit is not None:
            result['unit'] = self.unit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.GetGwpBenchmarkListResponseBodyDataItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        return self

class GetGwpBenchmarkListResponseBodyDataItems(DaraModel):
    def __init__(
        self,
        active_reduction: float = None,
        benchmark_emission: float = None,
        benchmark_name: str = None,
        carbon_emission: float = None,
        name: str = None,
        percent: str = None,
    ):
        # `activeReduction=benchmarkEmission-carbonEmission` Generally, baseline emissions are greater than inventory emissions. Maintain four decimal places. Unit pertains to a higher-level unit.
        self.active_reduction = active_reduction
        # Benchmark emissions. Maintain four decimal places. Unit pertains to a higher-level unit.
        self.benchmark_emission = benchmark_emission
        # Benchmark name
        self.benchmark_name = benchmark_name
        # Inventory emissions. Maintain four decimal places. Unit pertains to a higher-level unit.
        self.carbon_emission = carbon_emission
        # name
        self.name = name
        # Unused temporarily.
        self.percent = percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_reduction is not None:
            result['activeReduction'] = self.active_reduction

        if self.benchmark_emission is not None:
            result['benchmarkEmission'] = self.benchmark_emission

        if self.benchmark_name is not None:
            result['benchmarkName'] = self.benchmark_name

        if self.carbon_emission is not None:
            result['carbonEmission'] = self.carbon_emission

        if self.name is not None:
            result['name'] = self.name

        if self.percent is not None:
            result['percent'] = self.percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activeReduction') is not None:
            self.active_reduction = m.get('activeReduction')

        if m.get('benchmarkEmission') is not None:
            self.benchmark_emission = m.get('benchmarkEmission')

        if m.get('benchmarkName') is not None:
            self.benchmark_name = m.get('benchmarkName')

        if m.get('carbonEmission') is not None:
            self.carbon_emission = m.get('carbonEmission')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('percent') is not None:
            self.percent = m.get('percent')

        return self

