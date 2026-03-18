# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQuotasPlansRequest(DaraModel):
    def __init__(
        self,
        region: str = None,
        tenant_id: str = None,
    ):
        self.region = region
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region is not None:
            result['region'] = self.region

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

