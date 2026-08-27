# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCustomOrgRequest(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        corp_name: str = None,
        tenant_id: str = None,
    ):
        # The corpId of the activated enterprise.
        # 
        # This parameter is required.
        self.corp_id = corp_id
        # The organization name.
        self.corp_name = corp_name
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['corpId'] = self.corp_id

        if self.corp_name is not None:
            result['corpName'] = self.corp_name

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('corpId') is not None:
            self.corp_id = m.get('corpId')

        if m.get('corpName') is not None:
            self.corp_name = m.get('corpName')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

