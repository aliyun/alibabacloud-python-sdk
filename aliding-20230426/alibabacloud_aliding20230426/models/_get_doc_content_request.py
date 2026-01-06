# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetDocContentRequest(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        target_format: str = None,
        tenant_context: main_models.GetDocContentRequestTenantContext = None,
        user_token: str = None,
    ):
        # This parameter is required.
        self.dentry_uuid = dentry_uuid
        self.target_format = target_format
        self.tenant_context = tenant_context
        # This parameter is required.
        self.user_token = user_token

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.target_format is not None:
            result['TargetFormat'] = self.target_format

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.user_token is not None:
            result['userToken'] = self.user_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('TargetFormat') is not None:
            self.target_format = m.get('TargetFormat')

        if m.get('TenantContext') is not None:
            temp_model = main_models.GetDocContentRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('userToken') is not None:
            self.user_token = m.get('userToken')

        return self

class GetDocContentRequestTenantContext(DaraModel):
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

