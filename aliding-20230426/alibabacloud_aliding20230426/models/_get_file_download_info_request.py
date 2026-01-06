# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class GetFileDownloadInfoRequest(DaraModel):
    def __init__(
        self,
        dentry_id: str = None,
        option: main_models.GetFileDownloadInfoRequestOption = None,
        space_id: str = None,
        tenant_context: main_models.GetFileDownloadInfoRequestTenantContext = None,
    ):
        self.dentry_id = dentry_id
        self.option = option
        self.space_id = space_id
        self.tenant_context = tenant_context

    def validate(self):
        if self.option:
            self.option.validate()
        if self.tenant_context:
            self.tenant_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_id is not None:
            result['DentryId'] = self.dentry_id

        if self.option is not None:
            result['Option'] = self.option.to_map()

        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryId') is not None:
            self.dentry_id = m.get('DentryId')

        if m.get('Option') is not None:
            temp_model = main_models.GetFileDownloadInfoRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.GetFileDownloadInfoRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class GetFileDownloadInfoRequestTenantContext(DaraModel):
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

class GetFileDownloadInfoRequestOption(DaraModel):
    def __init__(
        self,
        prefer_intranet: bool = None,
        version: int = None,
    ):
        self.prefer_intranet = prefer_intranet
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.prefer_intranet is not None:
            result['PreferIntranet'] = self.prefer_intranet

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreferIntranet') is not None:
            self.prefer_intranet = m.get('PreferIntranet')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

