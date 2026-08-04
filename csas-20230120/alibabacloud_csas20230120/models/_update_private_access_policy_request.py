# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdatePrivateAccessPolicyRequest(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        custom_user_attributes: List[main_models.UpdatePrivateAccessPolicyRequestCustomUserAttributes] = None,
        description: str = None,
        device_attribute_action: str = None,
        device_attribute_id: str = None,
        modify_type: str = None,
        name: str = None,
        policy_action: str = None,
        policy_id: str = None,
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
        # The IDs of applications associated with the internal network access policy. A single policy supports up to 100 application IDs.
        self.application_ids = application_ids
        # The application type for the internal network access policy. Valid values:
        # 
        # - **Application**: Application.
        # 
        # - **Tag**: Tag.
        self.application_type = application_type
        # This parameter specifies a collection of custom user groups for the private network access policy. It is required when the user group type is **Custom**. This collection is mutually exclusive with the user group ID collection, and you can specify a maximum of 10 custom user groups.
        self.custom_user_attributes = custom_user_attributes
        # A description of the internal network access policy. The description must be 1 to 128 characters in length. It can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), hyphens (-), and spaces.
        self.description = description
        # The action taken when a device does not meet the security baseline. Valid values:
        # 
        # - **Block**: Block access.
        # 
        # - **Observe**: Monitor access.
        self.device_attribute_action = device_attribute_action
        # The ID of the security baseline policy.
        self.device_attribute_id = device_attribute_id
        # The method used to update the internal network access policy. Valid values:
        # 
        # - **Cover** (default): Replace the existing application IDs, user group IDs, and custom user attributes with the values specified in **ApplicationIds**, **UserGroupIds**, and **CustomUserAttributes**.
        # 
        # - **Append**: Add the values specified in **ApplicationIds**, **UserGroupIds**, and **CustomUserAttributes** to the existing application IDs, user group IDs, and custom user attributes.
        self.modify_type = modify_type
        self.name = name
        # The action that the internal network access policy takes. Valid values:
        # 
        # - **Block**: Block access.
        # 
        # - **Allow**: Allow access.
        self.policy_action = policy_action
        # The ID of the internal network access policy. Get this value from one of the following operations:
        # 
        # - [ListPrivateAccessPolices](~~ListPrivateAccessPolices~~): List internal network access policies in batches.
        # 
        # - [CreatePrivateAccessPolicy](~~CreatePrivateAccessPolicy~~): Create an internal network access policy.
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The priority of the internal network access policy. Priority 1 is the highest. Valid values: 1 to 1000. The maximum value is the total number of internal network access policies minus 1.
        self.priority = priority
        # The status of the internal network access policy. Valid values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        self.status = status
        # The IDs of tags associated with the internal network access policy. A single policy supports up to 100 tag IDs.
        self.tag_ids = tag_ids
        # The ID of the trigger template.
        self.trigger_template_id = trigger_template_id
        # The IDs of trusted process groups.
        self.trusted_process_group_ids = trusted_process_group_ids
        # The status of the trusted process feature. Valid values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        self.trusted_process_status = trusted_process_status
        # The IDs of trusted software.
        self.trusted_software_ids = trusted_software_ids
        # The IDs of user groups associated with the internal network access policy. This parameter is required when UserGroupMode is set to Normal. This parameter is mutually exclusive with **CustomUserAttributes**. A single policy supports up to 10,000 user groups. You can update up to 2,000 user group IDs at a time.
        self.user_group_ids = user_group_ids
        # The user group type for the internal network access policy. Valid values:
        # 
        # - **Normal**: Regular user group.
        # 
        # - **Custom**: Custom user group.
        self.user_group_mode = user_group_mode
        # The start time of the zero-trust policy\\"s effective period, in seconds since the Unix epoch.
        self.valid_from = valid_from
        # The status of the effective time feature. Valid values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        self.valid_time_status = valid_time_status
        # The end time of the zero-trust policy\\"s effective period, in seconds since the Unix epoch.
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

        if self.modify_type is not None:
            result['ModifyType'] = self.modify_type

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
                temp_model = main_models.UpdatePrivateAccessPolicyRequestCustomUserAttributes()
                self.custom_user_attributes.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DeviceAttributeAction') is not None:
            self.device_attribute_action = m.get('DeviceAttributeAction')

        if m.get('DeviceAttributeId') is not None:
            self.device_attribute_id = m.get('DeviceAttributeId')

        if m.get('ModifyType') is not None:
            self.modify_type = m.get('ModifyType')

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

class UpdatePrivateAccessPolicyRequestCustomUserAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The identity provider ID for the custom user attribute. This parameter is required when UserGroupType is **department**.
        self.idp_id = idp_id
        # The relation used to match the custom user attribute. Valid values:
        # 
        # - **Equal**: Equal to.
        # 
        # - **Unequal**: Not equal to.
        # 
        # This parameter is required.
        self.relation = relation
        # The type of the custom user attribute. Valid values:
        # 
        # - **username**: Username.
        # 
        # - **department**: Department.
        # 
        # - **email**: Email address.
        # 
        # - **telephone**: Phone number.
        # 
        # This parameter is required.
        self.user_group_type = user_group_type
        # The value of the custom user attribute.
        # 
        # - If UserGroupType is **username**, this is the username. The value must be 1 to 128 characters in length. It can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), hyphens (-), asterisks (\\*), at signs (@), and spaces.
        # 
        # - If UserGroupType is **department**, this is the department name. Example: OU=Department 1,OU=SASE DingTalk.
        # 
        # - If UserGroupType is **email**, this is the email address. Example: username\\@example.com.
        # 
        # - If UserGroupType is **telephone**, this is the phone number. Example: 13900001234.
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

