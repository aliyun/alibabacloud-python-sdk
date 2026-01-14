# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceAccountRequest(DaraModel):
    def __init__(
        self,
        account_status: str = None,
        account_type: str = None,
        page_number: int = None,
        page_size: int = None,
        username: str = None,
    ):
        # The status of the account.
        # 
        # Valid values:
        # 
        # *   DISABLE
        # *   ENABLE
        self.account_status = account_status
        # The account type.
        #   - CUSTOMER
        #   - DEFAULT
        self.account_type = account_type
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The username of the account.
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_status is not None:
            result['accountStatus'] = self.account_status

        if self.account_type is not None:
            result['accountType'] = self.account_type

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountStatus') is not None:
            self.account_status = m.get('accountStatus')

        if m.get('accountType') is not None:
            self.account_type = m.get('accountType')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self

