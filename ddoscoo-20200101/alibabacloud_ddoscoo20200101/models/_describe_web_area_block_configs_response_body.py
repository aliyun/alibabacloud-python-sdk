# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebAreaBlockConfigsResponseBody(DaraModel):
    def __init__(
        self,
        area_block_configs: List[main_models.DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs] = None,
        request_id: str = None,
    ):
        # An array that consists of the configurations of the Location Blacklist (Domain Names) policy.
        self.area_block_configs = area_block_configs
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.area_block_configs:
            for v1 in self.area_block_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AreaBlockConfigs'] = []
        if self.area_block_configs is not None:
            for k1 in self.area_block_configs:
                result['AreaBlockConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.area_block_configs = []
        if m.get('AreaBlockConfigs') is not None:
            for k1 in m.get('AreaBlockConfigs'):
                temp_model = main_models.DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs()
                self.area_block_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigs(DaraModel):
    def __init__(
        self,
        domain: str = None,
        region_list: List[main_models.DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList] = None,
    ):
        # The domain name of the website.
        self.domain = domain
        # The configuration of the blocked locations.
        self.region_list = region_list

    def validate(self):
        if self.region_list:
            for v1 in self.region_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain is not None:
            result['Domain'] = self.domain

        result['RegionList'] = []
        if self.region_list is not None:
            for k1 in self.region_list:
                result['RegionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        self.region_list = []
        if m.get('RegionList') is not None:
            for k1 in m.get('RegionList'):
                temp_model = main_models.DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList()
                self.region_list.append(temp_model.from_map(k1))

        return self

class DescribeWebAreaBlockConfigsResponseBodyAreaBlockConfigsRegionList(DaraModel):
    def __init__(
        self,
        block: int = None,
        region: str = None,
    ):
        # Indicates whether the location is blocked. Valid values:
        # 
        # *   **0**: yes
        # *   **1**: no
        self.block = block
        # The name of the location.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.block is not None:
            result['Block'] = self.block

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Block') is not None:
            self.block = m.get('Block')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self

