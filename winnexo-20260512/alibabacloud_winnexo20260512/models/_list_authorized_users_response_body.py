# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizedUsersResponseBody(DaraModel):
    def __init__(
        self,
        auth_mode: str = None,
        code: str = None,
        items: List[main_models.ListAuthorizedUsersResponseBodyItems] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        # The authentication mode.
        self.auth_mode = auth_mode
        # The status code.
        self.code = code
        # The details.
        self.items = items
        # The description of the status code.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total = total

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_mode is not None:
            result['authMode'] = self.auth_mode

        if self.code is not None:
            result['code'] = self.code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authMode') is not None:
            self.auth_mode = m.get('authMode')

        if m.get('code') is not None:
            self.code = m.get('code')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListAuthorizedUsersResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListAuthorizedUsersResponseBodyItems(DaraModel):
    def __init__(
        self,
        expire_date: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        granted_by: int = None,
        grantee_id: str = None,
        grantee_type: str = None,
        id: int = None,
        member_count: int = None,
        permissions: List[str] = None,
        user_group_id: str = None,
        user_group_name: str = None,
        user_id: int = None,
        user_name: str = None,
    ):
        # The authorization expiration timestamp in milliseconds. If not specified, the authorization never expires.
        self.expire_date = expire_date
        # The creation time.
        self.gmt_create = gmt_create
        # The last update time.
        self.gmt_modified = gmt_modified
        # The user ID of the person who granted the authorization.
        self.granted_by = granted_by
        # The ID of the authorized object.
        self.grantee_id = grantee_id
        # The authorization object type. Valid values: USER, USER_GROUP.
        self.grantee_type = grantee_type
        # The Operation logs ID.
        self.id = id
        # The number of members.
        self.member_count = member_count
        # The permission member type. Valid values:
        # 
        # - **ORG**: Enterprise.
        # 
        # - **DEPT**: Department.
        # 
        # - **TAG**: Custom tag.
        # 
        # - **CONVERSATION**: Conversation.
        # 
        # - **USER**: User.
        self.permissions = permissions
        # The user group ID. This parameter has a value only when granteeType is set to USER_GROUP.
        self.user_group_id = user_group_id
        # The user group name.
        self.user_group_name = user_group_name
        # The user ID. This parameter has a value only when granteeType is set to USER.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_date is not None:
            result['expireDate'] = self.expire_date

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.granted_by is not None:
            result['grantedBy'] = self.granted_by

        if self.grantee_id is not None:
            result['granteeId'] = self.grantee_id

        if self.grantee_type is not None:
            result['granteeType'] = self.grantee_type

        if self.id is not None:
            result['id'] = self.id

        if self.member_count is not None:
            result['memberCount'] = self.member_count

        if self.permissions is not None:
            result['permissions'] = self.permissions

        if self.user_group_id is not None:
            result['userGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['userGroupName'] = self.user_group_name

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expireDate') is not None:
            self.expire_date = m.get('expireDate')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('grantedBy') is not None:
            self.granted_by = m.get('grantedBy')

        if m.get('granteeId') is not None:
            self.grantee_id = m.get('granteeId')

        if m.get('granteeType') is not None:
            self.grantee_type = m.get('granteeType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('memberCount') is not None:
            self.member_count = m.get('memberCount')

        if m.get('permissions') is not None:
            self.permissions = m.get('permissions')

        if m.get('userGroupId') is not None:
            self.user_group_id = m.get('userGroupId')

        if m.get('userGroupName') is not None:
            self.user_group_name = m.get('userGroupName')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        return self

