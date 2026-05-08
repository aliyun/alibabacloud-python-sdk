# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeAllAccountsResponseBody(DaraModel):
    def __init__(
        self,
        account_list: List[main_models.DescribeAllAccountsResponseBodyAccountList] = None,
        request_id: str = None,
    ):
        # The queried database accounts.
        self.account_list = account_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.account_list:
            for v1 in self.account_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccountList'] = []
        if self.account_list is not None:
            for k1 in self.account_list:
                result['AccountList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account_list = []
        if m.get('AccountList') is not None:
            for k1 in m.get('AccountList'):
                temp_model = main_models.DescribeAllAccountsResponseBodyAccountList()
                self.account_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAllAccountsResponseBodyAccountList(DaraModel):
    def __init__(
        self,
        user: str = None,
    ):
        # The name of the database account.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('User') is not None:
            self.user = m.get('User')

        return self

