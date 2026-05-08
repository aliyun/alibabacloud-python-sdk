# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20190315 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountsResponseBody(DaraModel):
    def __init__(
        self,
        account_list: main_models.DescribeAccountsResponseBodyAccountList = None,
        request_id: str = None,
    ):
        self.account_list = account_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.account_list:
            self.account_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_list is not None:
            result['AccountList'] = self.account_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountList') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountList()
            self.account_list = temp_model.from_map(m.get('AccountList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountsResponseBodyAccountList(DaraModel):
    def __init__(
        self,
        dbaccount: List[main_models.DescribeAccountsResponseBodyAccountListDBAccount] = None,
    ):
        self.dbaccount = dbaccount

    def validate(self):
        if self.dbaccount:
            for v1 in self.dbaccount:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBAccount'] = []
        if self.dbaccount is not None:
            for k1 in self.dbaccount:
                result['DBAccount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbaccount = []
        if m.get('DBAccount') is not None:
            for k1 in m.get('DBAccount'):
                temp_model = main_models.DescribeAccountsResponseBodyAccountListDBAccount()
                self.dbaccount.append(temp_model.from_map(k1))

        return self

class DescribeAccountsResponseBodyAccountListDBAccount(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
        tags: main_models.DescribeAccountsResponseBodyAccountListDBAccountTags = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_status = account_status
        self.account_type = account_type
        self.tags = tags

    def validate(self):
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountListDBAccountTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeAccountsResponseBodyAccountListDBAccountTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeAccountsResponseBodyAccountListDBAccountTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAccountsResponseBodyAccountListDBAccountTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAccountsResponseBodyAccountListDBAccountTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

