# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListRegistrationPoliciesForUserGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        user_groups: List[main_models.ListRegistrationPoliciesForUserGroupResponseBodyUserGroups] = None,
    ):
        self.request_id = request_id
        self.user_groups = user_groups

    def validate(self):
        if self.user_groups:
            for v1 in self.user_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UserGroups'] = []
        if self.user_groups is not None:
            for k1 in self.user_groups:
                result['UserGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k1 in m.get('UserGroups'):
                temp_model = main_models.ListRegistrationPoliciesForUserGroupResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k1))

        return self

class ListRegistrationPoliciesForUserGroupResponseBodyUserGroups(DaraModel):
    def __init__(
        self,
        policies: List[main_models.ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies] = None,
        user_group_id: str = None,
    ):
        self.policies = policies
        self.user_group_id = user_group_id

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

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

class ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPolicies(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        limit_detail: List[main_models.ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail] = None,
        match_mode: str = None,
        name: str = None,
        policy_id: str = None,
        priority: int = None,
        status: str = None,
        whitelist: List[str] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.limit_detail = limit_detail
        self.match_mode = match_mode
        self.name = name
        self.policy_id = policy_id
        self.priority = priority
        self.status = status
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
                temp_model = main_models.ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail()
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

        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')

        return self

class ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetail(DaraModel):
    def __init__(
        self,
        device_belong: str = None,
        limit_count: main_models.ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount = None,
        limit_type: str = None,
    ):
        self.device_belong = device_belong
        self.limit_count = limit_count
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
            temp_model = main_models.ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount()
            self.limit_count = temp_model.from_map(m.get('LimitCount'))

        if m.get('LimitType') is not None:
            self.limit_type = m.get('LimitType')

        return self

class ListRegistrationPoliciesForUserGroupResponseBodyUserGroupsPoliciesLimitDetailLimitCount(DaraModel):
    def __init__(
        self,
        all: str = None,
        mobile: str = None,
        pc: str = None,
    ):
        self.all = all
        self.mobile = mobile
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

