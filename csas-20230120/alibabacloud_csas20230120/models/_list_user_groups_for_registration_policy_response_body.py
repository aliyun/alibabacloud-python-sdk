# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListUserGroupsForRegistrationPolicyResponseBody(DaraModel):
    def __init__(
        self,
        policies: List[main_models.ListUserGroupsForRegistrationPolicyResponseBodyPolicies] = None,
        request_id: str = None,
    ):
        # A list of device registration policies.
        self.policies = policies
        # The ID of this request.
        self.request_id = request_id

    def validate(self):
        if self.policies:
            for v1 in self.policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListUserGroupsForRegistrationPolicyResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUserGroupsForRegistrationPolicyResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        policy_id: str = None,
        user_groups: List[main_models.ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups] = None,
    ):
        # The ID of the device registration policy.
        self.policy_id = policy_id
        # A collection of user groups associated with the device registration policy.
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for v1 in self.user_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        result['UserGroups'] = []
        if self.user_groups is not None:
            for k1 in self.user_groups:
                result['UserGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k1 in m.get('UserGroups'):
                temp_model = main_models.ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups()
                self.user_groups.append(temp_model.from_map(k1))

        return self

class ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroups(DaraModel):
    def __init__(
        self,
        attributes: List[main_models.ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes] = None,
        create_time: str = None,
        description: str = None,
        name: str = None,
        user_group_id: str = None,
    ):
        # A collection of user group attributes.
        self.attributes = attributes
        # The time when the user group was created.
        self.create_time = create_time
        # A description of the user group.
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
                temp_model = main_models.ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes()
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

class ListUserGroupsForRegistrationPolicyResponseBodyPoliciesUserGroupsAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The identity provider ID for the user group. This field appears only when UserGroupType is **department**.
        self.idp_id = idp_id
        # The relation for the user group. Valid values:
        # 
        # - **Equal**: Equal to.
        # 
        # - **Unequal**: Not equal to.
        self.relation = relation
        # The type of the user group. Valid values:
        # 
        # - **username**: A username.
        # 
        # - **department**: A department.
        # 
        # - **email**: An email address.
        # 
        # - **telephone**: A phone number.
        self.user_group_type = user_group_type
        # The value of the user group attribute.
        # 
        # - If UserGroupType is **username**, this is the username. It must be 1–128 characters long and can contain uppercase and lowercase letters, Chinese characters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # - If UserGroupType is **department**, this is the department name. Example: OU=Department 1,OU=SASE DingTalk.
        # 
        # - If UserGroupType is **email**, this is the email address. Example: username\\@example.com.
        # 
        # - If UserGroupType is **telephone**, this is the phone number. Example: 13900001234.
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

