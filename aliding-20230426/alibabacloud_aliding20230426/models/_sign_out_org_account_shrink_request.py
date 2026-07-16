# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SignOutOrgAccountShrinkRequest(DaraModel):
    def __init__(
        self,
        reason: str = None,
        reason_i18n_for_employee_shrink: str = None,
        tenant_context_shrink: str = None,
    ):
        # This parameter is required.
        self.reason = reason
        self.reason_i18n_for_employee_shrink = reason_i18n_for_employee_shrink
        self.tenant_context_shrink = tenant_context_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reason is not None:
            result['Reason'] = self.reason

        if self.reason_i18n_for_employee_shrink is not None:
            result['ReasonI18nForEmployee'] = self.reason_i18n_for_employee_shrink

        if self.tenant_context_shrink is not None:
            result['TenantContext'] = self.tenant_context_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('ReasonI18nForEmployee') is not None:
            self.reason_i18n_for_employee_shrink = m.get('ReasonI18nForEmployee')

        if m.get('TenantContext') is not None:
            self.tenant_context_shrink = m.get('TenantContext')

        return self

