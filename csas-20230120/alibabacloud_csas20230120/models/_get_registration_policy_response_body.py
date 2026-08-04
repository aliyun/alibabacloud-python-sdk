# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetRegistrationPolicyResponseBody(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        limit_detail: List[main_models.GetRegistrationPolicyResponseBodyLimitDetail] = None,
        match_mode: str = None,
        name: str = None,
        policy_id: str = None,
        priority: int = None,
        request_id: str = None,
        status: str = None,
        user_group_ids: List[str] = None,
        whitelist: List[str] = None,
    ):
        # The time when the device registration policy was created.
        self.create_time = create_time
        # The description of the device registration policy.
        self.description = description
        # The list of limit details of the device registration policy.
        self.limit_detail = limit_detail
        # The match mode of the policy. Valid values:
        # - **UserGroupAll**: associated with all users.
        # - **UserGroupNormal**: associated with specific user groups.
        self.match_mode = match_mode
        # The name of the device registration policy.
        self.name = name
        # The ID of the device registration policy.
        self.policy_id = policy_id
        # The priority of the device registration policy. The value 0 indicates the highest priority, and the value 99 indicates the lowest priority.
        self.priority = priority
        # The request ID.
        self.request_id = request_id
        # The status of the device registration policy. Valid values:
        # - **Enabled**: enabled.
        # - **Disabled**: disabled.
        self.status = status
        # The IDs of the user groups associated with the device registration policy. This parameter is valid when the match mode of the policy is **UserGroupNormal**.
        self.user_group_ids = user_group_ids
        # The list of whitelisted users in the device registration policy.
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

        if self.request_id is not None:
            result['RequestId'] = self.request_id

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
                temp_model = main_models.GetRegistrationPolicyResponseBodyLimitDetail()
                self.limit_detail.append(temp_model.from_map(k1))

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

class GetRegistrationPolicyResponseBodyLimitDetail(DaraModel):
    def __init__(
        self,
        device_belong: str = None,
        limit_count: main_models.GetRegistrationPolicyResponseBodyLimitDetailLimitCount = None,
        limit_type: str = None,
    ):
        # The ownership of the device. Valid values:
        # - **Company**: company-owned device.
        # - **Personal**: personal device.
        self.device_belong = device_belong
        # The device registration limit count.
        self.limit_count = limit_count
        # The type of the device registration limit. Valid values:
        # - **Unlimited**: no limit.
        # - **LimitAll**: limit by total count.
        # - **LimitDiff**: limit by terminal category.
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
            temp_model = main_models.GetRegistrationPolicyResponseBodyLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m.get('LimitCount'))

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        return self

class GetRegistrationPolicyResponseBodyLimitDetailLimitCount(DaraModel):
    def __init__(
        self,
        all: int = None,
        mobile: int = None,
        pc: int = None,
    ):
        # The total device registration limit. This parameter is valid when the device registration limit type is **LimitAll**.
        self.all = all
        # The number of mobile logins allowed by the device registration limit. This parameter is valid when the device registration limit type is **LimitDiff**.
        self.mobile = mobile
        # The number of PC logins allowed by the device registration limit. This parameter is valid when the device registration limit type is **LimitDiff**.
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

