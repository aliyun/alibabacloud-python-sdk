# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class SignOutOrgAccountRequest(DaraModel):
    def __init__(
        self,
        reason: str = None,
        reason_i18n_for_employee: Dict[str, str] = None,
        tenant_context: main_models.SignOutOrgAccountRequestTenantContext = None,
    ):
        # This parameter is required.
        self.reason = reason
        self.reason_i18n_for_employee = reason_i18n_for_employee
        self.tenant_context = tenant_context

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['Reason'] = self.reason

        if self.reason_i18n_for_employee is not None:
            result['ReasonI18nForEmployee'] = self.reason_i18n_for_employee

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ReasonI18nForEmployee') is not None:
            self.reason_i18n_for_employee = m.get('ReasonI18nForEmployee')

        if m.get('TenantContext') is not None:
            temp_model = main_models.SignOutOrgAccountRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class SignOutOrgAccountRequestTenantContext(DaraModel):
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

