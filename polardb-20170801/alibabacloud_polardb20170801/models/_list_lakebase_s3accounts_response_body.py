# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ListLakebaseS3AccountsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        s_3accounts: List[main_models.ListLakebaseS3AccountsResponseBodyS3Accounts] = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The list of S3 accounts.
        self.s_3accounts = s_3accounts
        # The total number of accounts.
        self.total_count = total_count

    def validate(self):
        if self.s_3accounts:
            for v1 in self.s_3accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['S3Accounts'] = []
        if self.s_3accounts is not None:
            for k1 in self.s_3accounts:
                result['S3Accounts'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.s_3accounts = []
        if m.get('S3Accounts') is not None:
            for k1 in m.get('S3Accounts'):
                temp_model = main_models.ListLakebaseS3AccountsResponseBodyS3Accounts()
                self.s_3accounts.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLakebaseS3AccountsResponseBodyS3Accounts(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        user_acc_ak: str = None,
        user_acc_sk: str = None,
    ):
        # The account type. Valid values:
        # - default: the built-in default account.
        # - user: a user-created account.
        self.account_type = account_type
        # The access key of the S3 account.
        self.user_acc_ak = user_acc_ak
        # The secret key of the S3 account (displayed in masked format).
        self.user_acc_sk = user_acc_sk

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.user_acc_ak is not None:
            result['UserAccAk'] = self.user_acc_ak

        if self.user_acc_sk is not None:
            result['UserAccSk'] = self.user_acc_sk

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('UserAccAk') is not None:
            self.user_acc_ak = m.get('UserAccAk')

        if m.get('UserAccSk') is not None:
            self.user_acc_sk = m.get('UserAccSk')

        return self

