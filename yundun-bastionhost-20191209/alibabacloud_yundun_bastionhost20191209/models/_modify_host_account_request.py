# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyHostAccountRequest(DaraModel):
    def __init__(
        self,
        host_account_id: str = None,
        host_account_name: str = None,
        host_share_key_id: str = None,
        instance_id: str = None,
        pass_phrase: str = None,
        password: str = None,
        private_key: str = None,
        privilege_type: str = None,
        region_id: str = None,
        rotation_mode: str = None,
    ):
        # Specifies the ID of the host account to be modified.
        # 
        # > You can call the [ListHostAccounts](https://help.aliyun.com/document_detail/204372.html) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.host_account_id = host_account_id
        # Specifies the modified host account name, which can contain up to 128 characters.
        self.host_account_name = host_account_name
        # The host shared key ID.
        # 
        # > You can obtain this ID by calling the [ListHostShareKeys](https://help.aliyun.com/document_detail/462973.html) operation.
        self.host_share_key_id = host_share_key_id
        # Specifies the ID of the Bastionhost instance where the host account to be modified resides.
        # 
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the Bastionhost instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies the modified security token of the host account\\"s private key.
        # 
        # > This parameter takes effect when the host account protocol is SSH. This parameter is not required when the host account protocol is RDP.
        self.pass_phrase = pass_phrase
        # Specifies the modified password of the host account.
        self.password = password
        # Specifies the modified private key of the host account, which is a Base64-encoded string.
        # 
        # > This parameter takes effect when the host account protocol is SSH. This parameter is not required when the host account protocol is RDP. You can call the [GetHostAccount](https://help.aliyun.com/document_detail/204391.html) operation to query the protocol used by the host account. You can configure both a password and a private key for a host account. When connecting to an asset, Bastionhost preferentially uses the private key for connection.
        self.private_key = private_key
        # Account permission type. Valid values:
        # 
        # - **Privileged**: privileged account
        # 
        # - **Normal**: regular account
        # 
        # > This parameter is supported only in V3.2.47 and later versions.
        self.privilege_type = privilege_type
        # Specifies the region ID of the Bastionhost instance where the host account to be queried resides.
        # 
        # > For the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # Account password rotation mode. Valid values:
        # 
        # - **Privileged**: Use a privileged account to change the password
        # 
        # - **Self**: Do not use a privileged account to change the password
        # 
        # > This parameter is supported only in V3.2.47 and later versions.
        self.rotation_mode = rotation_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id

        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name

        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase

        if self.password is not None:
            result['Password'] = self.password

        if self.private_key is not None:
            result['PrivateKey'] = self.private_key

        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rotation_mode is not None:
            result['RotationMode'] = self.rotation_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')

        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')

        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')

        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RotationMode') is not None:
            self.rotation_mode = m.get('RotationMode')

        return self

