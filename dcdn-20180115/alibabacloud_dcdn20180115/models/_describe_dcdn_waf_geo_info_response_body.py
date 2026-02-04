# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dcdn20180115 import models as main_models
from darabonba.model import DaraModel

class DescribeDcdnWafGeoInfoResponseBody(DaraModel):
    def __init__(
        self,
        content: List[main_models.DescribeDcdnWafGeoInfoResponseBodyContent] = None,
        request_id: str = None,
    ):
        # The type of information about the country or region.
        self.content = content
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.DescribeDcdnWafGeoInfoResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDcdnWafGeoInfoResponseBodyContent(DaraModel):
    def __init__(
        self,
        continents: List[main_models.DescribeDcdnWafGeoInfoResponseBodyContentContinents] = None,
        type: str = None,
    ):
        # The information about the country or region.
        self.continents = continents
        # The type of the region.
        # 
        # *   CN: China
        # *   Other: outside China
        self.type = type

    def validate(self):
        if self.continents:
            for v1 in self.continents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Continents'] = []
        if self.continents is not None:
            for k1 in self.continents:
                result['Continents'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.continents = []
        if m.get('Continents') is not None:
            for k1 in m.get('Continents'):
                temp_model = main_models.DescribeDcdnWafGeoInfoResponseBodyContentContinents()
                self.continents.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeDcdnWafGeoInfoResponseBodyContentContinents(DaraModel):
    def __init__(
        self,
        name: str = None,
        regions: List[main_models.DescribeDcdnWafGeoInfoResponseBodyContentContinentsRegions] = None,
    ):
        # The district to which the country or region belongs.
        self.name = name
        # The region information.
        self.regions = regions

    def validate(self):
        if self.regions:
            for v1 in self.regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.DescribeDcdnWafGeoInfoResponseBodyContentContinentsRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class DescribeDcdnWafGeoInfoResponseBodyContentContinentsRegions(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the country or region.
        self.name = name
        # The code of the country or region.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

