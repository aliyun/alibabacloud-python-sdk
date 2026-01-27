# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetPrivateAccessPolicyResponseBody(DaraModel):
    def __init__(
        self,
        policy: main_models.GetPrivateAccessPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        # Intranet access policy.
        self.policy = policy
        # The ID of the current request.
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = main_models.GetPrivateAccessPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPrivateAccessPolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        create_time: str = None,
        custom_user_attributes: List[main_models.GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes] = None,
        description: str = None,
        device_attribute_action: str = None,
        device_attribute_id: str = None,
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
        # A collection of application IDs for the private access policy. This field has a value when the application type is Application.
        self.application_ids = application_ids
        # The application type of the private access policy. Possible values:
        # - **Application**: Application.
        # - **Tag**: Tag.
        self.application_type = application_type
        # Intranet access policy creation time.
        self.create_time = create_time
        # Collection of custom user group attributes. Multiple custom user group attributes are combined with an OR relationship and take effect as a set.
        self.custom_user_attributes = custom_user_attributes
        # Intranet access policy description.
        self.description = description
        # The action to take if the security baseline is not met. Possible values:
        # 
        # - **Block**: Block.
        # - **Observe**: Observe.
        self.device_attribute_action = device_attribute_action
        # The ID of the security baseline policy.
        self.device_attribute_id = device_attribute_id
        # Intranet access policy name.
        self.name = name
        # Intranet access policy action. Values:
        # - **Block**: Block.
        # - **Allow**: Allow.
        self.policy_action = policy_action
        # Intranet access policy ID.
        self.policy_id = policy_id
        # Intranet access policy priority. A value of 1 indicates the highest priority.
        self.priority = priority
        # Intranet access policy status. Values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.status = status
        # A collection of tag IDs for the private access policy. This field has a value when the application type is Tag.
        self.tag_ids = tag_ids
        # The trigger template ID.
        self.trigger_template_id = trigger_template_id
        # A list of trusted process group IDs.
        self.trusted_process_group_ids = trusted_process_group_ids
        # The status of the trusted process switch. Possible values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.trusted_process_status = trusted_process_status
        # A list of trusted software IDs.
        self.trusted_software_ids = trusted_software_ids
        # Collection of user group IDs for the intranet access policy. This field is populated when the user group type is Normal.
        self.user_group_ids = user_group_ids
        # User group type for the intranet access policy. Values:
        # - **Normal**: Normal user group.
        # - **Custom**: Custom user group.
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

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

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

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        self.custom_user_attributes = []
        if m.get('CustomUserAttributes') is not None:
            for k1 in m.get('CustomUserAttributes'):
                temp_model = main_models.GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes()
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

class GetPrivateAccessPolicyResponseBodyPolicyCustomUserAttributes(DaraModel):
    def __init__(
        self,
        idp_id: int = None,
        relation: str = None,
        user_group_type: str = None,
        value: str = None,
    ):
        # The identity provider ID for the custom user group. This field is required when the custom user group type is **department**.
        self.idp_id = idp_id
        # Custom user group relationship. Values: - **Equal**: Equal to. - **Unequal**: Not equal to.
        self.relation = relation
        # Type of the custom user group. Values:
        # - **username**: Username.
        # - **department**: Department.
        # - **email**: Email.
        # - **telephone**: Telephone.
        self.user_group_type = user_group_type
        # The value of the custom user group attribute.
        # - When the user group type is **username**, it represents the value of the username. The length should be 1 to 128 characters, supporting Chinese and case-sensitive English letters, and can include numbers, periods (.), underscores (_), and hyphens (-).
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

