# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_tag20180828 import models as main_models
from darabonba.model import DaraModel

class GetPolicyResponseBody(DaraModel):
    def __init__(
        self,
        policy: main_models.GetPolicyResponseBodyPolicy = None,
        request_id: str = None,
    ):
        # The details of the tag policy.
        self.policy = policy
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            temp_model = main_models.GetPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        policy_content: str = None,
        policy_desc: str = None,
        policy_name: str = None,
        user_type: str = None,
    ):
        # The document of the tag policy.
        self.policy_content = policy_content
        # The description of the tag policy.
        self.policy_desc = policy_desc
        # The name of the tag policy.
        self.policy_name = policy_name
        # The mode of the Tag Policy feature. Valid values:
        # 
        # *   USER: single-account mode
        # *   RD: multi-account mode
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

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

