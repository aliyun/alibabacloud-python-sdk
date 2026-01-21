# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateHostAccountRequest(DaraModel):
    def __init__(
        self,
        host_account_name: str = None,
        host_id: str = None,
        host_share_key_id: str = None,
        instance_id: str = None,
        pass_phrase: str = None,
        password: str = None,
        private_key: str = None,
        privilege_type: str = None,
        protocol_name: str = None,
        region_id: str = None,
        rotation_mode: str = None,
    ):
        # The name of the host account. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.host_account_name = host_account_name
        # The ID of the host to which you want to add a host account.
        # 
        # >  You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to query the ID of the host.
        # 
        # This parameter is required.
        self.host_id = host_id
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The ID of the bastion host in which you want to add a host account to the host.
        # 
        # >  You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the ID of the bastion host.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The passphrase for the private key of the host account.
        # 
        # > You can configure this parameter only if ProtocolName is set to SSH. You do not need to configure this parameter if ProtocolName is set to RDP.
        self.pass_phrase = pass_phrase
        # The password of the host account.
        self.password = password
        # The private key of the host account. Specify a Base64-encoded string.
        # 
        # > This parameter is valid only if ProtocolName is set to SSH. You do not need to configure this parameter if ProtocolName is set to RDP. You can configure a password and a private key for the host account at the same time. If both a password and a private key are configured for the host account, Bastionhost preferentially uses the private key for logon.
        self.private_key = private_key
        self.privilege_type = privilege_type
        # The protocol of the host to which you want to add a host account.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        # 
        # This parameter is required.
        self.protocol_name = protocol_name
        # The region ID of the bastion host in which you want to add a host account to the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        self.rotation_mode = rotation_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name

        if self.host_id is not None:
            result['HostId'] = self.host_id

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

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rotation_mode is not None:
            result['RotationMode'] = self.rotation_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

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

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RotationMode') is not None:
            self.rotation_mode = m.get('RotationMode')

        return self

