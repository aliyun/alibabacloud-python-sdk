# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListPolicesForPrivateAccessApplicationResponseBody(DaraModel):
    def __init__(
        self,
        applications: List[main_models.ListPolicesForPrivateAccessApplicationResponseBodyApplications] = None,
        request_id: str = None,
    ):
        # The list of private access applications.
        self.applications = applications
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.applications:
            for v1 in self.applications:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Applications'] = []
        if self.applications is not None:
            for k1 in self.applications:
                result['Applications'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.applications = []
        if m.get('Applications') is not None:
            for k1 in m.get('Applications'):
                temp_model = main_models.ListPolicesForPrivateAccessApplicationResponseBodyApplications()
                self.applications.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPolicesForPrivateAccessApplicationResponseBodyApplications(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        policies: List[main_models.ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies] = None,
    ):
        # The ID of the private access application.
        self.application_id = application_id
        # The collection of private access policies.
        self.policies = policies

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
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        result['Policies'] = []
        if self.policies is not None:
            for k1 in self.policies:
                result['Policies'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies()
                self.policies.append(temp_model.from_map(k1))

        return self

class ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPolicies(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        create_time: str = None,
        custom_user_attributes: List[main_models.ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes] = None,
        description: str = None,
        name: str = None,
        policy_action: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_type: str = None,
    ):
        # The application type of the private access policy. Valid values:
        # 
        # - **Application**: Application.
        # 
        # - **Tag**: Tag.
        self.application_type = application_type
        # The time when the private access policy was created.
        self.create_time = create_time
        # The collection of custom user group attributes. If you specify multiple attributes, the relationship between them is OR.
        self.custom_user_attributes = custom_user_attributes
        # The description of the private access policy.
        self.description = description
        # The name of the private access policy.
        self.name = name
        # The action of the private access policy. Valid values:
        # 
        # - **Block**: Blocks access.
        # 
        # - **Allow**: Allows access.
        self.policy_action = policy_action
        # The ID of the private access policy.
        self.policy_id = policy_id
        # The priority of the private access policy. The value 1 indicates the highest priority.
        self.priority = priority
        # The status of the private access policy. Valid values:
        # 
        # - **Enabled**: The policy is enabled.
        # 
        # - **Disabled**: The policy is disabled.
        self.status = status
        # The user group type of the private access policy. Valid values:
        # 
        # - **Normal**: Regular user group.
        # 
        # - **Custom**: Custom user group.
        self.user_group_type = user_group_type

    def validate(self):
        if self.custom_user_attributes:
            for v1 in self.custom_user_attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k1 in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        if self.user_group_type is not None:
            result['UserGroupType'] = self.user_group_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k1 in m.get('CustomUserAttributes'):
                temp_model = main_models.ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserGroupType') is not None:
            self.user_group_type = m.get('UserGroupType')

        return self

class ListPolicesForPrivateAccessApplicationResponseBodyApplicationsPoliciesCustomUserAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The ID of the identity provider (IdP) for the user group. This parameter is returned when the custom user group type is **department**.
        self.idp_id = idp_id
        # The relationship of the user group. Valid values:
        # 
        # - **Equal**: Equal to.
        # 
        # - **Unequal**: Not equal to.
        self.relation = relation
        # The type of the user group. Valid values:
        # 
        # - **username**: Username.
        # 
        # - **department**: Department.
        # 
        # - **email**: Email.
        # 
        # - **telephone**: Mobile number.
        self.user_group_type = user_group_type
        # The value of the user group attribute.
        # 
        # - If the user group type is **username**, this parameter specifies the value of the username. The value can be 1 to 128 characters in length and can contain Chinese characters, letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # - If the user group type is **department**, this parameter specifies the value of the department. Example: OU=Department 1,OU=SASE DingTalk.
        # 
        # - If the user group type is **email**, this parameter specifies the value of the email address. Example: username\\@example.com.
        # 
        # - If the user group type is **telephone**, this parameter specifies the value of the mobile number. Example: 13900001234.
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

