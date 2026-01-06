# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryGroupLiveInfoRequest(DaraModel):
    def __init__(
        self,
        anchor_union_id: str = None,
        live_uuid: str = None,
        tenant_context: main_models.QueryGroupLiveInfoRequestTenantContext = None,
    ):
        # This parameter is required.
        self.anchor_union_id = anchor_union_id
        # This parameter is required.
        self.live_uuid = live_uuid
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.anchor_union_id is not None:
            result['AnchorUnionId'] = self.anchor_union_id

        if self.live_uuid is not None:
            result['LiveUuid'] = self.live_uuid

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorUnionId') is not None:
            self.anchor_union_id = m.get('AnchorUnionId')

        if m.get('LiveUuid') is not None:
            self.live_uuid = m.get('LiveUuid')

        if m.get('TenantContext') is not None:
            temp_model = main_models.QueryGroupLiveInfoRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class QueryGroupLiveInfoRequestTenantContext(DaraModel):
    def __init__(
        self,
        tenant_id: str = None,
    ):
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

