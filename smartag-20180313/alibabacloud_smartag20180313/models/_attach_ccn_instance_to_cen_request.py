# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AttachCcnInstanceToCenRequest(DaraModel):
    def __init__(
        self,
        ccn_id: str = None,
        cen_id: str = None,
        region_id: str = None,
        subnet: str = None,
    ):
        # The ID of the Cloud Connect Network (CCN) instance to attach.
        self.ccn_id = ccn_id
        # The ID of the CEN instance to authorize.
        self.cen_id = cen_id
        # The region ID of the Cloud Connect Network (CCN) instance. You can invoke the DescribeRegions operation to query the regions supported by Smart Access Gateway and the corresponding region IDs.
        self.region_id = region_id
        # The Internet CIDR block used when the Cloud Connect Network (CCN) instance is attached to the CEN instance.
        self.subnet = subnet

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Subnet') is not None:
            self.subnet = m.get('Subnet')

        return self

