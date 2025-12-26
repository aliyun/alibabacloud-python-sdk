# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class ListRegionsResponseBody(DaraModel):
    def __init__(
        self,
        region_models: List[main_models.ListRegionsResponseBodyRegionModels] = None,
        request_id: str = None,
    ):
        # The region IDs.
        self.region_models = region_models
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.region_models:
            for v1 in self.region_models:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionModels'] = []
        if self.region_models is not None:
            for k1 in self.region_models:
                result['RegionModels'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_models = []
        if m.get('RegionModels') is not None:
            for k1 in m.get('RegionModels'):
                temp_model = main_models.ListRegionsResponseBodyRegionModels()
                self.region_models.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListRegionsResponseBodyRegionModels(DaraModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

