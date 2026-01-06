# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class QueryDentriesInfoRequest(DaraModel):
    def __init__(
        self,
        app_ids_for_app_properties: List[str] = None,
        dentry_id: str = None,
        space_id: str = None,
        tenant_context: main_models.QueryDentriesInfoRequestTenantContext = None,
        with_thumbnail: bool = None,
    ):
        self.app_ids_for_app_properties = app_ids_for_app_properties
        # This parameter is required.
        self.dentry_id = dentry_id
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
        if self.app_ids_for_app_properties is not None:
            result['AppIdsForAppProperties'] = self.app_ids_for_app_properties

        if self.dentry_id is not None:
            result['DentryId'] = self.dentry_id

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.with_thumbnail is not None:
            result['WithThumbnail'] = self.with_thumbnail

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppIdsForAppProperties') is not None:
            self.app_ids_for_app_properties = m.get('AppIdsForAppProperties')

        if m.get('DentryId') is not None:
            self.dentry_id = m.get('DentryId')

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.QueryDentriesInfoRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('WithThumbnail') is not None:
            self.with_thumbnail = m.get('WithThumbnail')

        return self

class QueryDentriesInfoRequestTenantContext(DaraModel):
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

