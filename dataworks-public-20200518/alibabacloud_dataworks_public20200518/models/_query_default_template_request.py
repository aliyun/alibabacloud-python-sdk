# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryDefaultTemplateRequest(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        # The tenant ID. You can log on to the [DataWorks console](https://workbench.data.aliyun.com/console), go to the DataStudio page, click your username in the upper-right corner, and choose Menu > User Info to obtain the tenant ID.
        # 
        # You can also obtain the tenant ID from Data.TenantId in the response of the GetProject operation.
        # 
        # This parameter is required.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

