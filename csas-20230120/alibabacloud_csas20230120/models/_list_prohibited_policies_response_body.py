# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListProhibitedPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        policies: List[main_models.ListProhibitedPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        total_num: int = None,
    ):
        # The list of software prohibition policies, sorted by priority from highest to lowest.
        self.policies = policies
        # Id of the request
        self.request_id = request_id
        # The total number of software prohibition policies.
        self.total_num = total_num

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

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListProhibitedPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListProhibitedPoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        allow_report: bool = None,
        create_time: str = None,
        description: str = None,
        enabled: bool = None,
        force_kill: bool = None,
        main_button_text_ch: str = None,
        main_button_text_en: str = None,
        match_mode: str = None,
        minor_button_text_ch: str = None,
        minor_button_text_en: str = None,
        name: str = None,
        object_type: str = None,
        policy_id: str = None,
        policy_type: str = None,
        priority: int = None,
        prompt_ch: str = None,
        prompt_en: str = None,
        software_ids: List[main_models.ListProhibitedPoliciesResponseBodyPoliciesSoftwareIds] = None,
        tag_ids: List[str] = None,
        title_ch: str = None,
        title_en: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # Indicates whether endpoint users are allowed to submit a filing request for this policy. Valid values:
        # - **true**: Filing is allowed. The endpoint pop-up notification provides a filing entry.
        # - **false**: Filing is not allowed.
        self.allow_report = allow_report
        # The creation time of the software prohibition policy, in the format of yyyy-MM-dd HH:mm:ss, using the UTC+8 time zone.
        self.create_time = create_time
        # The description of the software prohibition policy.
        self.description = description
        # Specifies whether the policy is enabled. Valid values:
        # - **true**: Enabled. The policy is delivered to endpoints and takes effect.
        # - **false**: Disabled. The policy configuration is retained but not delivered to endpoints.
        self.enabled = enabled
        # Specifies whether to forcibly terminate running software processes. Valid values:
        # - **true**: The endpoint immediately terminates the running processes of the software when the policy is matched.
        # - **false**: Running processes are not terminated. Only subsequent launches are blocked.
        self.force_kill = force_kill
        # The Chinese text of the primary button in the endpoint pop-up notification.
        self.main_button_text_ch = main_button_text_ch
        # The English text of the primary button in the endpoint pop-up notification.
        self.main_button_text_en = main_button_text_en
        # The policy matching target type. Valid values:
        # - **UserGroupAll**: Associated with all users.
        # - **UserGroupNormal**: Associated with specific user groups.
        self.match_mode = match_mode
        # The Chinese text of the secondary button in the endpoint pop-up notification.
        self.minor_button_text_ch = minor_button_text_ch
        # The English text of the secondary button in the endpoint pop-up notification.
        self.minor_button_text_en = minor_button_text_en
        # The name of the software prohibition policy.
        self.name = name
        # The object type of the controlled target. Valid values:
        # - **App**: Controls by prohibited software. The controlled objects are specified by SoftwareIds.
        # - **Tag**: Controls by prohibited software tag. The controlled objects are specified by TagIds. All prohibited software under the tag is controlled.
        self.object_type = object_type
        # The ID of the software prohibition policy.
        self.policy_id = policy_id
        # The action to take. Valid values:
        # - **Ban**: Blocks the software from running and displays a pop-up notification on the endpoint to alert the user.
        # - **BanSilent**: Blocks the software from running without notifying the user. The blocking is silent.
        # - **Warn**: Only displays a pop-up notification on the endpoint to alert the user without blocking the software from running.
        self.policy_type = policy_type
        # The policy priority. Valid values: 0 to 99. A smaller value indicates a higher priority.
        self.priority = priority
        # The Chinese prompt content displayed in the endpoint pop-up notification.
        self.prompt_ch = prompt_ch
        # The English prompt content displayed in the endpoint pop-up notification.
        self.prompt_en = prompt_en
        # The collection of prohibited software directly controlled by this policy.
        self.software_ids = software_ids
        # The collection of prohibited software tag IDs controlled by this policy.
        self.tag_ids = tag_ids
        # The Chinese title of the endpoint pop-up notification.
        self.title_ch = title_ch
        # The English title of the endpoint pop-up notification.
        self.title_en = title_en
        # The collection of user group IDs to which this policy applies.
        self.user_group_ids = user_group_ids
        # The list of exempted usernames.
        self.whitelist = whitelist

    def validate(self):
        if self.software_ids:
            for v1 in self.software_ids:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_report is not None:
            result['AllowReport'] = self.allow_report

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.force_kill is not None:
            result['ForceKill'] = self.force_kill

        if self.main_button_text_ch is not None:
            result['MainButtonTextCh'] = self.main_button_text_ch

        if self.main_button_text_en is not None:
            result['MainButtonTextEn'] = self.main_button_text_en

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.minor_button_text_ch is not None:
            result['MinorButtonTextCh'] = self.minor_button_text_ch

        if self.minor_button_text_en is not None:
            result['MinorButtonTextEn'] = self.minor_button_text_en

        if self.name is not None:
            result['Name'] = self.name

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.prompt_ch is not None:
            result['PromptCh'] = self.prompt_ch

        if self.prompt_en is not None:
            result['PromptEn'] = self.prompt_en

        result['SoftwareIds'] = []
        if self.software_ids is not None:
            for k1 in self.software_ids:
                result['SoftwareIds'].append(k1.to_map() if k1 else None)

        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids

        if self.title_ch is not None:
            result['TitleCh'] = self.title_ch

        if self.title_en is not None:
            result['TitleEn'] = self.title_en

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowReport') is not None:
            self.allow_report = m.get('AllowReport')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('ForceKill') is not None:
            self.force_kill = m.get('ForceKill')

        if m.get('MainButtonTextCh') is not None:
            self.main_button_text_ch = m.get('MainButtonTextCh')

        if m.get('MainButtonTextEn') is not None:
            self.main_button_text_en = m.get('MainButtonTextEn')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('MinorButtonTextCh') is not None:
            self.minor_button_text_ch = m.get('MinorButtonTextCh')

        if m.get('MinorButtonTextEn') is not None:
            self.minor_button_text_en = m.get('MinorButtonTextEn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('PromptCh') is not None:
            self.prompt_ch = m.get('PromptCh')

        if m.get('PromptEn') is not None:
            self.prompt_en = m.get('PromptEn')

        self.software_ids = []
        if m.get('SoftwareIds') is not None:
            for k1 in m.get('SoftwareIds'):
                temp_model = main_models.ListProhibitedPoliciesResponseBodyPoliciesSoftwareIds()
                self.software_ids.append(temp_model.from_map(k1))

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        if m.get('TitleCh') is not None:
            self.title_ch = m.get('TitleCh')

        if m.get('TitleEn') is not None:
            self.title_en = m.get('TitleEn')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

class ListProhibitedPoliciesResponseBodyPoliciesSoftwareIds(DaraModel):
    def __init__(
        self,
        is_default: bool = None,
        software_id: str = None,
    ):
        # Indicates whether the prohibited software is a system built-in entry. Valid values:
        # - **true**: A system built-in prohibited software entry shared by all Alibaba Cloud accounts. Modification and deletion are not supported.
        # - **false**: Custom prohibited software under the current Alibaba Cloud account.
        self.is_default = is_default
        # The prohibited software ID.
        self.software_id = software_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.software_id is not None:
            result['SoftwareId'] = self.software_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')

        return self

