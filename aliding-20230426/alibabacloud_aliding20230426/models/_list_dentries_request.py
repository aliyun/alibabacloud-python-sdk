# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListDentriesRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        order: str = None,
        order_by: str = None,
        parent_id: str = None,
        space_id: str = None,
        tenant_context: main_models.ListDentriesRequestTenantContext = None,
        with_thumbnail: bool = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.order = order
        self.order_by = order_by
        # This parameter is required.
        self.parent_id = parent_id
        # This parameter is required.
        self.space_id = space_id
        self.tenant_context = tenant_context
        self.with_thumbnail = with_thumbnail

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.order is not None:
            result['Order'] = self.order

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.with_thumbnail is not None:
            result['WithThumbnail'] = self.with_thumbnail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.ListDentriesRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('WithThumbnail') is not None:
            self.with_thumbnail = m.get('WithThumbnail')

        return self

class ListDentriesRequestTenantContext(DaraModel):
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

