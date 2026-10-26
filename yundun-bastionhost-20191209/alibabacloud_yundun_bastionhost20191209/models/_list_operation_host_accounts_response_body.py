# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListOperationHostAccountsResponseBody(DaraModel):
    def __init__(
        self,
        host_accounts: List[main_models.ListOperationHostAccountsResponseBodyHostAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The host accounts.
        self.host_accounts = host_accounts
        # The ID of the request.
        self.request_id = request_id
        # The total number of host accounts.
        self.total_count = total_count

    def validate(self):
        if self.host_accounts:
            for v1 in self.host_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k1 in self.host_accounts:
                result['HostAccounts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k1 in m.get('HostAccounts'):
                temp_model = main_models.ListOperationHostAccountsResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOperationHostAccountsResponseBodyHostAccounts(DaraModel):
    def __init__(
        self,
        has_password: bool = None,
        host_account_id: str = None,
        host_account_name: str = None,
        host_id: str = None,
        host_share_key_id: str = None,
        private_key_fingerprint: str = None,
        protocol_name: str = None,
        sshconfig: main_models.ListOperationHostAccountsResponseBodyHostAccountsSSHConfig = None,
    ):
        # Indicates whether a password is set for the host account.
        # 
        # - **true**: A password is set.
        # - **false**: No password is set.
        self.has_password = has_password
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host.
        self.host_id = host_id
        # The ID of the host shared key.
        self.host_share_key_id = host_share_key_id
        # The fingerprint of the private key for the host account.
        self.private_key_fingerprint = private_key_fingerprint
        # The protocol name of the host account.
        # - **SSH**
        # - **RDP**
        self.protocol_name = protocol_name
        # The O&M permissions of the SSH account.
        self.sshconfig = sshconfig

    def validate(self):
        if self.sshconfig:
            self.sshconfig.validate()

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

        if self.private_key_fingerprint is not None:
            result['PrivateKeyFingerprint'] = self.private_key_fingerprint

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        if self.sshconfig is not None:
            result['SSHConfig'] = self.sshconfig.to_map()

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

        if m.get('PrivateKeyFingerprint') is not None:
            self.private_key_fingerprint = m.get('PrivateKeyFingerprint')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        if m.get('SSHConfig') is not None:
            temp_model = main_models.ListOperationHostAccountsResponseBodyHostAccountsSSHConfig()
            self.sshconfig = temp_model.from_map(m.get('SSHConfig'))

        return self

class ListOperationHostAccountsResponseBodyHostAccountsSSHConfig(DaraModel):
    def __init__(
        self,
        enable_sftpchannel: bool = None,
        enable_sshchannel: bool = None,
    ):
        # Indicates whether the SFTP channel is enabled for the account.
        self.enable_sftpchannel = enable_sftpchannel
        # Indicates whether the SSH channel is enabled for the account.
        self.enable_sshchannel = enable_sshchannel

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_sftpchannel is not None:
            result['EnableSFTPChannel'] = self.enable_sftpchannel

        if self.enable_sshchannel is not None:
            result['EnableSSHChannel'] = self.enable_sshchannel

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableSFTPChannel') is not None:
            self.enable_sftpchannel = m.get('EnableSFTPChannel')

        if m.get('EnableSSHChannel') is not None:
            self.enable_sshchannel = m.get('EnableSSHChannel')

        return self

