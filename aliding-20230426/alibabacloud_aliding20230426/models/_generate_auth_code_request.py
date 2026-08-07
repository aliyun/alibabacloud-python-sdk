# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GenerateAuthCodeRequest(DaraModel):
    def __init__(
        self,
        buc_app_name: str = None,
        sso_ticket: str = None,
        tenant_context: main_models.GenerateAuthCodeRequestTenantContext = None,
        valid_redirect_uri: str = None,
    ):
        # This parameter is required.
        self.buc_app_name = buc_app_name
        # This parameter is required.
        self.sso_ticket = sso_ticket
        self.tenant_context = tenant_context
        # This parameter is required.
        self.valid_redirect_uri = valid_redirect_uri

    def validate(self):
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buc_app_name is not None:
            result['BucAppName'] = self.buc_app_name

        if self.sso_ticket is not None:
            result['SsoTicket'] = self.sso_ticket

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        if self.valid_redirect_uri is not None:
            result['ValidRedirectUri'] = self.valid_redirect_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucAppName') is not None:
            self.buc_app_name = m.get('BucAppName')

        if m.get('SsoTicket') is not None:
            self.sso_ticket = m.get('SsoTicket')

        if m.get('TenantContext') is not None:
            temp_model = main_models.GenerateAuthCodeRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        if m.get('ValidRedirectUri') is not None:
            self.valid_redirect_uri = m.get('ValidRedirectUri')

        return self

class GenerateAuthCodeRequestTenantContext(DaraModel):
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

