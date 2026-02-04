# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcedirectorymaster20220419 import models as main_models
from darabonba.model import DaraModel

class ListDelegatedAdministratorsResponseBody(DaraModel):
    def __init__(
        self,
        accounts: main_models.ListDelegatedAdministratorsResponseBodyAccounts = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the delegated administrator accounts.
        self.accounts = accounts
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.accounts:
            self.accounts.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accounts is not None:
            result['Accounts'] = self.accounts.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accounts') is not None:
            temp_model = main_models.ListDelegatedAdministratorsResponseBodyAccounts()
            self.accounts = temp_model.from_map(m.get('Accounts'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListDelegatedAdministratorsResponseBodyAccounts(DaraModel):
    def __init__(
        self,
        account: List[main_models.ListDelegatedAdministratorsResponseBodyAccountsAccount] = None,
    ):
        self.account = account

    def validate(self):
        if self.account:
            for v1 in self.account:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Account'] = []
        if self.account is not None:
            for k1 in self.account:
                result['Account'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('Account') is not None:
            for k1 in m.get('Account'):
                temp_model = main_models.ListDelegatedAdministratorsResponseBodyAccountsAccount()
                self.account.append(temp_model.from_map(k1))

        return self

class ListDelegatedAdministratorsResponseBodyAccountsAccount(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        delegation_enabled_time: str = None,
        display_name: str = None,
        join_method: str = None,
        service_principal: str = None,
    ):
        # The Alibaba Cloud account ID of the member.
        self.account_id = account_id
        # The time when the member was specified as a delegated administrator account.
        self.delegation_enabled_time = delegation_enabled_time
        # The display name of the member.
        self.display_name = display_name
        # The way in which the member joins the resource directory. Valid values:
        # 
        # *   invited: The member is invited to join the resource directory.
        # *   created: The member is directly created in the resource directory.
        self.join_method = join_method
        # The identifier of the trusted service.
        self.service_principal = service_principal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.delegation_enabled_time is not None:
            result['DelegationEnabledTime'] = self.delegation_enabled_time

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.join_method is not None:
            result['JoinMethod'] = self.join_method

        if self.service_principal is not None:
            result['ServicePrincipal'] = self.service_principal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DelegationEnabledTime') is not None:
            self.delegation_enabled_time = m.get('DelegationEnabledTime')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('JoinMethod') is not None:
            self.join_method = m.get('JoinMethod')

        if m.get('ServicePrincipal') is not None:
            self.service_principal = m.get('ServicePrincipal')

        return self

