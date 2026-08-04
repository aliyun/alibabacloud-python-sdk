# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListPolicesForPrivateAccessTagResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        tags: List[main_models.ListPolicesForPrivateAccessTagResponseBodyTags] = None,
    ):
        # The ID of this request.
        self.request_id = request_id
        # List of private network access tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ListPolicesForPrivateAccessTagResponseBodyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListPolicesForPrivateAccessTagResponseBodyTags(DaraModel):
    def __init__(
        self,
        polices: List[main_models.ListPolicesForPrivateAccessTagResponseBodyTagsPolices] = None,
        tag_id: str = None,
    ):
        # Collection of private network access policies.
        self.polices = polices
        # Private network access tag ID.
        self.tag_id = tag_id

    def validate(self):
        if self.polices:
            for v1 in self.polices:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Polices'] = []
        if self.polices is not None:
            for k1 in self.polices:
                result['Polices'].append(k1.to_map() if k1 else None)

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k1 in m.get('Polices'):
                temp_model = main_models.ListPolicesForPrivateAccessTagResponseBodyTagsPolices()
                self.polices.append(temp_model.from_map(k1))

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        return self

class ListPolicesForPrivateAccessTagResponseBodyTagsPolices(DaraModel):
    def __init__(
        self,
        application_type: str = None,
        create_time: str = None,
        custom_user_attributes: List[main_models.ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes] = None,
        description: str = None,
        name: str = None,
        policy_action: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_type: str = None,
    ):
        # The application type of the private network access policy. Values:
        # 
        # - **Application**: Application.
        # 
        # - **Tag**: Tag.
        self.application_type = application_type
        # Creation time of the private network access policy.
        self.create_time = create_time
        # A collection of custom user group attributes. Multiple custom user group attributes have an OR relationship and take effect as a union.
        self.custom_user_attributes = custom_user_attributes
        # Description of the private network access policy.
        self.description = description
        # Private network access policy name.
        self.name = name
        # The action that the private access policy performs. Valid values:
        # 
        # - **Block**: Blocks access.
        # 
        # - **Allow**: Allows access.
        self.policy_action = policy_action
        # Private network access policy ID.
        self.policy_id = policy_id
        # The private network access policy priority. The number 1 indicates the highest priority.
        self.priority = priority
        # The status of the private network access policy. Values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        self.status = status
        # The user group type of the private network access policy. Values:
        # 
        # - **Normal**: Normal user group.
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
                temp_model = main_models.ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes()
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

class ListPolicesForPrivateAccessTagResponseBodyTagsPolicesCustomUserAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The identity provider ID of the user group. This value exists if the custom user group type is **department**.
        self.idp_id = idp_id
        # The relationship of the user group. Values:
        # 
        # - **Equal**: Equal.
        # 
        # - **Unequal**: Unequal.
        self.relation = relation
        # The type of user group. Values:
        # 
        # - **username**: Username.
        # 
        # - **department**: Department.
        # 
        # - **email**: Mailbox.
        # 
        # - **telephone**: Mobile phone.
        self.user_group_type = user_group_type
        # The value of the user group attribute.
        # 
        # - If the user group type is **username**, this indicates the username\\"s value. The length is 1 to 128 characters. It supports Chinese characters, uppercase and lowercase English letters, and can include numbers, periods (.), underscores (_), and hyphens (-).
        # 
        # - If the user group type is **department**, this indicates the department\\"s value. For example: OU=Department 1,OU=SASE DingTalk.
        # 
        # - If the user group type is **email**, this indicates the mailbox\\"s value. For example: username\\@example.com.
        # 
        # - If the user group type is **telephone**, this indicates the mobile phone\\"s value. For example: 13900001234.
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

