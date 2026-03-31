# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ram20150501 import models as main_models
from darabonba.model import DaraModel

class ListRolesResponseBody(DaraModel):
    def __init__(
        self,
        is_truncated: bool = None,
        marker: str = None,
        request_id: str = None,
        roles: main_models.ListRolesResponseBodyRoles = None,
    ):
        # Indicates whether the response is truncated.
        self.is_truncated = is_truncated
        # The marker. This parameter is returned only if the value of `IsTruncated` is `true`. If the parameter is returned, you can call this operation again and set this parameter to obtain the truncated part.````
        self.marker = marker
        # The request ID.
        self.request_id = request_id
        self.roles = roles

    def validate(self):
        if self.roles:
            self.roles.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_truncated is not None:
            result['IsTruncated'] = self.is_truncated

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.roles is not None:
            result['Roles'] = self.roles.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsTruncated') is not None:
            self.is_truncated = m.get('IsTruncated')

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Roles') is not None:
            temp_model = main_models.ListRolesResponseBodyRoles()
            self.roles = temp_model.from_map(m.get('Roles'))

        return self

class ListRolesResponseBodyRoles(DaraModel):
    def __init__(
        self,
        role: List[main_models.ListRolesResponseBodyRolesRole] = None,
    ):
        self.role = role

    def validate(self):
        if self.role:
            for v1 in self.role:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Role'] = []
        if self.role is not None:
            for k1 in self.role:
                result['Role'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.role = []
        if m.get('Role') is not None:
            for k1 in m.get('Role'):
                temp_model = main_models.ListRolesResponseBodyRolesRole()
                self.role.append(temp_model.from_map(k1))

        return self

class ListRolesResponseBodyRolesRole(DaraModel):
    def __init__(
        self,
        arn: str = None,
        create_date: str = None,
        description: str = None,
        max_session_duration: int = None,
        role_id: str = None,
        role_name: str = None,
        tags: main_models.ListRolesResponseBodyRolesRoleTags = None,
        update_date: str = None,
    ):
        self.arn = arn
        self.create_date = create_date
        self.description = description
        self.max_session_duration = max_session_duration
        self.role_id = role_id
        self.role_name = role_name
        self.tags = tags
        self.update_date = update_date

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.arn is not None:
            result['Arn'] = self.arn

        if self.create_date is not None:
            result['CreateDate'] = self.create_date

        if self.description is not None:
            result['Description'] = self.description

        if self.max_session_duration is not None:
            result['MaxSessionDuration'] = self.max_session_duration

        if self.role_id is not None:
            result['RoleId'] = self.role_id

        if self.role_name is not None:
            result['RoleName'] = self.role_name

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.update_date is not None:
            result['UpdateDate'] = self.update_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Arn') is not None:
            self.arn = m.get('Arn')

        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MaxSessionDuration') is not None:
            self.max_session_duration = m.get('MaxSessionDuration')

        if m.get('RoleId') is not None:
            self.role_id = m.get('RoleId')

        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')

        if m.get('Tags') is not None:
            temp_model = main_models.ListRolesResponseBodyRolesRoleTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('UpdateDate') is not None:
            self.update_date = m.get('UpdateDate')

        return self

class ListRolesResponseBodyRolesRoleTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.ListRolesResponseBodyRolesRoleTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.ListRolesResponseBodyRolesRoleTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class ListRolesResponseBodyRolesRoleTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

