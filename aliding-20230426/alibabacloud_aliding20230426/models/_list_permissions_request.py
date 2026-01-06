# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListPermissionsRequest(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        option: main_models.ListPermissionsRequestOption = None,
        tenant_context: main_models.ListPermissionsRequestTenantContext = None,
    ):
        # This parameter is required.
        self.dentry_uuid = dentry_uuid
        self.option = option
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
        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.option is not None:
            result['Option'] = self.option.to_map()

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('Option') is not None:
            temp_model = main_models.ListPermissionsRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('TenantContext') is not None:
            temp_model = main_models.ListPermissionsRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class ListPermissionsRequestTenantContext(DaraModel):
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

class ListPermissionsRequestOption(DaraModel):
    def __init__(
        self,
        filter_role_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        self.filter_role_ids = filter_role_ids
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_role_ids is not None:
            result['FilterRoleIds'] = self.filter_role_ids

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterRoleIds') is not None:
            self.filter_role_ids = m.get('FilterRoleIds')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

