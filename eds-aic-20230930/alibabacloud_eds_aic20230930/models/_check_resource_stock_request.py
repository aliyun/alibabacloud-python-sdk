# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckResourceStockRequest(DaraModel):
    def __init__(
        self,
        acp_spec_id: str = None,
        amount: int = None,
        biz_region_id: str = None,
        gpu_acceleration: bool = None,
        zone_id: str = None,
    ):
        # Specification ID.
        self.acp_spec_id = acp_spec_id
        self.amount = amount
        # Region ID.
        # 
        # This parameter is required.
        self.biz_region_id = biz_region_id
        self.gpu_acceleration = gpu_acceleration
        # The availability zone of the resource.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acp_spec_id is not None:
            result['AcpSpecId'] = self.acp_spec_id

        if self.amount is not None:
            result['Amount'] = self.amount

        if self.biz_region_id is not None:
            result['BizRegionId'] = self.biz_region_id

        if self.gpu_acceleration is not None:
            result['GpuAcceleration'] = self.gpu_acceleration

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcpSpecId') is not None:
            self.acp_spec_id = m.get('AcpSpecId')

        if m.get('Amount') is not None:
            self.amount = m.get('Amount')

        if m.get('BizRegionId') is not None:
            self.biz_region_id = m.get('BizRegionId')

        if m.get('GpuAcceleration') is not None:
            self.gpu_acceleration = m.get('GpuAcceleration')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

