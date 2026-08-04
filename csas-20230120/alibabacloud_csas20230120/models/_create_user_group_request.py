# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateUserGroupRequest(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.CreateUserGroupRequestAttributes] = None,
        description: str = None,
        name: str = None,
    ):
        # The collection of user group attributes. You can specify a maximum of 3,000 attributes. The attributes are combined using a logical OR.
        # 
        # This parameter is required.
        self.attributes = attributes
        # The user group description. The description must be 1 to 128 characters long and can contain Chinese characters, letters, digits, periods (.), underscores (_), hyphens (-), and spaces.
        self.description = description
        # The user group name. The name must be 1 to 128 characters long and can contain Chinese characters, letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.name = name

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

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.CreateUserGroupRequestAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateUserGroupRequestAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The ID of the identity provider (IdP) for the user group. This parameter is used when UserGroupType is set to **department**.
        self.idp_id = idp_id
        # The relationship for the user group. Valid values:
        # 
        # - **Equal**: Equal to.
        # 
        # - **Unequal**: Not equal to.
        # 
        # This parameter is required.
        self.relation = relation
        # The type of the user group. Valid values:
        # 
        # - **username**: Username.
        # 
        # - **department**: Department.
        # 
        # - **email**: Email.
        # 
        # - **telephone**: Mobile phone.
        # 
        # This parameter is required.
        self.user_group_type = user_group_type
        # The value of the user group attribute.
        # 
        # - If UserGroupType is set to **username**, this parameter specifies the username value. The value must be 1 to 128 characters long. It can contain Chinese characters, letters, digits, periods (.), underscores (_), hyphens (-), asterisks (\\*), at signs (@), and spaces.
        # 
        # - If UserGroupType is set to **department**, this parameter specifies the department value. For example: OU=Department 1,OU=SASE DingTalk.
        # 
        # - If UserGroupType is set to **email**, this parameter specifies the email address. For example: username\\@example.com.
        # 
        # - If UserGroupType is set to **telephone**, this parameter specifies the mobile phone number. For example: 13900001234.
        # 
        # This parameter is required.
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

