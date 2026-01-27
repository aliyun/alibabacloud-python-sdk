# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreatePrivateAccessPolicyRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        custom_user_attributes: List[main_models.CreatePrivateAccessPolicyRequestCustomUserAttributes] = None,
        description: str = None,
        device_attribute_action: str = None,
        device_attribute_id: str = None,
        name: str = None,
        policy_action: str = None,
        priority: int = None,
        status: str = None,
        tag_ids: List[str] = None,
        trigger_template_id: str = None,
        trusted_process_group_ids: List[str] = None,
        trusted_process_status: str = None,
        trusted_software_ids: List[str] = None,
        user_group_ids: List[str] = None,
        user_group_mode: str = None,
        valid_from: int = None,
        valid_time_status: str = None,
        valid_until: int = None,
    ):
        # Set of application IDs for the private access policy. Up to 100 application IDs can be entered. Required when **ApplicationType** is **Application**. Mutually exclusive with **TagIds**.
        self.application_ids = application_ids
        # Application type of the private access policy. Values:
        # - **Application**: Application.
        # - **Tag**: Tag.
        # 
        # This parameter is required.
        self.application_type = application_type
        # Set of custom user groups for the private access policy. Required when the user group type is **Custom**. Mutually exclusive with the user group ID set. Up to 10 custom user groups can be entered.
        self.custom_user_attributes = custom_user_attributes
        # Description of the private access policy. The length is 1 to 128 characters, supporting Chinese and uppercase and lowercase English letters, and can include numbers, periods (.), underscores (_), hyphens (-), and spaces.
        self.description = description
        # The execution policy for not meeting the security baseline. Values:
        # 
        # - **Block**: Block.
        # - **Observe**: Observe.
        self.device_attribute_action = device_attribute_action
        # The ID of the security baseline policy.
        self.device_attribute_id = device_attribute_id
        # Name of the private access policy. The length is 1 to 128 characters, supporting Chinese and uppercase and lowercase English letters, and can include numbers, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.name = name
        # Action of the private access policy. Values:
        # - **Block**: Block.
        # - **Allow**: Allow.
        # 
        # This parameter is required.
        self.policy_action = policy_action
        # The priority of the private access policy. The number 1 indicates the highest priority. Range: 1~1000, with the maximum value being the total number of private access policies.
        # 
        # This parameter is required.
        self.priority = priority
        # The status of the private access policy. Values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        # 
        # This parameter is required.
        self.status = status
        # Set of tag IDs for the private access policy. Up to 100 tag IDs can be entered. Required when **ApplicationType** is **Tag**. Mutually exclusive with **ApplicationIds**.
        self.tag_ids = tag_ids
        # The trigger template ID.
        self.trigger_template_id = trigger_template_id
        # The ID of the trusted process group.
        self.trusted_process_group_ids = trusted_process_group_ids
        # The switch status of the trusted process. Values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.trusted_process_status = trusted_process_status
        # The ID of the trusted software.
        self.trusted_software_ids = trusted_software_ids
        # Set of user group IDs for the private access policy. Required when the user group type is **Normal**. Mutually exclusive with the custom user group set. Up to 2000 user group IDs can be entered.
        self.user_group_ids = user_group_ids
        # User group type of the private access policy. Values:
        # - **Normal**: Normal user group.
        # - **Custom**: Custom user group.
        # 
        # This parameter is required.
        self.user_group_mode = user_group_mode
        # The start time when the zero trust policy takes effect, represented as a timestamp in seconds.
        self.valid_from = valid_from
        # Switch status for effective time. Values: - **Enabled**: On. - **Disabled**: Off.
        self.valid_time_status = valid_time_status
        # The expiration time of the zero trust policy, in seconds timestamp.
        self.valid_until = valid_until

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
        if self.application_ids is not None:
            result['ApplicationIds'] = self.application_ids

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        result['CustomUserAttributes'] = []
        if self.custom_user_attributes is not None:
            for k1 in self.custom_user_attributes:
                result['CustomUserAttributes'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.device_attribute_action is not None:
            result['DeviceAttributeAction'] = self.device_attribute_action

        if self.device_attribute_id is not None:
            result['DeviceAttributeId'] = self.device_attribute_id

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_action is not None:
            result['PolicyAction'] = self.policy_action

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids

        if self.trigger_template_id is not None:
            result['TriggerTemplateId'] = self.trigger_template_id

        if self.trusted_process_group_ids is not None:
            result['TrustedProcessGroupIds'] = self.trusted_process_group_ids

        if self.trusted_process_status is not None:
            result['TrustedProcessStatus'] = self.trusted_process_status

        if self.trusted_software_ids is not None:
            result['TrustedSoftwareIds'] = self.trusted_software_ids

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_group_mode is not None:
            result['UserGroupMode'] = self.user_group_mode

        if self.valid_from is not None:
            result['ValidFrom'] = self.valid_from

        if self.valid_time_status is not None:
            result['ValidTimeStatus'] = self.valid_time_status

        if self.valid_until is not None:
            result['ValidUntil'] = self.valid_until

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationIds') is not None:
            self.application_ids = m.get('ApplicationIds')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k1 in m.get('CustomUserAttributes'):
                temp_model = main_models.CreatePrivateAccessPolicyRequestCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceAttributeAction') is not None:
            self.device_attribute_action = m.get('DeviceAttributeAction')

        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyAction') is not None:
            self.policy_action = m.get('PolicyAction')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        if m.get('TriggerTemplateId') is not None:
            self.trigger_template_id = m.get('TriggerTemplateId')

        if m.get('TrustedProcessGroupIds') is not None:
            self.trusted_process_group_ids = m.get('TrustedProcessGroupIds')

        if m.get('TrustedProcessStatus') is not None:
            self.trusted_process_status = m.get('TrustedProcessStatus')

        if m.get('TrustedSoftwareIds') is not None:
            self.trusted_software_ids = m.get('TrustedSoftwareIds')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserGroupMode') is not None:
            self.user_group_mode = m.get('UserGroupMode')

        if m.get('ValidFrom') is not None:
            self.valid_from = m.get('ValidFrom')

        if m.get('ValidTimeStatus') is not None:
            self.valid_time_status = m.get('ValidTimeStatus')

        if m.get('ValidUntil') is not None:
            self.valid_until = m.get('ValidUntil')

        return self

class CreatePrivateAccessPolicyRequestCustomUserAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The ID of the identity source for the custom user group. Required when the custom user group type is **department**.
        self.idp_id = idp_id
        # Relation of the custom user group. Values:
        # - **Equal**: Equal.
        # - **Unequal**: Not equal.
        self.relation = relation
        # Type of the custom user group. Values:
        # - **username**: Username.
        # - **department**: Department.
        # - **email**: Email.
        # - **telephone**: Telephone.
        self.user_group_type = user_group_type
        # Value of the custom user group attribute.
        # - When the user group type is **username**, it represents the value of the username. The length is 1 to 128 characters, supporting Chinese and uppercase and lowercase English letters, and can include numbers, periods (.), underscores (_), hyphens (-), asterisks (*), at (@) symbols, and spaces.
        # - When the user group type is **department**, it represents the value of the department. For example: OU=Department1,OU=SASE DingTalk.
        # - When the user group type is **email**, it represents the value of the email. For example: username@example.com.
        # - When the user group type is **telephone**, it represents the value of the telephone. For example: 13900001234.
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

