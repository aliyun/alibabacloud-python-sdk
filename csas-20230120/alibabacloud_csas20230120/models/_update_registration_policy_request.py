# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class UpdateRegistrationPolicyRequest(DaraModel):
    def __init__(
        self,
        company_limit_count: main_models.UpdateRegistrationPolicyRequestCompanyLimitCount = None,
        company_limit_type: str = None,
        description: str = None,
        match_mode: str = None,
        name: str = None,
        personal_limit_count: main_models.UpdateRegistrationPolicyRequestPersonalLimitCount = None,
        personal_limit_type: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # The registration limit for corporate devices.
        self.company_limit_count = company_limit_count
        # The registration limit type for corporate devices. Valid values:
        # 
        # - **Unlimited**: No limit.
        # 
        # - **LimitAll**: Limits the total number of devices.
        # 
        # - **LimitDiff**: Limits devices by terminal type.
        self.company_limit_type = company_limit_type
        # The description of the device registration policy. The description can be 1 to 128 characters long and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), hyphens (-), and spaces.
        self.description = description
        # The matching target type of the policy. Valid values:
        # 
        # - **UserGroupAll**: Associates with all users.
        # 
        # - **UserGroupNormal**: Associates with specific user groups.
        self.match_mode = match_mode
        # The name of the device registration policy. The name must be 1 to 128 characters in length and can contain Chinese characters, uppercase and lowercase letters, digits, periods (.), underscores (_), and hyphens (-).
        self.name = name
        # The registration limit for personal devices.
        self.personal_limit_count = personal_limit_count
        # The registration limit type for personal devices. Valid values:
        # 
        # - **Unlimited**: No limit.
        # 
        # - **LimitAll**: Limits the total number of devices.
        # 
        # - **LimitDiff**: Limits devices by terminal type.
        self.personal_limit_type = personal_limit_type
        # The ID of the device registration policy. You can obtain the ID by calling one of the following operations:
        # 
        # - [ListRegistrationPolicies](~~ListRegistrationPolicies~~)
        # 
        # - [GetRegistrationPolicy](~~GetRegistrationPolicy~~)
        # 
        # - [CreateRegistrationPolicy](~~CreateRegistrationPolicy~~)
        # 
        # - [UpdateRegistrationPolicy](~~UpdateRegistrationPolicy~~)
        # 
        # This parameter is required.
        self.policy_id = policy_id
        # The priority of the device registration policy. A smaller value indicates a higher priority. The value 0 indicates the highest priority, and 99 indicates the lowest priority.
        self.priority = priority
        # The status of the device registration policy. Valid values:
        # 
        # - **Enabled**
        # 
        # - **Disabled**
        self.status = status
        # The IDs of user groups. This parameter is required when MatchMode is set to **UserGroupNormal**. A policy can be associated with up to 100 user groups.
        self.user_group_ids = user_group_ids
        # The list of whitelisted users for the device registration policy. You can add up to 1,000 usernames.
        self.whitelist = whitelist

    def validate(self):
        if self.company_limit_count:
            self.company_limit_count.validate()
        if self.personal_limit_count:
            self.personal_limit_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_limit_count is not None:
            result['CompanyLimitCount'] = self.company_limit_count.to_map()

        if self.company_limit_type is not None:
            result['CompanyLimitType'] = self.company_limit_type

        if self.description is not None:
            result['Description'] = self.description

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.personal_limit_count is not None:
            result['PersonalLimitCount'] = self.personal_limit_count.to_map()

        if self.personal_limit_type is not None:
            result['PersonalLimitType'] = self.personal_limit_type

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.status is not None:
            result['Status'] = self.status

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyLimitCount') is not None:
            temp_model = main_models.UpdateRegistrationPolicyRequestCompanyLimitCount()
            self.company_limit_count = temp_model.from_map(m.get('CompanyLimitCount'))

        if m.get('CompanyLimitType') is not None:
            self.company_limit_type = m.get('CompanyLimitType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PersonalLimitCount') is not None:
            temp_model = main_models.UpdateRegistrationPolicyRequestPersonalLimitCount()
            self.personal_limit_count = temp_model.from_map(m.get('PersonalLimitCount'))

        if m.get('PersonalLimitType') is not None:
            self.personal_limit_type = m.get('PersonalLimitType')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

class UpdateRegistrationPolicyRequestPersonalLimitCount(DaraModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        # The total number of personal devices that can be registered. The value can be from 0 to 100. The default value is 0. This parameter is valid only when PersonalLimitType is set to **LimitAll**.
        self.all = all
        # The number of personal mobile devices that can be registered. The value can be from 0 to 100. The default value is 0. This parameter is valid only when PersonalLimitType is set to **LimitDiff**.
        self.mobile = mobile
        # The number of personal PCs that can be registered. The value can be from 0 to 100. The default value is 0. This parameter is valid only when PersonalLimitType is set to **LimitDiff**.
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.pc is not None:
            result['PC'] = self.pc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('PC') is not None:
            self.pc = m.get('PC')

        return self

class UpdateRegistrationPolicyRequestCompanyLimitCount(DaraModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        # The total number of corporate devices that can be registered. The value can be from 0 to 100. The default value is 0. This parameter is valid only when CompanyLimitType is set to **LimitAll**.
        self.all = all
        # The number of corporate mobile devices that can be registered. The value can be from 0 to 100. The default value is 0. This parameter is valid only when CompanyLimitType is set to **LimitDiff**.
        self.mobile = mobile
        # The number of corporate PCs that can be registered. The value can be from 0 to 100. The default value is 0. This parameter is valid only when CompanyLimitType is set to **LimitDiff**.
        self.pc = pc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.pc is not None:
            result['PC'] = self.pc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('PC') is not None:
            self.pc = m.get('PC')

        return self

