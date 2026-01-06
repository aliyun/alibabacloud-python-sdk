# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class AddRecordPermissionRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        conference_id: str = None,
        tenant_context: main_models.AddRecordPermissionRequestTenantContext = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.biz_type = biz_type
        # This parameter is required.
        self.conference_id = conference_id
        self.tenant_context = tenant_context
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.AddRecordPermissionRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class AddRecordPermissionRequestTenantContext(DaraModel):
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

