# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: List[main_models.DescribeRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # The collection of region information.
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
                temp_model = main_models.DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        classic_unavailable: bool = None,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
        vpc_unavailable: bool = None,
    ):
        # Indicates whether the current region supports scaling groups that reside in the classic network. Valid values:
        # 
        # *   true
        # *   false
        self.classic_unavailable = classic_unavailable
        # The region name.
        self.local_name = local_name
        # The region endpoint.
        self.region_endpoint = region_endpoint
        # The region ID.
        self.region_id = region_id
        # Indicates whether the current region supports scaling groups that reside in virtual private clouds (VPCs). Valid values:
        # 
        # *   true
        # *   false
        self.vpc_unavailable = vpc_unavailable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classic_unavailable is not None:
            result['ClassicUnavailable'] = self.classic_unavailable

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_unavailable is not None:
            result['VpcUnavailable'] = self.vpc_unavailable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassicUnavailable') is not None:
            self.classic_unavailable = m.get('ClassicUnavailable')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcUnavailable') is not None:
            self.vpc_unavailable = m.get('VpcUnavailable')

        return self

