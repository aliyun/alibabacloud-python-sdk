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
        # Specifies whether end users are allowed to submit a report request for this policy. Valid values:
        # 
        # - **true**: Reporting is allowed. The pop-up window on the endpoint provides a reporting entry.
        # - **false**: Reporting is not allowed.
        self.allow_report = allow_report
        # The description of the software ban policy. The description can be up to 128 characters in length and can be left empty.
        self.description = description
        # Specifies whether the policy is enabled. Valid values:
        # - **true**: Enabled. The policy is delivered to the endpoint and takes effect.
        # - **false**: Disabled. The policy configuration is retained but not delivered to the endpoint.
        # 
        # This parameter is required.
        self.enabled = enabled
        # Specifies whether to forcefully terminate running software processes. Valid values:
        self.force_kill = force_kill
        # The Chinese text of the primary button in the pop-up window on the endpoint.
        self.main_button_text_ch = main_button_text_ch
        # The English text of the primary button in the pop-up window on the endpoint.
        self.main_button_text_en = main_button_text_en
        # The scope in which the policy takes effect. Valid values:
        # 
        # This parameter is required.
        self.match_mode = match_mode
        # The Chinese text of the secondary button in the pop-up window on the endpoint.
        self.minor_button_text_ch = minor_button_text_ch
        # The English text of the secondary button in the pop-up window on the endpoint.
        self.minor_button_text_en = minor_button_text_en
        # Policy Name of the software ban policy. Policy Name must be 1 to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-). Spaces are not supported.
        # 
        # This parameter is required.
        self.name = name
        # The object type. Valid values:
        # 
        # This parameter is required.
        self.object_type = object_type
        # The action to take. Valid values:
        # 
        # - **Ban**: Blocks the software from running and displays a pop-up notification to the end user.
        # - **BanSilent**: Blocks the software from running without notifying the end user (silent blocking).
        # - **Warn**: Displays a pop-up notification to the end user without blocking the software from running.
        # 
        # This parameter is required.
        self.policy_type = policy_type
        # The policy priority. Valid values: 0 to 99. A smaller value indicates a higher priority.
        # 
        # This parameter is required.
        self.priority = priority
        # The Chinese prompt content displayed in the pop-up window on the endpoint.
        # 
        # This parameter is required.
        self.prompt_ch = prompt_ch
        # The English prompt content displayed in the pop-up window on the endpoint.
        # 
        # This parameter is required.
        self.prompt_en = prompt_en
        # The collection of banned software directly controlled by this policy.
        self.software_ids = software_ids
        # The collection of banned software tag IDs controlled by this policy.
        self.tag_ids = tag_ids
        # The Chinese title of the pop-up window on the endpoint.
        self.title_ch = title_ch
        # The English title of the pop-up window on the endpoint.
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
        # Specifies whether the blocked software is a built-in blocked software entry. Valid values:
        # - **true**: A built-in blocked software entry that is shared across all Alibaba Cloud accounts. Built-in entries cannot be modified or deleted.
        # - **false**: A custom blocked software entry under the current Alibaba Cloud account.
        self.is_default = is_default
        # The ID of the prohibited software. You can obtain the value from the following operations:
        # - [ListProhibitedSoftware](~~ListProhibitedSoftware~~): Lists prohibited software.
        # - [CreateProhibitedSoftware](~~CreateProhibitedSoftware~~): Creates custom prohibited software.
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

