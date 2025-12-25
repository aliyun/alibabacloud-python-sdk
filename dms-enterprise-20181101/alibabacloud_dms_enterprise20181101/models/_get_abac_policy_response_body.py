# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetAbacPolicyResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        policy: main_models.GetAbacPolicyResponseBodyPolicy = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message that is returned if the request failed.
        self.error_message = error_message
        # The details of the policy.
        self.policy = policy
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.policy:
            self.policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.policy is not None:
            result['Policy'] = self.policy.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Policy') is not None:
            temp_model = main_models.GetAbacPolicyResponseBodyPolicy()
            self.policy = temp_model.from_map(m.get('Policy'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAbacPolicyResponseBodyPolicy(DaraModel):
    def __init__(
        self,
        authorized_quantity: str = None,
        creator_id: int = None,
        policy_content: str = None,
        policy_desc: str = None,
        policy_id: int = None,
        policy_name: str = None,
        policy_source: str = None,
    ):
        # The number of users or custom roles to which the policy is attached.
        self.authorized_quantity = authorized_quantity
        # The ID of the user who create the policy.
        self.creator_id = creator_id
        # The content of the policy.
        self.policy_content = policy_content
        # The description of the policy.
        self.policy_desc = policy_desc
        # The ID of the policy.
        self.policy_id = policy_id
        # The name of the policy.
        self.policy_name = policy_name
        # The source of the policy. Valid values:
        self.policy_source = policy_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorized_quantity is not None:
            result['AuthorizedQuantity'] = self.authorized_quantity

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.policy_content is not None:
            result['PolicyContent'] = self.policy_content

        if self.policy_desc is not None:
            result['PolicyDesc'] = self.policy_desc

        if self.policy_id is not None:
            result['PolicyId'] = self.policy_id

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.policy_source is not None:
            result['PolicySource'] = self.policy_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizedQuantity') is not None:
            self.authorized_quantity = m.get('AuthorizedQuantity')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('PolicyContent') is not None:
            self.policy_content = m.get('PolicyContent')

        if m.get('PolicyDesc') is not None:
            self.policy_desc = m.get('PolicyDesc')

        if m.get('PolicyId') is not None:
            self.policy_id = m.get('PolicyId')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('PolicySource') is not None:
            self.policy_source = m.get('PolicySource')

        return self

