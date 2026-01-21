# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class GetHostAccountResponseBody(DaraModel):
    def __init__(
        self,
        host_account: main_models.GetHostAccountResponseBodyHostAccount = None,
        request_id: str = None,
    ):
        # The details of the host account that was queried.
        self.host_account = host_account
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.host_account:
            self.host_account.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_account is not None:
            result['HostAccount'] = self.host_account.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccount') is not None:
            temp_model = main_models.GetHostAccountResponseBodyHostAccount()
            self.host_account = temp_model.from_map(m.get('HostAccount'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetHostAccountResponseBodyHostAccount(DaraModel):
    def __init__(
        self,
        has_password: bool = None,
        host_account_id: str = None,
        host_account_name: str = None,
        host_id: str = None,
        host_share_key_id: str = None,
        host_share_key_name: str = None,
        private_key_fingerprint: str = None,
        privilege_type: str = None,
        protocol_name: str = None,
        rotation_mode: str = None,
    ):
        # Indicates whether a password is configured for the host account. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_password = has_password
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host to which the host account belongs.
        self.host_id = host_id
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name
        # The fingerprint of the private key.
        self.private_key_fingerprint = private_key_fingerprint
        self.privilege_type = privilege_type
        # The protocol that is used by the host. Valid values:
        # 
        # *   **SSH**
        # *   **RDP**
        self.protocol_name = protocol_name
        self.rotation_mode = rotation_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.has_password is not None:
            result['HasPassword'] = self.has_password

        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id

        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name

        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id

        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name

        if self.private_key_fingerprint is not None:
            result['PrivateKeyFingerprint'] = self.private_key_fingerprint

        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        if self.rotation_mode is not None:
            result['RotationMode'] = self.rotation_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')

        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')

        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')

        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')

        if m.get('PrivateKeyFingerprint') is not None:
            self.private_key_fingerprint = m.get('PrivateKeyFingerprint')

        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('RotationMode') is not None:
            self.rotation_mode = m.get('RotationMode')

        return self

