# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SubmitBatchChangeTableOwnerRequest(DaraModel):
    def __init__(
        self,
        enable_cross_tenant: bool = None,
        owner: str = None,
        table_meta_entity_ids: List[str] = None,
    ):
        self.enable_cross_tenant = enable_cross_tenant
        # This parameter is required.
        self.owner = owner
        # This parameter is required.
        self.table_meta_entity_ids = table_meta_entity_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_cross_tenant is not None:
            result['EnableCrossTenant'] = self.enable_cross_tenant

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.table_meta_entity_ids is not None:
            result['TableMetaEntityIds'] = self.table_meta_entity_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableCrossTenant') is not None:
            self.enable_cross_tenant = m.get('EnableCrossTenant')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('TableMetaEntityIds') is not None:
            self.table_meta_entity_ids = m.get('TableMetaEntityIds')

        return self

