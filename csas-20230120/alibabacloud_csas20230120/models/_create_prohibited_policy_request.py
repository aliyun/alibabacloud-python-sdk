# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class CreateProhibitedPolicyRequest(DaraModel):
    def __init__(
        self,
        allow_report: str = None,
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
        policy_type: str = None,
        priority: int = None,
        prompt_ch: str = None,
        prompt_en: str = None,
        software_ids: List[main_models.CreateProhibitedPolicyRequestSoftwareIds] = None,
        tag_ids: List[str] = None,
        title_ch: str = None,
        title_en: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # Specifies whether to allow terminal users to submit an exception request for the policy. Valid values:
        # - **true**: Exception requests are allowed. The terminal pop-up window provides an entry for the request.
        # - **false**: Exception requests are not allowed.
        self.allow_report = allow_report
        # The description of the prohibited software policy. The description can be up to 128 characters in length and can be empty.
        self.description = description
        # Specifies whether the policy is enabled. Valid values:
        # - **true**: The policy is enabled, delivered to terminals, and takes effect.
        # - **false**: The policy is disabled. The configuration is retained but not delivered to terminals.
        # 
        # This parameter is required.
        self.enabled = enabled
        # Specifies whether to forcibly terminate running processes of the software. Valid values:
        # - **true**: The terminal immediately terminates the running processes of the software when the policy is matched.
        # - **false**: The terminal does not terminate running processes but only prevents subsequent startups.
        self.force_kill = force_kill
        # The Chinese text of the primary button in the terminal pop-up window.
        self.main_button_text_ch = main_button_text_ch
        # The English text of the primary button in the terminal pop-up window.
        self.main_button_text_en = main_button_text_en
        # The effective scope. Valid values:
        # - **UserGroupAll**: The policy takes effect for all users under the current Alibaba Cloud account. You do not need to specify user groups.
        # - **UserGroupNormal**: The policy takes effect only for users in the user groups specified by UserGroupIds.
        # 
        # This parameter is required.
        self.match_mode = match_mode
        # The Chinese text of the secondary button in the terminal pop-up window.
        self.minor_button_text_ch = minor_button_text_ch
        # The English text of the secondary button in the terminal pop-up window.
        self.minor_button_text_en = minor_button_text_en
        # Policy Name of the prohibited software policy. Policy Name must be 1 to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        # 
        # This parameter is required.
        self.name = name
        # The object type. Valid values:
        # - **App**: controls disable software. The managed objects are specified by SoftwareIds.
        # - **Tag**: controls disable software labels. The managed objects are specified by TagIds. All disable software within the labels is managed.
        # 
        # This parameter is required.
        self.object_type = object_type
        # The action to take. Valid values:
        # - **Ban**: blocks the software from running and displays a pop-up window on the terminal to notify the user.
        # - **BanSilent**: blocks the software from running without notifying the user.
        # - **Warn**: displays a pop-up window on the terminal to notify the user without blocking the software from running.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The policy priority. Valid values: 0 to 99. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.priority = priority
        # The Chinese prompt content in the terminal pop-up window.
        # 
        # This parameter is required.
        self.prompt_ch = prompt_ch
        # The English prompt content in the terminal pop-up window.
        # 
        # This parameter is required.
        self.prompt_en = prompt_en
        # The collection of prohibited software directly managed by the policy.
        self.software_ids = software_ids
        # The collection of prohibited software tag IDs managed by the policy.
        self.tag_ids = tag_ids
        # The Chinese title of the terminal pop-up window.
        self.title_ch = title_ch
        # The English title of the terminal pop-up window.
        self.title_en = title_en
        # The collection of user group IDs for which the policy takes effect.
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
                temp_model = main_models.CreateProhibitedPolicyRequestSoftwareIds()
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

class CreateProhibitedPolicyRequestSoftwareIds(DaraModel):
    def __init__(
        self,
        is_default: bool = None,
        software_id: str = None,
    ):
        # Specifies whether the prohibited software is built-in. Valid values:
        # - **true**: The software is built-in, shared by all Alibaba Cloud accounts, and cannot be modified or deleted.
        # - **false**: The software is custom prohibited software under the current Alibaba Cloud account.
        self.is_default = is_default
        # The ID of the prohibited software. You can obtain the value from the following sources:
        # - [ListProhibitedSoftware](~~ListProhibitedSoftware~~): queries prohibited software in batches.
        # - [CreateProhibitedSoftware](~~CreateProhibitedSoftware~~): creates custom prohibited software.
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

