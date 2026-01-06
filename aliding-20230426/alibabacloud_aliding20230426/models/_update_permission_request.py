# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class UpdatePermissionRequest(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        members: List[main_models.UpdatePermissionRequestMembers] = None,
        option: main_models.UpdatePermissionRequestOption = None,
        role_id: str = None,
        tenant_context: main_models.UpdatePermissionRequestTenantContext = None,
    ):
        self.dentry_uuid = dentry_uuid
        # This parameter is required.
        self.members = members
        self.option = option
        self.role_id = role_id
        self.tenant_context = tenant_context

    def validate(self):
        if self.members:
            for v1 in self.members:
                 if v1:
                    v1.validate()
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

        result['Members'] = []
        if self.members is not None:
            for k1 in self.members:
                result['Members'].append(k1.to_map() if k1 else None)

        if self.option is not None:
            result['Option'] = self.option.to_map()

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.tenant_context is not None:
            result['TenantContext'] = self.tenant_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        self.members = []
        if m.get('Members') is not None:
            for k1 in m.get('Members'):
                temp_model = main_models.UpdatePermissionRequestMembers()
                self.members.append(temp_model.from_map(k1))

        if m.get('Option') is not None:
            temp_model = main_models.UpdatePermissionRequestOption()
            self.option = temp_model.from_map(m.get('Option'))

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('TenantContext') is not None:
            temp_model = main_models.UpdatePermissionRequestTenantContext()
            self.tenant_context = temp_model.from_map(m.get('TenantContext'))

        return self

class UpdatePermissionRequestTenantContext(DaraModel):
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

class UpdatePermissionRequestOption(DaraModel):
    def __init__(
        self,
        duration: int = None,
    ):
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        return self

class UpdatePermissionRequestMembers(DaraModel):
    def __init__(
        self,
        corp_id: str = None,
        id: str = None,
        type: str = None,
    ):
        self.corp_id = corp_id
        self.id = id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.corp_id is not None:
            result['CorpId'] = self.corp_id

        if self.id is not None:
            result['Id'] = self.id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorpId') is not None:
            self.corp_id = m.get('CorpId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

