# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vod20170321 import models as main_models
from darabonba.model import DaraModel

class ListAppPoliciesForIdentityResponseBody(DaraModel):
    def __init__(
        self,
        app_policy_list: List[main_models.ListAppPoliciesForIdentityResponseBodyAppPolicyList] = None,
        request_id: str = None,
    ):
        # The details of each policy.
        # 
        # > A maximum of 100 entries can be returned.
        self.app_policy_list = app_policy_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.app_policy_list:
            for v1 in self.app_policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AppPolicyList'] = []
        if self.app_policy_list is not None:
            for k1 in self.app_policy_list:
                result['AppPolicyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_policy_list = []
        if m.get('AppPolicyList') is not None:
            for k1 in m.get('AppPolicyList'):
                temp_model = main_models.ListAppPoliciesForIdentityResponseBodyAppPolicyList()
                self.app_policy_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAppPoliciesForIdentityResponseBodyAppPolicyList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        creation_time: str = None,
        description: str = None,
        modification_time: str = None,
        policy_name: str = None,
        policy_type: str = None,
        policy_value: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The time when the application policy was created. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The description of the policy.
        self.description = description
        # The last time when the application policy was modified. The time follows the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The name of the policy.
        self.policy_name = policy_name
        # The type of the policy. Valid values:
        # 
        # *   **System**
        # *   **Custom**
        self.policy_type = policy_type
        # The content of the policy.
        self.policy_value = policy_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        if self.policy_value is not None:
            result['PolicyValue'] = self.policy_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        if m.get('PolicyValue') is not None:
            self.policy_value = m.get('PolicyValue')

        return self

