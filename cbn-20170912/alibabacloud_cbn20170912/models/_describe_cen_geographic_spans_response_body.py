# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cbn20170912 import models as main_models
from darabonba.model import DaraModel

class DescribeCenGeographicSpansResponseBody(DaraModel):
    def __init__(
        self,
        geographic_span_models: main_models.DescribeCenGeographicSpansResponseBodyGeographicSpanModels = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.geographic_span_models = geographic_span_models
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.geographic_span_models:
            self.geographic_span_models.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.geographic_span_models is not None:
            result['GeographicSpanModels'] = self.geographic_span_models.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GeographicSpanModels') is not None:
            temp_model = main_models.DescribeCenGeographicSpansResponseBodyGeographicSpanModels()
            self.geographic_span_models = temp_model.from_map(m.get('GeographicSpanModels'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCenGeographicSpansResponseBodyGeographicSpanModels(DaraModel):
    def __init__(
        self,
        geographic_span_model: List[main_models.DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel] = None,
    ):
        self.geographic_span_model = geographic_span_model

    def validate(self):
        if self.geographic_span_model:
            for v1 in self.geographic_span_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['GeographicSpanModel'] = []
        if self.geographic_span_model is not None:
            for k1 in self.geographic_span_model:
                result['GeographicSpanModel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.geographic_span_model = []
        if m.get('GeographicSpanModel') is not None:
            for k1 in m.get('GeographicSpanModel'):
                temp_model = main_models.DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel()
                self.geographic_span_model.append(temp_model.from_map(k1))

        return self

class DescribeCenGeographicSpansResponseBodyGeographicSpanModelsGeographicSpanModel(DaraModel):
    def __init__(
        self,
        geographic_span_id: str = None,
        local_geo_region_id: str = None,
        opposite_geo_region_id: str = None,
    ):
        self.geographic_span_id = geographic_span_id
        self.local_geo_region_id = local_geo_region_id
        self.opposite_geo_region_id = opposite_geo_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.geographic_span_id is not None:
            result['GeographicSpanId'] = self.geographic_span_id

        if self.local_geo_region_id is not None:
            result['LocalGeoRegionId'] = self.local_geo_region_id

        if self.opposite_geo_region_id is not None:
            result['OppositeGeoRegionId'] = self.opposite_geo_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GeographicSpanId') is not None:
            self.geographic_span_id = m.get('GeographicSpanId')

        if m.get('LocalGeoRegionId') is not None:
            self.local_geo_region_id = m.get('LocalGeoRegionId')

        if m.get('OppositeGeoRegionId') is not None:
            self.opposite_geo_region_id = m.get('OppositeGeoRegionId')

        return self

