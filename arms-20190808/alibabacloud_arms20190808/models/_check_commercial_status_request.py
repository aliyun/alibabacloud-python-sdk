# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckCommercialStatusRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        service: str = None,
    ):
        # The region ID. Default value: cn-hangzhou.
        self.region_id = region_id
        # The ARMS sub-service. Valid values:
        # 
        # *   apm: Application Monitoring
        # *   rum: RUM
        # *   prometheus: Managed Service for Prometheus
        # *   xtrace: Managed Service for OpenTelemetry
        # 
        # This parameter is required.
        self.service = service

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service is not None:
            result['Service'] = self.service

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Service') is not None:
            self.service = m.get('Service')

        return self

