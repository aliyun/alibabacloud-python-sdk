# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListInstanceUserPermissionsResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
        user_permissions: main_models.ListInstanceUserPermissionsResponseBodyUserPermissions = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # - true: The request is successful.
        # - false: The request fails.
        self.success = success
        # The total number of returned entries.
        self.total_count = total_count
        # The permissions of the user on the instance.
        self.user_permissions = user_permissions

    def validate(self):
        if self.user_permissions:
            self.user_permissions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.user_permissions is not None:
            result['UserPermissions'] = self.user_permissions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('UserPermissions') is not None:
            temp_model = main_models.ListInstanceUserPermissionsResponseBodyUserPermissions()
            self.user_permissions = temp_model.from_map(m.get('UserPermissions'))

        return self

class ListInstanceUserPermissionsResponseBodyUserPermissions(DaraModel):
    def __init__(
        self,
        user_permission: List[main_models.ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermission] = None,
    ):
        self.user_permission = user_permission

    def validate(self):
        if self.user_permission:
            for v1 in self.user_permission:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['UserPermission'] = []
        if self.user_permission is not None:
            for k1 in self.user_permission:
                result['UserPermission'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_permission = []
        if m.get('UserPermission') is not None:
            for k1 in m.get('UserPermission'):
                temp_model = main_models.ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermission()
                self.user_permission.append(temp_model.from_map(k1))

        return self

class ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermission(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        perm_details: main_models.ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails = None,
        user_id: str = None,
        user_nick_name: str = None,
    ):
        # The ID of the instance.
        self.instance_id = instance_id
        # The details of permissions.
        self.perm_details = perm_details
        # The ID of the user.
        self.user_id = user_id
        # The nickname of the user.
        self.user_nick_name = user_nick_name

    def validate(self):
        if self.perm_details:
            self.perm_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.perm_details is not None:
            result['PermDetails'] = self.perm_details.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_nick_name is not None:
            result['UserNickName'] = self.user_nick_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PermDetails') is not None:
            temp_model = main_models.ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails()
            self.perm_details = temp_model.from_map(m.get('PermDetails'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserNickName') is not None:
            self.user_nick_name = m.get('UserNickName')

        return self

class ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetails(DaraModel):
    def __init__(
        self,
        perm_detail: List[main_models.ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail] = None,
    ):
        self.perm_detail = perm_detail

    def validate(self):
        if self.perm_detail:
            for v1 in self.perm_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PermDetail'] = []
        if self.perm_detail is not None:
            for k1 in self.perm_detail:
                result['PermDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.perm_detail = []
        if m.get('PermDetail') is not None:
            for k1 in m.get('PermDetail'):
                temp_model = main_models.ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail()
                self.perm_detail.append(temp_model.from_map(k1))

        return self

class ListInstanceUserPermissionsResponseBodyUserPermissionsUserPermissionPermDetailsPermDetail(DaraModel):
    def __init__(
        self,
        create_date: str = None,
        expire_date: str = None,
        extra_data: str = None,
        origin_from: str = None,
        perm_type: str = None,
        user_access_id: str = None,
    ):
        # The time when the permissions were granted.
        self.create_date = create_date
        # The time when the permissions expire.
        self.expire_date = expire_date
        # This parameter is reserved.
        self.extra_data = extra_data
        # The user who grants the permissions.
        self.origin_from = origin_from
        # The type of the permissions. Valid values:
        # 
        # *   LOGIN: the logon permissions
        # *   PERF: the query permissions on the instance
        self.perm_type = perm_type
        # The ID of the authorization record.
        self.user_access_id = user_access_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.extra_data is not None:
            result['ExtraData'] = self.extra_data

        if self.origin_from is not None:
            result['OriginFrom'] = self.origin_from

        if self.perm_type is not None:
            result['PermType'] = self.perm_type

        if self.user_access_id is not None:
            result['UserAccessId'] = self.user_access_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('ExtraData') is not None:
            self.extra_data = m.get('ExtraData')

        if m.get('OriginFrom') is not None:
            self.origin_from = m.get('OriginFrom')

        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')

        if m.get('UserAccessId') is not None:
            self.user_access_id = m.get('UserAccessId')

        return self

