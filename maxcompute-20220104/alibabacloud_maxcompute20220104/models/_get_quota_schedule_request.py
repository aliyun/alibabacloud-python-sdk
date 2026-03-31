# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetQuotaScheduleRequest(DaraModel):
    def __init__(
        self,
        display_timezone: str = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The time zone.
        self.display_timezone = display_timezone
        # The ID of the region.
        self.region = region
        # The ID of the tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_timezone is not None:
            result['displayTimezone'] = self.display_timezone

        if self.region is not None:
            result['region'] = self.region

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayTimezone') is not None:
            self.display_timezone = m.get('displayTimezone')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

