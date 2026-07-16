# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeRefundPriceRequest(DaraModel):
    def __init__(
        self,
        desktop_id: List[str] = None,
        refund_type: str = None,
        region_id: str = None,
        reseller_owner_uid: int = None,
    ):
        # A list of cloud desktop IDs. You can specify one or more IDs. The number of IDs (N) must be between 1 and 20.
        # 
        # This parameter is required.
        self.desktop_id = desktop_id
        # Refund type.
        self.refund_type = refund_type
        # Region ID. Call [DescribeRegions](~~DescribeRegions~~) to get a list of regions supported by WUYING Workspace.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.reseller_owner_uid = reseller_owner_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desktop_id is not None:
            result['DesktopId'] = self.desktop_id

        if self.refund_type is not None:
            result['RefundType'] = self.refund_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reseller_owner_uid is not None:
            result['ResellerOwnerUid'] = self.reseller_owner_uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesktopId') is not None:
            self.desktop_id = m.get('DesktopId')

        if m.get('RefundType') is not None:
            self.refund_type = m.get('RefundType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResellerOwnerUid') is not None:
            self.reseller_owner_uid = m.get('ResellerOwnerUid')

        return self

