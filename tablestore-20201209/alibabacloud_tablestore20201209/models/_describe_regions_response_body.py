# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tablestore20201209 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: List[main_models.DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The regions.
        self.regions = regions
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
                temp_model = main_models.DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        i_18n_key: str = None,
        region_id: str = None,
    ):
        # The key of the region.
        self.i_18n_key = i_18n_key
        # The ID of the region.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.i_18n_key is not None:
            result['I18nKey'] = self.i_18n_key

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('I18nKey') is not None:
            self.i_18n_key = m.get('I18nKey')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

