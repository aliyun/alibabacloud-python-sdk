# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DetachCcnInstanceFromCenRequest(DaraModel):
    def __init__(
        self,
        ccn_id: str = None,
        cen_id: str = None,
        region_binding_list: List[main_models.DetachCcnInstanceFromCenRequestRegionBindingList] = None,
        region_id: str = None,
    ):
        # The ID of the attached Cloud Connect Network (CCN).
        self.ccn_id = ccn_id
        # The ID of the CEN instance from which you want to revoke authorization.
        self.cen_id = cen_id
        # The list of transit routers to be disassociated from the CCN.
        self.region_binding_list = region_binding_list
        # The region ID of the Smart Access Gateway instance. You can call the DescribeRegions operation to query the regions supported by Smart Access Gateway and the corresponding region IDs.
        self.region_id = region_id

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

        result['RegionBindingList'] = []
        if self.region_binding_list is not None:
            for k1 in self.region_binding_list:
                result['RegionBindingList'].append(k1.to_map() if k1 else None)

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcnId') is not None:
            self.ccn_id = m.get('CcnId')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        self.region_binding_list = []
        if m.get('RegionBindingList') is not None:
            for k1 in m.get('RegionBindingList'):
                temp_model = main_models.DetachCcnInstanceFromCenRequestRegionBindingList()
                self.region_binding_list.append(temp_model.from_map(k1))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DetachCcnInstanceFromCenRequestRegionBindingList(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        transit_router_id: str = None,
    ):
        # The region ID of the transit router to be disassociated.
        self.region_id = region_id
        # The instance ID of the forward routing transit router.
        self.transit_router_id = transit_router_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.transit_router_id is not None:
            result['TransitRouterId'] = self.transit_router_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TransitRouterId') is not None:
            self.transit_router_id = m.get('TransitRouterId')

        return self

