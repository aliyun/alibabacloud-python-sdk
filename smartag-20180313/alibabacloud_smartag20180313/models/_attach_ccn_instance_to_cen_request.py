# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class AttachCcnInstanceToCenRequest(DaraModel):
    def __init__(
        self,
        ccn_id: str = None,
        cen_id: str = None,
        cidr_allocation_mode: str = None,
        region_binding_list: List[main_models.AttachCcnInstanceToCenRequestRegionBindingList] = None,
        region_id: str = None,
        subnet: str = None,
    ):
        # The ID of the Cloud Connect Network (CCN) to attach.
        self.ccn_id = ccn_id
        # The ID of the CEN instance to which you want to attach the CCN instance.
        self.cen_id = cen_id
        # The CIDR block allocation mode. Valid values: - PER_REGION: Custom CIDR blocks are allocated for each region. - UNIFIED: A unified CIDR block is allocated.
        self.cidr_allocation_mode = cidr_allocation_mode
        # The list of transit routers to be newly attached to the CCN instance.
        self.region_binding_list = region_binding_list
        # The region ID of the Cloud Connect Network (CCN) instance. You can invoke the DescribeRegions operation to query the regions supported by Smart Access Gateway and the corresponding region IDs.
        self.region_id = region_id
        # The Internet CIDR block used to attach the Cloud Connect Network (CCN) to the Cloud Enterprise Network (CEN).
        self.subnet = subnet

    def validate(self):
        if self.region_binding_list:
            for v1 in self.region_binding_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ccn_id is not None:
            result['CcnId'] = self.ccn_id

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.cidr_allocation_mode is not None:
            result['CidrAllocationMode'] = self.cidr_allocation_mode

        result['RegionBindingList'] = []
        if self.region_binding_list is not None:
            for k1 in self.region_binding_list:
                result['RegionBindingList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.subnet is not None:
            result['Subnet'] = self.subnet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcnId') is not None:
            self.ccn_id = m.get('CcnId')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('CidrAllocationMode') is not None:
            self.cidr_allocation_mode = m.get('CidrAllocationMode')

        self.region_binding_list = []
        if m.get('RegionBindingList') is not None:
            for k1 in m.get('RegionBindingList'):
                temp_model = main_models.AttachCcnInstanceToCenRequestRegionBindingList()
                self.region_binding_list.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')

        return self

class AttachCcnInstanceToCenRequestRegionBindingList(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        region_id: str = None,
        transit_router_id: str = None,
    ):
        # The custom CIDR block for each region when the CidrAllocationMode parameter is set to PER_REGION.
        self.cidr_block = cidr_block
        # The region ID of the transit router.
        self.region_id = region_id
        # The instance ID of the transit router used for forward routing.
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

