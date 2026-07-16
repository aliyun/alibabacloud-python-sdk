# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class ListPoliciesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        policy_list: List[main_models.ListPoliciesResponseBodyPolicyList] = None,
        request_id: str = None,
    ):
        # Indicates whether the next query is required.
        # 
        # - If the value of this parameter is empty (`"NextToken": ""`), all results are returned, and the next query is not required.
        # 
        # - If the value of this parameter is not empty, the next query is required, and the value is the token used to start the next query.
        self.next_token = next_token
        # The tag policies.
        self.policy_list = policy_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.policy_list:
            for v1 in self.policy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['PolicyList'] = []
        if self.policy_list is not None:
            for k1 in self.policy_list:
                result['PolicyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.policy_list = []
        if m.get('PolicyList') is not None:
            for k1 in m.get('PolicyList'):
                temp_model = main_models.ListPoliciesResponseBodyPolicyList()
                self.policy_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListPoliciesResponseBodyPolicyList(DaraModel):
    def __init__(
        self,
        policy_content: str = None,
        policy_desc: str = None,
        policy_id: str = None,
        policy_name: str = None,
        user_type: str = None,
    ):
        # The document of the tag policy.
        self.policy_content = policy_content
        # The description of the tag policy.
        self.policy_desc = policy_desc
        # The ID of the tag policy.
        self.policy_id = policy_id
        # The name of the tag policy.
        self.policy_name = policy_name
        # The mode of the Tag Policy feature. Valid values:
        # 
        # - USER: single-account mode
        # 
        # - RD: multi-account mode
        # 
        # For more information about the modes of the Tag Policy feature, see [Modes of the Tag Policy feature](https://help.aliyun.com/document_detail/417434.html).
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content

        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')

        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

