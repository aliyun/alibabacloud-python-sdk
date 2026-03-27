# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: List[main_models.DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.regions = regions
        # Id of the request
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
        result['regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['regions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('regions') is not None:
            for k1 in m.get('regions'):
                temp_model = main_models.DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['localName'] = self.local_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('localName') is not None:
            self.local_name = m.get('localName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

