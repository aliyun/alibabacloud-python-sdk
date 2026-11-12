# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DetachCcnInstanceFromCenShrinkRequest(DaraModel):
    def __init__(
        self,
        ccn_id: str = None,
        cen_id: str = None,
        region_binding_list_shrink: str = None,
        region_id: str = None,
    ):
        # The ID of the attached Cloud Connect Network (CCN).
        self.ccn_id = ccn_id
        # The ID of the CEN instance from which you want to revoke authorization.
        self.cen_id = cen_id
        # The list of transit routers to be disassociated from the CCN.
        self.region_binding_list_shrink = region_binding_list_shrink
        # The region ID of the Smart Access Gateway instance. You can call the DescribeRegions operation to query the regions supported by Smart Access Gateway and the corresponding region IDs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ccn_id is not None:
            result['CcnId'] = self.ccn_id

        if self.cen_id is not None:
            result['CenId'] = self.cen_id

        if self.region_binding_list_shrink is not None:
            result['RegionBindingList'] = self.region_binding_list_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CcnId') is not None:
            self.ccn_id = m.get('CcnId')

        if m.get('CenId') is not None:
            self.cen_id = m.get('CenId')

        if m.get('RegionBindingList') is not None:
            self.region_binding_list_shrink = m.get('RegionBindingList')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

