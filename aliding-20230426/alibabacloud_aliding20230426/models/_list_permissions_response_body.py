# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListPermissionsResponseBody(DaraModel):
    def __init__(
        self,
        duration: int = None,
        next_token: str = None,
        permissions: List[main_models.ListPermissionsResponseBodyPermissions] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.duration = duration
        self.next_token = next_token
        self.permissions = permissions
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.permissions:
            for v1 in self.permissions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['duration'] = self.duration

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        result['permissions'] = []
        if self.permissions is not None:
            for k1 in self.permissions:
                result['permissions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        self.permissions = []
        if m.get('permissions') is not None:
            for k1 in m.get('permissions'):
                temp_model = main_models.ListPermissionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class ListPermissionsResponseBodyPermissions(DaraModel):
    def __init__(
        self,
        dentry_uuid: str = None,
        member: main_models.ListPermissionsResponseBodyPermissionsMember = None,
        role: main_models.ListPermissionsResponseBodyPermissionsRole = None,
    ):
        self.dentry_uuid = dentry_uuid
        self.member = member
        self.role = role

    def validate(self):
        if self.member:
            self.member.validate()
        if self.role:
            self.role.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dentry_uuid is not None:
            result['DentryUuid'] = self.dentry_uuid

        if self.member is not None:
            result['Member'] = self.member.to_map()

        if self.role is not None:
            result['Role'] = self.role.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DentryUuid') is not None:
            self.dentry_uuid = m.get('DentryUuid')

        if m.get('Member') is not None:
            temp_model = main_models.ListPermissionsResponseBodyPermissionsMember()
            self.member = temp_model.from_map(m.get('Member'))

        if m.get('Role') is not None:
            temp_model = main_models.ListPermissionsResponseBodyPermissionsRole()
            self.role = temp_model.from_map(m.get('Role'))

        return self

class ListPermissionsResponseBodyPermissionsRole(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListPermissionsResponseBodyPermissionsMember(DaraModel):
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

