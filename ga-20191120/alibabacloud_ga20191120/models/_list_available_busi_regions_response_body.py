# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListAvailableBusiRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: List[main_models.ListAvailableBusiRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The information about the regions.
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

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
        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.ListAvailableBusiRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAvailableBusiRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        china_mainland: bool = None,
        local_name: str = None,
        pop: bool = None,
        region_id: str = None,
    ):
        # Indicates whether the region is in the Chinese mainland. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.china_mainland = china_mainland
        # The name of the region.
        self.local_name = local_name
        # Indicates whether it is a point of presence (PoP) of Alibaba Cloud. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.pop = pop
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.china_mainland is not None:
            result['ChinaMainland'] = self.china_mainland

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.pop is not None:
            result['Pop'] = self.pop

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChinaMainland') is not None:
            self.china_mainland = m.get('ChinaMainland')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('Pop') is not None:
            self.pop = m.get('Pop')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

