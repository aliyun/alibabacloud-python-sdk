# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListUserPrivateAccessPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        polices: List[main_models.ListUserPrivateAccessPoliciesResponseBodyPolices] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # List of authorized policies.
        self.polices = polices
        # ID of the request.
        self.request_id = request_id
        # Total number of authorized policies.
        self.total_num = total_num

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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.polices = []
        if m.get('Polices') is not None:
            for k1 in m.get('Polices'):
                temp_model = main_models.ListUserPrivateAccessPoliciesResponseBodyPolices()
                self.polices.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListUserPrivateAccessPoliciesResponseBodyPolices(DaraModel):
    def __init__(
        self,
        custom_user_attributes: List[main_models.ListUserPrivateAccessPoliciesResponseBodyPolicesCustomUserAttributes] = None,
        device_attribute_name: str = None,
        matched_user_group: str = None,
        name: str = None,
        policy_action: str = None,
        policy_id: str = None,
        priority: int = None,
        trusted_process_group_ids: List[str] = None,
        trusted_software_ids: List[str] = None,
        user_group_mode: str = None,
    ):
        # Set of custom user group attributes. Multiple custom user group attributes are in an OR relationship, effective as a union.
        self.custom_user_attributes = custom_user_attributes
        # Associated security baseline.
        self.device_attribute_name = device_attribute_name
        # Associated user group.
        self.matched_user_group = matched_user_group
        # Intranet access policy name.
        self.name = name
        # Action of the intranet access policy. Values:
        # - **Block**: Block.
        # - **Allow**: Allow.
        self.policy_action = policy_action
        # Intranet access policy ID.
        self.policy_id = policy_id
        # Priority of the intranet access policy. The number 1 indicates the highest priority.
        self.priority = priority
        # List of trusted process group IDs.
        self.trusted_process_group_ids = trusted_process_group_ids
        # List of trusted software IDs.
        self.trusted_software_ids = trusted_software_ids
        # Type of the user group for the intranet access policy. Values:
        # - **Normal**: Normal user group.
        # - **Custom**: Custom user group.
        self.user_group_mode = user_group_mode

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
        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k1 in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k1.to_map() if k1 else None)

        if self.device_attribute_name is not None:
            result['DeviceAttributeName'] = self.device_attribute_name

        if self.matched_user_group is not None:
            result['MatchedUserGroup'] = self.matched_user_group

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.trusted_process_group_ids is not None:
            result['TrustedProcessGroupIds'] = self.trusted_process_group_ids

        if self.trusted_software_ids is not None:
            result['TrustedSoftwareIds'] = self.trusted_software_ids

        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k1 in m.get('CustomUserAttributes'):
                temp_model = main_models.ListUserPrivateAccessPoliciesResponseBodyPolicesCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k1))

        if m.get('DeviceAttributeName') is not None:
            self.device_attribute_name = m.get('DeviceAttributeName')

        if m.get('MatchedUserGroup') is not None:
            self.matched_user_group = m.get('MatchedUserGroup')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('TrustedProcessGroupIds') is not None:
            self.trusted_process_group_ids = m.get('TrustedProcessGroupIds')

        if m.get('TrustedSoftwareIds') is not None:
            self.trusted_software_ids = m.get('TrustedSoftwareIds')

        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')

        return self

class ListUserPrivateAccessPoliciesResponseBodyPolicesCustomUserAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The identity provider ID of the user group. This value exists when the custom user group type is **department**.
        self.idp_id = idp_id
        # Relation of the user group. Values:
        # - **Equal**: Equal.
        # - **Unequal**: Not equal.
        self.relation = relation
        # Type of the user group. Values:
        # - **username**: Username.
        # - **department**: Department.
        # - **email**: Email.
        # - **telephone**: Telephone.
        self.user_group_type = user_group_type
        # The value of the user group attribute.
        # - When the user group type is **username**, it represents the value of the username. The length is 1 to 128 characters, supporting Chinese and case-sensitive English letters, and can include numbers, periods (.), underscores (_), and hyphens (-).
        # - When the user group type is **department**, it represents the value of the department. For example: OU=Department1,OU=SASE DingTalk.
        # - When the user group type is **email**, it represents the value of the email. For example: username@example.com.
        # - When the user group type is **telephone**, it represents the value of the phone number. For example: 13900001234.
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

