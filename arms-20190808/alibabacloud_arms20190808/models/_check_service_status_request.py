# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckServiceStatusRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        svc_code: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The service code of an Alibaba Cloud service. The service code of Managed Service for Prometheus is prometheus.
        # 
        # This parameter is required.
        self.svc_code = svc_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.svc_code is not None:
            result['SvcCode'] = self.svc_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SvcCode') is not None:
            self.svc_code = m.get('SvcCode')

        return self

