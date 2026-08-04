# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetUserGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_group: main_models.GetUserGroupResponseBodyUserGroup = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The user group.
        self.user_group = user_group

    def validate(self):
        if self.user_group:
            self.user_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_group is not None:
            result['UserGroup'] = self.user_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserGroup') is not None:
            temp_model = main_models.GetUserGroupResponseBodyUserGroup()
            self.user_group = temp_model.from_map(m.get('UserGroup'))

        return self

class GetUserGroupResponseBodyUserGroup(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.GetUserGroupResponseBodyUserGroupAttributes] = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        user_group_id: str = None,
    ):
        # The collection of user group properties. The properties are evaluated with a logical OR operator.
        self.attributes = attributes
        # The time when the user group was created.
        self.create_time = create_time
        # The description of the user group.
        self.description = description
        # The name of the user group.
        self.name = name
        # The ID of the user group.
        self.user_group_id = user_group_id

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['Attributes'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.GetUserGroupResponseBodyUserGroupAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

class GetUserGroupResponseBodyUserGroupAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The ID of the identity provider (IdP) for the user group. This parameter is returned when UserGroupType is set to **department**.
        self.idp_id = idp_id
        # The relationship of the user group. Valid values:
        # 
        # - **Equal**: Equal to.
        # 
        # - **Unequal**: Not equal to.
        self.relation = relation
        # The type of the user group. Valid values:
        # 
        # - **username**: The username.
        # 
        # - **department**: The department.
        # 
        # - **email**: The email address.
        # 
        # - **telephone**: The mobile phone number.
        self.user_group_type = user_group_type
        # The value of the user group property.
        # 
        # - If UserGroupType is set to **username**, this parameter specifies the value of the username. The value can be 1 to 128 characters in length and can contain Chinese characters, letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # - If UserGroupType is set to **department**, this parameter specifies the value of the department. Example: OU=Department 1,OU=SASE DingTalk.
        # 
        # - If UserGroupType is set to **email**, this parameter specifies the value of the email address. Example: username\\@example.com.
        # 
        # - If UserGroupType is set to **telephone**, this parameter specifies the value of the mobile phone number. Example: 13900001234.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idp_id is not None:
            result['IdpId'] = self.idp_id

        if self.relation is not None:
            result['Relation'] = self.relation

        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdpId') is not None:
            self.idp_id = m.get('IdpId')

        if m.get('Relation') is not None:
            self.relation = m.get('Relation')

        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

