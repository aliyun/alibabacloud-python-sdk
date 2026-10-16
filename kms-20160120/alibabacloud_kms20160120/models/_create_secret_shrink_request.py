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
        # The instance ID of the KMS instance.
        self.dkmsinstance_id = dkmsinstance_id
        # The description of the secret.
        self.description = description
        # Specifies whether to enable automatic rotation. Valid values:
        # - true: enables automatic rotation.
        # - false: disables automatic rotation. This is the default value.
        # 
        # 
        # > This parameter takes effect only when SecretType is set to Rds (ApsaraDB RDS secret), PolarDB (PolarDB secret), Redis (Redis secret), RAMCredentials (RAM secret), or ECS (ECS secret). When SecretType is set to Generic (generic secret), automatic rotation is not supported. You can call the [PutSecretValue](https://help.aliyun.com/document_detail/154503.html) operation to manually rotate the secret.
        self.enable_automatic_rotation = enable_automatic_rotation
        # The ID of the key used to encrypt the secret value.
        # 
        # > The key and the secret must belong to the same KMS instance, and the key must be a symmetric key.
        self.encryption_key_id = encryption_key_id
        # The extended configuration of the secret, which is used to specify the property of a specific secret type. The value can be up to 1,024 characters in length.
        # 
        # - When SecretType is set to Generic (generic secret), this parameter is ignored.
        # 
        # - When SecretType is set to Rds (ApsaraDB RDS secret), you must specify the following parameters in ExtendedConfig:
        #      - SecretSubType (required): the child class of the secret. Valid values:  
        # 
        #         - SingleUser: specifies that Secrets Manager manages the ApsaraDB RDS secret in single-account pattern. During secret rotation, the password of the specified account is reset to a new random password.
        #         - DoubleUsers: specifies that Secrets Manager manages the ApsaraDB RDS secret in dual-account pattern. ACSCurrent and ACSPrevious reference one account each. During secret rotation, the password of the account referenced by ACSPrevious is reset to a new random password, and then Secrets Manager swaps the accounts referenced by ACSCurrent and ACSPrevious.
        #     - DBInstanceId (required): instance ID of the ApsaraDB RDS instance to which the account belongs.
        #     - CustomData (optional): custom data. The value is a JSON-formatted key-value pair. You can specify up to 10 key-value pairs, separated by commas (,). Example: `{"Key1": "v1", "fds":"fdsf"}`. Default value: `{}`.  
        # 
        # - When SecretType is set to Redis (Redis secret), you must specify the following parameters in ExtendedConfig:
        #     - SecretSubType (required): the child class of the secret. Valid values:  
        #         - DoubleUsers: specifies that Secrets Manager manages the Redis secret in dual-account pattern. ACSCurrent and ACSPrevious reference one account each. During secret rotation, the password of the account referenced by ACSPrevious is reset to a new random password, and then Secrets Manager swaps the accounts referenced by ACSCurrent and ACSPrevious.
        #     - AccountName (required): the database username.
        #     - CloneAccountName (required): the database username, which is the value of AccountName appended with the `_clone` suffix.
        #     - AccountPrivilege (required): the permissions to access the database.
        #     - InstanceId (required): instance ID of the Redis instance.
        #     - RegionId (required): the region ID of the Redis instance.
        #     - CustomData (optional): custom data. The value is a JSON-formatted key-value pair. You can specify up to 10 key-value pairs, separated by commas (,). Example: `{"Key1": "v1", "fds":"fdsf"}`. Default value: `{}`.  
        # 
        # - When SecretType is set to RAMCredentials (RAM secret), you must specify the following parameters in ExtendedConfig:
        #     - SecretSubType (required): the child class of the secret. Valid value: RamUserAccessKey.
        #     - UserName (required): the name of the Resource Access Management (RAM) user.
        #     - CustomData (optional): custom data. The value is a JSON-formatted key-value pair. You can specify up to 10 key-value pairs, separated by commas (,). Default value: `{}`.  
        # - When SecretType is set to ECS (ECS secret), you must specify the following parameters in ExtendedConfig:
        #     - SecretSubType (required): the child class of the secret. Valid values:  
        # 
        #         - Password: ECS password.
        #         - SSHKey: ECS SSH public and private keys.
        #     - RegionId (required): the region ID of the ECS instance.  
        #     - InstanceId (required): instance ID of the ECS instance.
        #     - CustomData (optional): custom data. The value is a JSON-formatted key-value pair. You can specify up to 10 key-value pairs, separated by commas (,). Default value: `{}`.    
        # - When SecretType is set to PolarDB, you must specify the following parameters in ExtendedConfig:
        #     - SecretSubType (required): DoubleUsers (fixed value).
        # 
        #     - RegionId (required): the region ID.
        # 
        #     - DBClusterId (required): instance ID of the PolarDB cluster.
        # 
        #     - DBType (required): MySQL or PostgreSQL.
        # 
        #     - AccountName (required): the account name.
        # 
        #     - CloneAccountName: the value of AccountName appended with `_clone`.
        # 
        #     - AccountType: the account type. Only Normal is supported.
        # 
        #     - AccountPrivilege: the account permissions. This parameter is available only for MySQL.
        # 
        #     - DBName: the database name. This parameter is available only for MySQL.
        # 
        #     - CustomData (optional): custom data. The value is a JSON-formatted key-value pair. You can specify up to 10 key-value pairs, separated by commas (,). Example: `{"Key1": "v1", "fds":"fdsf"}`. Default value: `{}`.
        # 
        # > When SecretType is set to Rds, Redis, PolarDB, RAMCredentials, or ECS, you must set this parameter.
        self.extended_config_shrink = extended_config_shrink
        # The content of the access policy in JSON format. The maximum length is 32,768 bytes.
        # 
        # For more information about secret policies, see [Overview of secret policies](https://help.aliyun.com/document_detail/2716465.html). If you do not specify this parameter, the default access policy is used.
        # 
        # The access policy includes the following fields:
        # 
        # - Version: the version of the access policy. Currently, only version 1 is supported.
        # - Statement: the statements in the access policy. Each access policy contains one or more statements.
        # 
        # The access policy uses the following format:
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
        # Statement details:
        # - Sid: optional. The custom statement identifier. The value can be up to 128 characters in length and can contain uppercase letters (A-Z), lowercase letters (a-z), digits (0-9), and special characters (_/+=.@-).
        # - Effect: required. Specifies whether to allow or deny the permissions in the policy statement. Valid values: Allow and Deny.
        # 
        # - Principal: required. The principal to which the policy is attached. You can set this field to the current Alibaba Cloud account (the account to which the secret belongs), a RAM user or RAM role under the current Alibaba Cloud account, or a RAM user or RAM role under another Alibaba Cloud account.
        # 
        # - Action: required. The API operations to allow or deny. The value must start with "kms:". For the list of available operations, see [Overview of secret policies](https://help.aliyun.com/document_detail/2716465.html). If you specify an operation that is not in the list, the setting does not take effect.
        # 
        # - Resource: required. The value can only be *, which indicates the current KMS secret.
        # 
        # - Condition: optional. The conditions that must be met for the authorization to take effect. You can use conditions to evaluate the context of an API request to determine whether the policy statement applies. The format is `"Condition": {"condition operator": {"condition key": "condition value"}}`. For more information, see [Overview of secret policies](https://help.aliyun.com/document_detail/2716465.html).
        # 
        # > After you grant Resource Access Management (RAM) user or RAM role under another Alibaba Cloud account, you must also use the Alibaba Cloud account of the RAM user or RAM role to authorize them to use the secret in the RAM console. Only then can the RAM user or RAM role use the secret. For more information, see [Custom policy examples for Key Management Service](https://help.aliyun.com/document_detail/480682.html), [Grant Resource Access Management (RAM) user](https://help.aliyun.com/document_detail/116146.html), and [Grant permissions to a RAM role](https://help.aliyun.com/document_detail/116147.html).
        self.policy = policy
        # The interval for automatic rotation. Valid values: 6 hours to 8,760 hours (365 days).  
        # The value must be in the `integer[unit]` format. `integer` specifies the time length, and `unit` specifies the time unit.  
        # Valid values for `unit`: d (days), h (hours), m (minutes), and s (seconds). For example, both 7d and 604,800s indicate a 7-day interval.  
        # 
        # > You must set this parameter only when EnableAutomaticRotation is set to true.
        self.rotation_interval = rotation_interval
        # The secret value. The value can be up to 30,720 bytes (30 KB) in length. KMS encrypts the value by using the specified key and stores it in the initial version.
        # 
        # - When SecretType is set to Generic (generic secret), you can customize the secret value.
        # 
        # - When SecretType is set to Rds (ApsaraDB RDS secret), the secret value must be in the following format: `{"Accounts":[{"AccountName":"","AccountPassword":""}]}`. `AccountName` specifies the username of the ApsaraDB RDS instance, and `AccountPassword` specifies the password of the account.  
        # - When SecretType is set to Redis (Redis secret), set this parameter to `$Auto`.
        # 
        # - When SecretType is set to RAMCredentials (RAM secret), the secret value must be in the following format: `{"AccessKeys":[{"AccessKeyId":"","AccessKeySecret":""}]}`. `AccessKeyId` specifies the AccessKey ID, and `AccessKeySecret` specifies the AccessKey secret. You must specify all AccessKey pairs of the Resource Access Management (RAM) user.
        # 
        # - When SecretType is set to PolarDB, set this parameter to `$Auto`.
        # 
        # - When SecretType is set to ECS (ECS secret), the secret value must be in one of the following formats:  
        # 
        #    - When SecretSubType in the ExtendedConfig parameter is set to Password: `{"UserName":"","Password": ""}`. `UserName` specifies the username used to log on to the ECS instance, and `Password` specifies the logon password.  
        # 
        #    - When SecretSubType in the ExtendedConfig parameter is set to SSHKey: `{"UserName":"","PublicKey": "", "PrivateKey": ""}`. `PublicKey` specifies the SSH public key used to log on to the ECS instance, and `PrivateKey` specifies the private key.
        # 
        # This parameter is required.
        self.secret_data = secret_data
        # The type of the secret value. Valid values:
        # - text: text. This is the default value.
        # - binary: binary data.
        # 
        # > When SecretType is set to Rds, Redis, PolarDB, RAMCredentials, or ECS, SecretDataType can only be set to text.
        self.secret_data_type = secret_data_type
        # The secret name. The secret name must be unique within the current region.
        # The name can be up to 192 characters in length and can contain letters, digits, underscores (_), forward slashes (/), plus signs (+), equal signs (=), periods (.), hyphens (-), and at signs (@). The naming requirements vary based on the secret type:  
        # 
        # - When SecretType is set to Generic (generic secret), Rds (ApsaraDB RDS secret), or Redis (Redis or Tair secret), the name cannot start with `acs/`.  
        # 
        # - When SecretType is set to RAMCredentials (RAM secret), use the fixed value `$Auto`. In this case, KMS automatically generates the secret name, which starts with `acs/ram/user/` and includes the display name of the Resource Access Management (RAM) user.
        # 
        # - When SecretType is set to ECS (ECS secret), the name must start with `acs/ecs/`.
        # 
        # This parameter is required.
        self.secret_name = secret_name
        # The type of the secret. Valid values:
        # 
        # - Generic: generic secret. This is the default value.  
        # - Rds: ApsaraDB RDS secret.  
        # 
        # - Redis: Redis secret.
        # 
        # - RAMCredentials: RAM secret.  
        # 
        # - ECS: ECS secret.
        # 
        # - PolarDB: PolarDB secret.
        self.secret_type = secret_type
        # The tags of the secret. Each tag is a key-value pair that consists of a tag key and a tag value.
        # 
        # The tag key and tag value can be up to 128 characters in length and can contain uppercase and lowercase letters, digits, forward slashes (/), backslashes (\\), underscores (_), hyphens (-), periods (.), plus signs (+), equal signs (=), colons (:), and at signs (@).
        # 
        # - A tag key cannot start with aliyun or acs:.
        # 
        # - You can add up to 20 tags to each secret.
        self.tags = tags
        # The version ID of the initial version. The version ID must be unique within the secret.
        # The version ID can be up to 64 characters in length.
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

