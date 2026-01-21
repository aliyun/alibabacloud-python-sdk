# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_bastionhost20191209 import models as main_models
from darabonba.model import DaraModel

class ListHostAccountsForHostShareKeyResponseBody(DaraModel):
    def __init__(
        self,
        host_accounts: List[main_models.ListHostAccountsForHostShareKeyResponseBodyHostAccounts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the host accounts that are associated with the shared key.
        self.host_accounts = host_accounts
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of the host accounts that are associated with the shared key.
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
                temp_model = main_models.ListHostAccountsForHostShareKeyResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHostAccountsForHostShareKeyResponseBodyHostAccounts(DaraModel):
    def __init__(
        self,
        host_account_name: str = None,
        host_id: str = None,
        hosts_account_id: str = None,
        protocol_name: str = None,
    ):
        # The name of the host account.
        self.host_account_name = host_account_name
        # The ID of the host.
        self.host_id = host_id
        # The ID of the host account.
        self.hosts_account_id = hosts_account_id
        # The O\\&M protocol.
        self.protocol_name = protocol_name

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

        if self.hosts_account_id is not None:
            result['HostsAccountId'] = self.hosts_account_id

        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')

        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('HostsAccountId') is not None:
            self.hosts_account_id = m.get('HostsAccountId')

        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')

        return self

