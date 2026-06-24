# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class StartTerminalSessionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        command_line: str = None,
        connection_type: str = None,
        encryption_options: main_models.StartTerminalSessionRequestEncryptionOptions = None,
        instance_id: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        password_name: str = None,
        port_number: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        target_server: str = None,
        username: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but make sure that the token is unique among different requests. The value of **ClientToken** can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The command to run after the session is initiated. The command can be up to 512 characters in length.
        # 
        # > After you specify CommandLine, you cannot specify PortNumber or TargetServer.
        self.command_line = command_line
        # The network type of the WebSocket URL for the remote connection to the instance. Valid values:
        # - Internet: public network. This is the default value.
        # - Intranet: internal network.
        self.connection_type = connection_type
        # The session encryption configuration.
        self.encryption_options = encryption_options
        # The instance ID list.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The name of the password used by the user when using Session Manager on a Windows instance. The name can be up to 255 characters in length.
        # When you want to use Session Manager on a Windows instance as a non-default user (System), you must specify both Username and this parameter. To reduce the risk of password leaks, store the plaintext password in the parameter repository of operations management and specify only the password name here. For more information, see [Encryption parameters](https://help.aliyun.com/document_detail/186828.html).
        self.password_name = password_name
        # The port number of the ECS instance for data forwarding. After this parameter is set, Cloud Assistant Agent forwards data to the specified port for port forwarding. For example, SSH uses port 22.
        # 
        # Default value: empty, which indicates that no port number is set for data forwarding.
        self.port_number = port_number
        # The region ID of the instance. You can call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent list of regions.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The address of the destination server in the VPC that you want to access through the instance.
        # 
        # > When this parameter is not empty, PortNumber specifies the port number of the destination server in the VPC that you want to access through the managed instance.
        self.target_server = target_server
        # The username used for the connection.
        self.username = username

    def validate(self):
        if self.encryption_options:
            self.encryption_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.command_line is not None:
            result['CommandLine'] = self.command_line

        if self.connection_type is not None:
            result['ConnectionType'] = self.connection_type

        if self.encryption_options is not None:
            result['EncryptionOptions'] = self.encryption_options.to_map()

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password_name is not None:
            result['PasswordName'] = self.password_name

        if self.port_number is not None:
            result['PortNumber'] = self.port_number

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.target_server is not None:
            result['TargetServer'] = self.target_server

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CommandLine') is not None:
            self.command_line = m.get('CommandLine')

        if m.get('ConnectionType') is not None:
            self.connection_type = m.get('ConnectionType')

        if m.get('EncryptionOptions') is not None:
            temp_model = main_models.StartTerminalSessionRequestEncryptionOptions()
            self.encryption_options = temp_model.from_map(m.get('EncryptionOptions'))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PasswordName') is not None:
            self.password_name = m.get('PasswordName')

        if m.get('PortNumber') is not None:
            self.port_number = m.get('PortNumber')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('TargetServer') is not None:
            self.target_server = m.get('TargetServer')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self

class StartTerminalSessionRequestEncryptionOptions(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        kmskey_id: str = None,
        mode: str = None,
    ):
        # Specifies whether to enable end-to-end encryption for the session connection.
        self.enabled = enabled
        # The KMS key ID.
        # Note:
        # - Only KMS symmetric keys are supported.
        # - This parameter is supported only when the encryption mode is set to Kms.
        self.kmskey_id = kmskey_id
        # The encryption pattern. Valid values:
        # - Auto: uses an automatically negotiated secret key encryption for the session.
        # - Kms: uses a KMS secret key encryption for the session.
        # - Default value: Auto.
        # 
        # Note:
        # - This parameter is supported only when session encryption is enabled.
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.mode is not None:
            result['Mode'] = self.mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        return self

