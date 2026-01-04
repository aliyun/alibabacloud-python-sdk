# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class ListBusinessRegionsResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        geographic_sub_regions: List[main_models.ListBusinessRegionsResponseBodyGeographicSubRegions] = None,
        request_id: str = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The list of regions available for Express Connect circuits.
        self.geographic_sub_regions = geographic_sub_regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.geographic_sub_regions:
            for v1 in self.geographic_sub_regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['GeographicSubRegions'] = []
        if self.geographic_sub_regions is not None:
            for k1 in self.geographic_sub_regions:
                result['GeographicSubRegions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.geographic_sub_regions = []
        if m.get('GeographicSubRegions') is not None:
            for k1 in m.get('GeographicSubRegions'):
                temp_model = main_models.ListBusinessRegionsResponseBodyGeographicSubRegions()
                self.geographic_sub_regions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListBusinessRegionsResponseBodyGeographicSubRegions(DaraModel):
    def __init__(
        self,
        name: str = None,
        region_id: str = None,
    ):
        # The name of the region where circuits are available.
        self.name = name
        # The ID of the region where circuits are available.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

