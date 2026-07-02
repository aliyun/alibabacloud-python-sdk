# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSecretShrinkRequest(DaraModel):
    def __init__(
        self,
        dkmsinstance_id: str = None,
        description: str = None,
        enable_automatic_rotation: bool = None,
        encryption_key_id: str = None,
        extended_config_shrink: str = None,
        policy: str = None,
        rotation_interval: str = None,
        secret_data: str = None,
        secret_data_type: str = None,
        secret_name: str = None,
        secret_type: str = None,
        tags: str = None,
        version_id: str = None,
    ):
        # The ID of the KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The description of the secret.
        self.description = description
        # Specifies whether to enable automatic rotation. Valid values:
        # 
        # - true: enables automatic rotation.
        # 
        # - false (default): disables automatic rotation.
        # 
        # > This parameter is valid only if SecretType is set to Rds, PolarDB, Redis, RAMCredentials, or ECS. If SecretType is set to Generic, automatic rotation is not supported. You can call the [PutSecretValue](https://help.aliyun.com/document_detail/154503.html) operation to manually rotate the secret.
        self.enable_automatic_rotation = enable_automatic_rotation
        # The ID of the key used to encrypt the secret value.
        # 
        # > The key and the secret must be in the same KMS instance. The key must be a symmetric key.
        self.encryption_key_id = encryption_key_id
        # The extended configuration of the secret. This parameter specifies the properties of the secret of a specific type. The value can be up to 1,024 characters in length.
        # 
        # - If SecretType is set to Generic, this parameter is ignored.
        # 
        # - If SecretType is set to Rds, you must specify the following parameters in ExtendedConfig:
        # 
        #   - SecretSubType (Required): The subtype of the secret. Valid values:
        # 
        #     - SingleUser: Secrets Manager manages the RDS secret in single-account mode. When the secret is rotated, the password of the specified account is reset to a new random password.
        # 
        #     - DoubleUsers: Secrets Manager manages the RDS secret in double-account mode. ACSCurrent and ACSPrevious point to one of the accounts. When the secret is rotated, the password of the account pointed to by ACSPrevious is reset to a new random password. Then, Secrets Manager swaps the accounts that ACSCurrent and ACSPrevious point to.
        # 
        #   - DBInstanceId (Required): The ID of the RDS instance to which the account belongs.
        # 
        #   - CustomData (Optional): The custom data. The value is a key-value pair in the JSON format. You can specify up to 10 key-value pairs. Separate multiple key-value pairs with commas (,). Example: `{"Key1": "v1", "fds":"fdsf"}`. The default value is `{}`.
        # 
        # - If SecretType is set to Redis, you must specify the following parameters in ExtendedConfig:
        # 
        #   - SecretSubType (Required): The subtype of the secret. Valid values:
        # 
        #     - DoubleUsers: Secrets Manager manages the Redis secret in double-account mode. ACSCurrent and ACSPrevious point to one of the accounts. When the secret is rotated, the password of the account pointed to by ACSPrevious is reset to a new random password. Then, Secrets Manager swaps the accounts that ACSCurrent and ACSPrevious point to.
        # 
        #   - AccountName (Required): The database username.
        # 
        #   - CloneAccountName (Required): The database username, which is the value of AccountName with the `_clone` suffix.
        # 
        #   - AccountPrivilege (Required): The permissions to access the database.
        # 
        #   - InstanceId (Required): The ID of the Redis instance.
        # 
        #   - RegionId (Required): The ID of the region where the Redis instance resides.
        # 
        #   - CustomData (Optional): The custom data. The value is a key-value pair in the JSON format. You can specify up to 10 key-value pairs. Separate multiple key-value pairs with commas (,). Example: `{"Key1": "v1", "fds":"fdsf"}`. The default value is `{}`.
        # 
        # - If SecretType is set to RAMCredentials, you must specify the following parameters in ExtendedConfig:
        # 
        #   - SecretSubType (Required): The subtype of the secret. The value is RamUserAccessKey.
        # 
        #   - UserName (Required): The name of the RAM user.
        # 
        #   - CustomData (Optional): The custom data. The value is a key-value pair in the JSON format. You can specify up to 10 key-value pairs. Separate multiple key-value pairs with commas (,). The default value is `{}`.
        # 
        # - If SecretType is set to ECS, you must specify the following parameters in ExtendedConfig:
        # 
        #   - SecretSubType (Required): The subtype of the secret. Valid values:
        # 
        #     - Password: an ECS password.
        # 
        #     - SSHKey: an ECS SSH key pair.
        # 
        #   - RegionId (Required): The ID of the region where the ECS instance resides.
        # 
        #   - InstanceId (Required): The ID of the ECS instance.
        # 
        #   - CustomData (Optional): The custom data. The value is a key-value pair in the JSON format. You can specify up to 10 key-value pairs. Separate multiple key-value pairs with commas (,). The default value is `{}`.
        # 
        # - If SecretType is set to PolarDB, you must specify the following parameters in ExtendedConfig:
        # 
        #   - SecretSubType (Required): The fixed value is DoubleUsers.
        # 
        #   - RegionId (Required): The region.
        # 
        #   - DBClusterId (Required): The ID of the PolarDB instance.
        # 
        #   - DBType (Required): MySQL or PostgreSQL.
        # 
        #   - AccountName (Required): The account name.
        # 
        #   - CloneAccountName: The value is AccountName_clone.
        # 
        #   - AccountType: Only Normal is supported.
        # 
        #   - AccountPrivilege: This parameter is available only for MySQL.
        # 
        #   - DBName: This parameter is available only for MySQL.
        # 
        #   - CustomData (Optional): The custom data. The value is a key-value pair in the JSON format. You can specify up to 10 key-value pairs. Separate multiple key-value pairs with commas (,). Example: {"Key1": "v1", "fds":"fdsf"}. The default value is {}.
        # 
        # > If SecretType is set to Rds, Redis, PolarDB, RAMCredentials, or ECS, you must configure this parameter.
        self.extended_config_shrink = extended_config_shrink
        # The content of the secret policy. The value is in the JSON format. The value can be up to 32,768 bytes in length.
        # 
        # For more information about secret policies, see [Overview of secret policies](https://help.aliyun.com/document_detail/2716465.html). If you do not specify this parameter, the default secret policy is used.
        # 
        # A secret policy contains the following parts:
        # 
        # - Version: The version of the secret policy. Only 1 is supported.
        # 
        # - Statement: The statements of the secret policy. Each secret policy can contain one or more statements.
        # 
        # The following is the format of a secret policy:
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
        # Details about a statement:
        # 
        # - Sid: (Optional) The custom identifier of the statement. The value can be up to 128 characters in length and can contain uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and special characters, including underscores (_), forward slashes (/), plus signs (+), equal signs (=), periods (.), at signs (@), and hyphens (-).
        # 
        # - Effect: (Required) The effect of the policy statement. Valid values: Allow and Deny.
        # 
        # - Principal: (Required) The principal that is authorized by the policy. You can specify the current Alibaba Cloud account (the account to which the secret belongs), a RAM user or RAM role of the current Alibaba Cloud account, or a RAM user or RAM role of another Alibaba Cloud account.
        # 
        # - Action: (Required) The API operations that are allowed or denied. The value must start with "kms:". For the list of supported operations, see [Overview of secret policies](https://help.aliyun.com/document_detail/2716465.html). If you specify an operation that is not in the list, the setting does not take effect.
        # 
        # - Resource: (Required) The resource. The value can only be \\*, which indicates the current KMS secret.
        # 
        # - Condition: (Optional) The conditions for the authorization to take effect. You can use conditions to evaluate the context of an API request to determine whether to apply the policy statement. The format is `"Condition": {"condition operator": {"condition key": "condition value"}}`. For more information, see [Overview of secret policies](https://help.aliyun.com/document_detail/2716465.html).
        # 
        # > After you grant permissions to a RAM user or RAM role of another Alibaba Cloud account, you must use the Alibaba Cloud account to which the RAM user or RAM role belongs to grant the RAM user or RAM role the permissions to use the secret in the RAM console. Then, the RAM user or RAM role can use the secret. For more information, see [Custom policies for KMS](https://help.aliyun.com/document_detail/480682.html), [Grant permissions to a RAM user](https://help.aliyun.com/document_detail/116146.html), and [Grant permissions to a RAM role](https://help.aliyun.com/document_detail/116147.html).
        self.policy = policy
        # The interval for automatic rotation. The value is in the range of 6 hours to 8,760 hours (365 days).<br>
        # The value is in the `integer[unit]` format. `integer` indicates the interval. `unit` indicates the unit of time.<br>
        # Valid values for unit: d (day), h (hour), m (minute), and s (second). For example, both 7d and 604,800s indicate a rotation interval of 7 days.<br><br>
        # 
        # > You must specify this parameter if you set EnableAutomaticRotation to true. You do not need to specify this parameter if you set EnableAutomaticRotation to false.
        self.rotation_interval = rotation_interval
        # The value of the secret. The value can be up to 30,720 bytes (30 KB) in length. KMS encrypts the secret value with the specified key and stores the encrypted value in the initial version.
        # 
        # - If SecretType is set to Generic, you can specify a custom secret value.
        # 
        # - If SecretType is set to Rds, the secret value must be in the following format: `{"Accounts":[{"AccountName":"","AccountPassword":""}]}`. In the format, `AccountName` specifies the username of the account for the RDS instance and `AccountPassword` specifies the password of the account.
        # 
        # - If SecretType is set to Redis, set this parameter to `$Auto`.
        # 
        # - If SecretType is set to RAMCredentials, the secret value must be in the following format: `{"AccessKeys":[{"AccessKeyId":"","AccessKeySecret":""}]}`. In the format, `AccessKeyId` specifies the AccessKey ID and `AccessKeySecret` specifies the AccessKey secret. You must specify all AccessKey pairs of the RAM user.
        # 
        # - If SecretType is set to PolarDB, set this parameter to `$Auto`.
        # 
        # - If SecretType is set to ECS, the secret value must be in one of the following formats:
        # 
        #   - If SecretSubType in the ExtendedConfig parameter is set to Password: `{"UserName":"","Password": ""}`. In the format, `UserName` specifies the username used to log on to the ECS instance and `Password` specifies the password used to log on to the ECS instance.
        # 
        #   - If SecretSubType in the ExtendedConfig parameter is set to SSHKey: `{"UserName":"","PublicKey": "", "PrivateKey": ""}`. In the format, `PublicKey` specifies the SSH-formatted public key used to log on to the ECS instance and `PrivateKey` specifies the private key used to log on to the ECS instance.
        # 
        # This parameter is required.
        self.secret_data = secret_data
        # The type of the secret value. Valid values:
        # 
        # - text (default): The secret value is a text string.
        # 
        # - binary: The secret value is a binary string.
        # 
        # > If SecretType is set to Rds, Redis, PolarDB, RAMCredentials, or ECS, SecretDataType must be set to text.
        self.secret_data_type = secret_data_type
        # The name of the secret. The name must be unique in the same region.
        # The name can be up to 192 characters in length and can contain letters, digits, underscores (_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The following limits apply to secret names for different types of secrets:
        # 
        # - If SecretType is set to Generic, Rds, or Redis, the name cannot start with `acs/`.
        # 
        # - If SecretType is set to RAMCredentials, set this parameter to the fixed value `$Auto`. In this case, KMS automatically generates a secret name that starts with `acs/ram/user/` and contains the display name of the RAM user.
        # 
        # - If SecretType is set to ECS, the name must start with `acs/ecs/`.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # The type of the secret. Valid values:
        # 
        # - Generic (default): a generic secret.
        # 
        # - Rds: an RDS secret.
        # 
        # - Redis: a Redis secret.
        # 
        # - RAMCredentials: a RAM secret.
        # 
        # - ECS: an ECS secret.
        # 
        # - PolarDB: a PolarDB secret.
        self.secret_type = secret_type
        # The tags of the secret. Each tag consists of a key-value pair. A tag consists of a tag key and a tag value.
        # 
        # The tag key and tag value can be up to 128 characters in length and can contain letters, digits, forward slashes (/), backslashes (\\), underscores (_), hyphens (-), periods (.), plus signs (+), equal signs (=), colons (:), and at signs (@).
        # 
        # - The tag key cannot start with aliyun or acs:.
        # 
        # - You can specify up to 20 key-value pairs for each secret.
        self.tags = tags
        # The version number of the initial version. The version number must be unique within the secret.
        # The version number can be up to 64 characters in length.
        # 
        # This parameter is required.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dkmsinstance_id is not None:
            result['DKMSInstanceId'] = self.dkmsinstance_id

        if self.description is not None:
            result['Description'] = self.description

        if self.enable_automatic_rotation is not None:
            result['EnableAutomaticRotation'] = self.enable_automatic_rotation

        if self.encryption_key_id is not None:
            result['EncryptionKeyId'] = self.encryption_key_id

        if self.extended_config_shrink is not None:
            result['ExtendedConfig'] = self.extended_config_shrink

        if self.policy is not None:
            result['Policy'] = self.policy

        if self.rotation_interval is not None:
            result['RotationInterval'] = self.rotation_interval

        if self.secret_data is not None:
            result['SecretData'] = self.secret_data

        if self.secret_data_type is not None:
            result['SecretDataType'] = self.secret_data_type

        if self.secret_name is not None:
            result['SecretName'] = self.secret_name

        if self.secret_type is not None:
            result['SecretType'] = self.secret_type

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DKMSInstanceId') is not None:
            self.dkmsinstance_id = m.get('DKMSInstanceId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnableAutomaticRotation') is not None:
            self.enable_automatic_rotation = m.get('EnableAutomaticRotation')

        if m.get('EncryptionKeyId') is not None:
            self.encryption_key_id = m.get('EncryptionKeyId')

        if m.get('ExtendedConfig') is not None:
            self.extended_config_shrink = m.get('ExtendedConfig')

        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RotationInterval') is not None:
            self.rotation_interval = m.get('RotationInterval')

        if m.get('SecretData') is not None:
            self.secret_data = m.get('SecretData')

        if m.get('SecretDataType') is not None:
            self.secret_data_type = m.get('SecretDataType')

        if m.get('SecretName') is not None:
            self.secret_name = m.get('SecretName')

        if m.get('SecretType') is not None:
            self.secret_type = m.get('SecretType')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

