# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeEnsRegionsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        ens_regions: main_models.DescribeEnsRegionsResponseBodyEnsRegions = None,
        request_id: str = None,
    ):
        # The service code. 0 is returned for a successful request. An error code is returned for a failed request.
        self.code = code
        # The information about the regions.
        self.ens_regions = ens_regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.ens_regions:
            self.ens_regions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.ens_regions is not None:
            result['EnsRegions'] = self.ens_regions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EnsRegions') is not None:
            temp_model = main_models.DescribeEnsRegionsResponseBodyEnsRegions()
            self.ens_regions = temp_model.from_map(m.get('EnsRegions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEnsRegionsResponseBodyEnsRegions(DaraModel):
    def __init__(
        self,
        ens_regions: List[main_models.DescribeEnsRegionsResponseBodyEnsRegionsEnsRegions] = None,
    ):
        self.ens_regions = ens_regions

    def validate(self):
        if self.ens_regions:
            for v1 in self.ens_regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EnsRegions'] = []
        if self.ens_regions is not None:
            for k1 in self.ens_regions:
                result['EnsRegions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ens_regions = []
        if m.get('EnsRegions') is not None:
            for k1 in m.get('EnsRegions'):
                temp_model = main_models.DescribeEnsRegionsResponseBodyEnsRegionsEnsRegions()
                self.ens_regions.append(temp_model.from_map(k1))

        return self

class DescribeEnsRegionsResponseBodyEnsRegionsEnsRegions(DaraModel):
    def __init__(
        self,
        area: str = None,
        en_name: str = None,
        ens_region_id: str = None,
        name: str = None,
        province: str = None,
    ):
        # The code of the region.
        self.area = area
        # The name of the node.
        self.en_name = en_name
        # The ID of the node.
        self.ens_region_id = ens_region_id
        # The name of the node.
        self.name = name
        # The province where the node is deployed.
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.en_name is not None:
            result['EnName'] = self.en_name

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.name is not None:
            result['Name'] = self.name

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('EnName') is not None:
            self.en_name = m.get('EnName')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

