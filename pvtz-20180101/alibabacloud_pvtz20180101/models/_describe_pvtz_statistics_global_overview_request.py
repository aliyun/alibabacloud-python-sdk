# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribePvtzStatisticsGlobalOverviewRequest(DaraModel):
    def __init__(
        self,
        network_params: List[main_models.DescribePvtzStatisticsGlobalOverviewRequestNetworkParams] = None,
        overview_period: str = None,
        server_region: str = None,
    ):
        self.network_params = network_params
        self.overview_period = overview_period
        self.server_region = server_region

    def validate(self):
        if self.network_params:
            for v1 in self.network_params:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['NetworkParams'] = []
        if self.network_params is not None:
            for k1 in self.network_params:
                result['NetworkParams'].append(k1.to_map() if k1 else None)

        if self.overview_period is not None:
            result['OverviewPeriod'] = self.overview_period

        if self.server_region is not None:
            result['ServerRegion'] = self.server_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.network_params = []
        if m.get('NetworkParams') is not None:
            for k1 in m.get('NetworkParams'):
                temp_model = main_models.DescribePvtzStatisticsGlobalOverviewRequestNetworkParams()
                self.network_params.append(temp_model.from_map(k1))

        if m.get('OverviewPeriod') is not None:
            self.overview_period = m.get('OverviewPeriod')

        if m.get('ServerRegion') is not None:
            self.server_region = m.get('ServerRegion')

        return self

class DescribePvtzStatisticsGlobalOverviewRequestNetworkParams(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
        vpc_owner: str = None,
        vpc_type: str = None,
    ):
        self.region_id = region_id
        # VPC ID。
        self.vpc_id = vpc_id
        self.vpc_owner = vpc_owner
        self.vpc_type = vpc_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_owner is not None:
            result['VpcOwner'] = self.vpc_owner

        if self.vpc_type is not None:
            result['VpcType'] = self.vpc_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcOwner') is not None:
            self.vpc_owner = m.get('VpcOwner')

        if m.get('VpcType') is not None:
            self.vpc_type = m.get('VpcType')

        return self

