# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListRegistrationPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        policies: List[main_models.ListRegistrationPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
        total_num: str = None,
    ):
        # The list of device registration policies.
        self.policies = policies
        # The ID of this request.
        self.request_id = request_id
        # The total number of device registration policies.
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
                temp_model = main_models.ListRegistrationPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListRegistrationPoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        limit_detail: List[main_models.ListRegistrationPoliciesResponseBodyPoliciesLimitDetail] = None,
        match_mode: str = None,
        name: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # The creation time of the device registration policy.
        self.create_time = create_time
        # The description of the device registration policy.
        self.description = description
        # The list of device registration policy limit details.
        self.limit_detail = limit_detail
        # The policy matching target type. Valid values:
        # 
        # - **UserGroupAll**: Associate all users.
        # 
        # - **UserGroupNormal**: Associate some user groups.
        self.match_mode = match_mode
        # The name of the device registration policy.
        self.name = name
        # The ID of the device registration policy.
        self.policy_id = policy_id
        # The policy priority for device registration. A value of 0 indicates the highest priority, and 99 indicates the lowest priority.
        self.priority = priority
        # The status of the device registration policy. Valid values:
        # 
        # - **Enabled**: Enabled.
        # 
        # - **Disabled**: Disabled.
        self.status = status
        # A collection of user group IDs for the device registration policy. This field has a value when the policy matching target type is **UserGroupNormal**.
        self.user_group_ids = user_group_ids
        # The whitelist of users for the device registration policy.
        self.whitelist = whitelist

    def validate(self):
        if self.limit_detail:
            for v1 in self.limit_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        result['LimitDetail'] = []
        if self.limit_detail is not None:
            for k1 in self.limit_detail:
                result['LimitDetail'].append(k1.to_map() if k1 else None)

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.name is not None:
            result['Name'] = self.name

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
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.limit_detail = []
        if m.get('LimitDetail') is not None:
            for k1 in m.get('LimitDetail'):
                temp_model = main_models.ListRegistrationPoliciesResponseBodyPoliciesLimitDetail()
                self.limit_detail.append(temp_model.from_map(k1))

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

class ListRegistrationPoliciesResponseBodyPoliciesLimitDetail(DaraModel):
    def __init__(
        self,
        device_belong: str = None,
        limit_count: main_models.ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount = None,
        limit_type: str = None,
    ):
        # The device ownership. Valid values:
        # 
        # - **Company**: Company device.
        # 
        # - **Personal**: Personal device.
        self.device_belong = device_belong
        # The number of device registration limits.
        self.limit_count = limit_count
        # The type of device registration limit. Valid values:
        # 
        # - **Unlimited**: No limit.
        # 
        # - **LimitAll**: Limit by total number.
        # 
        # - **LimitDiff**: Limit by device categorization.
        self.limit_type = limit_type

    def validate(self):
        if self.limit_count:
            self.limit_count.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.device_belong is not None:
            result['DeviceBelong'] = self.device_belong

        if self.limit_count is not None:
            result['LimitCount'] = self.limit_count.to_map()

        if self.limit_type is not None:
            result['LimitType'] = self.limit_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceBelong') is not None:
            self.device_belong = m.get('DeviceBelong')

        if m.get('LimitCount') is not None:
            temp_model = main_models.ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m.get('LimitCount'))

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        return self

class ListRegistrationPoliciesResponseBodyPoliciesLimitDetailLimitCount(DaraModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        # The total number of device registration limits. This field is valid when the device registration limit type is **LimitAll**.
        self.all = all
        # The number of mobile client log ons allowed for device registration. This field is valid when the device registration limit type is **LimitDiff**.
        self.mobile = mobile
        # The number of PC client log ons allowed for device registration. This field is valid when the device registration limit type is **LimitDiff**.
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

