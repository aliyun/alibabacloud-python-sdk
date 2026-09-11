# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAliDingMinutesContentRequest(DaraModel):
    def __init__(
        self,
        minutes_id: str = None,
        tenant_id: str = None,
    ):
        # The DingTalk minutes ID.
        # 
        # This parameter is required.
        self.minutes_id = minutes_id
        # The ID of the effective tenant.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.minutes_id is not None:
            result['minutesId'] = self.minutes_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('minutesId') is not None:
            self.minutes_id = m.get('minutesId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

