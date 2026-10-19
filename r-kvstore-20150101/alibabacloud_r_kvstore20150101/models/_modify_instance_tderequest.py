# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceTDERequest(DaraModel):
    def __init__(
        self,
        encryption_key: str = None,
        encryption_name: str = None,
        instance_id: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        role_arn: str = None,
        security_token: str = None,
        tdestatus: str = None,
    ):
        # The ID of the custom key. You can call [DescribeEncryptionKeyList](https://help.aliyun.com/document_detail/473860.html) to query the key ID.
        # 
        # > * If you do not specify this parameter, [Key Management Service](https://help.aliyun.com/document_detail/28935.html) automatically generates a key.
        # > * To create a custom key, call the [CreateKey](https://help.aliyun.com/document_detail/28947.html) operation of Key Management Service.
        self.encryption_key = encryption_key
        # The encryption algorithm. Default value: AES-CTR-256.
        # > This parameter is available only when **TDEStatus** is set to **Enabled**.
        self.encryption_name = encryption_name
        # The instance ID. You can call [DescribeInstances](https://help.aliyun.com/document_detail/473778.html) to query the instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The global resource descriptor Alibaba Cloud Resource Name (ARN) of the role to be authorized. After the authorization is complete, the related Key Management Service can be used. Format: `acs:ram::$accountID:role/$roleName`.
        # 
        # > * `$accountID`: the Alibaba Cloud account ID. Log on to the Alibaba Cloud Management Console, move the mouse over the profile picture in the upper-right corner, and then click **Security Settings** to view the account ID.
        # > * `$roleName`: the RAM role name. Set this value to **AliyunRdsInstanceEncryptionDefaultRole**.
        self.role_arn = role_arn
        self.security_token = security_token
        # Enables the transparent data encryption feature. Set the value to **Enabled**.
        # > The TDE feature cannot be disabled after it is enabled. Before enabling TDE, evaluate whether it affects your business. For more information, see [Enable transparent data encryption TDE](https://help.aliyun.com/document_detail/265913.html).
        # 
        # This parameter is required.
        self.tdestatus = tdestatus

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encryption_key is not None:
            result['EncryptionKey'] = self.encryption_key

        if self.encryption_name is not None:
            result['EncryptionName'] = self.encryption_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.tdestatus is not None:
            result['TDEStatus'] = self.tdestatus

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionKey') is not None:
            self.encryption_key = m.get('EncryptionKey')

        if m.get('EncryptionName') is not None:
            self.encryption_name = m.get('EncryptionName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('TDEStatus') is not None:
            self.tdestatus = m.get('TDEStatus')

        return self

