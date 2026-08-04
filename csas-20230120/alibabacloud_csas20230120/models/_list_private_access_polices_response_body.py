# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListPrivateAccessPolicesResponseBody(DaraModel):
    def __init__(
        self,
        polices: List[main_models.ListPrivateAccessPolicesResponseBodyPolices] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The list of private access policies.
        self.polices = polices
        # The request ID.
        self.request_id = request_id
        # The total number of private access policies.
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
                temp_model = main_models.ListPrivateAccessPolicesResponseBodyPolices()
                self.polices.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListPrivateAccessPolicesResponseBodyPolices(DaraModel):
    def __init__(
        self,
        application_ids: List[str] = None,
        application_type: str = None,
        create_time: str = None,
        custom_user_attributes: List[main_models.ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes] = None,
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
        # The collection of application IDs of the private access policy. This field has a value when the application type is **Application**.
        self.application_ids = application_ids
        # The application type of the private access policy. Valid values:
        # - **Application**: Application.
        # - **Tag**: Tag.
        self.application_type = application_type
        # The creation time of the private access policy.
        self.create_time = create_time
        # The collection of custom user group attributes. Multiple custom user group attributes have an OR relationship and take effect by union.
        self.custom_user_attributes = custom_user_attributes
        # The description of the private access policy.
        self.description = description
        # The action to take when the security baseline is not met. Valid values:
        # - **Block**: Block.
        # - **Observe**: Observe.
        self.device_attribute_action = device_attribute_action
        # The ID of the security baseline policy.
        self.device_attribute_id = device_attribute_id
        # The name of the private access policy.
        self.name = name
        # The action of the private access policy. Valid values:
        # - **Block**: Block.
        # - **Allow**: Allow.
        self.policy_action = policy_action
        # The ID of the private access policy.
        self.policy_id = policy_id
        # The priority of the private access policy. A value of 1 indicates the highest priority.
        self.priority = priority
        # The status of the private access policy. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.status = status
        # The collection of tag IDs of the private access policy. This field has a value when the application type is **Tag**.
        self.tag_ids = tag_ids
        # The ID of the trigger template.
        self.trigger_template_id = trigger_template_id
        # The list of trusted process group IDs.
        self.trusted_process_group_ids = trusted_process_group_ids
        # The status of the trusted process switch. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.trusted_process_status = trusted_process_status
        # The list of trusted software IDs.
        self.trusted_software_ids = trusted_software_ids
        # The collection of user group IDs for the private access policy. This field has a value when the user group type is **Normal**.
        self.user_group_ids = user_group_ids
        # The user group type of the private access policy. Valid values:
        # - **Normal**: Normal user group.
        # - **Custom**: Custom user group.
        self.user_group_mode = user_group_mode
        # The effective start time of the zero trust policy, in second-level Unix timestamp.
        self.valid_from = valid_from
        # The status of the effective time switch. Valid values:
        # - **Enabled**: Enabled.
        # - **Disabled**: Disabled.
        self.valid_time_status = valid_time_status
        # The effective end time of the zero trust policy, in second-level Unix timestamp.
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
                temp_model = main_models.ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes()
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

class ListPrivateAccessPolicesResponseBodyPolicesCustomUserAttributes(DaraModel):
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
        # - **Equal**: Equal.
        # - **Unequal**: Not equal.
        self.relation = relation
        # The type of the user group. Valid values:
        # - **username**: Username.
        # - **department**: Department.
        # - **email**: Email.
        # - **telephone**: Mobile phone.
        self.user_group_type = user_group_type
        # The value of the user group attribute.
        # - When the user group type is **username**, this indicates the value of the username. The value must be 1 to 128 characters in length and supports Chinese characters and uppercase and lowercase English letters. It can contain digits, periods (.), underscores (_), and hyphens (-).
        # - When the user group type is **department**, this indicates the value of the department. For example: OU=Department1,OU=SASE DingTalk.
        # - When the user group type is **email**, this indicates the value of the email. For example: username@example.com.
        # - When the user group type is **telephone**, this indicates the value of the mobile phone. For example: 13900001234.
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

