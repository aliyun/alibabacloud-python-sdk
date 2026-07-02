# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetKeyPolicyRequest(DaraModel):
    def __init__(
        self,
        key_id: str = None,
        policy: str = None,
        policy_name: str = None,
    ):
        # The ID or Alibaba Cloud Resource Name (ARN) of the key.
        # 
        # > To access a key of another Alibaba Cloud account, you must specify the ARN of the key. The key ARN is in the format of `acs:kms:${region}:${account}:key/${keyid}`.
        # 
        # This parameter is required.
        self.key_id = key_id
        # The key policy. The policy is in the JSON format. The policy can be up to 32,768 bytes in length.
        # 
        # A key policy contains the following elements:
        # 
        # - Version: The version of the key policy. The value can only be 1.
        # 
        # - Statement: The statement of the key policy. Each key policy can contain one or more statements.
        # 
        # The following code provides an example of a key policy:
        # 
        # ```
        # {
        #     "Version": "1",
        #     "Statement": [
        #         {
        #             "Sid": "Enable RAM User Permissions",
        #             "Effect": "Allow",
        #             "Principal": {
        #               "RAM": ["acs:ram::112890462****:*"]
        #             },
        #             "Action": [
        #                 "kms:*"
        #             ],
        #             "Resource": [
        #                 "*"
        #             ]
        #         }
        #     ]
        # }
        # ```
        # 
        # The following section describes the elements in a Statement:
        # 
        # - Sid: Optional. The custom statement identifier. The value can be up to 128 characters in length and can contain uppercase letters, lowercase letters, digits, and the following special characters: _ / + = . @ -.
        # 
        # - Effect: Required. The effect of the policy statement. Valid values: Allow and Deny.
        # 
        # - Principal: Required. The principal that is authorized to access the key. You can set this parameter to the current Alibaba Cloud account, a RAM user or RAM role of the current Alibaba Cloud account, or a RAM user or RAM role of another Alibaba Cloud account.
        # 
        # - Action: Required. The API operations that are allowed or denied. The value must start with kms:. For more information about the operations, see [Key policy overview](https://help.aliyun.com/document_detail/2716468.html). If you specify an operation that is not included in the list, the operation will not take effect.
        # 
        # - Resource: Required. The key. The value can only be \\*.
        # 
        # - Condition: Optional. The conditions for the policy to take effect. You can use conditions to evaluate the context of an API request to determine whether the policy statement is applicable. The format is `"Condition": {"condition operator": {"condition key": "condition value"}}`. For more information, see [Key policy overview](https://help.aliyun.com/document_detail/2716468.html).
        # 
        # > After you grant permissions to a RAM user or RAM role of another Alibaba Cloud account, you must use the Alibaba Cloud account to which the RAM user or RAM role belongs to grant the RAM user or RAM role the permissions to use the key in the RAM console. For more information, see [Custom policies for KMS](https://help.aliyun.com/document_detail/480682.html), [Grant permissions to a RAM user](https://help.aliyun.com/document_detail/116146.html), and [Grant permissions to a RAM role](https://help.aliyun.com/document_detail/116147.html).
        # 
        # This parameter is required.
        self.policy = policy
        # The name of the key policy. The name can only be \\`default\\`.
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        return self

