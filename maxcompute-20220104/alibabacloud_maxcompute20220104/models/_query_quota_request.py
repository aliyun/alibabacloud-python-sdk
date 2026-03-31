# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryQuotaRequest(DaraModel):
    def __init__(
        self,
        ak_proven: str = None,
        mock: bool = None,
        region: str = None,
        tenant_id: str = None,
    ):
        # The trusted AccessKey pairs.
        self.ak_proven = ak_proven
        # Specifies whether to include submodules. Valid values: true and false. -true: The request includes submodules. -false (default): The request does not include submodules.
        self.mock = mock
        # The region ID.
        self.region = region
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ak_proven is not None:
            result['AkProven'] = self.ak_proven

        if self.mock is not None:
            result['mock'] = self.mock

        if self.region is not None:
            result['region'] = self.region

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AkProven') is not None:
            self.ak_proven = m.get('AkProven')

        if m.get('mock') is not None:
            self.mock = m.get('mock')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

