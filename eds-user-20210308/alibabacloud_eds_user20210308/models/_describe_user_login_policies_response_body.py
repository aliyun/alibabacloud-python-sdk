# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class DescribeUserLoginPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        policies: List[main_models.DescribeUserLoginPoliciesResponseBodyPolicies] = None,
        request_id: str = None,
    ):
        # The list of policies.
        self.policies = policies
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.policies = []
        if m.get('Policies') is not None:
            for k1 in m.get('Policies'):
                temp_model = main_models.DescribeUserLoginPoliciesResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserLoginPoliciesResponseBodyPolicies(DaraModel):
    def __init__(
        self,
        name: str = None,
        policy_id: str = None,
        user_groups: List[main_models.DescribeUserLoginPoliciesResponseBodyPoliciesUserGroups] = None,
    ):
        # The policy name.
        self.name = name
        # The policy ID.
        self.policy_id = policy_id
        # The associated user group information.
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
        if self.name is not None:
            result['Name'] = self.name

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        result['UserGroups'] = []
        if self.user_groups is not None:
            for k1 in self.user_groups:
                result['UserGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k1 in m.get('UserGroups'):
                temp_model = main_models.DescribeUserLoginPoliciesResponseBodyPoliciesUserGroups()
                self.user_groups.append(temp_model.from_map(k1))

        return self

class DescribeUserLoginPoliciesResponseBodyPoliciesUserGroups(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
    ):
        # The user group ID.
        self.group_id = group_id
        # The user group name.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

