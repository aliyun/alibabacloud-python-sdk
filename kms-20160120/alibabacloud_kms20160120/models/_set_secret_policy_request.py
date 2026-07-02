# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetSecretPolicyRequest(DaraModel):
    def __init__(
        self,
        policy: str = None,
        policy_name: str = None,
        secret_name: str = None,
    ):
        # The content of the secret policy. The value must be in the JSON format. The value can be up to 32,768 bytes in length.
        # 
        # A secret policy contains the following elements:
        # 
        # - Version: The version of the secret policy. The value can only be 1.
        # 
        # - Statement: The statement of the secret policy. Each secret policy can contain one or more statements.
        # 
        # The following code shows the format of a secret policy:
        # 
        # ```
        # {
        #     "Version": "1",
        #     "Statement": [
        #         {
        #             "Sid": "Enable RAM User Permissions",
        #             "Effect": "Allow",
        #             "Principal": {
        #               "RAM": ["acs:ram::12345678****:*"]
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
        # The following section describes the elements in a statement:
        # 
        # - Sid: Optional. The custom identifier of the statement. The value can be up to 128 characters in length and can contain uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and special characters, including underscores (_), forward slashes (/), equal signs (=), plus signs (+), periods (.), at signs (@), and hyphens (-).
        # 
        # - Effect: Required. Specifies whether to allow or deny the permissions in the statement. Valid values: Allow and Deny.
        # 
        # - Principal: Required. The principal that is authorized to access the secret. You can set this parameter to the current Alibaba Cloud account (the account to which the secret belongs), a RAM user or RAM role of the current Alibaba Cloud account, or a RAM user or RAM role of another Alibaba Cloud account.
        # 
        # - Action: Required. The API operations that are allowed or denied. The value must start with \\`kms:\\`. For a list of supported operations, see [Secret policy overview](https://help.aliyun.com/document_detail/2716465.html). If you specify an operation that is not in the list, the operation does not take effect.
        # 
        # - Resource: Required. The value can only be \\`\\*\\`, which indicates the current KMS secret.
        # 
        # - Condition: Optional. The conditions for the authorization to take effect. You can use conditions to evaluate the context of an API request to determine whether a policy statement is applicable. The format is `"Condition": {"condition operator": {"condition key": "condition value"}}`. For more information, see [Secret policy overview](https://help.aliyun.com/document_detail/2716465.html).
        # 
        # > After you grant permissions to a RAM user or RAM role of another Alibaba Cloud account, you must go to the RAM console and use the Alibaba Cloud account to which the RAM user or RAM role belongs to grant the RAM user or RAM role the permissions to use the secret. For more information, see [Custom policies for KMS](https://help.aliyun.com/document_detail/480682.html), [Grant permissions to a RAM user](https://help.aliyun.com/document_detail/116146.html), and [Grant permissions to a RAM role](https://help.aliyun.com/document_detail/116147.html).
        # 
        # This parameter is required.
        self.policy = policy
        # The name of the secret policy. The value can only be \\`default\\`.
        self.policy_name = policy_name
        # The name or Alibaba Cloud Resource Name (ARN) of the secret.
        # 
        # > When you access a secret in another Alibaba Cloud account, you must specify the ARN of the secret. The ARN of a secret is in the format of `acs:kms:${region}:${account}:secret/${secret-name}`.
        # 
        # This parameter is required.
        self.secret_name = secret_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy

        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        return self

