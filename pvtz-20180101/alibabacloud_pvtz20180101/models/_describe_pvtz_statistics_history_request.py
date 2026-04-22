# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pvtz20180101 import models as main_models
from darabonba.model import DaraModel

class DescribePvtzStatisticsHistoryRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_timestamp: str = None,
        module: str = None,
        network_params: List[main_models.DescribePvtzStatisticsHistoryRequestNetworkParams] = None,
        rcode: str = None,
        server_region: str = None,
        start_timestamp: str = None,
        statistical_type: str = None,
        zone_name: str = None,
    ):
        self.domain_name = domain_name
        self.end_timestamp = end_timestamp
        self.module = module
        self.network_params = network_params
        self.rcode = rcode
        self.server_region = server_region
        self.start_timestamp = start_timestamp
        self.statistical_type = statistical_type
        self.zone_name = zone_name

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
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.module is not None:
            result['Module'] = self.module

        result['NetworkParams'] = []
        if self.network_params is not None:
            for k1 in self.network_params:
                result['NetworkParams'].append(k1.to_map() if k1 else None)

        if self.rcode is not None:
            result['Rcode'] = self.rcode

        if self.server_region is not None:
            result['ServerRegion'] = self.server_region

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        if self.statistical_type is not None:
            result['StatisticalType'] = self.statistical_type

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        self.network_params = []
        if m.get('NetworkParams') is not None:
            for k1 in m.get('NetworkParams'):
                temp_model = main_models.DescribePvtzStatisticsHistoryRequestNetworkParams()
                self.network_params.append(temp_model.from_map(k1))

        if m.get('Rcode') is not None:
            self.rcode = m.get('Rcode')

        if m.get('ServerRegion') is not None:
            self.server_region = m.get('ServerRegion')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        if m.get('StatisticalType') is not None:
            self.statistical_type = m.get('StatisticalType')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

class DescribePvtzStatisticsHistoryRequestNetworkParams(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        vpc_id: str = None,
        vpc_owner: str = None,
        vpc_type: str = None,
    ):
        self.region_id = region_id
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

