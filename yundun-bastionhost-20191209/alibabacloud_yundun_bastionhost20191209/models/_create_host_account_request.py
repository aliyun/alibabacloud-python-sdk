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
        project_id: int = None,
        protocol_name: str = None,
        region_id: str = None,
        rotation_mode: str = None,
    ):
        # The name of the host account to create. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.host_account_name = host_account_name
        # The ID of the host for which you want to create a host account.
        # 
        # > You can call the [ListHosts](https://help.aliyun.com/document_detail/200665.html) operation to query this parameter.
        # 
        # This parameter is required.
        self.host_id = host_id
        # The ID of the shared key for the host.
        self.host_share_key_id = host_share_key_id
        # The ID of the Bastionhost instance where the host for which you want to create a host account resides.
        # > You can call the [DescribeInstances](https://help.aliyun.com/document_detail/153281.html) operation to query the Bastionhost instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The passphrase of the private key for the host account to create.
        # 
        # > You can configure this parameter when ProtocolName is set to SSH. You do not need to configure this parameter when ProtocolName is set to RDP.
        self.pass_phrase = pass_phrase
        # The password of the host account to create.
        self.password = password
        # The private key of the host account to create. The value is a Base64-encoded string.
        # 
        # > This parameter takes effect only when ProtocolName is set to SSH. You do not need to configure this parameter when ProtocolName is set to RDP. You can configure both a password and a private key for the host account. When connecting to an asset, Bastionhost preferentially uses the private key.
        self.private_key = private_key
        # The privilege type of the account. Default value: Normal.
        # - **Privileged**: privileged account.
        # - **Normal**: standard account.
        # >Only supported in V3.2.47 and later.
        self.privilege_type = privilege_type
        # The project ID.
        self.project_id = project_id
        # The protocol name of the host account to create.
        # <br>Valid values:
        # - SSH
        # - RDP
        # 
        # This parameter is required.
        self.protocol_name = protocol_name
        # The region ID of the Bastionhost instance where the host for which you want to create a host account resides.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](https://help.aliyun.com/document_detail/40654.html).
        self.region_id = region_id
        # The password change mode of the account. Default value: Self.
        # - **Privileged**: uses a privileged account to change the password.
        # - **Self**: does not use a privileged account to change the password.
        # >Only supported in V3.2.47 and later.
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

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

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

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RotationMode') is not None:
            self.rotation_mode = m.get('RotationMode')

        return self

