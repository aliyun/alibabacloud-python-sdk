# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListHostAccountsResponseBody(DaraModel):
    def __init__(
        self,
        host_accounts: List[main_models.ListHostAccountsResponseBodyHostAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the queried host accounts.
        self.host_accounts = host_accounts
        # The ID of the request.
        self.request_id = request_id
        # The total number of host accounts that are queried.
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
                temp_model = main_models.ListHostAccountsResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHostAccountsResponseBodyHostAccounts(DaraModel):
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
        # Indicates whether a password is configured for the host account.
        # 
        # Valid values:
        # 
        # *   true: A password is configured for the host account.
        # *   false: No passwords are configured for the host account.
        self.has_password = has_password
        # The ID of the host account.
        self.host_account_id = host_account_id
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host.
        self.host_id = host_id
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name
        # The fingerprint of the private key for the host account.
        self.private_key_fingerprint = private_key_fingerprint
        self.privilege_type = privilege_type
        # The protocol that is used by the host.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
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

