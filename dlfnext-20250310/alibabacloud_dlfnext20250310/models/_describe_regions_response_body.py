# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from alibabacloud_dlfnext20250310 import models as main_models 
from typing import List


class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: List[main_models.DescribeRegionsResponseBodyRegions] = None,
    ):
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
        result['regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['regions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('regions') is not None:
            for k1 in m.get('regions'):
                temp_model = main_models.DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        show_name: str = None,
        type: str = None,
    ):
        # The region description
        self.description = description
        # The region name
        self.name = name
        # The region show name
        self.show_name = show_name
        # The region type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.show_name is not None:
            result['showName'] = self.show_name

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('showName') is not None:
            self.show_name = m.get('showName')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

