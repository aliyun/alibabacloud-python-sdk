# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_selectdb20230522 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        region_model_list: List[main_models.DescribeRegionsResponseBodyRegionModelList] = None,
        request_id: str = None,
    ):
        # An array of regions.
        self.region_model_list = region_model_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.region_model_list:
            for v1 in self.region_model_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RegionModelList'] = []
        if self.region_model_list is not None:
            for k1 in self.region_model_list:
                result['RegionModelList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region_model_list = []
        if m.get('RegionModelList') is not None:
            for k1 in m.get('RegionModelList'):
                temp_model = main_models.DescribeRegionsResponseBodyRegionModelList()
                self.region_model_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionsResponseBodyRegionModelList(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        zones: List[main_models.DescribeRegionsResponseBodyRegionModelListZones] = None,
    ):
        # The region ID.
        self.region_id = region_id
        # An array of zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.DescribeRegionsResponseBodyRegionModelListZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegionModelListZones(DaraModel):
    def __init__(
        self,
        description: str = None,
        disabled: bool = None,
        label: str = None,
        name: str = None,
        region_id: str = None,
        sub_domain: str = None,
        vpc_enabled: bool = None,
        zone_id: str = None,
    ):
        # The zone description.
        self.description = description
        # Indicates whether the VPC is disabled.
        self.disabled = disabled
        # The label.
        self.label = label
        # The zone name.
        self.name = name
        # The region ID.
        self.region_id = region_id
        # The subdomain.
        self.sub_domain = sub_domain
        # Indicates whether the VPC is enabled.
        self.vpc_enabled = vpc_enabled
        # Indicates whether the virtual private cloud (VPC) is available.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.label is not None:
            result['Label'] = self.label

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sub_domain is not None:
            result['SubDomain'] = self.sub_domain

        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubDomain') is not None:
            self.sub_domain = m.get('SubDomain')

        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

