# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateUserGroupRequest(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.UpdateUserGroupRequestAttributes] = None,
        description: str = None,
        modify_type: str = None,
        user_group_id: str = None,
    ):
        # The set of user group attributes. The maximum total number is 3000. Multiple user group attributes have an OR relationship and take effect as a union.
        self.attributes = attributes
        # The description of the user group. The description must be 1 to 128 characters in length, and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), hyphens (-), and spaces.
        self.description = description
        # The modification type of the user group. Valid values:
        # - **Cover** (default): overwrites the original user group attribute set with the value of the **Attributes** parameter.
        # - **Append**: separately appends the values entered in the **Attributes** parameter to the user group attribute set.
        self.modify_type = modify_type
        # The ID of the user group. Value sources:
        # - [ListUserGroups](~~ListUserGroups~~): queries user groups in batches.
        # - [CreateUserGroup](~~CreateUserGroup~~): creates a user group.
        # 
        # This parameter is required.
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

        if self.description is not None:
            result['Description'] = self.description

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.UpdateUserGroupRequestAttributes()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

class UpdateUserGroupRequestAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The identity provider ID of the user group. This value exists when the custom user group type is **department**.
        self.idp_id = idp_id
        # The relation of the user group. Valid values:
        # - **Equal**: equal to.
        # - **Unequal**: not equal to.
        # 
        # This parameter is required.
        self.relation = relation
        # The type of the user group. Valid values:
        # - **username**: username.
        # - **department**: department.
        # - **email**: email.
        # - **telephone**: mobile phone.
        # 
        # This parameter is required.
        self.user_group_type = user_group_type
        # The value of the user group attribute.
        # - If the user group type is **username**, this parameter indicates the username value. The value must be 1 to 128 characters in length, and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), hyphens (-), asterisks (*), at signs (@), and spaces.
        # - If the user group type is **department**, this parameter indicates the department value. Example: OU=Department1,OU=SASEDingTalk.
        # - If the user group type is **email**, this parameter indicates the email value. Example: username@example.com.
        # - If the user group type is **telephone**, this parameter indicates the mobile phone value. Example: 13900001234.
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

